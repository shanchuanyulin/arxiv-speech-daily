# -*- coding: utf-8 -*-
"""
📚 arXiv 语音方向论文日报（HTML 邮件版）
功能：
  ✅ 自动检测最近更新日期
  ✅ --date 指定日期
  ✅ --broad 模糊扩展匹配
  ✅ 自动生成 Markdown & HTML 邮件
  ✅ 可在 GitHub Actions 中每天自动运行 + 推送 + 发信
"""

import argparse
import arxiv
from datetime import datetime, timedelta
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import os

# ===== 语音方向分类与关键词 =====
CATEGORIES = {
    "🗣️ Automatic Speech Recognition (ASR)": [
        "speech recognition", "ASR", "speech-to-text", "spoken language understanding",
        "speech encoder", "end-to-end ASR", "transducer", "speech transformer"
    ],
    "🎵 Text-to-Speech / Speech Synthesis (TTS)": [
        "text-to-speech", "speech synthesis", "vocoder", "neural vocoder",
        "voice cloning", "speech generation", "speech resynthesis", "multi-speaker TTS",
        "Flowtron", "HiFi-GAN", "WaveGlow", "Parallel WaveGAN", "WaveNet", "Seed-TTS"
    ],
    "🌫️ Diffusion / Generative Speech Models": [
        "diffusion", "speech diffusion", "generative speech", "score-based", "audio diffusion",
        "consistency model", "flow matching", "stable audio", "DiT-TTS", "E2 TTS", "CosyVoice"
    ],
    "🧠 Speech Foundation / Pretrained Models": [
        "whisper", "speech foundation model", "speech pretraining", "wav2vec",
        "HuBERT", "data2vec", "speech LM", "speech large model", "speech encoder-decoder",
        "SpeechLM", "AudioLM", "SpeechGPT"
    ],
    "🧩 Multimodal / Audio-Language Models": [
        "audio language model", "speech LLM", "audiollm", "speech2text", "speech2speech",
        "audio-text model", "audio captioning", "speech reasoning", "Audio-Maestro", "Audio Flamingo"
    ],
    "🎭 Speaker, Emotion & Style Modeling": [
        "speaker embedding", "speaker recognition", "emotion recognition", "prosody modeling",
        "style transfer", "voice conversion", "accent conversion", "speech identity"
    ]
}

OUTPUT_FILE = "debug_papers.md"
MAX_ABSTRACT_LENGTH = 500


def fetch_papers_for_category(cat_name, keywords, date_str, broad=False):
    """抓取指定日期的论文"""
    client = arxiv.Client(page_size=25, delay_seconds=1, num_retries=2)
    all_papers = []

    dt = datetime.strptime(date_str, "%Y-%m-%d")
    next_dt = dt + timedelta(days=2 if broad else 1)
    start_utc = dt.strftime("%Y%m%d") + "0000"
    end_utc = next_dt.strftime("%Y%m%d") + "0000"

    for kw in keywords:
        if broad:
            kw_q = f"(all:\"{kw}\")"
        else:
            kw_q = f"(ti:\"{kw}\" OR abs:\"{kw}\")"

        query = f"{kw_q} AND submittedDate:[{start_utc} TO {end_utc}]"
        print("🧪 Query:", query)

        search = arxiv.Search(query=query,
                              sort_by=arxiv.SortCriterion.SubmittedDate,
                              max_results=100)
        try:
            results = list(client.results(search))
            print(f"   → got {len(results)} results for {kw}")
            for result in results:
                summary = (result.summary or "").strip().replace("\n", " ")
                if len(summary) > MAX_ABSTRACT_LENGTH:
                    summary = summary[:MAX_ABSTRACT_LENGTH] + "..."
                paper = {
                    "title": result.title.strip(),
                    "authors": ", ".join(a.name for a in result.authors),
                    "url": result.entry_id,
                    "summary": summary,
                }
                if not any(p["title"] == paper["title"] for p in all_papers):
                    all_papers.append(paper)
        except Exception as e:
            print("⚠️ Exception:", e)

    return all_papers


