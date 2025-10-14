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


import time

import base64
import io
import matplotlib.pyplot as plt

def generate_html(all_results, date_str, runtime_sec=None, mode="daily"):
    """生成美观、带统计图的 HTML 邮件内容"""
    total_papers = sum(len(p) for p in all_results.values())
    runtime_info = f"{runtime_sec:.1f}s" if runtime_sec else "N/A"

    # === 生成分类统计图 ===
    categories = list(all_results.keys())
    counts = [len(all_results[c]) for c in categories if all_results[c]]

    if len(counts) > 0:
        fig, ax = plt.subplots(figsize=(6, 6))
        cmap = plt.get_cmap("tab20")
        colors = [cmap(i) for i in range(len(counts))]

        wedges, texts, autotexts = ax.pie(
            counts,
            labels=categories,
            autopct="%1.1f%%",
            startangle=140,
            colors=colors,
            textprops={"fontsize": 10},
        )
        ax.set_title(f"论文分类占比 ({date_str})", fontsize=13)
        plt.tight_layout()

        buf = io.BytesIO()
        plt.savefig(buf, format="png", bbox_inches="tight")
        plt.close(fig)
        img_base64 = base64.b64encode(buf.getvalue()).decode("utf-8")
        chart_html = f'<img src="data:image/png;base64,{img_base64}" alt="Chart" style="display:block;margin:auto;width:70%;border-radius:10px;box-shadow:0 3px 10px rgba(0,0,0,0.1);">'
    else:
        chart_html = "<p style='text-align:center;color:#999;'>暂无统计数据</p>"

    # === 生成主HTML ===
    html = f"""
    <html>
    <head>
        <meta charset="utf-8">
        <style>
            body {{
                font-family: "Segoe UI", "PingFang SC", "Microsoft YaHei", sans-serif;
                background: #f5f7fa;
                margin: 0;
                padding: 0;
            }}
            .banner {{
                background: linear-gradient(135deg, #2b5f9e, #3b82f6);
                color: white;
                padding: 25px;
                text-align: center;
                border-bottom: 4px solid #2563eb;
            }}
            .banner h1 {{
                margin: 0;
                font-size: 26px;
            }}
            .container {{
                max-width: 900px;
                margin: 20px auto;
                background: #ffffff;
                border-radius: 12px;
                box-shadow: 0 3px 12px rgba(0,0,0,0.08);
                padding: 30px 40px;
            }}
            .stats {{
                text-align: center;
                font-size: 14px;
                color: #555;
                margin-bottom: 15px;
            }}
            h2 {{
                font-size: 20px;
                border-left: 6px solid #2b5f9e;
                padding-left: 10px;
                margin-top: 40px;
                background: #f3f6fa;
                border-radius: 6px;
                padding: 8px 12px;
            }}
            .paper {{
                border-left: 4px solid #4a90e2;
                margin: 18px 0;
                padding: 12px 16px;
                border-radius: 8px;
                box-shadow: 0 1px 5px rgba(0,0,0,0.05);
            }}
            .title a {{
                font-size: 16px;
                font-weight: bold;
                color: #1a73e8;
                text-decoration: none;
            }}
            .authors {{
                color: #555;
                font-size: 13px;
                margin-top: 3px;
            }}
            .abstract {{
                margin-top: 8px;
                font-size: 14px;
                color: #333;
                line-height: 1.5;
            }}
            .footer {{
                text-align: center;
                font-size: 13px;
                color: #777;
                margin-top: 25px;
            }}
            hr {{
                margin: 30px 0;
                border: none;
                border-top: 1px solid #ddd;
            }}
        </style>
    </head>
    <body>
        <div class="banner">
            <h1>{'🗓️ 一周语音论文综述' if mode == 'weekly' else '📚 语音论文日报'}</h1>
            <div style="font-size:14px;opacity:0.9;">日期：{date_str}</div>
        </div>
        <div class="container">
            <div class="stats">
                📄 共收录 <b>{total_papers}</b> 篇论文 | ⏱️ 耗时 <b>{runtime_info}</b>
            </div>
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

    # === 插入图表 ===
    html += f"""
            <hr>
            <h2>📊 分类分布</h2>
            {chart_html}
            <div class="footer">
                ✅ 数据来源：<a href="https://arxiv.org">arXiv.org</a><br>
                🧠 自动生成 · Speech AI Daily · Powered by Python
            </div>
        </div>
    </body>
    </html>
    """
    return html



def send_email(all_results, date_str, mode="daily", runtime=0.0):
    """发送 HTML 邮件 + fallback 文本版本"""
    EMAIL_SENDER = os.environ.get("EMAIL_USER")
    EMAIL_PASS = os.environ.get("EMAIL_PASS")
    EMAIL_RECEIVER = os.environ.get("EMAIL_RECEIVER", EMAIL_SENDER)

    if not (EMAIL_SENDER and EMAIL_PASS):
        print("📭 未检测到邮箱配置，跳过邮件发送。")
        return

    html_content = generate_html(all_results, date_str, runtime)
    subject = (
        f"📚 arXiv 语音方向论文日报 {date_str}"
        if mode == "daily"
        else f"🗓️ arXiv 语音方向一周论文综述 ({date_str})"
    )

    # Fallback 文本内容
    text_version = f"Speech AI Report ({mode}) - {date_str}\n\n"
    for cat, papers in all_results.items():
        if not papers:
            continue
        text_version += f"\n[{cat}]\n"
        for p in papers:
            text_version += f"- {p['title']} ({p['authors']})\n  {p['url']}\n"

    try:
        msg = MIMEMultipart("alternative")
        msg["From"] = EMAIL_SENDER
        msg["To"] = EMAIL_RECEIVER
        msg["Subject"] = Header(subject, "utf-8")
        msg.attach(MIMEText(text_version, "plain", "utf-8"))
        msg.attach(MIMEText(html_content, "html", "utf-8"))

        with smtplib.SMTP_SSL("smtp.qq.com", 465) as server:
            server.login(EMAIL_SENDER, EMAIL_PASS)
            server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER.split(","), msg.as_string())

        print("📧 邮件发送成功！")
    except Exception as e:
        print(f"⚠️ 邮件发送失败：{e}")


import argparse
from datetime import datetime, timedelta

def parse_args():
    parser = argparse.ArgumentParser(description="Arxiv Speech Daily / Weekly Report Generator")
    parser.add_argument(
        "--weekly", action="store_true", help="抓取过去7天的语音方向论文 (生成周报)"
    )
    parser.add_argument(
        "--broad", action="store_true", help="使用更广泛关键词（推荐）"
    )
    parser.add_argument(
        "--date", type=str, default=None, help="指定日期（格式 YYYY-MM-DD）"
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()

    if args.date:
        date_str = args.date
    else:
        date_str = datetime.now().strftime("%Y-%m-%d")

    # 🗓️ 如果是周报模式，则查询过去7天
    if args.weekly:
        start_date = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")
        end_date = datetime.now().strftime("%Y-%m-%d")
        print(f"📅 生成周报：{start_date} → {end_date}")
        mode = "weekly"
    else:
        start_date = date_str
        end_date = date_str
        print(f"📅 生成日报：{date_str}")
        mode = "daily"

    # === 抓取数据 ===
    start_time = time.time()
    all_results = run_search(start_date, end_date, broad=args.broad)
    runtime = time.time() - start_time

    # === 输出结果 ===
    html = generate_html(all_results, date_str, runtime)
    md_filename = (
        f"reports/week_of_{end_date}.md" if mode == "weekly" else f"reports/{date_str}.md"
    )
    with open(md_filename, "w", encoding="utf-8") as f:
        f.write(convert_to_markdown(all_results, date_str))
    with open("debug_papers.md", "w", encoding="utf-8") as f:
        f.write(convert_to_markdown(all_results, date_str))

    print(f"✅ 已生成报告文件：{md_filename}")

    # === 邮件发送 ===
    send_email(all_results, date_str, mode, runtime)

html_content = generate_html(all_results, date_str, runtime_sec=time.time() - start_time)

# === 邮件发送部分 ===
EMAIL_SENDER = os.environ.get("EMAIL_USER")
EMAIL_PASS = os.environ.get("EMAIL_PASS")
EMAIL_RECEIVER = os.environ.get("EMAIL_RECEIVER", EMAIL_SENDER)

if EMAIL_SENDER and EMAIL_PASS:
    try:
        msg = MIMEMultipart("alternative")
        msg["From"] = EMAIL_SENDER
        msg["To"] = EMAIL_RECEIVER
        msg["Subject"] = Header(f"📚 arXiv 语音方向论文日报 {date_str}", "utf-8")

        # Fallback 文本内容（纯文字摘要）
        text_version = f"Speech Daily {date_str}\n\n"
        for cat, papers in all_results.items():
            if not papers:
                continue
            text_version += f"\n[{cat}]\n"
            for p in papers:
                text_version += f"- {p['title']} ({p['authors']})\n  {p['url']}\n"

        msg.attach(MIMEText(text_version, "plain", "utf-8"))
        msg.attach(MIMEText(html_content, "html", "utf-8"))

        smtp_host = "smtp.qq.com"
        with smtplib.SMTP_SSL(smtp_host, 465) as server:
            server.login(EMAIL_SENDER, EMAIL_PASS)
            server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER.split(","), msg.as_string())

        print("📧 邮件发送成功！")
    except Exception as e:
        print(f"⚠️ 邮件发送失败：{e}")
else:
    print("📭 未检测到邮箱配置，跳过邮件发送。")

