---
layout: default
title: 2026 LLM 大語言模型資源懶人包 | Agent, RAG & Fine-tuning | Deep Learning 101
description: 2026 最強大語言模型 (LLM) 與 AI Agent 開發指南。彙整 RAG 防幻覺實作、Deep Research 框架、Manus 開源平替、SLM 端側小模型與 LLaMA Factory 零程式碼微調資源。
permalink: /Large-Language-Model
lang: zh-Hant
schema_type: article
---

{% include header.html %}

# 📚 LLM 大語言模型・必讀資源總整理

> **編者按：** 本頁面彙整目前最主流的 LLM 排行榜、開源模型、推論與微調工具，以及相關學術論文。
>
> 如果您想尋找更詳細的筆記，歡迎訪問 **GitHub Repository**：
> 👉 [**GitHub: Natural-Language-Processing-Paper**](https://github.com/Deep-Learning-101/Natural-Language-Processing-Paper) (歡迎 Star ⭐)

---

{% include ai-share.html %}

---

## ✨LLM API Platform Price Comparison
大型語言模型API平台價格比較

| 平台 | 模型 | 輸入費用 (USD/1M Tokens) | 輸出費用 (USD/1M Tokens) | 上下文窗口 | 免費層級 | 最大速率限制 (RPM / TPM) | 多模態能力 | 特點 / 說明 | 定價連結 |
|------|------|---------------------------|---------------------------|-------------|-----------|---------------------------|----------------|----------------|-----------|
| OpenAI | OpenAI o1 | $15.00 | $60.00 | 200k | ❌ | 不公開 | ✅（文字＋圖像） | Frontier 模型，支援 Vision/Tools/結構化輸出 | [OpenAI Pricing](https://openai.com/api/pricing/) |
| OpenAI | OpenAI o3-mini | $1.10 | $4.40 | 200k | ❌ | 不公開 | ❌ | 成本效益模型，適合編碼與數學 | 同上 |
| Google | Gemini 2.5 Pro (Preview) | $1.25（≤200k），$2.50（>200k） | $10.00（≤200k），$15.00（>200k） | >200k | ✅（指定模型） | 150 RPM / 2M TPM（Tier 1） | ✅（文字＋圖像） | 高階推理力，企業級用途 | [Gemini API](https://ai.google.dev/gemini-api/docs/pricing) / [Gemini 網站](https://gemini.google.com/) |
| Google | Gemini 2.0 Flash | $0.10（圖文影），$0.70（音訊） | $0.40 | 1M | ✅（15 RPM） | 2,000 RPM / 4M TPM | ✅（文字＋圖＋影＋音） | 多模態支援，企業級速率與穩定性 | 同上 |
| Google | Gemini 2.0 Flash Lite | $0.075（全模態） | $0.30 | 1M | ✅（30 RPM） | 4,000 RPM / 4M TPM | ✅（全模態） | 超高速率、經濟型多模態模型 | 同上 |
| DeepSeek | deepseek-chat (V3) | $0.27 | $1.10 | 64K | ❌ | 不公開 | ❌ | 標準價，推理速度佳 | [DeepSeek Pricing](https://api-docs.deepseek.com/quick_start/pricing) / [DeepSeek Chat](https://chat.deepseek.com/) |
| DeepSeek | deepseek-reasoner (R1) | $0.55 | $2.19 | 64K | ❌ | 不公開 | ❌ | 高階邏輯推理與數據分析能力 | 同上 |
| Qwen | Qwen-Max | $1.60 | $6.40 | ~32K | ❌ | 不公開 | ❌ | 強推理型，偏向高品質產出 | [Qwen Chat](https://chat.qwen.ai/) |
| Qwen | Qwen-Plus | $0.40 | $1.20 | ~131K | ❌ | 不公開 | ❌ | 均衡型模型，支援較長上下文 | 同上 |
| Grok | grok-3 | $3.00 | $15.00 | 131k | ✅ | 不公開 | ❌ | 支援思考模式、有限搜尋功能 | [Grok 官網](https://grok.com/) |
| 百度 | 文心一言（ERNIE Bot） | 不公開（免費使用） | 不公開（免費使用） | 不公開 | ✅ | 不公開 | ✅（圖像/語音） | 支援中文語境與多模態任務 | [文心一言](https://yiyan.baidu.com/X1) |

---

### **文章目錄**
- [🏆 排行榜 (Leaderboards)](#leaderboards)
- [🖥️ NVIDIA Nemotron](#nvidia-nemotron)
- [🛠️ 微調技術與資源 (Fine-tuning)](#fine-tuning)
- [🧩 AI Agent 開源框架](#ai-agent)
- [🛠️ 開發工具 (Tools & Protocols)](#tools)
- [🌍 World Models (世界模型)](#world-models)
- [🧠 MoE (混合專家模型)](#moe)
- [📱 Small Language Models (小型語言模型)](#slm)
- [🤔 Reasoning Models (推理模型)](#reasoning)
- [🏛️ Large Language Models (大型語言模型)](#llm)
- [🔎 Embedding & Reranker](#embedding)
- [🔊 Speech-to-Speech LLM (語音大模型)](#speech)
- [👁️ Vision-Language Model (視覺大語言模型)](#vision)
- [🌌 Multimodal LLM (多模態大語言模型)](#multimodal)

---

## Leaderboards
**🏆 LLM 權威排行榜與評測指標 (Leaderboards)**

在開源模型百家爭鳴的時代，如何挑選最適合特定任務的大語言模型？以下整理了目前 AI 開發者社群中最具公信力的 4 大模型評測榜單與資源庫，幫助您快速定位所需模型：

* **[Open LLM Leaderboard (HuggingFace 官方榜單)](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)**
  * **適用情境**：尋找綜合能力最強的開源模型。
  * **特色亮點**：被譽為「開源模型的奧斯卡指標」。涵蓋推理解析、常識問答、數學運算與防幻覺等多項基準測試 (Benchmarks)，是決定本地部署模型前必看的權威榜單。

* **[AlpacaEval Leaderboard](https://tatsu-lab.github.io/alpaca_eval/)**
  * **適用情境**：評估模型「聽不聽得懂人話」。
  * **特色亮點**：專注於「指令跟隨 (Instruction-following)」能力的勝率榜。透過高速自動化評測，驗證模型在真實對話情境中，是否能精準理解並執行人類的複雜指令。

* **[Big Code Models Leaderboard](https://huggingface.co/spaces/bigcode/bigcode-models-leaderboard)**
  * **適用情境**：開發 AI 程式碼助手 (Coding Copilot)。
  * **特色亮點**：寫 Code 專用模型的專屬競技場。如果您需要尋找能輔助撰寫程式碼、代碼補全 (Code Completion) 或 Debug 的專項模型，請以這份榜單的排名為準。

* **[Awesome-Chinese-LLM](https://github.com/HqWu-HITCS/Awesome-Chinese-LLM)**
  * **適用情境**：開發中文專屬的 AI 應用或 RAG 知識庫。
  * **特色亮點**：這雖然不是單一的量化排行榜，卻是 GitHub 上最齊全的「中文大語言模型」開源專案、微調數據集與評測總整理。要在地化微調 (Fine-tuning) 中文模型，這是必備的尋寶圖。

---

## NVIDIA Nemotron
**🟢 NVIDIA Nemotron 企業級 AI 實戰指南**  

NVIDIA 開發的 Nemotron 系列模型，以其極高的推理效率與完整的 NeMo 生態系，成為企業落地生成式 AI 的首選。以下我們將資源依據「開發階段」與「業務場景」進行分類，幫助您快速掌握從模型部署到安全防護的完整技術棧。

### 1. 核心模型發佈與解析 (Core Models)
了解 Nemotron 系列的核心架構與性能指標，選擇適合您的硬體與應用場景的模型尺寸。

* **[Nemotron 3 Super (最新主力)](https://blogs.nvidia.com.tw/blog/nemotron-3-super-agentic-ai/)** (2026-03)
  * **特點**：專為 Agentic AI 設計的旗艦模型，強大的邏輯規劃能力。[👉 HuggingFace 權重下載](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-FP8)。
* **[Nemotron 3 Nano (端側輕量化)](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-Base-BF16)** (2025-12)
  * **特點**：適合資源受限的邊緣設備 (Edge) 或本地端推論。[👉 OpenRouter 免費測試](https://openrouter.ai/nvidia/nemotron-3-nano-30b-a3b:free)。
* **[深入解析 Nemotron 3 內部原理](https://developer.nvidia.cn/blog/inside-nvidia-nemotron-3-techniques-tools-and-data-that-make-it-efficient-and-accurate/)** (2025-12)
  * **必讀原因**：深度解析 Mamba-Transformer 混合架構，理解為何 Nemotron 能在長文本處理上達到極致的效率與準確度。

### 2. 本地微調與模型訓練 (Fine-tuning & Training)
沒有龐大的機房算力？教您如何在消費級顯示卡 (如 RTX 4090) 上，打造專屬的領域大模型。

* **[使用 Unsloth 低成本微調 LLM 實戰](https://blogs.nvidia.cn/blog/rtx-ai-garage-fine-tuning-unsloth-dgx-spark/)** (2025-12)
  * **解決痛點**：算力不足。這篇教學展示了如何在本地端使用 Unsloth 工具快速微調模型，是開發者入門 SFT (監督微調) 的首選。
* **[週末速成：用 NeMo 訓練具備「推理能力」的 LLM](https://developer.nvidia.cn/blog/train-a-reasoning-capable-llm-in-one-weekend-with-nvidia-nemo/)** (2025-07)
  * **解決痛點**：模型缺乏邏輯。這篇經典文章提供了極佳的方法論，教導如何準備數據，讓模型學會「思考鏈 (Chain of Thought)」，其策略完全適用於最新的 Nemotron-3。

### 3. RAG 知識庫與文檔處理 (Document Processing)
如何讓 AI 讀懂企業內部複雜的 PDF、報表與圖表，轉化為即時的商業價值。

* **[使用 Nemotron 為 RAG 建立文件處理流程](https://developer.nvidia.cn/blog/how-to-build-a-document-processing-pipeline-for-rag-with-nemotron/)** (2026-02)
  * **實戰指南**：企業導入 AI 最常見的需求。一步步教您如何使用最新模型，精準解析 PDF、表格與圖像資訊，解決傳統 RAG 系統「找不到資料」的問題。
* **[AI 智能體如何將文件轉化為即時商業智能 (IDP)](https://blogs.nvidia.cn/blog/ai-agents-intelligent-document-processing/)** (2026-02)
  * **架構規劃**：適合架構師或專案經理閱讀。解析 Docusign 等企業如何運用 AI 處理文檔 (IDP)，為您撰寫提案提供強大案例支持。

### 4. 語音智能體與安全護欄 (Voice Agent & Guardrails)
打造能聽會說、且「不亂說話」的企業級 AI 助理。

* **[如何使用 RAG 和安全護欄建立語音智能體](https://developer.nvidia.cn/blog/how-to-build-a-voice-agent-with-rag-and-safety-guardrails/)** (2026-01)
  * **整合應用**：展示如何將 Nemotron 與語音辨識技術結合。更重要的是，引入了 Guardrails 機制，確保 AI 的回答符合企業規範，防止幻覺與不當言論。
* **[開發專用 AI 智能體：視覺、RAG 與 Guardrail 綜合應用](https://developer.nvidia.cn/blog/develop-specialized-ai-agents-with-new-nvidia-nemotron-vision-rag-and-guardrail-models/)** (2025-10)
  * **進階防護**：雖然日期較早，但其探討的「安全護欄 (Guardrail)」與「視覺 (Vision)」整合概念，至今仍是企業 AI 系統防禦機制的必備參考。

---

## Fine-tuning
**🛠️ LLM 微調技術與實戰指南 (Fine-tuning & Distillation)**

在企業應用場景中，開源大模型往往需要經過「微調 (Fine-tuning)」才能成為特定領域的專家。本區塊為開發者梳理了從顯存估算、底層理論、到零程式碼實作的完整「煉丹」路徑。

### 1. 課前必讀：硬體門檻與顯存估算 (VRAM)
微調模型最常遇到的痛點就是「Out of Memory (OOM)」。在開始訓練前，精準估算所需的顯示卡記憶體是成功的第一步。
* **[大模型所需 GPU 記憶體筆記](https://mp.weixin.qq.com/s/M_hdtR7mVq14MnaaL0MAUw)**：快速了解參數規模 (7B, 72B) 對應的硬體需求。
* **[不同微調方法下所需的顯存總結](https://www.datalearner.com/blog/1051703254378255)**：比較全參數微調 (Full-tuning) 與 LoRA 等不同策略對顯存的實際消耗差異。

### 2. 理論心法：選擇正確的微調策略
了解底層邏輯，才能選對訓練工具。
* **[主流微調技術全解](https://zhuanlan.zhihu.com/p/643941480)**：適合初學者的概念掃盲，涵蓋 SFT (監督微調)、LoRA、P-tuning v2 與 Freeze 等主流方法。
* **[LoRA vs 完全微調差異解析](https://www.jiqizhixin.com/articles/2024-11-11-5)**：進階閱讀。透過 MIT 論文深入探討為何 LoRA 能在大幅降低算力成本的同時，保持極高的模型效能。
* **[大模型微調全生命週期解析](https://www.53ai.com/news/finetuning/2025022604125.html)**：從資料準備到模型評估的宏觀指南。

### 3. 實戰路徑：DeepSeek-R1 與零程式碼微調教學
想把 DeepSeek-R1 訓練成專屬的領域專家，卻不會寫複雜的訓練代碼？以下是為開發者量身打造的「從零到一」 LLaMA Factory 實戰路徑：
1. **資料集準備**：[如何建立高品質的微調資料集？](https://zhuanlan.zhihu.com/p/1916489160333714285) (垃圾進，垃圾出，這是最重要的一步)
2. **參數設定與優化**：[微調參數設置與顯存最佳化技巧](https://mp.weixin.qq.com/s/AbyWaTaPOp9sr5mz5SOVwg)
3. **訓練觀測與部署**：[如何觀測微調過程？模型如何合併與匯出部署？](https://mp.weixin.qq.com/s/6sNGvqLktPk6AP7kPs9JyA)
4. **領域專家實戰**：[完整案例：如何把 DeepSeek-R1 微調為領域專家](https://zhuanlan.zhihu.com/p/25054526736) | [從0到1微調安全大模型](https://mp.weixin.qq.com/s/hzdcutEL9yH1j8svMcXPGg)

### 4. 必備微調與蒸餾開源框架 (Frameworks)
依據您的算力資源與技術背景，挑選最適合的訓練武器：

* **[LLaMA Factory (地表最強零代碼微調)](https://github.com/hiyouga/LLaMA-Factory)**
  * **適用場景**：企業快速導入、無深度 AI 背景的開發者。
  * **特色亮點**：提供直覺的 WebUI 介面，支援海量開源模型與多卡平行運算，輕鬆完成 LoRA、SFT 與 RLHF 微調。[👉 中文文檔](https://github.com/hiyouga/LLaMA-Factory/blob/main/README_zh.md) | [👉 單卡訓練 Agent 實戰](https://zhuanlan.zhihu.com/p/678989191)
* **[Unsloth / Unsloth Studio (低算力救星)](https://github.com/unslothai/unsloth)**
  * **適用場景**：算力有限（如單張 RTX 4090）的本地端開發者。
  * **特色亮點**：極致優化的訓練速度與顯存佔用。提供開源 Web UI，在統一介面中完成訓練與模型匯出。[👉 官方微調技巧](https://mp.weixin.qq.com/s/COZfH_h36nX33TZGBVn0rg)
* **[EasyDistill (模型落地與端側部署必備)](https://github.com/modelscope/easydistill)**
  * **適用場景**：需大幅降低雲端推論成本，或實現手機端 AI 部署的企業。
  * **特色亮點**：阿里開源的知識蒸餾管線。能將千億參數巨獸的能力，無損轉移到微型模型上，解決大模型「算力成本過高」的致命痛點。
* **[Torchtune (PyTorch 官方原生架構)](https://github.com/pytorch/torchtune)**
  * **適用場景**：PyTorch 生態系重度使用者、底層研究人員。
  * **特色亮點**：程式碼極度乾淨、高度模組化，適合進行深度魔改與客製化訓練。[👉 Llama3.1 知識蒸餾實戰](https://pytorch.ac.cn/torchtune/stable/tutorials/llama_kd_tutorial.html)

### 資料集準備 (Datasets)
- **微調資料集實戰**
  - 資源：[📝 資料集怎麼搞？](https://zhuanlan.zhihu.com/p/29522986573) | [📝 LLaMA Factory 資料集建立](https://zhuanlan.zhihu.com/p/1916489160333714285)
- **Easy Dataset**
  - 說明：大模型微調資料集生產工具
  - 資源：[📝 知乎專欄](https://zhuanlan.zhihu.com/p/1908313086064042177)
- **OpenDeepWiki**
  - 說明：根據現有檔案產生微調資料集
  - 資源：[📝 知乎專欄](https://zhuanlan.zhihu.com/p/1908831694879985815)
- **COIG-CQIA**
  - 說明：零一萬物發布高品質中文指令微調數據
  - 資源：[📝 知乎專欄](https://zhuanlan.zhihu.com/p/694434197)

---

## AI-Agent
**🧩 AI Agent 開源框架**
> 概念說明請見：[避開 AI 代理 (AI Agents) 與 代理式人工智慧 (Agentic AI) 開發陷阱](https://deep-learning-101.github.io/agent)

### 🧠 核心概念與必讀文章：看懂 AI Agent 與 Agentic AI

在開發智能代理之前，理解底層邏輯與安全邊界至關重要。以下文獻涵蓋了從概念釐清、工作流設計到資安防護的必備知識：

* **[Agentic AI 與 AI Agents 的概念差異解析](https://www.alphaxiv.org/abs/2505.10468)**
  * **必讀原因**：釐清業界最容易混淆的兩個名詞。探討「AI 代理 (AI Agents)」作為單一執行體，與「代理式人工智慧 (Agentic AI)」作為系統性架構的分類學、應用場景與未來挑戰。
* **[Agentic AI 的資安威脅與緩解策略 (OWASP 官方指南)](https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations/)**
  * **必讀原因**：AI 失控怎麼辦？國際資安權威 OWASP 針對代理式 AI 可能面臨的 Prompt Injection (提示詞注入) 與權限濫用，提供了系統性的防禦與緩解架構 (Mitigations)。
* **[AI 搜尋引擎的致命傷：引用來源問題 (Citation Problem)](https://www.cjr.org/tow_center/we-compared-eight-ai-search-engines-theyre-all-bad-at-citing-news.php)**
  * **必讀原因**：當 AI 代理負責搜尋與總結時，如何避免侵權與幻覺？本文評測了八大 AI 搜尋引擎，揭露其在新聞與來源引用上的缺陷，是開發檢索代理 (Search Agent) 的重要借鏡。

---

### 🔄 Agent 工作流 (Workflow) 入門指南
AI Agent 的強大不在於單打獨鬥，而在於流程設計。以下精選教學幫助您從零建構多智能體系統：
* **基礎掃盲**：[萬字長文綜觀 Agent 發展史](https://zhuanlan.zhihu.com/p/29833831482) | [Agentic AI 的核心區別](https://zhuanlan.zhihu.com/p/705935464)
* **實戰架構**：[從單一 Agent 到複雜 Workflow 的演進](https://zhuanlan.zhihu.com/p/32491596217) | [什麼是 Agentic 工作流程？](https://zhuanlan.zhihu.com/p/32709535995)

---

### 💼 領域專用 Agent 實戰案例 (Finance & Coding)
* **[FinRobot (開源金融 AI 代理)](https://deepwiki.com/AI4Finance-Foundation/FinRobot)**
  * **應用場景**：專為金融分析打造的 Agent 框架，支援最新 Gemini 2.5 模型，能自動化執行財報分析、市場預測等量化任務。[👉 AlphaXiv 論文解析](https://www.alphaxiv.org/zh/overview/2405.14767)
* **[Jupyter-AI (程式碼編寫代理)](https://deepwiki.com/jupyterlab/jupyter-ai)**
  * **應用場景**：將生成式 AI 原生接入 Jupyter Notebook，支援 Gemini 2.5，能理解您的數據上下文並自動生成、除錯 Python 程式碼，是數據科學家的最強副駕。

---

### 🧩 2026 必備 AI Agent 開源框架與開發工具 (依據應用場景分類)

在 Agentic AI 時代，選擇正確的框架能讓開發事半功倍。以下依據「應用場景」精選目前 GitHub 上最活躍、最具生產力的 AI Agent 開源專案：

#### 1. 個人全自動化助理與通用 Agent (Personal & General Assistants)
* **[OpenClaw (原 Moltbot/Clawdbot)](https://openclaw.ai/)** `[2026-01-20]` 🔥 *(2026現象級專案)*
  * **特色**：你電腦上的全天候數位管家。可直接串接 Line、Telegram、WhatsApp 等通訊軟體，接收指令並**實際操作你的電腦**（如整理信箱、操作網頁）。
  * **必讀資源**：
    * [官方簡體中文文件](https://docs.openclaw.ai/zh-CN)
    * [深度技術與資安風險分析](https://deep-learning-101.github.io/LLM/OpenClaw-Moltbot-Clawdbot)
    * [白話文分析 ](https://blog.twman.org/2026/02/OpenClaw.html)
    * [ZeroClaw (低功耗部署版)](https://github.com/zeroclaw-labs/zeroclaw)
    * [DeepWiki](https://deepwiki.com/openclaw/openclaw)
    * [Zread](https://zread.ai/openclaw/openclaw)
    * [公眾號解讀 1](https://mp.weixin.qq.com/s/yFi8lWLWp7NPDO-zD6QW_Q)
    * [公眾號解讀 2](https://mp.weixin.qq.com/s/1ikfiU_eGnL5FRaPRddA2Q)
    * [知乎解讀](https://zhuanlan.zhihu.com/p/1999109634909303005)
    * [2026年OpenClaw Skills排行榜：Top 20必裝清單](https://mp.weixin.qq.com/s/wCoo-h4dEkxLjZo-lOsVmQ)
* **[Gemini CLI](https://github.com/google-gemini/gemini-cli)** `[2025-06-25]`：將 Google Gemini 轉化為終端機 (Terminal) 開源代理，開發者日常指令輔助利器。
* **[Agent Zero](https://github.com/frdel/agent-zero)** `[2025-06-01]`：主打全能 AI 代理，涵蓋 APP 生成、程式碼編寫與 RAG 應用。
* **[Lemon AI](https://github.com/hexdocom/lemonai)** `[2025-05-28]`：全球首款全端開源通用 AI Agent 框架。
* **[smolagents (Hugging Face 出品)](https://github.com/huggingface/smolagents)** `[2025-01-03]`：主打「程式碼即工具」，只需極少 Python 程式碼就能將任何開源 LLM 轉化為智能體。

  ---

#### 2. 複雜工作流與多智能體編排 (Workflow & Multi-Agent)
* **[DeerFlow 2.0 (字節跳動)](https://github.com/bytedance/deer-flow/blob/main/README_zh.md)** `[2026-03-26]`：從 Deep Research 升級的 Super Agent Harness，將 sub-agents、memory 和 sandbox 有機組織，能處理極度複雜任務。
* **[Agno](https://zread.ai/agno-agi/agno/)** `[2025-11]`：專注於高效能的多智能體 (Multi-agent) 系統框架。
* **[Microsoft Agent Framework](https://github.com/microsoft/agent-framework)** `[2025-08-29]`：微軟官方開發套件，專為 .NET 和 Python 開發者設計的企業級工作流。
* **[Agent-Squad (AWS Labs)](https://deepwiki.com/awslabs/agent-squad)** `[2025-05-18]`：輕量級的開源多智能體框架。
* **[FlowGram (字節跳動)](https://github.com/bytedance/flowgram.ai)** `[2025-05-10]`：開源版的 Coze 核心視覺化工作流引擎。
* **[Agent Development Kit (ADK)](https://github.com/google/adk-python)** `[2025-04-03]`：Google 官方釋出的智能體開發工具包。

---

#### 3. 深度研究與開源知識庫 (Deep Research & RAG)
* **[Tongyi DeepResearch](https://zread.ai/Alibaba-NLP/DeepResearch)** `[2025-10-28]`：阿里通義全面開源的深度研究框架，對標並試圖超越 OpenAI 閉源能力。
* **[DeepAgent](https://zread.ai/RUC-NLPIR/DeepAgent)** `[2025-10-28]`：業界首個全自主的深度推理智能體。
* **[SurfSense](https://zread.ai/MODSetter/SurfSense)** `[2025-05-11]`：萬星開源王炸，能完美整合並檢索 Slack、Notion、Jira 等四散的企業知識庫。
* **[MiroThinker](https://github.com/MiroMindAI/MiroThinker)** `[2025-08-29]`：針對學術研究和趨勢預測進行最佳化的深度研究代理。
* **開源 Perplexity 替代方案** `[2025-06-03]`：包含 [Gemini Fullstack LangGraph](https://deepwiki.com/google-gemini/gemini-fullstack-langgraph-quickstart) 與 [Perplexica](https://github.com/ItzCrazyKns/Perplexica)，適合自建 AI 搜尋引擎。
* **[PandaWiki](https://github.com/chaitin/PandaWiki)** `[2025-06-06]`：新一代 AI 大模型驅動的開源知識庫系統。
* **[AutoAgent](https://github.com/HKUDS/AutoAgent)** `[2025-04-03]`：港大打造的強大 Deep Research 開源框架。
* **[DeepSearcher](https://zread.ai/zilliztech/deep-searcher)** `[2025-03-20]`：私有資料庫結合 DeepSeek 打造的本地研究智能體。

---

#### 4. 電腦操作與軟體工程師 (Computer Use & Coding)
* **[Gemini Computer Use](https://github.com/google-gemini/computer-use-preview)** `[2025-10]`：Google 預覽版框架，讓 AI 直接操作網頁介面。
* **[WebDancer](https://www.alphaxiv.org/zh/overview/2505.22648)** `[2025-05-30]`：Alibaba 開源的 WebAgent，專精於網頁資料的自主瀏覽與操作。
* **[OpenHands (Devin 平替)](https://github.com/All-Hands-AI/OpenHands)** `[2025-05-25]`：具備完整沙盒執行環境，能自主寫 Code、修 Bug。
* **[Deepsite](https://huggingface.co/spaces/enzostvs/deepsite)** `[2025-04-03]`：基於 DeepSeek 的網頁開發智能體。
* **[DeepGemini](https://github.com/sligter/DeepGemini)** `[2025-03-30]`：被譽為 AI 界搭積木神器。
* **[autoMate](https://github.com/yuruotong1/autoMate)** `[2025-03-11]`：基於 OmniParser 的 AI 自動化 GUI 助手。
* **[OmniParser](https://github.com/microsoft/OmniParser)** `[2024-10-26]`：微軟開源的核心技術，將純視覺輸入轉化為可操作的 UI 元素。

---

#### 5. Manus 開源平替專區 (Manus Alternatives)
Manus 在 2025 年掀起了全自動代理狂潮，以下為開源社群的最強復刻版本：
* **[AI Manus](https://deepwiki.com/Simpleyyt/ai-manus)** `[2025-05-07]`
* **[suna](https://github.com/kortix-ai/suna)** `[2025-04-24]`：高關注度的輕量級復刻版。
* **[釦子空間 (Coze Space)](https://space.coze.cn/)** `[2025-04-22]`：字節跳動推出的類 Manus 解決方案。
* **[AgenticSeek](https://github.com/Fosowl/agenticSeek)** `[2025-03-24]`：主打「完全本地化部署」的 Manus 替代品。
* **[OpenManus](https://github.com/mannaandpoem/OpenManus)** `[2025-03-10]`：最知名、基礎的開源版。

---

#### 6. 特定場景應用 (Domain-Specific Automation)
* **[Paper2Poster](https://paper2poster.github.io/)** `[2025-06-02]`：學術利器，自動為 PDF 論文產生精美的發表海報。
* **[MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo)** `[2025-02-28]`：自媒體神器，AI 自動生成高清短影音工作流。

---

## Tools
**🛠️ 開發工具 (Tools & Protocols)**

### 🔍 RAG 檢索增強生成：從入門到次世代架構 (Retrieval-Augmented Generation)

傳統的 RAG (文本切塊 + 向量檢索) 已無法滿足企業對複雜排版、長文本與精準推理的需求。以下精選 2025-2026 年最具突破性的 RAG 開源框架，依據「技術流派與解決痛點」為您分類：

#### 1. 顛覆傳統：無切塊與 Agentic RAG 架構
放棄傳統向量資料庫，運用 AI 推理能力進行導航，解決長文檔檢索破碎的問題。

* **[PageIndex](https://zread.ai/VectifyAI/PageIndex)** `[2026-03-01]` | 授權：MIT
  * **技術突破**：UCL 團隊開發的 Agentic RAG 革命性開源專案。完全拋棄「向量庫」與「文本切片 (Chunking)」，改用大模型進行推理導航。
  * **解決痛點**：在超長文檔檢索中達到 98% 的驚人準確率，徹底重塑 RAG 的底層邏輯。[🌐 線上體驗](https://chat.pageindex.ai/) | [📝 公眾號教學](https://mp.weixin.qq.com/s/iivoQtqzLhFA69N5iaOvzQ) | [📝 深度解讀](https://mp.weixin.qq.com/s/wwRJYvRl_jFaiiJkdrJdgw)
* **[LinearRAG](https://github.com/DEEP-PolyU/LinearRAG)** `[2025-11-20]`
  * **技術突破**：全新的高效 RAG 框架，主打「無需進行複雜的關係抽取 (Relation Extraction)」，大幅降低構建知識庫的算力與時間成本。[📝 知乎解讀](https://zhuanlan.zhihu.com/p/1975321777342260763)

#### 2. 資料清洗與多模態解析 (Data Parsing & Multi-modal)
RAG 的成敗取決於資料輸入的品質。這些工具專精於處理複雜表格、圖片與數學公式。

* **[OpenDataLoader](https://github.com/opendataloader-project/opendataloader-pdf)** `[2026-03-20]`
  * **核心優勢**：在極度困難的「表格擷取」任務中拿下 0.93 的超高準確率。主打「不追求極限速度，但精準度無可挑剔」的穩健策略，是企業處理 PDF 財報與數據報表的神兵利器。[📝 公眾號解讀](https://mp.weixin.qq.com/s/mPjH0dTyAMLKL5Hq5KPqCw)
* **[RAG-Anything](https://github.com/HKUDS/RAG-Anything)** `[2025-07-02]`
  * **核心優勢**：港大 HKUDS 團隊打造的「全能多模態 RAG 系統」。能一鍵自動解析 PDF、Word、PPT 中的文字、圖片、複雜表格與公式，並無縫映射到知識圖譜 (KG) 中。極度適合金融財報、醫療病歷或科研文獻的深度推理。[📄 論文](https://arxiv.org/pdf/2510.12323) | [📝 36Kr 解讀](https://m.36kr.com/p/3358608090400776) | [📝 Milvus 實戰解析](https://milvus.io/zh-hant/blog/multimodal-rag-made-simple-rag-anything-milvus-instead-of-20-separate-tools.md)

#### 3. 圖譜增強與全局語意 (Graph-RAG)
解決傳統 RAG「只見樹木，不見森林」的問題，強化實體之間的邏輯關聯。

* **[LightRAG](https://github.com/HKUDS/LightRAG)** `[2024-12-19]` 
  * **核心優勢**：港大 HKUDS 團隊打造的結合圖結構 (Graph) 與雙層檢索機制，精準提取文件中的實體關聯。極度適合用於建構企業級法律合規知識庫、醫療問答系統等需要「高度準確性」與「防幻覺 (Anti-Hallucination)」的嚴苛場景。[📄 EMNLP2025 論文](https://arxiv.org/pdf/2410.05779) | [📝 技術框架解讀](https://zhuanlan.zhihu.com/p/13261291813)

#### 4. 實戰與競賽冠軍方案 (Battle-Tested Solutions)
* **[KohakuRAG](https://zread.ai/KohakuBlueleaf/KohakuRAG)** `[2026-03-14]` | 授權：Apache-2.0
  * **核心優勢**：經過頂級賽事淬鍊的實戰架構！這是 Kaggle RAG 競賽 (WattBot 2025) 的冠軍開源方案，適合想要直接抄作業、部署高效能 RAG 的開發者。[📝 公眾號教學](https://mp.weixin.qq.com/s/hUsr55bXBrHor0kHMo9htg)

### 🔌 MCP 協議生態與實戰工具 (Model Context Protocol)

MCP (Model Context Protocol) 是賦予大語言模型「使用外部工具」與「讀取本地端資料」的關鍵標準協議。以下精選 2025 下半年最具代表性的 MCP 伺服器建置框架與應用模組，幫助開發者快速打通 AI 與外部系統的任督二脈：

#### 1. 基礎設施與伺服器快速建置 (Infrastructure & Server Setup)
解決傳統手動編寫 MCP 伺服器耗時、繁瑣的痛點，實現快速封裝與部署。

* **[FastAPI-MCP](https://zread.ai/tadata-org/fastapi_mcp)** `[2025-08-20]`
  * **核心優勢**：將傳統 API 一鍵轉化為 AI 可讀工具！能將現有的 FastAPI 介面無縫、低成本地升級為標準的 MCP 工具服務，極大幅度降低後端開發門檻。[📝 公眾號教學](https://mp.weixin.qq.com/s/L568EP2tl2zwmC8vxz8s7w)
* **[automcp](https://github.com/NapthaAI/automcp)** `[2025-04-15]`
  * **核心優勢**：主打「秒級設定」的 MCP 伺服器建構工具，讓開發者跳過繁雜的底層通訊協定配置，直接專注於業務邏輯的開發。[📝 公眾號介紹](https://mp.weixin.qq.com/s/x-aZEhtnRYPFno81Fb9ttw)

#### 2. 自動化測試與網頁操控 (Automation & Web Control)
賦予大模型「眼睛」與「雙手」，讓 AI 能夠直接與動態網頁互動。

* **[playwright-mcp](https://github.com/microsoft/playwright-mcp)** `[2025-03-14]`
  * **核心優勢**：微軟開源的 AI 網頁自動化神器！結合強大且穩定的 Playwright 引擎，讓你的 AI Agent 透過 MCP 具備模擬人類點擊、滾動瀏覽器，以及抓取動態網頁資料的能力。[📝 知乎解讀](https://zhuanlan.zhihu.com/p/30178146112)

#### 3. 開發者工具與程式碼理解 (Developer Tools & Codebase)
讓 AI 成為你的最強 Code Reviewer，直接對接龐大的專案架構。

* **[GitMCP](https://github.com/idosal/git-mcp)** `[2025-04-05]`
  * **核心優勢**：讓 AI 秒懂 GitHub 龐大專案的利器。不用再辛苦地複製貼上程式碼，透過 GitMCP，AI 能直接存取、檢索並理解整個 Git 儲存庫的架構與歷史紀錄。[📝 53AI 報導](https://www.53ai.com/news/RAG/2025040590146.html)

#### 4. 社群通訊平台串接 (Social Media & Chatbots)
將大模型的強大能力，無縫接入日常使用的通訊軟體中。

* **[line-bot-mcp-server](https://github.com/line/line-bot-mcp-server)** `[2025-04-10]`
  * **核心優勢**：LINE 官方專案。將 LINE 官方帳號 (LINE Bot) 直接接入 MCP 生態系，讓開發者能輕鬆打造出可以靈活調用外部工具的「超級 LINE 機器人」。

---

### 🖱️ 深度聚焦：Browser-use 生態系與實戰路徑 (Browser Automation & Manus Alternatives)

從 2025 到 2026 年，AI Agent 正式從「純文本對話」進化為「代替人類操作電腦 (Actionable AI)」。以下精選目前最強大的開源瀏覽器自動化與 RPA (機器人流程自動化) 框架，它們是商用工具（如 Manus）的最佳免費平替方案：

| 框架/工具名稱 | 開發團隊/生態 | 💡 解決什麼痛點？ (核心優勢) | 🚀 推薦適用場景 & 規格標籤 |
| :--- | :--- | :--- | :--- |
| **OpenClaw** | 🌐 **開源社群** | **跑在本地的 AI 助手**。強調在地端環境運行，保障隱私與資料安全。 | 本地端資料處理、隱私優先企業<br>`[本地部署]` `[隱私安全]` |
| **Browser-use** | 🌐 **國際開源社群** | **讓 AI 像人一樣上網**。支援錄製工作流，一次錄製永久自動操作網頁。 | 網頁自動化測試、動態網頁爬蟲<br>`[瀏覽器自動化]` `[可錄製]` |
| **Gemini Computer Use** | 🇺🇸 **Google** | **直接操控作業系統**。Google 官方推出的代理工具，讓 AI 能直接理解並操作你的電腦介面。 | 跨 APP 自動化操作、系統級 RPA<br>`[Google生態]` `[系統控制]` |
| **OmniParser** | 🇺🇸 **Microsoft** | **精準解析 UI 元素**。微軟開源的強大視覺智能體，能看懂手機與電腦畫面的按鈕與架構。 | UI 自動化測試、多模態輸入<br>`[微軟開源]` `[UI解析]` |
| **OpenManus / suna** | 🇨🇳/🌐 **開源社群** | **Manus 的開源平替**。解決商用 Agent 昂貴的問題，提供高度相似的任務執行能力。 | 個人開發者、快速概念驗證<br>`[Manus平替]` `[低成本]` |

---

#### 🔍 深度聚焦：Browser-use 生態系與實戰路徑
在上述框架中，**Browser-use** 因其極高的開源活躍度，已發展出完整的工具鏈。如果您想讓 AI 幫您自動訂票、抓取動態網頁資料或執行重複性任務，請參考以下學習路徑：

* **核心底層與原理解析**
  * **[Browser-use 官方 GitHub](https://github.com/browser-use/browser-use)**：專案核心庫。
  * **[原理解析：讓 AI 像人類一樣使用瀏覽器](https://zhuanlan.zhihu.com/p/20038156945)** `[2025-01-23]`：初學者必讀！深入了解其底層邏輯與 DOM 樹解析技術。

* **零程式碼 / 視覺化操作 (WebUI)**
  * *痛點：不想寫複雜的 Python 腳本來啟動 Agent？*
  * **[browser-use-webui 部署教學](https://zhuanlan.zhihu.com/p/24116360552)** `[2025-02-16]`：手把手教你在本地端架設視覺化操作介面。
  * **[官方 Web-UI 專案](https://github.com/browser-use/web-ui)** `[2025-04-16更新]`：提供友善的圖形化介面，點擊即可指派網頁任務。[👉 DeepWiki 實操指南](https://deepwiki.com/search/_bfd33aa8-cd79-4f1d-a1e8-5620d4374329)

* **進階自動化：錄製與重複執行 (Workflow)**
  * *痛點：每次都要重新下 Prompt 指令太麻煩？*
  * **[workflow-use (工作流錄製神器)](https://github.com/browser-use/workflow-use)** `[2025-06-04]`：Browser-use 生態系的殺手級應用。主打「一次錄製，永久自動操作」，能將 AI 的執行路徑打包成標準化腳本，是企業打造自動化 RPA 的終極武器。

---

### 深度研究 (Deep Research) 與多智能體工作流

| 框架/工具名稱 | 開發團隊/生態 | 💡 解決什麼痛點？ (核心優勢) | 🚀 推薦適用場景 & 規格標籤 |
| :--- | :--- | :--- | :--- |
| **Tongyi DeepResearch** | 🇨🇳 **阿里巴巴** | **開源版深度研究**。通義全面開源，標榜效能超越 OpenAI 的閉源研究框架。 | 學術文獻統整、深度產業報告生成<br>`[大廠開源]` `[深度研究]` |
| **Agno** | 🌐 **開源社群** | **高效能 Multi-agent**。專注於多個 AI 智能體之間的協作與任務分發。 | 複雜專案拆解、軟體開發協作<br>`[多智能體]` `[高效能]` |
| **FlowGram** | 🇨🇳 **字節跳動** | **Coze 核心引擎開源**。強大的視覺化工作流引擎，適合構建複雜的邏輯鏈。 | 企業級 AI 服務編排、Chatbot 後台<br>`[工作流引擎]` `[可視化]` |
| **AutoAgent** | 🇭🇰 **香港大學** | **學術界最強大腦**。港大打造的開源 Deep Research 工具，學術底蘊深厚。 | 大學研究室、論文自動化分析<br>`[學術開源]` `[文獻分析]` |

---

### 📊 AI 簡報生成神器 (AI PPT & Slides Automation)

傳統的 PPT 製作耗時且高度依賴排版技巧。隨著生成式 AI 的進步，AI 簡報工具已從初期的「套用固定模板」，進化到「無模板自由生成」與「像素級逆向還原」。以下精選目前 GitHub 上最受關注的開源 AI PPT 解決方案：

### 1. 學術前沿與無模板自由生成 (Advanced & Template-Free Generation)
解決傳統 AI 簡報工具「排版死板、只能套模板」的致命痛點，真正實現高度自由的內容渲染。

* **[PPTAgent V2](https://github.com/icip-cas/PPTAgent)** `[2026-03-03]` 🔥
  * **核心優勢**：由中科院團隊開發（V1 曾發表於 EMNLP 2025）。V2 版本迎來重磅升級，徹底打破傳統套模板的限制，實現**無模板自由生成**。內建的 DeepPresenter 模組刷新了產業榜單，支援渲染後即時糾錯與修改程式碼，是將長篇文件轉化為高品質 PPT 的學術級首選。
  * **必讀資源**：[📝 公眾號推薦](https://mp.weixin.qq.com/s/2AEZpsC4wphAcpp5LtGqnw) | [📝 知乎推薦 (2025-01-13)](https://zhuanlan.zhihu.com/p/18105237248)
* **[Edit-Banana](https://github.com/BIT-DataLab/Edit-Banana)** `[2026-02-23]`
  * **核心優勢**：北京理工大學與亞利桑那大學團隊聯手打造。具備極強的「像素級逆向還原能力」，成功打通了 AIGC 繪圖與簡報排版落地的最後一哩路，適合對視覺呈現要求極高的專業簡報者。

### 2. 快速生成與本地部署方案 (Local Deployment & Quick Generation)
適合企業內部使用，解決雲端生成可能帶來的商業機密外洩風險，或追求極致的生成速度。

* **[presenton](https://github.com/presenton/presenton)** `[2025-07-26]`
  * **核心優勢**：主打**本地部署**的開源神器！確保資料不外流的前提下，只需輸入文本即可一鍵生成精美 PPT，是企業內網使用的最佳平替方案。[📝 公眾號推薦](https://mp.weixin.qq.com/s/QTMVGD_aP41qrwtbjLxV8Q)
* **[LangChat Slides](https://github.com/langchat/langchat-slides)** `[2026-01-04]`
  * **核心優勢**：由 LangChat 團隊開發的智慧幻燈片工具，提供流暢的生成式 AI 互動體驗。[🌐 線上 DEMO](https://slides.langchat.cn/) | [📝 掘金深度解讀](https://juejin.cn/post/7591861857465778214)
* **[banana-slides](https://github.com/Anionex/banana-slides)** `[2025-12-13]`
  * **核心優勢**：基於 nanobananapro🍌 的原生 AI PPT 應用。主打打造具有氛圍感與設計張力的「Vibe PPT」，適合行銷提案或創意展示。[📝 公眾號推薦](https://mp.weixin.qq.com/s/XXyCnEdrTVoK-m-EAW69nA)

### 3. 多智能體協同架構 (Multi-Agent Workflows)
將簡報製作拆解為「大綱規劃」、「資料檢索」、「視覺設計」等多個環節，交由不同的 AI 代理並行處理。

* **[MultiAgentPPT](https://github.com/johnson7788/MultiAgentPPT)** `[2025-07-03]`
  * **核心優勢**：引入 Multi-agent (多智能體) 並發處理機制。透過讓不同的 Agent 分工合作，大幅提升複雜簡報的生成速度與內容邏輯的嚴密性。[📝 知乎原理解讀](https://zhuanlan.zhihu.com/p/1920611446007497267)

---

### 🌍 知識管理革命：開源 AI PPT 與 NotebookLM 替代方案

| 專案名稱 | 分類 | 💡 解決什麼痛點？ (核心優勢) | 🚀 推薦適用場景 & 規格標籤 |
| :--- | :--- | :--- | :--- |
| **notebooklm-py / Notex** | NotebookLM 平替 | **隱私優先的知識庫**。提供類似 NotebookLM 的互動體驗，但支援命令列操作與本地部署。 | 企業內部文件庫、個人離線筆記本<br>`[開源平替]` `[重視隱私]` |
| **PageLM** | NotebookLM 平替 | **互動式學習神器**。把學習材料丟進去，自動生成互動式學習內容。 | 教育培訓、長篇報告快速消化<br>`[互動學習]` `[文件分析]` |
| **Edit-Banana** | AI PPT | **像素級逆向還原**。不直接生圖，而是理解、規劃再優化，打通 AI 簡報落地的最後一哩路。 | 專業商業簡報、學術海報生成<br>`[高質感排版]` `[學術開源]` |
| **MultiAgentPPT** | AI PPT | **多智能體協作生 PPT**。利用多個 Agent 並發處理大綱、文案與排版，速度極快。 | 急件簡報製作、大綱快速展開<br>`[多智能體]` `[自動排版]` |

-----

## NotebookLM 平替
**🌍 NotebookLM 平替**

- 2026-01-20 | **notebooklm-py**
  - 說明：將NotebookLM完整接入命令列環境，讓AI知識處理邁入自動化新紀元
  - 資源：[🐙 GitHub](https://github.com/teng-lin/notebooklm-py) | [📝 公眾號推薦](https://mp.weixin.qq.com/s/rATp6AhcQOzFe4t2QnA07w)
- 2026-01-04 | **Notex**
  - 說明：一個開源 NotebookLM 替代方案的實現
  - 資源：[🐙 GitHub](https://github.com/smallnest/notex) | [📝 公眾號推薦](https://mp.weixin.qq.com/s/65epWwIC7Lqalwh-WuoP3Q)
  - [DEMO](https://notex.rpcx.io/)
- 2025-12-12 | **PageLM**
  - 說明：把學習材料丟進去，互動式學習內容就出來
  - 資源：[🐙 GitHub](https://github.com/lfnovo/open-notebook) | [📝 知乎解讀](https://zhuanlan.zhihu.com/p/1980701578559234518) | [📝 公眾號解讀](https://mp.weixin.qq.com/s/3o8RcHicjt5FRdSzG_qGUw)
- 2025-12-06 | **Open NoteBook**
  - 說明：一個開源的、注重隱私的Google Notebook LM 替代方案
  - 資源：[🐙 GitHub](https://github.com/lfnovo/open-notebook) | [📝 公眾號解讀](https://mp.weixin.qq.com/s/Kncslf0XL1ucdPpQX_-a1g)
- 2025-12-06 | **Auto-Slides**
  - 說明：不只是幫你寫，還能幫你講。它讓論文第一次有機會“開口說話”
  - 資源：[🐙 GitHub](https://github.com/Westlake-AGI-Lab/Auto-Slides) | [📝 知乎解讀](https://zhuanlan.zhihu.com/p/1953393379334391701)

---

### 效率工具 (Efficiency Tools)
- 2026-02-24 | **PaperBanana**
  - 說明：核心思想是參考驅動+多智能體合作。它不會直接產生圖像，而是先理解、再規劃、再美化、最後迭代優化。
  - 資源：[🐙 GitHub](https://dwzhu-pku.github.io/PaperBanana/) | [📝 arxiv](https://arxiv.org/pdf/2601.23265)

- 2025-11-26｜**Crawl4AI**
  - 說明：對LLM 友善的網頁爬蟲和抓取工具，它將網頁內容轉化為乾淨、適合LLM 處理的Markdown 格式，非常適用於RAG (檢索增強生成)、智能代理和資料管道等場景。
  - 資源：[📝 zread](https://zread.ai/unclecode/crawl4ai) | [📝 公眾號解讀](https://mp.weixin.qq.com/s/5cNfBbKOHHjGin5I7XYlpw)

- 2025-11-20｜**LinearRAG**
  - 說明：全新 RAG 框架，無需關係抽取
  - 資源：[🐙 GitHub](https://github.com/DEEP-PolyU/LinearRAG) | [📝 知乎解讀](https://zhuanlan.zhihu.com/p/1975321777342260763)

- 2025-09-11｜**DeepMCPAgent**
  - 說明：教你讓模型自己「找工具」
  - 資源：[📝 zread](https://zread.ai/cryxnet/DeepMCPAgent) | [📝 公眾號解讀](https://mp.weixin.qq.com/s/Sj_7i1mTJ9WYaTlCzIqCFA)

- 2025-07-30｜**LangExtract**
  - 說明：Gemini 驅動的資訊擷取庫
  - 資源：[🐙 GitHub](https://github.com/google/langextract) | [📝 Google Developers](https://developers.googleblog.com/zh-hans/introducing-langextract-a-gemini-powered-information-extraction-library/)

- 2025-07-30｜**EasySpider**
  - 說明：可視化網頁爬蟲工具，不需要寫程式碼，所有的爬蟲任務都可以透過簡單的圖形化介面完成。
  - 資源：[🐙 GitHub](https://github.com/NaiboWang/EasySpider) | [📝 公眾號解讀](https://mp.weixin.qq.com/s/9MPKTOXzjzMOC57YU9Pw4w)

- 2025-06-28｜**docext**
  - 說明：基於 Qwen2.5VL 的文檔解析工具
  - 資源：[🐙 GitHub](https://github.com/NanoNets/docext) | [📝 知乎解讀](https://zhuanlan.zhihu.com/p/1919760450024879687)

- 2025-06-10｜**Agentic-Doc**
  - 說明：LandingAI 開源，百頁文檔秒變結構化資料
  - 資源：[🐙 GitHub](https://github.com/landing-ai/agentic-doc) | [📝 知乎解讀](https://zhuanlan.zhihu.com/p/1914259475306612709)

- 2025-06-06｜**daily-arXiv-ai-enhanced**
  - 說明：每日爬取 arXiv 並用 LLM 產生中文摘要
  - 資源：[🐙 GitHub](https://github.com/dw-dengwei/daily-arXiv-ai-enhanced)

- 2025-05-22｜**AingDesk**
  - 說明：零門檻本地 AI 部署
  - 資源：[📚 DeepWiki](https://deepwiki.com/aingdesk/AingDesk) | [📝 知乎解讀](https://zhuanlan.zhihu.com/p/29773848356)

- 2025-05-20｜**news-agents**
  - 資源：[📚 DeepWiki](https://deepwiki.com/eugeneyan/news-agents)

- 2025-05-16｜**Follow**
  - 說明：資訊聚合神器
  - 資源：[📚 DeepWiki](https://deepwiki.com/RSSNext/Folo) | [📝 知乎推薦](https://zhuanlan.zhihu.com/p/1906505020628795653)

- 2025-05-11｜**SurfSense**
  - 說明：打通 Notion/GitHub 的 AI 超腦
  - 資源：[🐙 GitHub](https://github.com/MODSetter/SurfSense) | [📝 公眾號推薦](https://mp.weixin.qq.com/s/kMhidgb6GkKEsl-D-u_7iw) | [📚 如何使用](https://deepwiki.com/search/_df4a192b-a253-4155-a2a2-4a6fda9037e9)

- 2025-04-28｜**PaperCoder (Paper2Code)**
  - 說明：Automating Code Generation from Scientific Papers
  - 資源：[📚 DeepWiki](https://deepwiki.com/going-doer/Paper2Code) | [📄 AlphaXiv](https://www.alphaxiv.org/overview/2504.17192)

- 2025-04-16｜**OneFileLLM**
  - 說明：一鍵聚合網頁、程式碼、論文到剪貼簿
  - 資源：[🐙 GitHub](https://github.com/jimmc414/onefilellm) | [📝 公眾號推薦](https://mp.weixin.qq.com/s/qNYX65fw-IWzEBLZpuaY6Q)

- 2025-04-16｜**ScrapeGraphAI**
  - 說明：顛覆傳統爬蟲的痛點！透過 LLM 解析網頁結構，只需輸入自然語言提示（Prompt），就能自動適應網站改版，精準抓取所需資料。非常適合開發用來監控競品電商價格、自動化收集產業新聞，或建立 AI 訓練語料庫的高彈性爬蟲管線。
  - 資源：[🐙 GitHub](https://github.com/ScrapeGraphAI/Scrapegraph-ai) | [📝 公眾號推薦](https://mp.weixin.qq.com/s/lQukAy12V5K1cH6rTkqxaA)

- 2025-04-11｜**nanobrowser**
  - 說明：AI 驅動的瀏覽器自動化神器
  - 資源：[🐙 GitHub](https://github.com/nanobrowser/nanobrowser) | [📝 公眾號推薦](https://mp.weixin.qq.com/s/65SwCtDta1cKvx1_BbaoHQ)

- 2025-04-06｜**sqlchat**
  - 說明：讓資料庫管理像聊天一樣簡單
  - 資源：[🐙 GitHub](https://github.com/sqlchat/sqlchat) | [📝 公眾號推薦](https://mp.weixin.qq.com/s/kieSzWn3QDYvZ5Zx35hr1A)

- 2025-03-26｜**pdf-craft**
  - 說明：PDF 秒轉 Markdown/EPUB
  - 資源：[🐙 GitHub](https://github.com/oomol-lab/pdf-craft) | [📝 知乎推薦](https://zhuanlan.zhihu.com/p/1888288260171744707)

- 2025-03-25｜**OCRmyPDF**
  - 說明：能力分析
  - 資源：[🐙 GitHub](https://github.com/ocrmypdf/OCRmyPDF) | [📝 知乎分析](https://www.zhihu.com/tardis/zm/art/32745781279?source_id=1003)

- 2025-03-12｜**AingDesk**
  - 資源：[📚 DeepWiki](https://deepwiki.com/aingdesk/AingDesk) | [📝 知乎解讀](https://zhuanlan.zhihu.com/p/29773848356)

- 2025-02-25｜**PySpur**
  - 說明：拖曳式開發 AI 工作流程
  - 資源：[🌐 官網](https://www.pyspur.dev/) | [📝 知乎解讀](https://zhuanlan.zhihu.com/p/26161709083)

- 2025-01-13｜**DocAligner**
  - 說明：拍照文件復原 (校正、版面定位)
  - 資源：[🐙 GitHub](https://github.com/ZZZHANG-jx/DocAligner) | [📝 公眾號推薦](https://mp.weixin.qq.com/s/Bra9h3ExddB5NiH1g4uk1g)

- 2024-12-15｜**markitdown**
  - 資源：[🐙 GitHub](https://github.com/microsoft/markitdown)

---

## World Models
**🌍 World Models (世界模型)**

- 2025-09-25｜**Code World Model**
  - 說明：Yann LeCun 攜 320 億參數開源世界模型
  - 資源：[📝 Meta Research](https://zread.ai/facebookresearch/cwm/1-overview) | [📝 新浪報導](https://t.cj.sina.com.cn/articles/view/1746173800/68147f6801901e2wa)

---

## MoE
**🧠 MoE (混合專家模型)**

- 2024-12-13｜**DeepSeek-VL2**
  - 說明：VLM 邁入 MoE 時代
  - 資源：[🐙 GitHub](https://github.com/deepseek-ai/DeepSeek-VL2) | [📝 機器之心](https://mp.weixin.qq.com/s/s832KUgixNuX4GUkvY7_Ag) | [📝 公眾號](https://mp.weixin.qq.com/s/p6r_b-k4UnSJED5cBTedZg)

- **騰訊混元 (Hunyuan-Large)**
  - 說明：騰訊最大 MoE 大模型
  - 資源：[🐙 GitHub](https://github.com/Tencent/Hunyuan-Large) | [🤗 DEMO](https://huggingface.co/spaces/tencent/Hunyuan-Large) | [🤗 Model](https://huggingface.co/tencent/Hunyuan-Large) | [📝 機器之心](https://www.jiqizhixin.com/articles/2024-11-06-6)

---

## SLM
**📱 Small Language Models (小型語言模型)**

- 2024-12-13｜**Phi-4**
  - 說明：微軟 Phi-4 正式發表，以小博大
  - 資源：[🤗 HuggingFace](https://huggingface.co/NyxKrage/Microsoft_Phi-4) | [📝 公眾號](https://mp.weixin.qq.com/s/uny1VUt7vk_ZU6hCH0EDGg)

- 2024-11-04｜**SmolLM2**
  - 說明：手機執行的小型語言模型
  - 資源：[🤗 HuggingFace](https://github.com/huggingface/smollm/) | [📝 iThome](https://www.ithome.com.tw/news/165832)

- 2024-09-25｜**Llama 3.2**
  - 說明：1B/3B 端側模型 (Edge AI)
  - 資源：[📝 Meta Blog](https://ai.meta.com/blog/llama-3-2-connect-2024-vision-edge-mobile-devices/)

---

## Reasoning
**🤔 Reasoning Models (推理模型)**

### 🧠 次世代 LLM：推理模型 (Reasoning) 與 小型語言模型 (SLM)

| 模型名稱 | 開發團隊 | 💡 核心優勢與突破點 | 🚀 推薦適用場景 & 規格標籤 |
| :--- | :--- | :--- | :--- |
| **gpt-oss (120B)** | 🇺🇸 **OpenAI** | **o4-mini 級別的開源震撼彈**。OpenAI 重新擁抱開源，提供極強的邏輯推理能力。 | 複雜程式碼生成、高階數學解題<br>`[頂級推理]` `[OpenAI]` |
| **Llama Nemotron Super v1.5** | 🇺🇸 **NVIDIA** (輝達) | **三倍吞吐，單卡可跑**。49B 的參數兼顧了極高的效能與相對親民的硬體需求。 | 企業內部知識庫、高併發 API 服務<br>`[NVIDIA特化]` `[單卡部署]` |
| **OpenReasoning-Nemotron** | 🇺🇸 **NVIDIA** (輝達) | **1.5B 參數秒殺 o3**。極小參數卻擁有恐怖的數學運算與邏輯推理能力。 | 邊緣設備即時運算、專精型任務<br>`[極端輕量]` `[數學核武]` |

### 🧠 邊緣運算首選：Small Language Models (SLM)

| 模型名稱 | 開發團隊 | 💡 核心優勢與突破點 | 🚀 推薦適用場景 & 規格標籤 |
| :--- | :--- | :--- | :--- |
| **Phi-4** | 🇺🇸 **Microsoft** | **以小博大的教科書**。微軟 Phi 家族最新力作，在各項 Benchmark 上經常越級打怪。 | 本地筆電開發、離線文件摘要<br>`[微軟生態]` `[高CP值]` |
| **Llama 3.2 (1B/3B)** | 🇺🇸 **Meta** | **專為端側與手機設計**。Meta 官方釋出的輕量版本，完美適配行動裝置。 | iOS/Android APP 內建 AI、物聯網設備<br>`[Edge AI]` `[手機可跑]` |
| **SmolLM2** | 🇺🇸/🇪🇺 **Hugging Face** | **專為手機執行的極小模型**。極致壓縮體積，適合資源極度受限的環境。 | 穿戴式裝置、超低功耗設備<br>`[極小體積]` `[HuggingFace]` |

---

- 2025-08-05｜**gpt-oss**
  - 說明：OpenAI 重新開源，o4-mini 水平
  - 資源：[🤗 HuggingFace](https://huggingface.co/openai/gpt-oss-120b) | [📝 OpenAI Blog](https://openai.com/zh-Hant/index/introducing-gpt-oss/) | [📝 機器之心](https://www.jiqizhixin.com/articles/2025-08-06-2)

- 2025-07-29｜**Llama Nemotron Super v1.5**
  - 說明：英偉達開源，三倍吞吐、單卡可跑
  - 資源：[🤗 HuggingFace](https://huggingface.co/nvidia/Llama-3_3-Nemotron-Super-49B-v1_5) | [📝 知乎解讀](https://zhuanlan.zhihu.com/p/1933514869279274584)

- 2025-07-27｜**OpenReasoning-Nemotron**
  - 說明：英偉達數學核武，1.5B 參數秒殺 o3
  - 資源：[🤗 HuggingFace](https://huggingface.co/nvidia/OpenReasoning-Nemotron-1.5B) | [📝 公眾號解讀](https://mp.weixin.qq.com/s/o7RhRAFzAKkHj2T0y3GVzA)

- 2025-05-06｜**Llama-Nemotron**
  - 說明：英偉達高效推理系列
  - 資源：[📄 AlphaXiv](https://www.alphaxiv.org/zh/overview/2505.00949) | [📚 DeepWiki](https://deepwiki.com/NVIDIA/NeMo) | [📝 知乎解讀](https://zhuanlan.zhihu.com/p/1903012593033012833)

- 2025-04-16｜**Video-R1**
  - 說明：Reinforcing Video Reasoning in MLLMs
  - 資源：[📄 AlphaXiv](https://www.alphaxiv.org/zh/overview/2503.21776) | [🐙 GitHub](https://github.com/tulerfeng/Video-R1) | [📝 36Kr 報導](https://www.36kr.com/p/3252742390655489)

---

## LLM
**🏛️ Large Language Models (大型語言模型)**

### 🌟 2026 主流大語言模型 (LLM) 推薦與比較指南

> **編者按：** 隨著 AI 技術迭代，目前市場已明確分為「頂尖閉源商業模型」、「國際開源標竿」以及「專精中文語境的生態系」。以下整理了較具代表性的大語言模型，並解析其適用場景。

### 📊 主流模型快速比較表  

| 模型系列 | 開源狀態 | 開發機構 | 核心優勢與亮點 | 最佳適用場景 |
| :--- | :--- | :--- | :--- | :--- |
| **Gemini 3.1** | 閉源 (API) | Google | 原生多模態、超長上下文處理 | 企業級複雜數據分析、跨模態整合 |
| **Claude Opus 4.1** | 閉源 (API) | Anthropic | 業界頂尖的邏輯推理與極少幻覺 | 進階代碼生成、深度學術論文分析 |
| **Llama 3.2** | 開源模型 | Meta | 支援視覺能力，涵蓋 90B/11B 規模 | 本地端多模態應用、邊緣運算 (Edge) |
| **Ai2 Tülu 3** | 真・開源 | Allen AI | 連同「後訓練 (Post-training)」過程全公開 | 深度 AI 訓練研究、微調 (Fine-tuning) 實驗 |
| **Qwen (通義千問)**| 開源為主 | 阿里雲 | 開源界最強中文能力，提供全場景尺寸 | 中文 RAG 知識庫、端側部署、語音交互 |
| **文心一言** | 閉源 (API) | 百度 | 中文互聯網資料庫龐大，外掛生態完整 | 針對中國市場的企業級應用 |
| **混元 (Hunyuan)** | 閉源 (API) | 騰訊 | 與騰訊雲、社群平台深度整合 | 微信小程式開發、多模態內容生成 |

---

### 🏢 頂級閉源商業模型 (Closed-Source LLM)
適合追求極致性能、需要強大邏輯推理與穩定 API 服務的企業級開發者。

* **Gemini 3.1 (Google)** * **發布時間**：2026-02-19
  * **技術亮點**：Google 世代的最強模型，具備原生的圖、文、音、影多模態理解能力，並支援極長的上下文窗口。
  * **資源**：[🌐 Gemini API 官方文件](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=zh-tw)
* **Claude Opus 4.1 (Anthropic)**
  * **發布時間**：2025-08-05
  * **技術亮點**：在程式碼編寫與深度邏輯分析上常被評為最強王者，以其安全性和極低的幻覺率著稱。
  * **資源**：[📝 機器之心解析](https://www.jiqizhixin.com/articles/2025-08-06-4)

### 🌍 國際開源標竿模型 (Open-Source LLM)
適合需要將資料留在本地端（Data Privacy）、或者需要自行微調模型以符合特定業務邏輯的技術團隊。

* **Llama 3.2 90B/11B (Meta)**
  * **發布時間**：2024-09-25
  * **技術亮點**：Meta 首次在開源主線模型中加入強大的視覺能力 (Vision)，並針對邊緣設備 (Edge/Mobile) 進行了輕量化優化。
  * **資源**：[📝 Meta 官方 Blog](https://ai.meta.com/blog/llama-3-2-connect-2024-vision-edge-mobile-devices/)
* **Ai2 Tülu 3 (Allen AI)**
  * **發布時間**：2024-11-23
  * **技術亮點**：被譽為「真・開源模型」。不僅開源權重，更史無前例地公開了完整的「後訓練」配方與數據，對 AI 研究社群貢獻巨大。
  * **資源**：[🐙 GitHub 源碼](https://github.com/allenai/open-instruct) | [🌐 Playground 測試](https://playground.allenai.org/) | [🤗 HuggingFace 模型](https://huggingface.co/allenai) 

### 🐉 中文生態系主流模型 (Chinese LLM Ecosystem)
針對繁體/簡體中文語境優化，理解中文成語、文化背景與特定領域知識的表現遠超多數西方開源模型。

* **通義千問 Qwen (阿里雲)** —— *開發者首選的中文開源全家桶*
  * **技術亮點**：目前開源界中文能力最強的模型系列。從單張顯卡就能跑的 7B 模型，到超越 GPT-4 基準的 72B 巨獸，甚至包含可以直接聽懂人話的語音多模態版本。
  * **資源連結**：
    * [🌐 官方網站體驗](https://tongyi.aliyun.com/)
    * [🤗 Qwen3.5-Omni (輸入支持圖、影片、文字。 輸出支援音訊、文字)](https://huggingface.co/spaces/Qwen/Qwen3.5-Omni-Offline-Demo) | [Qwen發表Qwen3.5-Omni，支援最長10小時語音輸入](https://www.ithome.com.tw/news/174791)
    * [🤗 Qwen-72B (企業級推理下載)](https://huggingface.co/Qwen/Qwen-72B)
    * [🐙 Qwen-7B (本地部署首選)](https://github.com/QwenLM/Qwen-7B)
  * **延伸閱讀**：[開源語音大語言模型 Qwen-Audio 原理](https://zhuanlan.zhihu.com/p/668608727) | [最小 18 億參數模型端側實戰](https://www.jiqizhixin.com/articles/2023-12-01-5)
* **文心一言 Wenxin (百度)**
  * **技術亮點**：依託百度龐大的中文搜尋數據庫，對中國在地化的知識庫理解極深。
  * **資源**：[🌐 文心一言官網](https://wenxin.baidu.com)
* **混元 Hunyuan (騰訊)**
  * **技術亮點**：主打多模態生成與企業級整合，適合需要與騰訊生態系（如微信小程式）對接的開發者。
  * **資源**：[🌐 騰訊雲混元](https://cloud.tencent.com/product/hunyuan)

---

## Embedding
**🔎 Embedding & Reranker**

- 2026-02-28 | **pplx-embed-v1 and pplx-embed-context-v1**
  - 說明：一系列尖端的文本嵌入模型，針對真實世界的 Web 規模檢索任務進行了優化，例如語義搜索和 RAG 系統
  - 資源：[📝 Perplexity Research](https://research.perplexity.ai/articles/pplx-embed-state-of-the-art-embedding-models-for-web-scale-retrieval) | [🤗 HuggingFace](https://huggingface.co/collections/perplexity-ai/pplx-embed)

- 2025-07-14｜**Gemini Embedding 001**
  - 資源：[☁️ Google Cloud](https://cloud.google.com/vertex-ai/generative-ai/docs/embeddings/get-text-embeddings?hl=zh-tw)

- 2025-06-05｜**Qwen3 Embedding**
  - 說明：新一代文本表徵與排序模型
  - 資源：[📝 Qwen Blog](https://qwenlm.github.io/zh/blog/qwen3-embedding/) | [🤗 Embedding](https://huggingface.co/collections/Qwen/qwen3-embedding-6841b2055b99c44d9a4c371f) | [🤗 Reranker](https://huggingface.co/collections/Qwen/qwen3-reranker-6841b22d0192d7ade9cdefea)

---

## Speech
**🔊 Speech-to-Speech LLM (語音大模型)**

- **TEN Agent**
  - 說明：王炸級開源端對端語音模型
  - 資源：[🐙 GitHub](https://github.com/TEN-framework/TEN-Agent) | [📝 公眾號](https://mp.weixin.qq.com/s/pw9LQyRCRogfxAlYG3EfcQ) | [📝 入坑記](https://mp.weixin.qq.com/s/ZVZHNP0XPwzGapWWqTk1kw) | [📝 搭建教學](https://uy6npdpeoi.feishu.cn/docx/EAWYdWWO7ormNPxUhyVcO3GSnUc)

- **pipecat**
  - 說明：用 ChatGPT 即時語音 API 建立應用
  - 資源：[🐙 GitHub](https://github.com/pipecat-ai/pipecat) | [📝 機器之心](https://www.jiqizhixin.com/articles/2025-01-10-4)

- 2026-01-24 | **FlashLabs-Chroma**
  - 說明：Speech-to-Speech, S2S
  - 資源：[🤗 HuggingFace](https://huggingface.co/FlashLabs/Chroma-4B)

- 2026-01-15 | **PersonaPlex-7B-V1**
  - 說明：重塑實時語音交互的 "全雙工" 黑科技 | [👉 點此看深度技術分析 ](https://deep-learning-101.github.io/LLM/PersonaPlex)
  - 資源：[🤗 HuggingFace](https://huggingface.co/nvidia/personaplex-7b-v1) | [🐙 GitHub](https://github.com/NVIDIA/personaplex) | [🌐 Project](https://research.nvidia.com/labs/adlr/personaplex/) | [論文](https://research.nvidia.com/labs/adlr/files/personaplex/personaplex_preprint.pdf) | [📝 公眾號解讀](https://mp.weixin.qq.com/s/dyAoh8hIjNw-LI-hb_1e6A)

- 2025-12-24｜**Fun-Audio-Chat-8B**
  - 資源：[🤗 HuggingFace](https://huggingface.co/FunAudioLLM/Fun-Audio-Chat-8B)

- 2025-11-03｜**LongCat-Flash-Omni**
  - 說明：開啟全模態即時互動時代
  - 資源：[🤗 HuggingFace](https://huggingface.co/meituan-longcat/LongCat-Flash-Omni) | [📝 知乎解讀](https://zhuanlan.zhihu.com/p/1968699530762491165)

- 2025-09-19 | **Xiaomi-MiMo-Audio**
  - 說明：小米開源首個原生端對端語音大模式
  - 資源：[🤗 HuggingFace](https://huggingface.co/XiaomiMiMo/MiMo-Audio-7B-Base) | [📝 知乎解讀](https://zhuanlan.zhihu.com/p/1991075806194205492)

- 2025-07-21｜**Audio Flamingo 3**
  - 說明：NVIDIA 開源多模態音訊模型
  - 資源：[🐙 GitHub](https://github.com/NVIDIA/audio-flamingo) | [📝 OSChina](https://www.oschina.net/news/361477/nvidia-audio-flamingo-3)

- 2025-05-08｜**Voila**
  - 說明：195ms 超低延遲引領全雙工對話
  - 資源：[🐙 GitHub](https://github.com/maitrix-org/Voila) | [📝 知乎解讀](https://zhuanlan.zhihu.com/p/1903776373765547954)

- **HuggingFace Speech-to-Speech**
  - 資源：[🐙 GitHub](https://github.com/huggingface/speech-to-speech)

---

## Vision
**👁️ Vision-Language Model (視覺大語言模型)**

- 2025-05-20｜**Seed1.5-VL**
  - 說明：具有視覺增強多模態能力的高階語言模型
  - 資源：[🐙 GitHub](https://github.com/ByteDance-Seed/Seed1.5-VL) | [📄 AlphaXiv](https://www.alphaxiv.org/zh/overview/2505.07062) | [📝 知乎解讀](https://zhuanlan.zhihu.com/p/1905914968433497765)

- 2025-05-12｜**nanoVLM**
  - 資源：[📚 DeepWiki](https://deepwiki.com/huggingface/nanoVLM)

---

## Multimodal
**🌌 Multimodal LLM (多模態大語言模型)**

- **InternVL**
  - 說明：刷新開源多模態大模型效能新紀錄
  - 資源：[🐙 GitHub](https://github.com/OpenGVLab/InternVL) | [📄 AlphaXiv](https://www.alphaxiv.org/zh/overview/2504.10479) | [📚 DeepWiki](https://deepwiki.com/OpenGVLab/InternVL) | [📝 知乎解讀](https://zhuanlan.zhihu.com/p/1897681159359551408)

- 2025-12-20 | **T5Gemma 2**
  - 說明：首個140語言+多模態+超長上下文，Google開源重磅模型
  - 資源：[🤗 HuggingFace](https://huggingface.co/collections/google/t5gemma-2) | [📝 公眾號解讀](https://mp.weixin.qq.com/s/dmg4wf4KGt_zByuaOe6qEA)

- 2025-05-24｜**Dolphin**
  - 說明：開源多模態複雜文件解析模型
  - 資源：[📄 AlphaXiv](https://www.alphaxiv.org/zh/overview/2505.14059) | [📚 DeepWiki](https://deepwiki.com/bytedance/Dolphin) | [📝 知乎解讀](https://zhuanlan.zhihu.com/p/1911355829485045020)

- 2025-05-21｜**Gemma 3n**
  - 資源：[🌐 Google DeepMind](https://deepmind.google/models/gemma/?hl=zh-tw) | [🤗 Preview](https://huggingface.co/google/gemma-3n-E4B-it-litert-preview)

- 2025-03-18｜**Mistral Small 3.1**
  - 說明：128K 上下文，效能碾壓 GPT-4o Mini
  - 資源：[🤗 HuggingFace](https://huggingface.co/mistralai/Mistral-Small-3.1-24B-Instruct-2503) | [📝 知乎解讀](https://zhuanlan.zhihu.com/p/31138756743)

- 2025-03-14｜**Vision-R1**
  - 說明：激發多模態大模型的推理能力
  - 資源：[🐙 GitHub](https://github.com/Osilly/Vision-R1) | [📝 知乎解讀](https://zhuanlan.zhihu.com/p/29618155786)

- 2025-02-28｜**HumanOmni**
  - 說明：阿里通義業界首個第一視角大模型
  - 資源：[🐙 GitHub](https://github.com/HumanMLLM/HumanOmni) | [📝 公眾號解讀1](https://mp.weixin.qq.com/s/acn16cvE8N4tMegKuGHAKQ) | [📝 公眾號解讀2](https://mp.weixin.qq.com/s/cO6xEAOCRUsLmoiDbq12tw)

- **Phi Family (Microsoft)**
  - 資源：[🤗 Collection](https://huggingface.co/collections/microsoft/phi-4-677e9380e514feb5577a40e4) | [🤗 Phi-4 Multimodal](https://huggingface.co/microsoft/Phi-4-multimodal-instruct)
  - 2025-02-27：[📝 56億參數秒殺 GPT-4o](https://zhuanlan.zhihu.com/p/26984226500) | [📝 小身材大智慧](https://zhuanlan.zhihu.com/p/26678433652)
  - 2024-09-12：[📝 Phi 3.5 mini 發布](https://mp.weixin.qq.com/s/EeALIBrvGWKtEBGnroZIvg)

- **MiniCPM**
  - 資源：[🐙 GitHub](https://github.com/OpenBMB)
  - 2025-01-16：[📝 MiniCPM-o 2.6 發布](https://mp.weixin.qq.com/s/bTRirDr-MCscYF88KmK5qw) | [📖 文檔](https://github.com/OpenBMB/MiniCPM-o/blob/main/README_zh.md#minicpm-o-26)
  - 2024-09-11：[📝 升級 Ollama 支援](https://mp.weixin.qq.com/s/6N-u8PcGEX6e4rryeqXglQ)
  - 2024-09-06：[📝 MiniCPM 3.0 開源](https://53ai.com/news/OpenSourceLLM/2024090659871.html) | [🐙 GitHub](https://github.com/OpenBMB/MiniCPM)
  - 2024-09-05：[📝 魔改 MiniCPM-V](https://mp.weixin.qq.com/s/DjDznmtKZoJNKXYz0X4zog) | [🐙 GitHub](https://github.com/OpenBMB/MiniCPM-V/)



**語音助手工具**
- [ESP-AI](https://espai.fun/)
- [xiaozhi-esp32](https://github.com/78/xiaozhi-esp32)
   - [購買連結](https://rcnv1t9vps13.feishu.cn/wiki/LdCrw9neaiGgzrkrFyjclllynYd)
   - [小智 AI 聊天機器人百科全書](https://ccnphfhqs21z.feishu.cn/wiki/F5krwD16viZoF0kKkvDcrZNYnhb)
- [xiaozhi-esp32-server](https://github.com/xinnan-tech/xiaozhi-esp32-server)：為xiaozhi-esp32提供後台服務，協助您快速建置ESP32設備控制伺服器
- [py-xiaozhi](https://github.com/Huang-junsen/py-xiaozhi)：python 版本小智ai，主要幫助那些沒有硬體的人體驗小智功能
- [xiaozhi-web-client](https://github.com/TOM88812/xiaozhi-web-client)
- [xiaozhi-android-client](https://github.com/TOM88812/xiaozhi-android-client)
- [OpenVoiceOS](https://github.com/OpenVoiceOS/ovos-core)
- [fast-voice-assistant](https://github.com/dsa/fast-voice-assistant)
- [gptspeaker](https://github.com/jackwuwei/gptspeaker)

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "TechArticle",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://deep-learning-101.github.io/Large-Language-Model"
  },
  "headline": "2026 大語言模型 (LLM) 與 AI Agent 開源資源大全",
  "description": "一份詳盡的大語言模型（LLM）資源清單，涵蓋端側推理模型(SLM)、微調技術(Fine-tuning)、RAG架構優化、AI Agent多智能體框架與Manus開源平替工具，助你掌握最新生成式AI技術。",
  "image": "https://raw.githubusercontent.com/Deep-Learning-101/TonTon/refs/heads/main/_includes/DL101-Logo.jpg",
  "author": {
    "@type": "Organization",
    "name": "Deep Learning 101, Taiwan",
    "url": "https://deep-learning-101.github.io/"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Deep Learning 101, Taiwan",
    "logo": {
      "@type": "ImageObject",
      "url": "https://raw.githubusercontent.com/Deep-Learning-101/TonTon/refs/heads/main/_includes/DL101-Logo.jpg"
    }
  },
  "datePublished": "2026-03-29",
  "dateModified": "2026-03-29",
  "keywords": "大語言模型, LLM, AI Agent, RAG, 微調, Fine-tuning, Deep Research, 知識庫, 推理模型, Reasoning, SLM, LLaMA, AI 自動化, Manus 平替",
  "about": {
    "@type": "Service",
    "serviceType": "GenAI Consulting",
    "provider": {
      "@type": "Organization",
      "name": "Deep Learning 101, Taiwan"
    },
    "name": "生成式 AI 諮詢 (GenAI Consulting)",
    "description": "提供關於大語言模型（LLM）的專業諮詢服務，包含模型微調、應用開發、框架選擇與技術導入。"
  }
}
</script>