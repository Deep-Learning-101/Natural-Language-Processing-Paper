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

{% include price.html %}

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
* **[[OpAgent]](https://github.com/codefuse-ai/OpAgent)** `[2026-02-20]` 🔥
  * **核心優勢**：**視覺驅動的 Web 智能體霸主，WebArena 成功率 71.6% 榮登榜首。** 由螞蟻集團研發，打破傳統對 HTML 代碼的過度依賴，改採網頁截圖直接進行空間佈局理解。結合線上強化學習（Online RL）與「規劃、執行、反思、總結」四位一體的協作架構，賦予 AI 像真人一樣在複雜網頁中試錯與導航的能力。
  * **解決痛點 / 推薦場景**：**完美解決了傳統網頁腳本因 UI 改版就失效、以及無法處理跨頁面複雜邏輯的問題。** 無需預設腳本，僅憑一條指令即可在亞馬遜（Amazon）等真實電商平台自主完成搜尋、識別與加購操作，是建構自動化電商助理與 RPA 流程的頂級引擎。
  * **資源**：[🐙 GitHub](https://github.com/codefuse-ai/OpAgent) | [🤗 HuggingFace](https://huggingface.co/codefuse-ai/OpAgent-32B) | [📄 Technical Report](https://arxiv.org/pdf/2602.13559) | [🌐 線上 Demo](https://huggingface.co/spaces/exias/OpAgent)
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
* **[nanobrowser](https://github.com/nanobrowser/nanobrowser)** `[2025-04-11]`：AI 驅動的瀏覽器自動化神器，透過輕量化架構實現網頁操作自動化。[📝 公眾號推薦](https://mp.weixin.qq.com/s/65SwCtDta1cKvx1_BbaoHQ)  

---

### 🕵️‍♂️ 深度研究 (Deep Research) 與多智能體工作流

面對海量文獻與複雜專案，傳統的單一 AI 已經不夠用。以下精選 2025-2026 年最強大的深度研究與多智能體編排框架，幫助企業與學術界打造自動化的「研究大腦」：

| 框架/工具名稱 | 開發團隊/生態 | 💡 解決什麼痛點？ (核心優勢) | 🚀 推薦適用場景 & 規格標籤 |
| :--- | :--- | :--- | :--- |
| **Tongyi DeepResearch** | 🇨🇳 **阿里巴巴** | **開源版深度研究霸主**。通義團隊全面開源，標榜其長文本檢索與邏輯梳理效能超越 OpenAI 的閉源研究框架。 | 學術文獻統整、深度產業報告生成<br>`[大廠開源]` `[深度研究]` |
| **Agno** | 🌐 **開源社群** | **高效能 Multi-agent 協作**。專注於多個 AI 智能體之間的底層協作、任務分發與記憶體共享。 | 複雜專案拆解、軟體開發協作<br>`[多智能體]` `[高效能]` |
| **FlowGram** | 🇨🇳 **字節跳動** | **Coze 核心引擎開源**。提供強大且直覺的視覺化工作流引擎，適合構建具備複雜條件分支的邏輯鏈。 | 企業級 AI 服務編排、Chatbot 後台<br>`[工作流引擎]` `[可視化]` |
| **AutoAgent** | 🇭🇰 **香港大學** | **學術界最強大腦**。由港大團隊打造的開源 Deep Research 工具，具備深厚的學術底蘊與嚴謹的文獻引用機制。 | 大學研究室、論文自動化分析<br>`[學術開源]` `[文獻分析]` |

---

### 📊 AI 簡報生成神器 (AI PPT & Slides Automation)

傳統的 PPT 製作耗時且高度依賴排版技巧。隨著生成式 AI 的進步，AI 簡報工具已從初期的「生硬套用模板」，進化到「無模板自由生成」與「像素級逆向還原」。以下為目前 GitHub 上最受關注的開源解決方案：

#### 1. 學術前沿與無模板自由生成 (Advanced & Template-Free)
解決傳統 AI 簡報工具「排版死板、只能套模板」的致命痛點，真正實現高度自由的內容渲染。

* **[PPTAgent V2](https://github.com/icip-cas/PPTAgent)** `[2026-03-03]` 🔥
  * **核心優勢**：中科院團隊重磅升級！徹底打破傳統套模板的限制，實現**無模板自由生成**。內建的 DeepPresenter 模組刷新了產業榜單，支援渲染後即時糾錯與修改程式碼，是將長篇論文轉化為高品質 PPT 的學術級首選。[📝 公眾號推薦](https://mp.weixin.qq.com/s/2AEZpsC4wphAcpp5LtGqnw) | [📝 知乎原理解讀](https://zhuanlan.zhihu.com/p/18105237248)
* **[PaperBanana](https://dwzhu-pku.github.io/PaperBanana/)** `[2026-02-24]`：基於「參考驅動 + 多智能體合作」的 AI 簡報生成器。它不直接生圖，而是先理解、規劃、美化，最後迭代優化出高品質 PPT。[📄 論文](https://arxiv.org/pdf/2601.23265)  
* **[Edit-Banana](https://github.com/BIT-DataLab/Edit-Banana)** `[2026-02-23]`
  * **核心優勢**：北理工與亞利桑那大學聯手打造。具備極強的「像素級逆向還原能力」，不盲目生圖，而是理解、規劃再優化，成功打通 AIGC 繪圖與簡報排版落地的最後一哩路。

#### 2. 快速生成與本地部署方案 (Local Deployment & Quick Gen)
適合企業內部使用，解決雲端生成可能帶來的商業機密外洩風險，或追求極致的生成速度。

* **[presenton](https://github.com/presenton/presenton)** `[2025-07-26]`
  * **核心優勢**：主打**本地部署**的開源神器！確保資料絕對不外流的前提下，只需輸入文本即可一鍵生成精美 PPT，企業內網平替首選。[📝 公眾號推薦](https://mp.weixin.qq.com/s/QTMVGD_aP41qrwtbjLxV8Q)
* **[LangChat Slides](https://github.com/langchat/langchat-slides)** `[2026-01-04]`
  * **核心優勢**：提供流暢的生成式 AI 互動體驗與現代化介面。[🌐 線上 DEMO](https://slides.langchat.cn/) | [📝 掘金深度解讀](https://juejin.cn/post/7591861857465778214)
* **[banana-slides](https://github.com/Anionex/banana-slides)** `[2025-12-13]`
  * **核心優勢**：基於 nanobananapro🍌 的原生應用。專注於打造具備高設計張力的「Vibe PPT」，極度適合行銷提案或創意展示。[📝 公眾號推薦](https://mp.weixin.qq.com/s/XXyCnEdrTVoK-m-EAW69nA)

#### 3. 多智能體協同架構 (Multi-Agent Workflows)
* **[MultiAgentPPT](https://github.com/johnson7788/MultiAgentPPT)** `[2025-07-03]`
  * **核心優勢**：引入多智能體並發處理機制。透過讓不同的 Agent 分工處理「大綱規劃」、「資料檢索」與「視覺排版」，大幅提升複雜簡報的生成速度與邏輯嚴密性。[📝 知乎原理解讀](https://zhuanlan.zhihu.com/p/1920611446007497267)

---

### 🌍 知識管理革命：NotebookLM 開源平替生態

Google 的 NotebookLM 改變了我們與長篇文獻互動的方式，但「資料上雲」的資安疑慮也讓許多企業卻步。以下精選 GitHub 上最受矚目的 NotebookLM 開源替代方案，讓您在保障資料隱私的前提下，打造專屬的第二大腦：

#### 📊 核心解決方案比較表
| 專案名稱 | 核心定位 | 💡 解決什麼痛點？ (核心優勢) | 🚀 推薦適用場景 & 規格標籤 |
| :--- | :--- | :--- | :--- |
| **Open NoteBook** | 企業私有化 | **隱私優先的知識庫**。完美復刻對話體驗，支援完全本地化部署，機密文件絕不外流。 | 企業內部文件庫、離線筆記本<br>`[本地部署]` `[重視隱私]` |
| **PageLM** | 學習與培訓 | **互動式學習神器**。把學習材料丟進去，自動提煉並生成互動式學習內容。 | 教育培訓、長篇報告快速消化<br>`[互動學習]` `[文件分析]` |
| **notebooklm-py** | 開發者自動化 | **終端機知識管線**。支援命令列操作，讓工程師能用語法批次處理海量文件。 | 批次資料處理、CLI 愛好者<br>`[命令列工具]` `[自動化管線]` |
| **Auto-Slides** | 語音播客生成 | **讓論文開口說話**。復刻 "Audio Overview" 殺手級功能，生成雙人對談的解說音訊。 | 學術論文導讀、語音知識吸收<br>`[Audio Overview]` `[語音生成]` |

#### 📂 專案下載與部署資源
* **[notebooklm-py](https://github.com/teng-lin/notebooklm-py)** `[2026-01-20]`：將 NotebookLM 完整接入命令列環境，讓 AI 知識處理邁入自動化新紀元。[📝 公眾號推薦](https://mp.weixin.qq.com/s/rATp6AhcQOzFe4t2QnA07w)
* **[Notex](https://github.com/smallnest/notex)** `[2026-01-04]`：一個輕量、開箱即用的 NotebookLM 替代方案實作。[🌐 線上 DEMO](https://notex.rpcx.io/) | [📝 公眾號推薦](https://mp.weixin.qq.com/s/65epWwIC7Lqalwh-WuoP3Q)
* **[PageLM](https://github.com/CaviraOSS/pagelm)** `[2025-12-12]`：把學習材料丟進去，互動式學習內容就出來。[📝 知乎解讀](https://zhuanlan.zhihu.com/p/1980701578559234518) | [📝 公眾號解讀](https://mp.weixin.qq.com/s/3o8RcHicjt5FRdSzG_qGUw)
* **[Open NoteBook](https://github.com/lfnovo/open-notebook)** `[2025-12-06]`：一個開源的、注重隱私的 Google NotebookLM 替代方案。[📝 公眾號解讀](https://mp.weixin.qq.com/s/Kncslf0XL1ucdPpQX_-a1g)
* **[Auto-Slides](https://github.com/Westlake-AGI-Lab/Auto-Slides)** `[2025-12-06]`：不只是幫你寫，還能幫你講。它讓論文第一次有機會「開口說話」，生成具備沈浸感的有聲討論。[📝 知乎解讀](https://zhuanlan.zhihu.com/p/1953393379334391701)

---

### 🧹 資料前處理與 AI 爬蟲神器 (Data Parsing & Web Scraping)
*「垃圾進，垃圾出 (Garbage In, Garbage Out)」。* 在建構 RAG 或微調模型之前，如何將混亂的網頁與 PDF 轉換為 AI 讀得懂的乾淨格式，是決定系統成敗的關鍵。

#### 1. 網頁爬蟲與資訊擷取 (Web Scraping)
* **[Crawl4AI](https://zread.ai/unclecode/crawl4ai)** `[2025-11-26]`
  * **核心優勢**：對 LLM 最友善的網頁爬蟲工具。能一鍵將網頁內容轉化為乾淨、適合大模型處理的 Markdown 格式，是構建 RAG 與智能代理資料管道的必備神器。[📝 公眾號解讀](https://mp.weixin.qq.com/s/5cNfBbKOHHjGin5I7XYlpw)
* **[ScrapeGraphAI](https://github.com/ScrapeGraphAI/Scrapegraph-ai)** `[2025-04-16]`
  * **核心優勢**：顛覆傳統爬蟲痛點！透過 LLM 解析網頁結構，只需輸入自然語言指令，就能自動適應網站改版，精準抓取資料。適合用於電商價格監控或收集產業新聞。[📝 公眾號推薦](https://mp.weixin.qq.com/s/lQukAy12V5K1cH6rTkqxaA)
* **[EasySpider](https://github.com/NaiboWang/EasySpider)** `[2025-07-30]`：無程式碼的可視化網頁爬蟲工具，透過簡單的圖形化介面即可完成複雜抓取。
* **[LangExtract](https://github.com/google/langextract)** `[2025-07-30]`：Google 開源，由 Gemini 驅動的高效資訊擷取庫。

#### 2. 文檔解析與 OCR (Document Parsing & OCR)
* **[Logics-Parsing-Omni (阿里通義)](https://github.com/alibaba/Logics-Parsing/tree/main/Logics-Parsing-Omni)** `[2026-03-12]` 🔥
  * **核心優勢**：阿里最新釋出的「全模態 (Omni)」終極解析框架！打破傳統 OCR 的極限，採用單一模型端對端 (End-to-End) 架構，能將極度複雜的排版、數學公式、甚至是化學結構式 (SMILES)，精準轉化為帶有邏輯標籤的乾淨 HTML。
  * **解決痛點**：解決傳統 RAG 系統前處理需要串接多個模型的「碎片化」痛點。主打「證據錨定 (Evidence anchoring)」，確保解析出來的結構化知識 100% 溯源，是目前企業對付複雜 STEM (理工科) 文件的最強清洗機。
* **[Agentic-Doc](https://github.com/landing-ai/agentic-doc)** `[2025-06-10]`
  * **核心優勢**：吳恩達帶領的 LandingAI 團隊開源，主打「百頁文檔秒變結構化資料」，解決企業 PDF 財報難以解析的問題。[📝 知乎解讀](https://zhuanlan.zhihu.com/p/1914259475306612709)
* **[markitdown](https://github.com/microsoft/markitdown)** `[2024-12-15]`：微軟官方開源的轉換神器，能將各種檔案格式（PDF, Word, Excel）轉化為乾淨的 Markdown。
* **[docext](https://github.com/NanoNets/docext)** `[2025-06-28]`：基於阿里 Qwen2.5VL 視覺大模型的文檔解析工具，專治排版混亂的複雜圖表。
* **[DocAligner](https://github.com/ZZZHANG-jx/DocAligner)** `[2025-01-13]`：實體文件數位化救星！專精於拍照文件的逆向還原（校正變形、版面精準定位）。
* **[pdf-craft](https://github.com/oomol-lab/pdf-craft)** `[2025-03-26]`：PDF 秒轉 Markdown/EPUB 的輕量化實用工具。
* **[OCRmyPDF](https://github.com/ocrmypdf/OCRmyPDF)** `[2025-03-25]`：為掃描版 PDF 加上可搜尋的文字層，老牌且強大的 OCR 解決方案。

---

### 3. 開發者與個人資訊自動化 (Personal Automation & Dev Tools)
解救你的知識焦慮！這些工具能幫你將四散的資訊聚合，並透過 LLM 轉化為個人生產力。

* **[OneFileLLM](https://github.com/jimmc414/onefilellm)** `[2025-04-16]`
  * **使用情境**：要餵給 AI 的資料太零碎？這款工具能一鍵將多個網頁、GitHub 程式碼與 PDF 論文，全部聚合壓縮到剪貼簿，方便你直接貼給 Claude 或 ChatGPT。
* **[daily-arXiv-ai-enhanced](https://github.com/dw-dengwei/daily-arXiv-ai-enhanced)** `[2025-06-06]`：研究員必備。每日自動爬取最新 arXiv 論文，並呼叫 LLM 產生中文摘要推送。
* **[Follow](https://deepwiki.com/RSSNext/Folo)** `[2025-05-16]`：次世代資訊聚合神器，重塑 RSS 閱讀體驗。[📝 知乎推薦](https://zhuanlan.zhihu.com/p/1906505020628795653)
* **[news-agents](https://deepwiki.com/eugeneyan/news-agents)** `[2025-05-20]`：自動化新聞摘要與分析智能體。
* **[DeepMCPAgent](https://zread.ai/cryxnet/DeepMCPAgent)** `[2025-09-11]`：教你如何透過 MCP 協議，讓大模型「自己學會找工具」。[📝 公眾號解讀](https://mp.weixin.qq.com/s/Sj_7i1mTJ9WYaTlCzIqCFA)
* **[sqlchat](https://github.com/sqlchat/sqlchat)** `[2025-04-06]`：讓資料庫管理像聊天一樣簡單，透過自然語言直接下達 SQL 查詢指令。
* **[PySpur](https://www.pyspur.dev/)** `[2025-02-25]`：拖曳式的視覺化開發介面，輕鬆編排你的專屬 AI 工作流 (Workflow)。
* **[PaperCoder (Paper2Code)](https://www.alphaxiv.org/overview/2504.17192)** `[2025-04-28]`：黑科技！嘗試直接從學術論文中，自動提取並生成對應的原始碼。
* **[AingDesk](https://deepwiki.com/aingdesk/AingDesk)** `[2025-05-22]`：主打「零門檻」的本地 AI 模型部署介面。

---

### 4. 視覺化畫布與 AI 創作引擎 (Visual Canvas & Creation)
打破傳統 ChatGPT「單線對話框 (Chat UI)」的限制，提供全局鳥瞰的空間思維，適合複雜企劃與長篇寫作。

* **[Refly (畫布式 AI 創作引擎)](https://github.com/refly-ai/refly)** `[持續更新]`
  * **核心優勢**：一款極具創新力的「無限畫布式 (Canvas)」開源 AI 原生創作引擎。內建整合 13+ 主流大語言模型，提供類似 Miro 結合 Notion AI 的白板工作流。
  * **解決痛點**：解決使用 AI 進行深度寫作或腦力激盪時「上下文容易丟失、邏輯難以串聯」的痛點。開發者與創作者可以在畫布上自由展開節點、對比多個模型的生成結果，是個人與團隊進行複雜 AI 內容協作的完美開源平替方案。[📖 官方中文文檔](https://docs.refly.ai/zh)

---

## World Models
**🌍 World Models (世界模型)**

如果說傳統 LLM 是「文字接龍」，那世界模型 (World Models) 就是讓 AI 具備「物理法則與常識預測能力」。透過預測環境的下一步變化，這是通往通用人工智慧 (AGI) 與具身智能 (Embodied AI) 的關鍵拼圖。

* **[Code World Model (Meta Yann LeCun 團隊)](https://zread.ai/facebookresearch/cwm/1-overview)** `[2025-09-25]`
  * **核心優勢**：AI 教父 Yann LeCun 領軍發布的 320 億參數開源世界模型。有別於生成式 AI，它採用 JEPA (聯合嵌入預測架構)，專注於理解系統的內部邏輯與預測代碼執行的結果，是 AI Agent 進行複雜規劃 (Planning) 的終極大腦。[📝 新浪深度報導](https://t.cj.sina.com.cn/articles/view/1746173800/68147f6801901e2wa)

---

## MoE
**🧠 MoE (Mixture of Experts 混合專家模型)**

MoE 架構是目前突破大模型「算力牆」的唯一解方。 它的核心概念是「術業有專攻」：模型可能擁有千億參數，但每次回答問題時，只會啟動（激活）最相關的幾個「專家神經網路」，從而在極低的推論成本下，展現出超越稠密模型 (Dense Model) 的極致效能。

#### 📊 頂級開源 MoE 模型比較表
| 模型名稱 | 開發團隊 | 💡 核心優勢與解決痛點 | 🚀 規格與激活參數 (Active Parameters) |
| :--- | :--- | :--- | :--- |
| **DeepSeek-V3** | 🇨🇳 **幻方量化** | **開源界的性價比之王**。用極低的訓練成本，達到持平甚至超越 GPT-4o 的驚人效能。 | 總參數 671B / 激活 37B<br>`[開源霸主]` `[推理極快]` |
| **DeepSeek-VL2** | 🇨🇳 **幻方量化** | **將 MoE 引入視覺領域**。解決了多模態大模型在處理高解析度圖片時的運算延遲問題。 | 視覺與語言混合專家<br>`[多模態 MoE]` `[動態解析]` |
| **Hunyuan-Large** | 🇨🇳 **Tencent (騰訊)** | **騰訊開源的最大 MoE**。專注於中文語境與超長上下文，並強化了企業級資料檢索能力。 | 總參數 389B / 激活 52B<br>`[企業級]` `[長文本]` |

#### 📂 核心模型下載與架構解析
* **[DeepSeek-V3 (震撼全球的開源 MoE)](https://github.com/deepseek-ai/DeepSeek-V3)** `[2024-12-26 更新補充]` 🔥
  * **必讀原因**：徹底改寫開源模型格局的巨獸！總參數高達 671B，但每次推論僅需激活 37B 參數。首創的多頭潛在注意力機制 (MLA) 與負載均衡策略，讓它在程式碼生成與數學邏輯上穩居開源第一。[📝 架構深度解析](https://zhuanlan.zhihu.com/p/123456789) *(註：可補上您部落格或知乎的相關文章)*
* **[DeepSeek-VL2 (VLM 邁入 MoE 時代)](https://github.com/deepseek-ai/DeepSeek-VL2)** `[2024-12-13]`
  * **核心優勢**：傳統視覺大模型 (VLM) 運算極度吃力，VL2 成功將混合專家架構引入視覺領域，大幅提升了圖片與文件的解析效率。[📝 機器之心解讀](https://mp.weixin.qq.com/s/s832KUgixNuX4GUkvY7_Ag) | [📝 公眾號解析](https://mp.weixin.qq.com/s/p6r_b-k4UnSJED5cBTedZg)
* **[Hunyuan-Large (騰訊混元最大 MoE)](https://github.com/Tencent/Hunyuan-Large)** `[2024-11-06]`
  * **核心優勢**：在中文互聯網資料的理解上具備極大優勢，且針對 RAG 檢索任務進行了深度最佳化。[🤗 線上 DEMO](https://huggingface.co/spaces/tencent/Hunyuan-Large) | [🤗 模型下載](https://huggingface.co/tencent/Hunyuan-Large) | [📝 機器之心報導](https://www.jiqizhixin.com/articles/2024-11-06-6)


---

## SLM
**📱 SLM (Small Language Models 小型語言模型)**
### 🧠 次世代 LLM：小型語言模型，邊緣運算首選：Small Language Models (SLM)

隨著端側算力提升，2025 年的 AI 戰場已從雲端燒向邊緣設備。小型語言模型 (SLM) 通常指參數在 8B 以下的模型，主打「低功耗、保護隱私、無網連線」。以下是專為手機與物聯網 (IoT) 設計的開源王者：

#### 📊 端側 SLM 快速比較表
| 模型名稱 | 開發團隊 | 💡 核心優勢與解決痛點 | 🚀 推薦適用場景 & 規格標籤 |
| :--- | :--- | :--- | :--- |
| **Phi-4** | 🇺🇸 **Microsoft** | **以小博大的教科書**。微軟 Phi 家族最新力作，透過高品質合成數據訓練，在各項 Benchmark 上經常越級打怪，擊敗百億參數模型。 | 本地筆電開發、離線文件摘要<br>`[微軟生態]` `[高CP值]` |
| **Llama 3.2 (1B/3B)** | 🇺🇸 **Meta** | **專為端側與手機設計**。Meta 官方釋出的輕量版本，完美適配行動裝置的記憶體限制，並保持強大的指令跟隨能力。 | iOS/Android APP 內建 AI、物聯網<br>`[Edge AI]` `[手機可跑]` |
| **SmolLM2** | 🌐 **Hugging Face** | **為極端環境打造的極小模型**。極致壓縮體積，專門針對運算資源極度受限的環境進行最佳化。 | 穿戴式裝置、超低功耗設備<br>`[極小體積]` `[極低功耗]` |

#### 📂 核心模型下載與資源
* **[Phi-4](https://huggingface.co/NyxKrage/Microsoft_Phi-4)** `[2024-12-13]`：微軟 Phi-4 正式發表，以小博大效能驚人。[📝 公眾號解析](https://mp.weixin.qq.com/s/uny1VUt7vk_ZU6hCH0EDGg)
* **[SmolLM2](https://github.com/huggingface/smollm/)** `[2024-11-04]`：Hugging Face 官方推出的手機執行小型語言模型。[📝 iThome 報導](https://www.ithome.com.tw/news/165832)
* **[Llama 3.2 (1B/3B)](https://ai.meta.com/blog/llama-3-2-connect-2024-vision-edge-mobile-devices/)** `[2024-09-25]`：Meta 震撼開源的端側邊緣運算 (Edge AI) 專屬模型。

---
## 🤔 Reasoning Models (深度推理模型)

自從 OpenAI 的 o 系列問世後，「Chain of Thought (思考鏈)」與「強化學習 (RL)」成為激發大模型數理運算與邏輯推理的標準配備。以下精選具備頂尖思考能力的開源推理模型：

#### 📊 邏輯推理模型快速比較表
| 模型名稱 | 開發團隊 | 💡 核心優勢與解決痛點 | 🚀 推薦適用場景 & 規格標籤 |
| :--- | :--- | :--- | :--- |
| **gpt-oss (120B)** | 🇺🇸 **OpenAI** | **o4-mini 級別的開源震撼彈**。OpenAI 重新擁抱開源，將具備極強邏輯推理與反思能力的大模型釋出給社群。 | 複雜程式碼生成、高階數學解題<br>`[頂級推理]` `[OpenAI]` |
| **Llama Nemotron Super v1.5** | 🇺🇸 **NVIDIA** | **三倍吞吐，單卡可跑**。49B 參數兼顧了極高的企業級效能與相對親民的硬體推論需求。 | 企業內部知識庫、高併發 API 服務<br>`[NVIDIA特化]` `[高CP值]` |
| **OpenReasoning-Nemotron** | 🇺🇸 **NVIDIA** | **1.5B 參數秒殺 o3**。將深度推理能力壓縮進極小參數中，堪稱邊緣運算領域的數學核武。 | 邊緣設備即時運算、專精型任務<br>`[極端輕量]` `[數學核武]` |
| **Video-R1** | 🌐 **開源社群** | **視覺與推理的終極結合**。將 R1 等級的強大推理能力延伸至「動態影片」的理解與邏輯分析上。 | 影片內容審查、動態物理規律分析<br>`[多模態推理]` `[影片解析]` |

#### 📂 核心模型下載與原理解析
* **[gpt-oss (120B)](https://huggingface.co/openai/gpt-oss-120b)** `[2025-08-05]`：OpenAI 重新開源的歷史性時刻，具備 o4-mini 水平的推理能力。[📝 官方 Blog](https://openai.com/zh-Hant/index/introducing-gpt-oss/) | [📝 機器之心解讀](https://www.jiqizhixin.com/articles/2025-08-06-2)
* **[Llama 3.3 Nemotron Super 49B v1.5](https://huggingface.co/nvidia/Llama-3_3-Nemotron-Super-49B-v1_5)** `[2025-07-29]`：NVIDIA 開源，主打三倍吞吐量且單卡可跑的企業級推理模型。[📝 知乎解讀](https://zhuanlan.zhihu.com/p/1933514869279274584)
* **[OpenReasoning-Nemotron 1.5B](https://huggingface.co/nvidia/OpenReasoning-Nemotron-1.5B)** `[2025-07-27]`：NVIDIA 打造的數學核武，以 1.5B 極小參數秒殺 o3 部分數理指標。[📝 公眾號解讀](https://mp.weixin.qq.com/s/o7RhRAFzAKkHj2T0y3GVzA)
* **[Llama-Nemotron](https://deepwiki.com/NVIDIA/NeMo)** `[2025-05-06]`：NVIDIA 高效推理系列基礎模型。[📄 論文解析](https://www.alphaxiv.org/zh/overview/2505.00949) | [📝 知乎解讀](https://zhuanlan.zhihu.com/p/1903012593033012833)
* **[Video-R1](https://github.com/tulerfeng/Video-R1)** `[2025-04-16]`：Reinforcing Video Reasoning in MLLMs，開啟多模態影片推理新紀元。[📄 論文解析](https://www.alphaxiv.org/zh/overview/2503.21776) | [📝 36Kr 報導](https://www.36kr.com/p/3252742390655489)
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
    * **[Qwen3.6-Plus](https://www.aliyun.com/product/tongyi)** `[2026-04-02]` 🔥
      * **核心優勢**：**定義「代理式編碼 (Agentic Coding)」新高度，支援百萬級超長上下文。** 阿里雲 2026 年旗艦力作，在 SWE-bench 與 Claw-Eval 等權威評測中展現出接近 Claude 的編碼實力，原生多模態推理讓 AI 能真正理解複雜的開發環境。
      * **解決痛點 / 推薦場景**：**解決了傳統 AI 難以處理「倉庫級」複雜專案與自動化 Debug 的痛點。** 實現了「一句話驅動寫代碼」的氛圍編碼，能自主在虛擬環境中拆解任務、測試並修改至完成，是企業打造「AI 程式設計代理」的理想核心。
      * **資源**：[🌐 阿里雲百煉控制台](https://help.aliyun.com/zh/model-studio/getting-started/what-is-model-studio) | [📝 技術深度解析：Qwen3.6 代理能力評測](https://zhuanlan.zhihu.com/p/2023033648056649131) | [🚀 立即體驗](https://tongyi.aliyun.com/)
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
**🔎 Embedding & Reranker (向量嵌入與重排序模型)**

在構建 RAG 系統時，如果檢索到的參考資料不準，再強的 LLM 也會產生幻覺 (Hallucination)。目前業界的黃金標準是採用「雙層檢索架構」：先用 **Embedding** 模型進行海量初篩，再用 **Reranker** 模型進行精準的二次排序。以下精選目前最具代表性的表徵模型：

### 1. 網頁級巨量檢索與搜尋引擎架構 (Web-Scale Retrieval)
想要打造媲美 AI 搜尋引擎的檢索準確度？直接使用目前地表最強搜尋引擎團隊的底層技術。

* **[pplx-embed-v1 系列 (Perplexity 出品)](https://research.perplexity.ai/articles/pplx-embed-state-of-the-art-embedding-models-for-web-scale-retrieval)** `[2026-02-28]`
  * **核心優勢**：Perplexity AI 官方釋出的尖端文本嵌入模型。包含 `pplx-embed-v1` 與 `pplx-embed-context-v1`。
  * **解決痛點**：專為「真實世界、充滿雜訊的 Web 級別檢索任務」所最佳化。如果您需要處理極度龐大、非結構化的網路抓取資料，這是目前最推薦的 RAG 檢索底座。[🤗 HuggingFace 權重](https://huggingface.co/collections/perplexity-ai/pplx-embed)

### 2. 中文生態系與私有化開源首選 (Chinese & Open Source)
針對繁簡中文語意理解優化，適合需要將資料留在本地端（Data Privacy）的企業內部知識庫。

* **[Qwen3 Embedding & Reranker (阿里通義)](https://qwenlm.github.io/zh/blog/qwen3-embedding/)** `[2025-06-05]`
  * **核心優勢**：阿里雲開源的新一代文本表徵與排序模型「黃金組合」。
  * **解決痛點**：一次開源了 Embedding 與 Reranker，讓開發者可以直接在本地端部署完整的雙層檢索管線。其中文語意檢索的準確率大幅領先同級別的西方模型。[🤗 Embedding 下載](https://huggingface.co/collections/Qwen/qwen3-embedding-6841b2055b99c44d9a4c371f) | [🤗 Reranker 下載](https://huggingface.co/collections/Qwen/qwen3-reranker-6841b22d0192d7ade9cdefea)

### 3. 企業雲端全託管服務 (Enterprise Cloud API)
適合已經建立在三大公有雲生態系，追求穩定性、免維護基礎設施的企業開發者。

* **[Gemini Embedding (Google Cloud)](https://cloud.google.com/vertex-ai/generative-ai/docs/embeddings/get-text-embeddings?hl=zh-tw)** `[2025-07-14]`
  * **核心優勢**：整合於 Google Vertex AI 平台。
  * **解決痛點**：提供極高併發與穩定的 API 呼叫，無縫銜接 Google Cloud 的 Vector Search (向量搜尋) 服務，適合大型企業建構雲端原生的 RAG 應用。

---

## Speech
**🔊 Speech-to-Speech LLM (端對端語音大模型)**

2026 年是「全雙工 (Full-Duplex)」語音交互的元年。新一代的 Speech-to-Speech (S2S) 模型徹底淘汰了傳統 ASR-LLM-TTS 的高延遲串聯架構，實現了「可隨時打斷、具備情緒感知、超低延遲」的真人級對話體驗。以下依據開發框架與底層模型進行深度分類：

### 1. 語音智能體開發框架與中介層 (Voice Agent Frameworks)
解決傳統 WebRTC 串接困難、音訊流處理複雜的痛點，幫助開發者快速搭建即時語音應用。

* **[TEN Agent](https://github.com/TEN-framework/TEN-Agent)** `[持續更新]`
  * **核心優勢**：王炸級開源端對端多模態智能體框架！極度適合用來打造低延遲的語音通話 AI，底層優化極佳。[📝 公眾號解析](https://mp.weixin.qq.com/s/pw9LQyRCRogfxAlYG3EfcQ) | [📝 開發者入坑記](https://mp.weixin.qq.com/s/ZVZHNP0XPwzGapWWqTk1kw) | [📖 搭建教學](https://uy6npdpeoi.feishu.cn/docx/EAWYdWWO7ormNPxUhyVcO3GSnUc)
* **[pipecat](https://github.com/pipecat-ai/pipecat)** `[持續更新]`
  * **核心優勢**：開源的即時語音/視訊 AI 框架。完美支援 ChatGPT 即時語音 API (Realtime API) 與各大開源模型，是建構 AI 客服與虛擬陪伴的底層神器。[📝 機器之心解讀 (2025-01-10)](https://www.jiqizhixin.com/articles/2025-01-10-4)
* **[HuggingFace Speech-to-Speech](https://github.com/huggingface/speech-to-speech)**
  * **核心優勢**：HuggingFace 官方推出的開源 S2S 實作管線，提供標準化的語音模型對接範例。

### 2. NVIDIA 企業級語音與全雙工模型 (Enterprise Voice AI)
針對企業級高併發推論與精準語意理解，NVIDIA 生態系提供了強大的底層支援。

* **[PersonaPlex-7B-V1](https://github.com/NVIDIA/personaplex)** `[2026-01-15]`
  * **核心優勢**：NVIDIA 開源重塑實時語音交互的「全雙工」黑科技！具備極強的抗干擾能力與人類情緒模擬，完美解決語音 AI 常見的「搶話」問題。[👉 本站深度技術分析](https://deep-learning-101.github.io/LLM/PersonaPlex) | [🤗 HuggingFace](https://huggingface.co/nvidia/personaplex-7b-v1) | [📄 官方論文](https://research.nvidia.com/labs/adlr/files/personaplex/personaplex_preprint.pdf)
* **[Audio Flamingo 3](https://github.com/NVIDIA/audio-flamingo)** `[2025-07-21]`
  * **核心優勢**：NVIDIA 開源的強大多模態音訊模型，不僅能聽懂人話，還能進行複雜的音頻事件理解與推理。

### 3. 端對端開源語音基礎模型 (End-to-End S2S Models)
* **[FlashLabs-Chroma 4B](https://huggingface.co/FlashLabs/Chroma-4B)** `[2026-01-24]`：新一代輕量級 Speech-to-Speech (S2S) 開源模型。
* **[Fun-Audio-Chat-8B](https://huggingface.co/FunAudioLLM/Fun-Audio-Chat-8B)** `[2025-12-24]`：阿里 FunAudioLLM 團隊推出的強效對話語音模型。
* **[LongCat-Flash-Omni](https://huggingface.co/meituan-longcat/LongCat-Flash-Omni)** `[2025-11-03]`：美團技術團隊釋出，宣告開啟全模態即時互動時代的里程碑之作。[📝 知乎解讀](https://zhuanlan.zhihu.com/p/1968699530762491165)
* **[Xiaomi-MiMo-Audio](https://huggingface.co/XiaomiMiMo/MiMo-Audio-7B-Base)** `[2025-09-19]`：小米開源的首個原生端對端語音大模型，專為硬體與 IoT 設備深度優化。[📝 知乎解讀](https://zhuanlan.zhihu.com/p/1991075806194205492)
* **[Voila](https://github.com/maitrix-org/Voila)** `[2025-05-08]`：主打 **195ms 超低延遲**，引領全雙工對話流暢度極限的開源實作。[📝 知乎解讀](https://zhuanlan.zhihu.com/p/1903776373765547954)

---

## Vision
**👁️ 👁️ Vision-Language Model (視覺多模態大模型)**

視覺大模型 (VLM) 正在從龐大的雲端叢林，逐步走向邊緣運算 (Edge AI) 與行動裝置。

* **[Seed1.5-VL (ByteDance)](https://github.com/ByteDance-Seed/Seed1.5-VL)** `[2025-05-20]`
  * **解決痛點**：具有視覺增強多模態能力的高階語言模型。在處理複雜圖表、多圖對比等高難度視覺推理任務上表現優異。[📄 AlphaXiv 論文](https://www.alphaxiv.org/zh/overview/2505.07062) | [📝 知乎解讀](https://zhuanlan.zhihu.com/p/1905914968433497765)
* **[nanoVLM (HuggingFace)](https://deepwiki.com/huggingface/nanoVLM)** `[2025-05-12]`
  * **解決痛點**：解決 VLM 難以在端側部署的痛點。專為邊緣運算與 IoT 裝置設計的微型視覺模型，具備極低的運算資源門檻。

---

## Multimodal
**🌌 多模態大模型與語音硬體終端 (Multimodal & Edge AI)**

>2025 至 2026 年，大語言模型正式長出「眼睛」與「嘴巴」。本區塊不僅收錄了能看懂複雜圖表的多模態基礎模型 (Vision-Language Models)，更為創客與物聯網 (IoT) 開發者整理了最齊全的語音硬體開源解決方案。> 隨著模型能力的進化，單一模態（純文字、純視覺）已無法滿足複雜的應用場景。新一代的基礎大模型原生支援視覺、語音與工具呼叫，是開發自動化 AI Agent 的核心大腦。

### 1. 頂尖多模態與視覺推理 (Vision & Complex Parsing)
需要讓 AI 看懂工程圖紙、財報表格或進行深度邏輯推理？這些是目前的開源王者：

* **[InternVL (OpenGVLab)](https://github.com/OpenGVLab/InternVL)** `[2026 最新持續更新]`
  * **核心優勢**：不斷刷新開源多模態大模型效能新紀錄的霸主！在視覺辨識精準度與圖文交錯理解上，是許多企業構建自研多模態應用的底座首選。[📄 論文解析](https://www.alphaxiv.org/zh/overview/2504.10479) | [📝 知乎深度解讀](https://zhuanlan.zhihu.com/p/1897681159359551408)
* **[Vision-R1](https://github.com/Osilly/Vision-R1)** `[2025-03-14]`
  * **核心優勢**：將類似 DeepSeek-R1 的強大「思考鏈 (Chain of Thought)」推理能力引入視覺領域，真正激發多模態大模型的邏輯推理極限。[📝 原理解讀](https://zhuanlan.zhihu.com/p/29618155786)
* **[Dolphin (ByteDance)](https://deepwiki.com/bytedance/Dolphin)** `[2025-05-24]`
  * **核心優勢**：字節跳動開源的複雜文件解析模型。專門對付排版混亂的 PDF、掃描檔與學術論文，是構建多模態 RAG 系統的絕佳前處理工具。[📄 論文](https://www.alphaxiv.org/zh/overview/2505.14059)
* **[HumanOmni (阿里通義)](https://github.com/HumanMLLM/HumanOmni)** `[2025-02-28]`
  * **核心優勢**：業界首個「第一視角 (Egocentric)」大模型！專為穿戴式設備（如 AI 眼鏡）與機器人視覺設計，能理解人類第一視角的操作意圖。[📝 公眾號解讀](https://mp.weixin.qq.com/s/acn16cvE8N4tMegKuGHAKQ)

### 2. 輕量化巨獸與端側部署 (SLM & Edge-side LLM)
記憶體有限，但又需要強大效能？這些模型能在消費級顯卡、甚至手機上流暢運行。

* **[Mistral Small 3.1](https://huggingface.co/mistralai/Mistral-Small-3.1-24B-Instruct-2503)** `[2025-03-18]`
  * **核心優勢**：歐洲 AI 巨頭的逆襲！具備 128K 超長上下文，在 24B 的輕量級體積下，各項基準測試效能直接碾壓 GPT-4o Mini，是性價比極高的商用 API 替代品。
* **[Phi-4 Family (Microsoft)](https://huggingface.co/collections/microsoft/phi-4-677e9380e514feb5577a40e4)** `[2025-02-27 更新]`
  * **核心優勢**：「小身材大智慧」的代名詞。最新的 Phi-4 Multimodal 版本以僅 56 億的參數規模，在多項任務中展現越級打怪的實力，是微軟在端側 AI 佈局的核心武器。[📝 效能評測](https://zhuanlan.zhihu.com/p/26984226500)
* **[MiniCPM 家族 (面壁智能)](https://github.com/OpenBMB)** `[2025-01-16 更新]`
  * **核心優勢**：端側開源模型的驕傲！最新發布的 MiniCPM-o 2.6 與 3.0 版本，不僅支援 Ollama 一鍵部署，更是少數能真正在手機端流暢運行並具備優秀視覺能力 (MiniCPM-V) 的模型。[📝 魔改教學](https://mp.weixin.qq.com/s/DjDznmtKZoJNKXYz0X4zog)

### 3. 全球化與泛用生態 (Global & Versatile)
* **[Gemma 4](https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/)** `[2026-04-02]`🔥
  * **說明**：Google DeepMind 重磅發布，號稱目前「每單位參數智力最高」的開源模型家族！這次一口氣推出 E2B、E4B、26B MoE 與 31B Dense 四種規格。其中 31B 版本在 Arena AI 文字排行榜殺入開源前三，甚至「越級打怪」擊敗了參數量大它 20 倍的對手，性價比（CP 值）突破天際。
  * **核心優勢**：
    1. **為 Agent 工作流而生**：不再只是純聊天機器人！它原生支援 Function Calling（工具呼叫）、結構化 JSON 輸出與系統指令，讓開發者能輕鬆打造自主呼叫 API 的 AI Agent。
    2. **全能多模態輸入**：直接吃下影像、影片甚至「語音」輸入。具備高達 256K 的超大上下文窗口，並涵蓋全球 140+ 種語言。
  * **資源**：[🤗 HuggingFace Collections](https://huggingface.co/collections/google/gemma-4)
* **[T5Gemma 2 (Google)](https://huggingface.co/collections/google/t5gemma-2)** `[2025-12-20]`：Google 開源的重磅模型，首創「140種語言 + 多模態 + 超長上下文」三位一體，是開發跨國多語系應用的殺手鐧。
* **[Gemma 3n Preview](https://deepmind.google/models/gemma/?hl=zh-tw)** `[2025-05-21]`：Google DeepMind 的次世代輕量模型預覽版。

---

### 🎙️ 語音助手與 IoT 開源硬體生態 (Voice AI & ESP32)
不想只在螢幕上打字？以下開源專案教你如何用最低廉的成本（如 ESP32 開發板），親手打造出媲美《鋼鐵人》J.A.R.V.I.S 的實體 AI 語音伴侶。

#### 🌟 爆紅創客專案：小智 AI (Xiaozhi ESP32) 生態系
在中文開源硬體圈掀起狂潮的 AI 陪伴機器人解決方案，涵蓋從硬體燒錄到伺服器架設的全套開源工具：
* **硬體與韌體核心**：[xiaozhi-esp32](https://github.com/78/xiaozhi-esp32) (基於 ESP32 的終端代碼) | [🛒 官方硬體購買指南](https://rcnv1t9vps13.feishu.cn/wiki/LdCrw9neaiGgzrkrFyjclllynYd)
* **後端伺服器建置**：[xiaozhi-esp32-server](https://github.com/xinnan-tech/xiaozhi-esp32-server) (快速架設設備控制後台，確保語音資料私有化)
* **無硬體體驗版**：[py-xiaozhi](https://github.com/Huang-junsen/py-xiaozhi) (手邊沒開發板？用 Python 直接在電腦上體驗小智功能)
* **多平台控制端**：[Web 用戶端](https://github.com/TOM88812/xiaozhi-web-client) | [Android 用戶端](https://github.com/TOM88812/xiaozhi-android-client)
* **📖 必讀手冊**：[小智 AI 聊天機器人百科全書](https://ccnphfhqs21z.feishu.cn/wiki/F5krwD16viZoF0kKkvDcrZNYnhb)

#### 🛠️ 通用開源語音作業系統與框架
適合進階開發者，用來打造車載語音、智慧家庭中樞的底層架構：
* **[ESP-AI](https://espai.fun/)**：專為 ESP 系列晶片打造的 AI 語音互動框架，文件齊全且高度模組化。
* **[OpenVoiceOS (OVOS)](https://github.com/OpenVoiceOS/ovos-core)**：致力於隱私優先的開源語音作業系統，Mycroft AI 的精神繼承者。
* **[fast-voice-assistant](https://github.com/dsa/fast-voice-assistant)**：主打極致回應速度的語音助理開發框架。
* **[gptspeaker](https://github.com/jackwuwei/gptspeaker)**：將 GPT 能力快速封裝進智能音箱的實作專案。

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