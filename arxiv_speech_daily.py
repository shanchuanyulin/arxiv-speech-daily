# -*- coding: utf-8 -*-
"""
📚 arXiv 语音方向论文日报 & 周报（HTML 邮件版）
功能：
  ✅ 自动检测最近更新日期
  ✅ --date 指定日期
  ✅ --weekly 汇总7天论文
  ✅ --broad 模糊匹配扩展
  ✅ 自动生成 Markdown + HTML 邮件 + 饼图
  ✅ 兼容 GitHub Actions 自动运行 + 推送 + 发信
"""

import argparse
import arxiv
from datetime import datetime, timedelta
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import os
import io
import base64
import time
import matplotlib.pyplot as plt

# ===== 语音方向分类与关键词 =====
CATEGORIES = {
    "🗣️ Automatic Speech Recognition (ASR)": [
        "speech recognition", "ASR", "speech-to-text", "spoken language understanding",
        "speech encoder", "end-to-end ASR", "transducer", "speech transformer"
    ],
    "🎵 Text-to-Speech / Speech Synthesis (TTS)": [
        "text-to-speech", "speech synthesis", "vocoder", "neural vocoder",
        "voice cloning", "speech generation", "multi-speaker TTS",
        "Flowtron", "HiFi-GAN", "WaveGlow", "Parallel WaveGAN", "WaveNet", "Seed-TTS"
    ],
    "🌫️ Diffusion / Generative Speech Models": [
        "diffusion", "speech diffusion", "generative speech", "score-based", "audio diffusion",
        "consistency model", "flow matching", "CosyVoice"
    ],
    "🧠 Speech Foundation / Pretrained Models": [
        "whisper", "speech foundation model", "speech pretraining", "wav2vec",
        "HuBERT", "data2vec", "speech LM", "speech large model", "SpeechLM", "AudioLM", "SpeechGPT"
    ],
    "🧩 Multimodal / Audio-Language Models": [
        "audio language model", "speech LLM", "audiollm", "speech2text", "speech2speech",
        "audio-text model", "audio captioning", "speech reasoning", "Audio-Maestro"
    ],
    "🎭 Speaker, Emotion & Style Modeling": [
        "speaker embedding", "speaker recognition", "emotion recognition", "prosody modeling",
        "style transfer", "voice conversion", "accent conversion", "speech identity"
    ]
}

MAX_ABSTRACT_LENGTH = 500


# ========= 数据抓取部分 =========
def fetch_papers_for_category(cat_name, keywords, start_date, end_date, broad=False):
    """抓取某个时间区间的论文"""
    client = arxiv.Client(page_size=25, delay_seconds=1, num_retries=2)
    all_papers = []
    start_utc = datetime.strptime(start_date, "%Y-%m-%d").strftime("%Y%m%d") + "0000"
    end_utc = datetime.strptime(end_date, "%Y-%m-%d").strftime("%Y%m%d") + "0000"

    for kw in keywords:
        kw_q = f"(all:\"{kw}\")" if broad else f"(ti:\"{kw}\" OR abs:\"{kw}\")"
        query = f"{kw_q} AND submittedDate:[{start_utc} TO {end_utc}]"
        print(f"🧪 Query: {query}")

        search = arxiv.Search(query=query, sort_by=arxiv.SortCriterion.SubmittedDate, max_results=100)
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


def run_search(start_date, end_date, broad=False):
    """抓取所有类别"""
    all_results = {}
    for cat, kws in CATEGORIES.items():
        print(f"\n📂 {cat}")
        papers = fetch_papers_for_category(cat, kws, start_date, end_date, broad=broad)
        all_results[cat] = papers
        print(f"   ✅ 共 {len(papers)} 篇")
    return all_results

def find_latest_available_date(max_days=10, broad=False):
    """自动检测最近有论文更新的日期"""
    today = datetime.now()
    for i in range(max_days):
        date = (today - timedelta(days=i)).strftime("%Y-%m-%d")
        print(f"\n🔎 检查 {date} 是否有论文...")
        results = run_search(date, date, broad=broad)
        total = sum(len(p) for p in results.values())
        if total > 0:
            print(f"✅ 找到最近有论文更新的日期：{date}（共 {total} 篇）")
            return date, results
        else:
            print(f"📭 {date} 无论文更新。")
    print("⚠️ 最近几天都未检索到论文。")
    return None, {}