def find_latest(broad=False):
    """自动检测最近一个有论文的日期"""
    today = datetime.utcnow().date()
    for i in range(1, 7):
        d = (today - timedelta(days=i)).strftime("%Y-%m-%d")
        print(f"\n== Trying {d}")
        all_res = {}
        tot = 0
        for cat, kws in CATEGORIES.items():
            papers = fetch_papers_for_category(cat, kws, d, broad=broad)
            all_res[cat] = papers
            tot += len(papers)
        if tot > 0:
            print(f"✅ Found {d} with {tot} papers")
            return d, all_res
    return today.strftime("%Y-%m-%d"), {}


def generate_html(all_results, date_str):
    """生成 HTML 邮件内容"""
    html = f"""
    <html>
    <head>
        <meta charset="utf-8">
        <style>
            body {{ font-family: 'Segoe UI', Arial, sans-serif; background-color: #fafafa; color: #333; }}
            h1 {{ text-align: center; color: #2b5f9e; }}
            h2 {{ color: #444; border-left: 5px solid #2b5f9e; padding-left: 8px; }}
            .paper {{ margin-bottom: 20px; padding: 10px; background-color: #fff; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }}
            .title {{ font-size: 16px; font-weight: bold; }}
            .authors {{ color: #555; font-size: 13px; }}
            .abstract {{ margin-top: 5px; font-size: 14px; color: #444; }}
            a {{ color: #2b5f9e; text-decoration: none; }}
            a:hover {{ text-decoration: underline; }}
        </style>
    </head>
    <body>
        <h1>📚 arXiv 语音方向论文日报</h1>
        <p style="text-align:center;">日期：{date_str}</p>
        <hr>
    """

    for cat, papers in all_results.items():
        if not papers:
            continue
        html += f"<h2>{cat}</h2>"
        for p in papers:
            html += f"""
            <div class="paper">
                <div class="title"><a href="{p['url']}">{p['title']}</a></div>
                <div class="authors">👥 {p['authors']}</div>
                <div class="abstract">{p['summary']}</div>
            </div>
            """
    html += "<hr><p style='text-align:center;'>✅ 数据来源：<a href='https://arxiv.org'>arXiv.org</a></p></body></html>"
    return html


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", type=str, help="手动指定日期 (YYYY-MM-DD)")
    parser.add_argument("--broad", action="store_true", help="启用模糊匹配与扩展窗口")
    args = parser.parse_args()

    broad = args.broad

    if args.date:
        date_str = args.date
        print(f"📅 使用手动指定日期: {date_str}")
        all_results = {cat: fetch_papers_for_category(cat, kws, date_str, broad=broad)
                       for cat, kws in CATEGORIES.items()}
    else:
        print("🔍 自动检测最近更新日期...")
        date_str, all_results = find_latest(broad=broad)

    # 生成 HTML
    html_content = generate_html(all_results, date_str)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"✅ 已写入 {OUTPUT_FILE}")

    # === 邮件发送 ===
    EMAIL_SENDER = os.environ.get("EMAIL_USER")
    EMAIL_PASS = os.environ.get("EMAIL_PASS")
    EMAIL_RECEIVER = os.environ.get("EMAIL_RECEIVER", EMAIL_SENDER)

    if EMAIL_SENDER and EMAIL_PASS:
        try:
            msg = MIMEMultipart("alternative")
            msg["From"] = EMAIL_SENDER
            msg["To"] = EMAIL_RECEIVER
            msg["Subject"] = Header(f"📚 arXiv 语音方向论文日报 {date_str}", "utf-8")
            msg.attach(MIMEText(html_content, "html", "utf-8"))

            smtp_host = "smtp.gmail.com" if "gmail" in EMAIL_SENDER else "smtp.qq.com"
            with smtplib.SMTP_SSL(smtp_host, 465) as server:
                server.login(EMAIL_SENDER, EMAIL_PASS)
                server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER.split(","), msg.as_string())

            print("📧 邮件发送成功！")
        except Exception as e:
            print(f"⚠️ 邮件发送失败：{e}")
    else:
        print("📭 未检测到邮箱配置，跳过邮件发送。")