# ========= HTML 邮件生成 =========
def generate_html(all_results, date_str, runtime_sec=None, mode="daily"):
    total_papers = sum(len(p) for p in all_results.values())
    runtime_info = f"{runtime_sec:.1f}s" if runtime_sec else "N/A"

    # === 生成分类统计饼图 ===
    categories = [c for c in all_results.keys() if all_results[c]]
    counts = [len(all_results[c]) for c in categories]
    if counts:
        fig, ax = plt.subplots(figsize=(6, 6))
        cmap = plt.get_cmap("tab20")
        colors = [cmap(i) for i in range(len(counts))]
        ax.pie(counts, labels=categories, autopct="%1.1f%%", startangle=140, colors=colors)
        ax.set_title(f"论文分类占比 ({date_str})", fontsize=13)
        plt.tight_layout()
        buf = io.BytesIO()
        plt.savefig(buf, format="png", bbox_inches="tight")
        plt.close(fig)
        img_base64 = base64.b64encode(buf.getvalue()).decode("utf-8")
        chart_html = f'<img src="data:image/png;base64,{img_base64}" alt="Chart" style="display:block;margin:auto;width:70%;border-radius:10px;box-shadow:0 3px 10px rgba(0,0,0,0.1);">'
    else:
        chart_html = "<p style='text-align:center;color:#999;'>暂无统计数据</p>"

    # === HTML 主体 ===
    html = f"""
    <html><head><meta charset="utf-8"><style>
    body {{font-family:"Segoe UI","PingFang SC","Microsoft YaHei",sans-serif;background:#f5f7fa;margin:0;padding:0;}}
    .banner {{background:linear-gradient(135deg,#2b5f9e,#3b82f6);color:white;padding:25px;text-align:center;border-bottom:4px solid #2563eb;}}
    .banner h1{{margin:0;font-size:26px;}}
    .container{{max-width:900px;margin:20px auto;background:#fff;border-radius:12px;box-shadow:0 3px 12px rgba(0,0,0,0.08);padding:30px 40px;}}
    .stats{{text-align:center;font-size:14px;color:#555;margin-bottom:15px;}}
    h2{{font-size:20px;border-left:6px solid #2b5f9e;padding-left:10px;margin-top:40px;background:#f3f6fa;border-radius:6px;padding:8px 12px;}}
    .paper{{border-left:4px solid #4a90e2;margin:18px 0;padding:12px 16px;border-radius:8px;box-shadow:0 1px 5px rgba(0,0,0,0.05);}}
    .title a{{font-size:16px;font-weight:bold;color:#1a73e8;text-decoration:none;}}
    .authors{{color:#555;font-size:13px;margin-top:3px;}}
    .abstract{{margin-top:8px;font-size:14px;color:#333;line-height:1.5;}}
    .footer{{text-align:center;font-size:13px;color:#777;margin-top:25px;}}
    hr{{margin:30px 0;border:none;border-top:1px solid #ddd;}}
    </style></head><body>
    <div class="banner"><h1>{'🗓️ 一周语音论文综述' if mode=='weekly' else '📚 语音论文日报'}</h1>
    <div style="font-size:14px;opacity:0.9;">日期：{date_str}</div></div>
    <div class="container"><div class="stats">📄 共收录 <b>{total_papers}</b> 篇论文 | ⏱️ 耗时 <b>{runtime_info}</b></div><hr>
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
            </div>"""

    html += f"<hr><h2>📊 分类分布</h2>{chart_html}<div class='footer'>✅ 数据来源：<a href='https://arxiv.org'>arXiv.org</a><br>🧠 自动生成 · Speech AI Daily · Powered by Python</div></div></body></html>"
    return html


# ========= 邮件发送 =========
def send_email(all_results, date_str, mode="daily", runtime=0.0):
    EMAIL_SENDER = os.environ.get("EMAIL_USER")
    EMAIL_PASS = os.environ.get("EMAIL_PASS")
    EMAIL_RECEIVER = os.environ.get("EMAIL_RECEIVER", EMAIL_SENDER)

    if not (EMAIL_SENDER and EMAIL_PASS):
        print("📭 未检测到邮箱配置，跳过邮件发送。")
        return

    html_content = generate_html(all_results, date_str, runtime, mode)
    subject = f"📚 arXiv 语音方向论文日报 {date_str}" if mode == "daily" else f"🗓️ arXiv 语音方向一周论文综述 ({date_str})"

    # fallback 文本
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

from notion_client import Client

def sync_to_notion(all_results, date_str, mode="daily"):
    """同步论文到 Notion 数据库"""
    notion_token = os.environ.get("NOTION_TOKEN")
    notion_db = os.environ.get("NOTION_DB_ID")

    if not (notion_token and notion_db):
        print("📭 未检测到 Notion 配置，跳过同步。")
        return

    notion = Client(auth=notion_token)

    total = 0
    for cat, papers in all_results.items():
        for p in papers:
            try:
                notion.pages.create(
                    parent={"database_id": notion_db},
                    properties={
                        "Title": {"title": [{"text": {"content": p["title"]}}]},
                        "Category": {"rich_text": [{"text": {"content": cat}}]},
                        "Authors": {"rich_text": [{"text": {"content": p["authors"]}}]},
                        "Date": {"date": {"start": date_str}},
                        "URL": {"url": p["url"]},
                    },
                    children=[
                        {
                            "object": "block",
                            "type": "toggle",
                            "toggle": {
                                "text": [
                                    {
                                        "type": "text",
                                        "text": {
                                            "content": "🧾 摘要（点击展开）"
                                        },
                                        "annotations": {"bold": True},
                                    }
                                ],
                                "children": [
                                    {
                                        "object": "block",
                                        "type": "paragraph",
                                        "paragraph": {
                                            "text": [
                                                {
                                                    "type": "text",
                                                    "text": {"content": p["summary"]},
                                                }
                                            ]
                                        },
                                    }
                                ],
                            },
                        }
                    ],
                )
                total += 1
            except Exception as e:
                print(f"⚠️ 同步失败: {p['title'][:40]}... ({e})")

    print(f"✅ 已同步 {total} 篇论文到 Notion ({mode})")

# ========= 命令行接口 =========
def parse_args():
    parser = argparse.ArgumentParser(description="Arxiv Speech Daily / Weekly Report Generator")
    parser.add_argument("--weekly", action="store_true", help="抓取过去7天的语音方向论文 (生成周报)")
    parser.add_argument("--broad", action="store_true", help="使用更广泛关键词（推荐）")
    parser.add_argument("--date", type=str, default=None, help="指定日期（格式 YYYY-MM-DD）")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    date_str = args.date or datetime.now().strftime("%Y-%m-%d")

if args.weekly:
    start_date = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")
    end_date = datetime.now().strftime("%Y-%m-%d")
    print(f"📅 生成周报：{start_date} → {end_date}")
    mode = "weekly"
    start_time = time.time()
    all_results = run_search(start_date, end_date, broad=args.broad)
else:
    # 🧩 自动检测最近有论文的日期
    if args.date:
        target_date = args.date
        print(f"📅 指定日期：{target_date}")
        start_time = time.time()
        all_results = run_search(target_date, target_date, broad=args.broad)
    else:
        print("🧭 未指定日期，正在检测最近有论文的日期...")
        start_time = time.time()
        latest_date, all_results = find_latest_available_date(broad=args.broad)
        if not latest_date:
            print("❌ 未找到最近有论文的日期，程序结束。")
            exit(0)
        target_date = latest_date
    mode = "daily"

runtime = time.time() - start_time
date_str = target_date



# 输出 Markdown
os.makedirs("reports", exist_ok=True)
md_path = f"reports/week_of_{end_date}.md" if mode == "weekly" else f"reports/{date_str}.md"
with open(md_path, "w", encoding="utf-8") as f:
    for cat, papers in all_results.items():
        if not papers:
            continue
        f.write(f"## {cat}\n")
        for p in papers:
            f.write(f"- [{p['title']}]({p['url']}) — {p['authors']}\n\n")
print(f"✅ 已生成报告文件：{md_path}")

send_email(all_results, date_str, mode, runtime)
    # === 同步到 Notion ===
sync_to_notion(all_results, date_str, mode)





