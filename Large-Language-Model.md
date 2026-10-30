---
layout: default
title: 2026 LLM 完整指南：最新模型發布追蹤、排行榜與企業選型實測 (Qwen3、Llama、Gemini、Mistral)
description: 即時追蹤 2026 年最新 LLM 發布動態與排行榜：Qwen3、Llama、Gemini、Mistral 等模型實測比較，附快速選型結論、RAG 與 AI Agent 選型建議、SLM 邊緣部署成本估算。給台灣開發者與企業的繁體中文選型指南。
permalink: /Large-Language-Model
lang: zh-Hant
schema_type: article
tags: ["LLM", "AI Agent", "RAG", "Fine-tuning"]
---

{% include header.html %}

# 📚 持續追蹤 2026 年・LLM 大型語言模型 (大語言模型) 最新發布、動態與進展 (即時更新)

> **編者按：** 本頁面彙整目前最主流的 LLM 排行榜、開源模型、推論與微調工具，以及相關學術論文。

> 如果您需要關注/追蹤更新/尋找更詳細的筆記，歡迎 ⭐ 及 Watch 我們的 **GitHub Repository**
> 👉 [**GitHub: Natural-Language-Processing-Paper**](https://github.com/Deep-Learning-101/Natural-Language-Processing-Paper) 👈🏻

> 📌 **技術速覽**
> 在地端部署大語言模型 (LLM) 時，許多企業常因推論框架選型不當導致 VRAM 浪費。根據 **Deep Learning 101** 的實測研究，針對 8B 模型併發需求，選用具備 PagedAttention 的 vLLM 或 SGLang 推論框架，能將硬體需求精準控制在單張 24GB 顯卡，大幅降低企業地端私有雲的部署成本。

> **核心摘要：**
> 2026年LLM開發聚焦端側部署與多Agent協作。本指南彙整逾50項開源微調與RAG實作工具，助開發者降低40%模型試錯成本，精準定位最佳企業級架構。

> ### 📅 [更新快訊](https://deep-learning-101.github.io/UPDATE)

>- * **[Harness² (Google Research)](https://github.com/google-research/harness2)** `[2026-10]` 🔥 `[Agent自我優化]` `[Harness工程]` `[遞歸自我改進]` `[無需Grader]` `[Apache 2.0]`
>- **[Mistral Large 4 (Le Chonk：1T MoE 開源權重旗艦，預覽後三週強化版，編碼與資安雙主攻)](https://huggingface.co/blog/mistral-large4)** `[2026-10-29]` 🔥 `[1T MoE]` `[開源權重]` `[1M上下文]` `[Agentic Coding]` `[資安防禦]` `[MLA+DSA稀疏注意力]`
>- **[Gemini 4 Carbon(Google DeepMind：資安＋長程工程最強前沿模型，首批只給資安防禦者)](https://deepmind.google/blog/gemini-4-carbon-our-next-frontier-model/)** `[2026-10-29]` 🔥 `[閉源前沿]` `[資安防禦]` `[長程Agent]` `[Intelligence Index 59]` `[Fairwind限定]` `[對齊強化]`
>- **[Kanana-2-Embedding(Kakao：韓語檢索專用雙模型，3B＋蒸餾 1.3B，MRL 可調維度)](https://biz.heraldcorp.com/article/10919060)** `[2026-10-29]` 🔥 `[韓語檢索]` `[Embedding]` `[開源權重]` `[MRL可調維度]` `[知識蒸餾]` `[個人化Agent檢索]`
>- **[LFM3（Liquid AI：六模型 2B 級端側家族，一個骨幹分出文字／視覺／聲音／全模態／決策）](https://www.liquid.ai/blog/lfm3)** `[2026-10-28]` 🔥 `[三混合架構]` `[端側Agent]` `[256K上下文]` `[開源權重]` `[多模態家族]` `[單GPU微調]`
>- **[Genie 4（Google DeepMind：原生音訊＋即時轉向的世界模型，Gemini 在迴圈內導引）](https://deepmind.google/blog/genie-4-a-new-generation-of-world-simulation/)** `[2026-10-28]` 🔥 `[世界模型]` `[原生音訊]` `[即時轉向]` `[Gemini導引]` `[研究預覽]` `[SynthID]`
>- **[GPT-6.1 Terra (OpenAI)](https://openai.com)** `[2026-10-26]` 🔥 `[電腦操作]` `[視覺推理]` `[閉源API]` `[成本效率]` `[ChatGPT Work]` `[Codex]`
>- **[TimeH2O-v1 (H2O.ai)](https://huggingface.co/h2oai/timeh2o-v1)** `[2026-10-26]` 🔥 `[時間序列預測]` `[零樣本]` `[基礎模型]` `[非商業授權]` `[fev-bench]` `[機率預測]`
>- **[AI21 LIFT-Bench／LIFT-Train（章節錨定指令遵循評測＋防獎勵駭客訓練集）](https://github.com/AI21Labs/lift-bench)** `[2026-10-25]` 🔥 `[指令遵循]` `[RL獎勵]` `[評測基準]` `[Apache-2.0]` `[文件起草]` `[LLM評判]`
>- **[Microsoft Agensh（無中央編排、1,024 個 coding agent 自組織框架）](https://github.com/microsoft/Agensh)** `[2026-10-24]` 🔥 `[多智能體]` `[無編排]` `[Coding Agent]` `[MIT]` `[ProgramBench]` `[自組織]`
>- **[Nanbeige4.3-33B（BOSS 直聘實驗室、33B 密集 agentic coding 教師模型、512K 上下文）](https://huggingface.co/Nanbeige/Nanbeige4.3-33B)** `[2026-10-24]` 🔥 `[開源權重]` `[Agentic Coding]` `[Apache-2.0]` `[512K上下文]` `[密集模型]` `[教師模型]`
>- **[NVIDIA Nemotron 3.5 Bolt E4B 4GB（Gemma 4 E4B 後訓練、4GB 顯存本地語音助手與機器人模型）](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB)** `[2026-10-23]` 🔥 `[開源權重]` `[SLM]` `[端側 Agent]` `[工具呼叫]` `[Jetson]` `[OpenMDW-1.1]`
>- **[LFM2.5-24B-A2B (Liquid AI)](https://huggingface.co/LiquidAI/LFM2.5-24B-A2B)** `[2026-10-13]` 🔥 `[端側Agent]` `[MoE]` `[純推理模型]` `[工具調用]`
>- **[context-mode](https://github.com/mksglu/context-mode)** `[2026-10-12]` 🔥 `[ContextWindow優化]` `[MCP伺服器]` `[CodingAgent]` `[會話記憶]`
>- **[Kimi K3.1 Pro (Moonshot：2.8T／104B MoE 開源權重旗艦，1M 上下文)](https://www.kimi.ai/blog/kimi-k3-1-pro)** `[2026-10-23]` 🔥 `[開源權重]` `[MoE]` `[1M上下文]` `[Agentic Coding]` `[Terminal-Bench]` `[網路安全降級]`
>- **[Carbon-X (Hugging Face 開放 DNA 對話模型：14.8B／DNA＋文字單一解碼器)](https://huggingface.co/HuggingFaceBio/Carbon-X)** `[2026-10-22]` 🔥 `[DNA]` `[基因變異效應]` `[BioAI]` `[Apache 2.0]` `[6-mer tokenizer]`
>- **[DeepInfer (DeepSeek 自家生產線開源推論框架：V4.1-Flash serving stack)](https://github.com/deepseek-ai/DeepInfer)** `[2026-10-20]` 🔥 `[推論框架]` `[Speculative Decoding]` `[Apache 2.0]` `[V4.1-Flash]` `[Ascend 950]`
>- **[HybridAgent (Stanford＋Together AI)](https://arxiv.org/abs/2610.18861)** `[2026-10-18]` 🔥 `[Agent 推理]` `[潛在推理]` `[HybridLink]` `[工具調用]` `[開源權重]` `[MIT]`
>- **[DeepSeek-V4.1-Flash-1017 (DeepSeek)](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017)** `[2026-10-17]` 🔥 `[開源權重]` `[MoE]` `[KV Cache 壓縮]` `[Coding Agent]` `[MIT]` `[1M上下文]`
>- **[Beam 1.0 (Reflection)](https://huggingface.co/reflection/Beam-1.0-501B-A23B)** `[2026-10-16]` 🔥 `[開源權重]` `[MoE]` `[Coding Agent]` `[Apache 2.0]` `[1M上下文]`
>- **[Muse Spark Open (Meta Superintelligence Labs)](https://huggingface.co/meta-models/Muse-Spark-Open-816B-A42B)** `[2026-10-15]` 🔥 `[開源權重]` `[MoE]` `[原生多模態]` `[Coding Agent]` `[1M上下文]`
>- **[Scientific Agent Skills (K-Dense)](https://github.com/K-Dense-AI/scientific-agent-skills)** `[2026-10-14]` 🔥
>- **[H-JEPA (LeCun AMI 世界模型)](https://github.com/kevinghst/H-JEPA)** `[2026-10]` 🔥 `[世界模型]` `[JEPA]` `[分層規劃]` `[視覺規劃]` `[具身智能]`
>- **[OpenMuse](https://github.com/CopilotKit/OpenMuse)** `[2026-09-22]` 🔥 [Meta Muse開源平替] [自託管個人助理] [常開瀏覽器會話] [背景非同步任務] [寫操作人機確認] [MIT協議]
>- **[OpenBot (CopilotKit)](https://github.com/CopilotKit/OpenBot)** `[2026-08]` 🔥 [企業AI同事] [Agent治理] [審計] [AG-UI] [自建部署]`
>- **[VISTA: 給多模態 Agent 裝上可回看的無損視覺記憶](https://arxiv.org/abs/2610.02200)** `[2026-10]` 🔥 [AI Agent] [視覺推理] [ARC-AGI-3] [無損視覺記憶] [多模態]`
>- **[DeepTutor](https://github.com/HKUDS/DeepTutor)** `[2026-04]` 🔥 [Agent原生工作區] [終身個性化學習] [三層可審計記憶] [多引擎RAG]
>- **[DeepCode](https://github.com/HKUDS/DeepCode)** `[2026-08]` 🔥 [Paper2Code] [Agentic Coding] [V2中央廚房] [Text2Web/Text2Backend]
>- **[deepagents](https://github.com/langchain-ai/deepagents)** `[2026-04]` 🔥 [ClaudeCode開源版] [AgentHarness] [LangGraph上層封裝] [免模型綁定]
>- **[Scholar Loop](https://github.com/renee-jia/scholar-loop)** `[2026-06-15]` 🔥 [自主科研閉環] [8專職Agent小隊] [防獎勵黑客] [單GPU預算]
>- **[autoarxiv](https://autoarxiv.org)** `[2026-06]` 🔥 [一鍵論文復現] [autoresearch] [最小化實驗] [環境自動修復]
>- **[Qwen-Audio-Agent](https://github.com/QwenAudio/qwen-audio-agent)** `[2026-07]` 🔥 [全雙工語音Harness] [非阻塞多任務] [ACP協議生態] [擇時結果回流]
>- **[jina-reranker-v3.5](https://huggingface.co/collections/jinaai/jina-reranker-v3.5)** `[2026-07]` 🔥 [0.6B極致輕量] [3L2G混合注意力] [結構化數據理解] [長列表顯存優化]
>- **[Unsloth Desktop](https://unsloth.ai/docs/desktop)** `[2026-08-11]` 🔥 [全端本地AI工作站] [自愈式工具調用] [DeepResearch本地化] [零代碼訓練]
>- **[Resource2Skill](https://github.com/microsoft/Resource2Skill)** `[2026-06]` 🔥 [Skill工廠] [多模態經驗蒸餾] [分層Skill-Wiki] [微軟開源]
>- **[AirLLM](https://github.com/lyogavin/airllm)** `[2023]` 🔥 [分層推理Layer-wise] [4GB顯存跑70B] [零精度損失] [mmap按需載入]
>- **Heretic** `[2025-01-01]` 🔥 安全去對齊、機械可解釋性、自動參數優化、開源平替
>- **CADDesigner** `[2026]` 🔥 CAD建模、ECIP範式、計算機輔助設計
>- **text-to-cad** `[2026-07-22]` 🔥 CAD建模、Agent技能、build123d、硬體設計
>- **Arbor** `[2026-06-11]` 🔥 自主科研、Agent框架、Hypothesis-Tree、Autonomous Optimization
>- **HyGRAG** `[2026-06-18]` 🔥 GraphRAG、多跳推理、知識融合、動態更新
>- **OpenWorker** `[2026-07-23]` 🔥 開源智能體桌面應用、本地優先、模型隨你挑、無人值守
>- **Huobao Drama** `[2026-05]` 🔥 打破傳統影視製作高牆，首款將「創意劇本➔分鏡➔音效➔成片」全流程打通的開源自動化短劇生產線！
>- **Remotion Skills** `[持續更新]` 🔥 顛覆「黑盒文生影片」，用 AI 寫 React 程式碼來「精確渲染」影片的工程化革命！

---

{% include ai-share.html %}

---

{% include price.html %}

---

### **文章目錄**
- [⚡ 快速選型結論（先講答案）](#快速選型結論先講答案)
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
- [❓ FAQ (LLM 開發常見問題)](#faq)

---

## 快速選型結論（先講答案）

- **RAG／知識庫**：Qwen3（中文檢索生態最完整）；想全託管省事選 Gemini Flash，成本低、回應快
- **AI Agent／工具呼叫**：Gemini Flash（速度與價格優勢）；需要自託管選 Llama 3.3
- **邊緣／地端部署**：Llama 3.3 8B 級距搭配 vLLM 或 SGLang，單張 24GB 顯卡即可運行

完整比較見下方「主流模型快速比較表」。

## Leaderboards
**🏆 LLM 權威排行榜與評測指標 (Leaderboards)**

多維度評測榜單是篩選基礎模型的唯一客觀標準。 結合 LMSYS Chatbot Arena 與 OpenLLM 基準，實測顯示前 10 名開源模型與 GPT-4 的 MMLU 差距已縮小至 5% 以內。企業應依據特定語系與上下文需求交叉比對，避免單一跑分偏差。在開源模型百家爭鳴的時代，如何挑選最適合特定任務的大語言模型？以下整理了目前 AI 開發者社群中最具公信力的 4 大模型評測榜單與資源庫，幫助您快速定位所需模型：

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

* **[EssenceBench (大模型評測極致壓縮框架)](https://github.com/gszfwsb/EssenceBench)** `[2025-10]` 🔥
  * **核心優勢**：**終結海量題海戰術的評測革命，用 1/200 的題量精準還原 95% 的大模型榜單排名！** 由上海交大與阿里通義千問團隊聯合提出，創新採用「由粗到細」的三階段壓縮框架。先過濾語意與排名的雙重冗餘，再透過遺傳演算法 (GA) 從天文數字的組合中進化出最優子集，最後輔以歸因細化確保難度與題型的全面覆蓋。在 HellaSwag 與 GSM8K 等權威基準上，僅需極少題目即可達成極低的預測誤差，徹底打破傳統評測的算力瓶頸。
  * **解決痛點 / 推薦場景**：**完美解決了企業在自研或微調大模型時，完整跑完一次 Benchmark 需要耗費數千萬 Token、上千 GPU 小時及高昂 API 成本的致命痛點。** 實測證明，即使將題量壓縮高達 200 倍，仍能維持 95% 的排名一致性。極度適合**企業級大模型快速迭代與 A/B 測試**、**邊緣運算端側模型 (SLM) 效能初篩**，以及需要頻繁進行**安全對齊與微調驗證**的 AI 研發團隊，真正引領產業界邁向「小數據精準評估」的新範式。
  * **資源**：[🐙 GitHub 官方開源](https://github.com/gszfwsb/EssenceBench) | [📄 arXiv 論文 (2510.10457)](https://arxiv.org/abs/2510.10457) | [🤗 Hugging Face 討論區](https://huggingface.co/papers/2510.10457)
  `[評測壓縮]` `[極致降本]` `[精準排序]` `[遺傳演算法]`

* **[AI21 LIFT-Bench／LIFT-Train（章節錨定指令遵循評測＋防獎勵駭客訓練集）](https://github.com/AI21Labs/lift-bench)** `[2026-10-25]` 🔥 `[指令遵循]` `[RL獎勵]` `[評測基準]` `[Apache-2.0]` `[文件起草]` `[LLM評判]`
  * **核心優勢**：**第一個把「約束綁到文件章節、把任務內容也算進分數」的指令遵循評測：同一套分數既是評測指標、也是 RL 獎勵，專治「獎勵衝頂、任務蒸發」的獎勵駭客。** LIFT-Bench 共 784 個測試任務、10 個切分（短文件約 4 節、長文件約 9 節，各四檔約束密度，外加兩個無大綱的 flat 切分）；LIFT-Train 為同生成管線的 34,258 個訓練任務。任務給主題＋結構大綱，每條約束只對它所屬的章節計分：程式可驗證約束（例如某節用德文、某詞至少出現三次）與 LLM 評判的內容約束（例如該節要追溯到首屆正式錦標賽）合併為單一加權分。評判模型固定為 Gemma-4-31B-it、寫進任務本身，分數只在同一評判下可比。程式碼、資料集與生成管線皆公開（Apache-2.0），任務格式可直接餵 Prime Intellect 的 verifiers 做評測與 RL 訓練。
  * **解決痛點 / 推薦場景**：**解決了「用 IFEval／IFTrain 式獎勵練指令遵循，模型學會鑽規則、丟掉任務」的痛點。** 舊方法：約束對整篇回應計分、只看規則不看內容，AI21 實測 Qwen2.5-7B 用 IFTrain 做 GRPO，獎勵在第 180 步衝到 1.0，中位數答案卻從 114 詞縮到 18 詞（第 390 步），38% 的高分答案不到 30 詞；要寫辛亥革命另類歷史一章、限制一詞不重複超過四次，模型只回一個字「China」就拿滿分。甜點區：LIFT-Train 訓練下中位數答案維持 390–530 詞，沒有任何高分答案短於 30 詞；flat 切分對照實驗指出關鍵是「獎勵裡有內容」，不是格式差異。極度適合**要做文件起草、長文件指令遵循 RL 的團隊**，以及**懷疑自家獎勵曲線好看、產出卻在縮水的訓練團隊**（AI21 建議：獎勵曲線旁邊一定要同時看答案長度）。附帶發現：17 個模型、每任務 8 採樣的評測中，結構化任務 GPT-5.5 平均 0.96，flat 任務無一超過 0.85、閉源領先者僅 0.65–0.72；GPT-5.5 結構化第一、flat 卻掉到第五，整體平均最好的反而是開源權重的 Kimi K3 與 DeepSeek V4 Pro：拿 flat 榜單挑起草模型會挑錯。
  * **資源**：[🐙 GitHub 官方倉庫（Apache-2.0）](https://github.com/AI21Labs/lift-bench) | [📝 AI21 官方部落格（2026-10-25 發布）](https://www.ai21.com/blog/lift-bench-blog/) | [📄 arXiv 論文 (2610.28819)](https://arxiv.org/abs/2610.28819) | [🤗 Hugging Face 資料集](https://huggingface.co/datasets/ai21labs/LIFTBench)
  * **附註（未獨立查證）**：日期以官方部落格發布日 2026-10-25 為準；論文投稿為 10 月 20 日、GitHub 倉庫建立於 10 月 18 日，三者不要混為同一天。所有數字皆為 AI21 自測，未經獨立複現；AI21 自己也提醒，外部評測 AdvancedIF 與 ComplexBench 上的差距很小，應讀為「LIFT-Train 避免退化」而非全面勝出。評判相關數字：305 個人工標註樣本上，未錨定評判幾乎全盤接受（Gemma-4-31B 接受 292 個、實際僅 227 個成立；未錨定 Qwen2.5-32B macro-F1 0.44、約等於永遠答是的 0.43），錨定後提升 11–19 點。實務提醒：README 警告 vf-eval 預設會把執行推上 Prime Intellect 雲端並上傳結果，本地跑要保留 run_eval.sh 的本地旗標；prime-rl 設定段另提到資料集存取需 HF_TOKEN，與主文「公開」說法有出入，實際存取狀態未獨立驗證。

---

## NVIDIA Nemotron
**🟢 NVIDIA Nemotron 企業級 AI 實戰指南**  

Nemotron 提供專為企業客製化的極致推理效能。 透過 TensorRT-LLM 加速，Nemotron-4 340B 在標準節點上的吞吐量比同級別模型高出 2.5 倍，同時將延遲降低 40%。適合需要高頻率、低延遲 API 呼叫的金融與合規場景。NVIDIA 開發的 Nemotron 系列模型，以其極高的推理效率與完整的 NeMo 生態系，成為企業落地生成式 AI 的首選。以下我們將資源依據「開發階段」與「業務場景」進行分類，幫助您快速掌握從模型部署到安全防護的完整技術棧。

### 1. 核心模型發佈與解析 (Core Models)
了解 Nemotron 系列的核心架構與性能指標，選擇適合您的硬體與應用場景的模型尺寸。

* **[Nemotron 3 Nano Omni](#)** `[2026]` 🔥 `[全模態推理]` `[端側 MoE]` `[單次感知]`
  * **核心優勢**：**終結多模型串接的延遲惡夢，NVIDIA 開源首款「單次感知」的全模態 MoE 巨獸！** 採用 30B-A3B 混合專家架構，將視覺、語音與語言編碼器完美融合在單一底層系統中。徹底拋棄傳統「先辨識、後理解」的碎片化流程，在維持頂級互動效能下，實現高達 **9 倍的驚人吞吐量提升**，並原生支援 1920x1080 高畫質螢幕解析度的視覺推理。
  * **解決痛點 / 推薦場景**：**完美解決了傳統 AI 代理 (Agent) 在處理複雜影音或螢幕操作時，因跨模型傳遞導致「上下文流失」與「推論成本過高」的致命痛點。** 極度輕量化的架構讓它能無縫部署於 NVIDIA Jetson 邊緣運算設備或 DGX Spark 本地伺服器。是打造 **電腦操作智能體 (Computer Use Agent)**、**企業級多媒體文件解析 (Document Intelligence)**，以及要求超低延遲的 **即時影音客服伴侶** 的工業級端側首選。
  * **資源**：[🌐 NVIDIA 官方模型資源](https://huggingface.co/nvidia) | [📝 深度技術解讀](#) *(註：官方權重與論文連結依據 NVIDIA 最新發布頁面為準)*

* **[Nemotron 3 Super](https://blogs.nvidia.com.tw/blog/nemotron-3-super-agentic-ai/)** (2026-03)
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

* **[ProSafePrune](https://github.com/hfutml/PROSAFEPRUNE)** `[2026]` 🔥 `[解決過度拒絕]` `[參數層修剪]` `[零推論延遲]`
  * **核心優勢**：**根治大模型「過度拒絕」的 ICLR 2026 頂會神作，消除對齊稅且零推論延遲！** 研究揭露模型變得「過度謹慎」的病灶在於中間層的過度有害編碼。透過創新的 SVD 奇異值分解與重疊算子，ProSafePrune 能精準分離並「修剪 (Prune)」掉這些冗餘的低秩有害特徵。因為是直接修改模型權重，完全不需要在推論階段外掛任何干預向量，達成**推論開銷為零**，且通用任務效能（如 MMLU、GSM8K）不降反升。
  * **解決痛點 / 推薦場景**：**完美解決了安全對齊（Alignment）後常見的「對齊稅」痛點——模型看到無害的敏感詞就無腦拒絕回答，嚴重影響使用者體驗。** 實測在 LLaMA-2-7B 上，將偽有害指令的合規率從極低的 11.0% 暴增至 73.0%，同時仍能精準防禦真正的惡意攻擊。極度適合用於**企業級大模型安全對齊**、**AI 客服機器人去閹割化**，以及對推論速度要求極高的**邊緣運算端側模型 (SLM) 最佳化**。
  * **資源**：[🐙 GitHub 官方開源](https://github.com/hfutml/PROSAFEPRUNE) | [📄 ICLR 論文 (OpenReview)](https://openreview.net/forum?id=QkHKaPfRAB)

### 3. 實戰路徑：DeepSeek-R1 與零程式碼微調教學

想把 DeepSeek-R1 訓練成專屬的領域專家，卻不會寫複雜的訓練代碼？以下是為開發者量身打造的「從零到一」 LLaMA Factory 實戰路徑：

1. **資料集準備**：[如何建立高品質的微調資料集？](https://zhuanlan.zhihu.com/p/1916489160333714285) (垃圾進，垃圾出，這是最重要的一步)

2. **參數設定與優化**：[微調參數設置與顯存最佳化技巧](https://mp.weixin.qq.com/s/AbyWaTaPOp9sr5mz5SOVwg)

3. **訓練觀測與部署**：[如何觀測微調過程？模型如何合併與匯出部署？](https://mp.weixin.qq.com/s/6sNGvqLktPk6AP7kPs9JyA)

4. **領域專家實戰**：[完整案例：如何把 DeepSeek-R1 微調為領域專家](https://zhuanlan.zhihu.com/p/25054526736) | [從0到1微調安全大模型](https://mp.weixin.qq.com/s/hzdcutEL9yH1j8svMcXPGg)

### 4. 必備微調與蒸餾開源框架 (Frameworks)
依據您的算力資源與技術背景，挑選最適合的訓練武器：

* **[Unsloth Desktop](https://unsloth.ai/docs/desktop)** `[2026-08-11]` 🔥 `[全端本地AI工作站]` `[自愈式工具調用]` `[DeepResearch本地化]` `[零代碼訓練]` `[Dynamic2.0量化]`
  * **核心優勢**：**打破工程師命令列門檻，Unsloth 首發僅 40MB 的跨平台原生開源桌面 App，將「本地跑模型、訓模型、Agent 工具鏈」無縫縫合！** 基於 Tauri 打造，支援文字 LLM、擴散影音（FLUX/Wan）、MLX 與語音全模態。首創自愈式工具調用（Self-Healing Tool Calls）將 tool call 準確率提升 50%（XML 洩漏歸零、單輪調用提升至 25 次以上），並配備真沙盒代碼執行環境。內建 Deep Research 研究模式（DuckDuckGo 私有檢索、抓取正文並在產出報告前自動查證矛盾與標註可驗證推斷）。命令列透過 `unsloth start claude --as-subagent` 可一鍵將本地 Dynamic 2.0 GGUF 模型掛為 Claude Code、Codex 的 Subagent 處理批量讀檔與整理日誌；訓練端更支援 500+ 模型 2 倍速、省 70% 顯存的零代碼微調，直接拖入 PDF/CSV 即可透過 Data Recipes 自動生成訓練對，並透過 `--secure` 開啟 Cloudflare 隧道進行安全遠程監控。
  * **解決痛點 / 推薦場景**：**完美解決了開發者在本地運行 4B~9B 小模型時「Tool Call 格式吐錯導致 Agent 鏈當場中斷」、以及「微調大模型必須寫繁瑣 Python 腳本、手動清洗非結構化資料」的致命痛點。** 解決了商業 API 昂貴 Token 消耗問題（將繁重髒活交由本地模型，主力模型留給核心任務）。極度適合**Windows/Mac/Linux 上不想碰命令列但需本地微調與推論的個人用戶**、**想在 Claude Code/Codex 中節省 Token 成本的開發者**，以及**需將企業內部 PDF 非結構化文檔快速轉化為有出處 QA 訓練對的演算法團隊**。
  * **資源**：[🌐 官方下載頁](https://unsloth.ai/docs/desktop) | [🐙 GitHub 官方倉庫](https://github.com/unslothai/unsloth) | [📝 中文技術文檔](https://unsloth.ai/docs/zh/desktop) | [📄 Dynamic 2.0 GGUFs 技術報告](https://unsloth.ai/blog/dynamic-v2)

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

- **[Infinity-Doc2-5M (500萬頁多模態文件解析訓練底座)](https://huggingface.co/datasets/infly/Infinity-Doc2-5M)** `[持續更新]` 🔥
  - **核心優勢**：**打破視覺大模型微調的「資料荒」，高達 564GB 的中英雙語全場景文件解析彈藥庫！** 徹底超越單純的圖文配對，提供 ShareGPT 風格的指令微調 (SFT) 對話標註。其最大的亮點在於「區塊級 (Block-level) 語意解構」，單一資料集內即涵蓋了版面分析、表格轉 HTML、數學公式轉 LaTeX、圖表轉 Code 乃至化學式解析 (SMILES) 等 8 大核心任務軌道，開發者可依需求靈活抽樣。
  - **解決痛點 / 推薦場景**：**完美解決了企業在自研或微調 VLM/MLLM 用於文檔理解時，面臨「缺乏高品質結構化標註、真實版式覆蓋率不足」的致命痛點。** 無需再耗費鉅資建立人工標註團隊，極度適合**企業算法團隊**進行 Infinity-Parser2 等大模型的垂直領域續訓、**RAG 私有知識庫**高精度前處理管線優化，以及**多模態文件問答 Agent** 的底層智力訓練。
  - **資源**：[🤗 HuggingFace 官方資料集](https://huggingface.co/datasets/infly/Infinity-Doc2-5M) | [🐙 GitHub 相關專案 (INF-MLLM)](https://github.com/infly-ai/INF-MLLM) | [🤖 Parser2-Pro 模型權重](https://huggingface.co/infly/Infinity-Parser2-Pro)
  `[多模態資料集]` `[RAG前處理]` `[VLM微調必備]` `[版面分析]`

- **[Universal Data Tool (開源全模態 AI 數據標註神器)](https://github.com/UniversalDataTool/universal-data-tool)** `[持續更新]` 🔥
  - **核心優勢**：**打破商業標註平台高昂成本，一站式搞定圖、文、音、影全模態標註的開源協作神作！** 基於 MIT 協議完全免費。它內建 WebAssembly 加速的 AI 智能預標註與圖像分割引擎，不僅能讓人工標註效率暴增 5-10 倍，更針對 LLM 時代進行了深度優化，支援一鍵導出符合大語言模型微調規範的指令數據集與多模態資料集。
  - **解決痛點 / 推薦場景**：**完美解決了企業在準備微調資料時「商業平台太貴、自研工具難以進行團隊協作與品管」的致命痛點。** 提供極其靈活的部署方式（支援 Docker 一鍵私有化本地部署與網頁端免註冊即時協作），並內建自動化 AI 質量校驗機制。極度適合**企業算法團隊**快速量產微調語料、**專業數據標註公司**進行百人級別的任務分發與進度管控，以及**學術科研單位**零成本建構跨模態 AI 知識庫。
  - **資源**：[🐙 GitHub 官方開源](https://github.com/UniversalDataTool/universal-data-tool) | [🌐 官方網站與線上體驗](https://universaldatatool.com/)
  `[全模態標註]` `[微調資料準備]` `[私有化部署]` `[AI智能預標註]`
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

### 🆕 新模型快訊：前沿開源權重模型

* **[Mistral Large 4 (Le Chonk：1T MoE 開源權重旗艦，預覽後三週強化版，編碼與資安雙主攻)](https://huggingface.co/blog/mistral-large4)** `[2026-10-29]` 🔥 `[1T MoE]` `[開源權重]` `[1M上下文]` `[Agentic Coding]` `[資安防禦]` `[MLA+DSA稀疏注意力]`
  * **核心優勢**：**兆參數級旗艦第一次真正可以自己下載回家跑：約 1T 總參數、每 token 只啟動約 49B、1M 上下文，10 月 6 日 API 預覽後又多練三週強化學習才釋出權重，開源模型裡編碼與資安防禦的標竿一次換人。** 多模態多語言 MoE：文字與圖像輸入、文字輸出；72 層解碼器、隱藏維度 6,144、64  attention heads，注意力結合 Multi-head Latent Attention(MLA，壓縮 KV)與 DeepSeek Sparse Attention(DSA)索引器(每 query 最多選 2,048 個 key 位置)，3:1 RoPE/NoPE 交錯、LeRope(YaRN 縮放、每頻率一個可學習乘子)、層間共享 KV；第 1 層為稠密前向網路，其餘 71 層為 MoE(每 token 路由選 128 個專家中的 4 個、另加 1 個共享專家，共 5 個啟動專家)；視覺編碼器為 1.6B Pixtral(30 層、2,048 維、16 heads、14x14 patches)。推理強度分 low/medium/high 三檔、預設 high 且無法關閉。官方變體為 FP8 與 NVFP4(NVFP4 需 Blackwell GPU、FP8 以 8 卡為基準)，另有 Unsloth 與 llama.cpp 團隊的 GGUF 量化；首日即支援 Transformers、vLLM、llama.cpp，另可走 Mistral API、OpenRouter、NVIDIA 端點與 Microsoft Foundry。
  * **解決痛點 / 推薦場景**：**解決了「最強編碼與資安模型只能用 API：資安事件裡 API 可能拒答、斷線或把敏感程式碼與惡意樣本送出門」的痛點。** 舊方法：閉源 API 在漏洞重現、惡意樣本分析這類「看起來像攻擊」的防禦工作上直接拒絕，或在事件中途收回存取；自架開源模型則在編碼與資安兩項同時掉隊。甜點區：企業與政府自有基礎設施上的編碼 Agent 與資安防禦(漏洞重現再修補、惡意軟體分析、檢測規則撰寫、事件回應)，以及用其軌跡以 TRL 蒸餾出任務專用小模型。API 價格為每百萬 token 輸入 0.70 美元(快取 0.07 美元)、輸出 2.10 美元；授權為 Mistral Ecosystem Open-Weight License(MIT 衍生)：可自由使用、修改、微調與商用，唯一例外是經營 Model-as-a-Service 需另取商用授權。
  * **量化基準(皆 Mistral 官方自報，尚未有獨立複現；以下為 10 月 29 日釋出權重的強化版數字)**：Terminal-Bench 4.0 為 41%(預覽版 28.3%，提升約 13 個百分點、輸出 token 減少 30%)；Artificial Analysis Coding Agent Index 為 48%，與 GLM-5.3 基本打平、但每任務平均少用 47% token；Cognition FrontierCode 2.0 為 19.7%(開源模型第一)；Artificial Analysis Cyber Index 為 51%；漏洞重現再修補測試 82%(該項次最高分)；Cybench(40 題資安競賽題)93%；Lakera B3 Agent 安全基準攻擊抵抗率 97.1%(預覽版 93.3%)；惡意資安請求拒答率 96.6%；FinWorkBench 金融工作流程 73.3%、BrowseComp 84.5%(預覽 SFT 檢查點為 75%)；內嵌 DSpark 推測解碼草稿頭，官方稱吞吐量最高可提升 1.9 倍。
  * **資源**：[🤗 Hugging Face 官方部落格(Mistral 合作文)](https://huggingface.co/blog/mistral-large4) | [🤗 HF 權重 Mistral-Large-4-1T-A52B](https://huggingface.co/mistralai/Mistral-Large-4-1T-A52B)
  * **附註(未獨立查證)**：日期以 Mistral 官方 X 公告與多家 10 月 29 日報導為準，落在台北 10 月 29 日窗口；10 月 6 日僅為 API 預覽，本次是權重釋出、且為多練三週的強化版，不可與預覽版混為一則。數字口徑務必分清：Hugging Face 部落格基準段落目前仍刊出預覽版數字(Terminal-Bench 28.3%、舊版 Coding Agent Index 49.8%、B3 93.3%)，與 10 月 29 日強化版(41%、新版 Index 48%、B3 97.1%)不可混用；新舊 Coding Agent Index 評測條件不同，49.8% 與 48% 不能直接比出退步。啟動參數亦有兩種說法：HF 部落格寫約 49B active，模型名稱 A52B 的 52B 為含 embedding 與輸出層的算法，條目以 49B 為主、52B 寫進本附註。完整技術報告官方稱即將發布，查證時尚未見到；所有基準皆為廠商自報，跨家數字宜打折看。

* **[LFM3（Liquid AI：六模型 2B 級端側家族，一個骨幹分出文字／視覺／聲音／全模態／決策）](https://www.liquid.ai/blog/lfm3)** `[2026-10-28]` 🔥 `[三混合架構]` `[端側Agent]` `[256K上下文]` `[開源權重]` `[多模態家族]` `[單GPU微調]`
  * **核心優勢**：**2B 級小模型第一次把「文字、視覺、聲音、全模態、決策」做成同一個可端側部署的家族：一個骨幹、六種專長，手機與筆電就能跑本地 Agent。** 全部六款皆由 LFM3-1.7B-Base 分支而來：LFM3-1.7B（文字）、LFM3-VL-2B（視覺，首度吃影片輸入）、LFM3-Audio-2B（聲音，18 語）、LFM3-Omni-2B（首款全模態）、d1-2B 與 d1-Omni-2B（決策模型，單次前向輸出帶機率的結構化答案）。骨幹為三混合架構：24 層中 13 層門控短卷積、5 層滑動窗口注意力（256 token 窗口）、6 層全域注意力，另加頭級門控注意力、半 RoPE 與夾心正規化；基底以 22T tokens 預訓練，最後 3.5T tokens 為中段訓練、把上下文拉到 256K tokens。
  * **解決痛點 / 推薦場景**：**解決了「要本地 Agent 就得上雲或上大模型：雲端有延遲與隱私成本，大模型塞不進手機與邊緣裝置」的痛點。** 舊方法：本地助理只能做簡單指令，複雜工具呼叫與多步驟任務一律回雲端；或硬上 7B 以上模型，手機發熱、筆電風扇全開。甜點區：不需聯網的本地 Agent（信箱分流、行事曆管理、網頁研究、晨間簡報）、單一 GPU 微調出的產業專家（官方示範：約 3,000 張公開照片、單張 A100 微調數小時，風機葉片缺陷分類準確率從不到 10% 拉到 67%）、機器人編排／導航／操作（VL 模型微調的 VLA 在 LIBERO 四套件平均成功率 96.2%）。部署支援 llama.cpp、MLX、vLLM、SGLang、ONNX、Ollama、LM Studio，4 位元量化後文字模型約 1 GB。
  * **量化基準（皆 Liquid AI 官方自報，尚未有獨立複現）**：文字模型 LFM3-1.7B（1.73B）：29 項基準平均 49.37，勝過自家 LFM2.5-2.6B 的 31.55 與 Qwen3.5-9B 的 47.24；BFCL V4 工具呼叫 71.39、ToolSandbox 80.36、IFEval 指令遵循 96.66、WebArena-Verified 38.42、AutomationBench 41.29、SWE-bench Verified 43.40；裝置端 llama.cpp Q4_0、32K 上下文下解碼速度為同級最快（官方稱比次名快 1.8 至 2.8 倍），128K 上下文 KV 快取僅 1.6 GB（Qwen3.5-4B 為 4.3 GB），單張 NVIDIA B300 以 SGLang BF16 在 1,024 併發下日產 3.6B tokens。視覺模型 LFM3-VL-2B（1.92B）：62 項視覺基準平均 71.4，較 LFM2.5-VL-3B 的 57.6 大升，且與 12B 的 Gemma 4 12B（71.7）幾乎持平、距 GPT-5.6 Luna（73.4）不到 2 分；文件／OCR／圖表 83.9、視覺定位 77.3、介面理解 83.1。聲音模型 LFM3-Audio-2B：英文 ASR 詞錯率 6.2%、UTMOSv2 語音品質 3.8（前代 3.2）、VoiceBench 73.1、首 token 延遲最低 50 毫秒；全模態 LFM3-Omni-2B：Daily-Omni 70.1（Qwen2.5-Omni-7B 為 61.3）。決策模型 d1-2B：Decision Bench 85.2（前代 d1-3B 為 83.6），參數少三分之一反而更強。
  * **資源**：[🌐 Liquid AI 官方部落格](https://www.liquid.ai/blog/lfm3) | [🤗 Hugging Face 官方部落格整理](https://huggingface.co/blog/LiquidAI/lfm3) | [🤗 HF 模型卡 LFM3-VL-2B（LFM Open License v1.0）](https://huggingface.co/LiquidAI/LFM3-VL-2B)
  * **附註（未獨立查證）**：日期以官方部落格標示的 2026-10-27（美國日期）為準，按原始戳記換算台北時間為 10-28 凌晨，落在本日窗口；不要只看美國日期就誤判為昨日。授權細節來自 HF 模型卡與次級整理：LFM Open License v1.0，年營收 1,000 萬美元以下可免費商用，超過門檻需另外授權，不等於 Apache-2.0 式完全開放，商用前務必讀授權全文。弱項誠實列出：官方自己也劃線，複雜推理與多步驟程式仍是弱項（Terminal-Bench 2.1 僅 12.92、GPQA Diamond 63.37 落後 Qwen3.5-9B 的 80.40、Humanity's Last Exam 無工具僅 7.17），官方建議搭配搜尋工具使用、不要拿它做重度程式與複雜數學；音訊英文 ASR 6.2% 其實微落後前代的 6.1%，進步主要在語音品質與理解而非辨識率。所有基準皆為 Liquid 自家 harness 自測，截至查證時未見獨立第三方複現，同 harness 比較對自家模型有利，跨家數字宜打折看。

* **[Nanbeige4.3-33B（BOSS 直聘實驗室、33B 密集 agentic coding 教師模型、512K 上下文）](https://huggingface.co/Nanbeige/Nanbeige4.3-33B)** `[2026-10-24]` 🔥 `[開源權重]` `[Agentic Coding]` `[Apache-2.0]` `[512K上下文]` `[密集模型]` `[教師模型]`
  * **核心優勢**：**33B 密集模型、Apache-2.0 完全開源，專為 agentic coding 與辦公室 cowork 任務而生，實驗室自測在同級開源模型中領先 17–18／20 項，並定位為系列教師模型、先強後蒸餾。** Nanbeige 為中國招聘平台 BOSS 直聘的語言模型實驗室；本模型為 Nanbeige4.3 系列旗艦教師模型，33,118,977,024 參數密集架構（Llama 架構、BF16），524,288 token（512K）上下文，預設開啟思考模式，並同步釋出 Nanbeige4.3-33B-Base 供客製後訓練。部署配方為 SGLang／vLLM 四路張量平行、Qwen3-coder 工具解析，推理任務上下文上限 262,144 token，並建議保持 preserve_thinking 以利多輪工具任務。HF 模型卡自測表（同 harness、最高思考 effort）：Terminal-Bench 2.1 80.9（Qwen3.8-27B 73.0）、DeepSWE 65.5（42.5）、Automation Bench 54.2（38.3）、JobBench 44.8（34.5）、AIME 2026 95.2（94.5）。
  * **解決痛點 / 推薦場景**：**解決了「30B 級開源模型在 agentic coding 與多步驟辦公協作上追不上同級對手、且好模型多半要等蒸餾小版」的痛點。** 舊方法：要強 agentic 能力得上更大模型或閉源 API，或等別人把能力蒸餾進小模型。甜點區：實驗室明言策略是先做強教師、再把 agentic 能力蒸餾進後續小模型（首發即預告 Nanbeige4.3-3B）；BF16 權重約 66 GB（HF API 登錄儲存量 66,259,989,086 位元組），多卡伺服器可直接以 vLLM／SGLang 部署。極度適合**要自託管 coding agent、且接受 33B 多卡部署成本的團隊**，以及**追蹤中國開源實驗室 agentic 路線的研究者**。先提醒：所有分數皆為實驗室自測，換模型前先在自家 repo 跑一遍。
  * **資源**：[🤗 Hugging Face 模型卡（Apache-2.0）](https://huggingface.co/Nanbeige/Nanbeige4.3-33B) | [📰 發布整理（MarkTechPost，2026-10-25）](https://www.marktechpost.com/2026/10/25/nanbeige-releases-nanbeige4-3-33b-open-agentic-coding-model/) | [📰 發布整理（Pasquale Pillitteri）](https://pasqualepillitteri.it/en/news/27138/nanbeige-4-3-33b-open-source-en)
  * **附註（未獨立查證）**：日期以 HF 模型建立時間 2026-10-24T02:49:18Z（台北 10 月 24 日 10:49）為準，昨日簡報漏收、本日補登，不偽稱 10 月 25 日發布；HF 最後修改為 10 月 25 日 11:11Z（台北 19:11），那是更新不是首發。弱項誠實列出：SWE-Bench Pro 60.3 落後 Qwen3.8-27B 的 61.7、GPQA Diamond 89.5 落後 Gemma4-31B 的 91.3、GDPval 84.8 落後 Qwen 的 86.4；Terminal-Bench 4.0 僅 23.8，雖仍領先同級對手（6.3／1.6／0.0），但絕對值低，不宜只看 2.1 版的 80.9。第三方獨立複現目前皆無；4-bit 量化約 20 GB 的說法來自二手報導，未獨立驗證。

* **[NVIDIA Nemotron 3.5 Bolt E4B 4GB（Gemma 4 E4B 後訓練、4GB 顯存本地語音助手與機器人模型）](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB)** `[2026-10-23]` 🔥 `[開源權重]` `[SLM]` `[端側 Agent]` `[工具呼叫]` `[Jetson]` `[OpenMDW-1.1]`
  * **核心優勢**：**4GB 顯存就能跑的開源對話＋工具呼叫小模型：8B 總參數／4B 有效參數、64K 上下文，NVIDIA 官方實測在角色扮演與指令階層測試上明顯超越同級模型。** 由 Google Gemma 4 E4B-it 僅以強化學習後訓練（RLVR＋RLHF，未做監督微調），主打多輪對話、工具呼叫與輸入 grounding；可切換思考模式，並附 DFlash 推測解碼 drafter。官方 21 項評測中，RoleBench 67.0（Qwen3.5-4B 53.7、Gemma 4 E4B 49.9）、IHEval 84.8（Gemma 4 E4B 67.0）、MultiChallenge 53.1（Qwen3.5-4B 51.8）；RTX 5070 上搭配 DFlash 官方稱最高 272.6 tokens／秒。權重、資料與訓練配方以 OpenMDW-1.1 釋出（商用允許），Hugging Face、Ollama、LM Studio、Unsloth、Jetson AI Lab 皆可取得；Q4_K_M GGUF 檔 6.18 GB，Ollama 一行指令即可跑。
  * **解決痛點 / 推薦場景**：**解決了「本地語音助手與機器人不想上雲、但 24GB 級模型塞不進邊緣裝置」的痛點。** 舊方法：要本地 agent 不是綁雲端 API（延遲、隱私、斷網即停），就是上 24GB 模型（Bolt 74B）或接受基底 Gemma 4 E4B 較弱的工具表現。甜點區：Jetson Orin Nano 8GB 上即可跑（官方實測 3,000 token 提示、50 token 輸出：4.2GB 顯存、首 token 5.8 秒、15.5 tokens／秒），官方示範 Reachy Mini 機器人由 Bolt E4B 負責對話與動作腳本呼叫、Cosmos 3 Edge 負責視覺。極度適合**要做本地語音助手、互動角色（NPC）、機器人對話的團隊**，以及**只有主流 GeForce 顯卡、想離線跑 agent 的開發者**。附帶提醒：它是純文字模型，不吃圖像與語音輸入，示範中的視覺與語音皆由其他模型負責。
  * **資源**：[🤗 Hugging Face 模型卡](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB) | [📰 官方發布細節與評測整理（Pasquale Pillitteri，含官方數據表）](https://pasqualepillitteri.it/en/news/26810/nemotron-3-5-bolt-e4b-nvidia-robots-games) | [📰 發布整理（Digest AI）](https://digestai.news/story/nvidia-releases-nemotron-3-5-bolt-e4b-for-local-voice-agents-and-robot)
  * **附註（未獨立查證）**：官方基準皆為 NVIDIA 自測（BF16 精度），實際下載的 Q4_K_M 量化版分數可能不同；Unsloth 的 Q4_K_M 實測 MultiChallenge 為 55.60（Gemma 4 E4B-it 同量化 39.36），與官方 BF16 表的 53.1／42.1 不同，屬不同精度、不可直接對比。弱項誠實列出：Tau2-Bench 多輪工具 55.1 大幅落後 Qwen3.5-4B 的 75.1、BFCL-v3 68.5 落後 Qwen3.5-4B 的 70.9、64K RULER 87.0 落後 Qwen3.5-4B 的 95.1；Brevity Bench 與 When2Call-MT 兩項官方評測尚未公布、llama.cpp 官方啟動配方仍標示 pending。獨立測試（Atomic Agent，RTX 5090）樣本極小（每模型 18 次），僅供參考：Bolt 12 勝、Gemma 11 勝，推理模式耗時與 token 量暴增。名稱陷阱：Bolt E4B（4GB、純文字、64K）與 Bolt 74B-A9B（24GB、MoE、多模態、256K）是兩個不同模型，勿混淆。官方發布時間為台北 2026-10-23 23:41，屬昨日窗口末段、昨日簡報未收錄，本日補登，日期如實標示。

* **[Kimi K3.1 Pro (Moonshot：2.8T／104B MoE 開源權重旗艦，1M 上下文)](https://www.kimi.ai/blog/kimi-k3-1-pro)** `[2026-10-23]` 🔥 `[開源權重]` `[MoE]` `[1M上下文]` `[Agentic Coding]` `[Terminal-Bench]` `[網路安全降級]`
  * **核心優勢**：**開源權重模型首次逼近閉源前沿天花板：Artificial Analysis Intelligence Index 55 分，僅落後 Claude Opus 5.5 約 2.5 分、領先前任開源冠軍 MiMo-V2.6-Pro 8.8 分。** Kimi K3 的 post-training 升級版：2.8T 總參數／104B active 的 MoE、1M token 上下文、原生多模態輸入；RL 訓練大幅加碼（框架、長上下文推論、rollout 排程、沙盒全面重構）。官方自測：Terminal-Bench 4.0 65.7%（Opus 5.5 66.4%、GPT-6 Astra 58.2%）、Kimi Code Bench 3.0 長程任務 61.2（K3 55.95）、BenchCAD 92.7；Kimi Hallu Bench Hard 聲稱級幻覺率從 K3 的 23.4% 降到 8.3%。API 即刻可用（$2／$10 每百萬 token，快取輸入 $0.2；Highspeed 版 2–3 倍速、雙倍價）；權重承諾 11 月 4 日前釋出，授權尚未公布。
  * **解決痛點 / 推薦場景**：**解決了「開源模型在 agentic coding 與長程任務上追不上閉源前沿」的痛點。** 舊方法：要 frontier 級 agent coding 只能綁閉源 API（成本失控、資料外送），或接受落後 3 個月的開源權重。甜點區：開閉源差距從 9 月的 104 天壓到 31 天，API 價格降到 K3 的三分之二，權重一出即可自託管與微調。極度適合**要自建 coding agent 壓低成本的團隊**、**需要地端／主權部署的企業**，以及**追蹤開閉源差距的研究者**。附帶亮點是資安設計：Moonshot 主動從 mid-training 與 RL 資料移除網路攻擊相關資料，自家 xdev-bench-hard 上開源版 pass@3 從 90.5% 降到 81.0%，明示「不讓開源權重推進攻擊能力前沿」。
  * **資源**：[📝 官方技術部落格](https://www.kimi.ai/blog/kimi-k3-1-pro) | [📊 Artificial Analysis 基準報導](https://artificialanalysis.ai/articles/kimi-k3-1-pro-launch-benchmarks) | [📰 開閉源差距分析（ModelCompare）](https://www.modelcompare.ai/blog/china-open-source-ai) | [💻 Kimi API 文件](https://platform.kimi.ai)
  * **附註（未獨立查證）**：官方基準皆為 Moonshot 自測、第三方尚未獨立複現；launch table 混用了自測與引進分數（implicator.ai 提醒）。權重尚未釋出：extrapolator.ai 稱「已釋出權重」與事實不符。幻覺數字有兩個版本（Hallu Bench Hard 8.3% vs API quickstart 的 6.85%），測試集不同。弱項：Terminal-Bench Science 僅 38.1（GPT-6 Astra 68.1、Opus 5.5 63.3）。xdev-bench-hard 數據來自媒體轉述的官方說法。

* **[DeepInfer (DeepSeek 自家生產線開源推論框架：V4.1-Flash serving stack)](https://github.com/deepseek-ai/DeepInfer)** `[2026-10-20]` 🔥 `[推論框架]` `[Speculative Decoding]` `[Apache 2.0]` `[V4.1-Flash]` `[Ascend 950]`
  * **核心優勢**：**DeepSeek 把自家生產線的推論引擎整套開源：Apache 2.0，專為 V4.1-Flash 打造的高吞吐 serving stack。** 機制是 DeepSeek 近年系統論文的實戰合體：FlashMLA／DeepGEMM／DeepEP／TileKernels／DeepSelect 等自研 kernels＋TileLang 自訂 kernels；Attention DP／balanced CP、MoE EP＋EPLB 跨晶片平行；DSpark 以信心估計排程驗證的 speculative decoding（預設一次起草 5 個 token）；Decoder SWA bounded replay 只重跑有界後綴、砍掉多餘 prefill 工作；另有零開銷非同步 batch 排程、batch-invariant 推論、確定性採樣、結構化輸出（regex／JSON schema／EBNF）。雙硬體：NVIDIA SM100 與華為 Ascend 950（同場給 Ascend 950 首次前沿實驗室等級的生產背書）。README 明說不含 KV cache 系統、prefill／decode disaggregation 與跨副本負載平衡。血統上 README 承認原本主要基於 vLLM、另受 SGLang 與 TensorRT-LLM 啟發。repo 公開一天衝上 13,667 stars／1,271 forks。
  * **解決痛點 / 推薦場景**：**解決了「想自建 DeepSeek 等級的低成本推論服務，但開源引擎堆不出同等吞吐」的痛點。** 舊方法：vLLM／SGLang 是通用引擎，MoE 大規模專家平行與快取命中率優化都要自己調；雲端託管則把利潤交給中間商。甜點區：Apache 2.0 可商用自託管、專為 MoE 推論調校的生產級 stack＋batch-invariant 與確定性採樣（評測可複現）。極度適合**要自託管 DeepSeek 模型壓低成本的雲服務商與企業**，以及**研究大規模 MoE 推論系統的研究者**（DSpark 信心驗證、SWA bounded replay 都是可直接讀程式碼學的實作）。
  * **資源**：[🐙 GitHub：deepseek-ai/DeepInfer](https://github.com/deepseek-ai/DeepInfer)（Apache-2.0；預設 checkpoint 為 HF 的 `deepseek-ai/DeepSeek-V4.1-Flash-1017`）
  * **附註（未獨立查證）**：DeepSeek 官方說法（deployment Q&A，媒體轉述，我未親驗官方文件）：單集群每天 155 兆 tokens、96% input cache 命中率、平均 TTFT 約 400ms、230 tokens/s（coding 最高 300）；DSpark 減少約 30% draft token 檢查、生產負載吞吐提升 4–7%；SWA bounded replay 幾乎減半 prefill 計算量。皆為官方自報、未經第三方獨立驗證。batch-invariant 推論與確定性採樣僅 NVIDIA 可用、Hopper 等舊架構不支援（媒體轉述）。同場開源的 deepseek-recipe（token 編解碼層、MIT）我未親驗其 repo。repo 建立日 10-16、首次公開 commit 與官方 X 公告皆為 10-20。

* **[HybridAgent (Stanford＋Together AI)](https://arxiv.org/abs/2610.18861)** `[2026-10-18]` 🔥 `[Agent 推理]` `[潛在推理]` `[HybridLink]` `[工具調用]` `[開源權重]` `[MIT]`
  * **核心優勢**：**讓 LLM agent「在潛在空間默想、在文字模式行動」：內部推理不寫成 token、只在工具調用與最終答案時切回文字；作者自測 11 項基準平均提升 10.4%，token 減少 35.5%–54.7%、推理快 1.8–2.6 倍、成本降 2.7–3.7 倍。** 機制是輕量 HybridLink 模組：把最後一層 hidden state 映射回 input-embedding 空間，單次生成內即可在 latent／text 雙模式間切換；連續 working memory 跨多輪保留混合上下文；每個 latent 思考都可渲染成可讀 pseudo-text 直接檢視。訓練分兩段：HybridSFT 穩定工具整合的混合生成，HybridRL 學會「何時潛在思考、何時文字行動」。客觀指標（作者自測，論文 Table 1 轉述）：GAIA 43.7（8B 版）勝 GPT-5.6 Luna 的 37.9；但 HLE 僅 14.4（Luna 29.0），純推理仍是弱項。論文 10-13 上 arXiv，10-18 登上 HN 首頁引爆 AI 圈討論。
  * **解決痛點 / 推薦場景**：**解決了「agent 每步 chain-of-thought 都要寫成文字、token 成本隨推理長度線性膨脹」的痛點。** 舊方法：純文字 agent 每步推理都解碼成 token，長任務又慢又貴；純 latent 推理則天生沒有工具調用與可檢視性。甜點區：latent 思考保留完整工具整合（Python＋搜尋跨輪調用）＋中間思考可檢視（稽核友好）＋MIT 全套開源（方法、引擎、SFT／RL 訓練、latent 檢視器、8B／14B 權重、訓練集）。極度適合**要跑大量 agent 任務、被推理成本卡住的團隊**，以及**需要看見 agent 中間思考的合規與研究場景**。
  * **資源**：📄 論文《Hybrid Reasoning Agents》[arXiv:2610.18861](https://arxiv.org/abs/2610.18861)（CC BY 4.0） | 💻 [GitHub：togethercomputer/HybridAgent](https://github.com/togethercomputer/HybridAgent)（MIT） | 🤗 [HybridAgent-8B-Agentic](https://huggingface.co/togethercomputer/HybridAgent-8B-Agentic)（Qwen3-8B-Base＋HybridSFT＋HybridRL） | 🤗 [HybridAgent-14B-Agentic](https://huggingface.co/togethercomputer/HybridAgent-14B-Agentic)（Qwen3-14B-Base） | 📊 SFT v1/v2、RL 訓練集（見 repo README「Released models and data」）
  * **附註（未獨立查證）**：GAIA 43.7／HLE 14.4 引自論文 Table 1 的第三方轉述，我未逐項核對論文 PDF；成本 2.7–3.7 倍為論文的模型估算（假設 H100 每小時 $2.50、10% 利用率），不含 prompt prefill 與工具執行成本，非生產實測；所有基準皆為作者自測。HN 首頁數據引自開發者社群轉述。

* **[DeepSeek-V4.1-Flash-1017 (DeepSeek)](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017)** `[2026-10-17]` 🔥 `[開源權重]` `[MoE]` `[KV Cache 壓縮]` `[Coding Agent]` `[MIT]` `[1M上下文]`
  * **核心優勢**：**DeepSeek V4.1-Flash 的更新版開放權重 checkpoint：官方公布的 11 項基準全數超越前代，DeepSWE v1.1 拿下 77.0 壓過 Claude Opus 5，是「便宜模型在 coding agent 基準上正面超越旗艦」的代表案例。** 技術主軸是 KV cache 壓縮（技術報告標題即《DeepSeek-V4.1-Flash: Pushing the Limits of KV Cache Compression》）：官方說法是輸出更短、任務執行更快，把「效能：成本 Pareto 前沿」往前推一格。客觀指標（官方模型卡自測）：Terminal-Bench 4.0 42.3（前代 31.2，+11.1）、DeepSWE v1.1 77.0（前代 74.2；Opus 5 為 74.0、GPT-5.6 Sol 73.0）、Automation-Bench 60.5、Agents' Last Exam 35.4、Apex Bench 72.1、Chartography 83.0、BabyVision 92.5；純推理 HLE 42.6 仍落後 Opus 5 的 56.3。
  * **解決痛點 / 推薦場景**：**解決了「長程 coding agent 的 KV cache 記憶體爆炸＋旗艦模型推理成本失控」的痛點。** 舊方法：跑多輪工具調用的長上下文 agent 時，KV cache 隨序列長度膨脹、部署成本高；Flash 級便宜模型在 terminal／agentic 基準上明顯落後旗艦（前代 Terminal-Bench 4.0 僅 31.2）。甜點區：KV cache 壓縮＋MIT 授權（程式碼與權重皆可商用）＋權重發布當天即上架 Hugging Face＋1M 上下文，小團隊能以低成本自建部署、直接對照官方 API 表現。極度適合**預算有限但要跑長程 coding agent 的團隊**，以及**需要授權乾淨、可地端部署的企業**。
  * **資源**：[🤗 Hugging Face 權重](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017)（FP8 dense＋FP4 experts 量化配置；官方另提供 Rust 工具庫 deepseek-recipe 做 prompt 編碼） | 📄 技術報告《DeepSeek-V4.1-Flash: Pushing the Limits of KV Cache Compression》（模型卡引用格式，尚未見獨立 arXiv 頁）
  * **附註（未獨立查證）**：架構細節（Causal Encoder-Decoder 稀疏 MoE、552B backbone＋196B Engram 參數、input 激活 8B／output 激活 16B、FP4 主 KV cache 每 token 890 bytes 約前代四分之一、SWA Bounded Replay、API 價格 $0.15/M input）來自技術媒體報導轉述，官方模型卡未載明參數量與 KV bytes 數字；所有基準皆為官方自測、未經第三方獨立驗證。

* **[Beam 1.0 (Reflection)](https://huggingface.co/reflection/Beam-1.0-501B-A23B)** `[2026-10-16]` 🔥 `[開源權重]` `[MoE]` `[Coding Agent]` `[Apache 2.0]` `[1M上下文]`
  * **核心優勢**：**Reflection 釋出的第一個開放權重模型：501B 總參數、每 token 僅激活 23B 的稀疏 MoE，賣點是 frontier 級推理效率。** 架構：52 層（3 dense＋49 MoE）、256 experts、Gated GQA＋滑動窗口注意力、詞表 152k，上下文 1M tokens（純文字模型）；BF16／FP8／NVFP4 三種精度權重＋推測性解碼 drafter 模型，Day-0 原生支援 Transformers、vLLM、SGLang、Unsloth、Axolotl、NVIDIA Dynamo。客觀指標（官方模型卡自測，temp=0.7／top_p=0.99）：SWEBench Verified 81.6%、Terminal-Bench 2.1 80.1%、LiveCodeBench 88.3%、SWE Bench Pro v2-Hard 76.5%、AIME 2026 97.7%、GPQA Diamond 90.6%、HLE（tools 版）51.1%、MCP Atlas 80.8%、BrowseComp 76.8%。官方主打 token-efficient reasoning：達到領先開源模型同等解題品質只需約三分之一的推理 token。訓練側：RL 階段跑了約 13 億個沙盒環境，並把經驗上游成開源的 OpenEnv 環境標準。
  * **解決痛點 / 推薦場景**：**解決了「頂級 agentic coding 能力只能從閉源 API 或自訂授權權重取得」的痛點。** 舊方法：前沿 coding agent 能力鎖在閉源 API（成本失控、資料外流），或開源權重的自訂授權（例如 Meta 的 Muse Model License 要求產品標示出處、年營收 2000 萬美元以上的模型即服務另簽約）。甜點區：真・Apache 2.0 權重＋完整官方基準＋商用可用，且官方明示**不禁止蒸餾**（連拿模型輸出訓練別的模型都允許，業界罕見）、微調、量化、合併；附開源終端 agent harness（Mirror CLI：Python 前端＋Rust agent core，支援斷點續跑、多 agent 平行）。極度適合**自建 coding agent 與長程自動化系統的團隊**、**需要合法蒸餾或魔改權重的企業**，以及**需要地端／主權部署的研究機構**（Dell、HPE 合作機房內版本）。
  * **資源**：[🤗 Hugging Face 權重](https://huggingface.co/reflection/Beam-1.0-501B-A23B)（BF16／FP8／NVFP4＋speculative decoding drafter） | [📢 官方發布公告](https://reflection.ai/blog/beam-is-available) | [🛡️ Beam 安全技術報告](https://reflection.ai/beam-safety-report) | [📖 開發者文件](https://developers.reflection.ai)（含 Mirror CLI）
  * **附註（未獨立查證）**：二次來源提及的訓練規模（23.8 兆 tokens 預訓練、1 億次以上 RL rollouts、10.5K GB300 訓練 4 週）未見於官方公告頁與模型卡，條目採官方公告的「約 13 億沙盒」數字；技術報告（Technical Report）官方標示 coming，尚未釋出。

* **[Muse Spark Open (Meta Superintelligence Labs)](https://huggingface.co/meta-models/Muse-Spark-Open-816B-A42B)** `[2026-10-15]` 🔥 `[開源權重]` `[MoE]` `[原生多模態]` `[Coding Agent]` `[1M上下文]`
  * **核心優勢**：**Meta Superintelligence Labs 迄今釋出的最大開放模型：816B 總參數、每 token 僅激活 42B 的原生多模態 MoE。** 架構為 MoE Transformer＋1.8B 感知編碼器：256 experts 每 token top-8 路由、62 層、詞表 202,048；原生支援文字、圖像、影片、音訊輸入（文字輸出），推理時上下文達 1M tokens；獨家 Reasoning Effort 參數（low／medium／high／xhigh，預設 xhigh）控制思考深度。客觀指標（官方自測，對打同級開源權重）：Agentic 類 JobBench 61.8、MCP-Atlas 89.2 居榜首；多模態 ZeroBench 50.0、SimpleVQA 73.6、IntPhys2 68.3 拿第一；知識推理 HLE-Diamond 26.1 第一、GPQA Diamond 89.0；AA Intelligence Index 39 落後中國同級開源模型（GLM 5.3 45、Kimi K3 44、Qwen3.8-2.4T-A95B 40）；安全面 FORTRESS ARS 5.8、StrongREJECT v2 0.5 皆為表中最低（越低越好）。
  * **解決痛點 / 推薦場景**：**完美解決了「想自建頂級 coding／agentic 系統，卻被迫依賴閉源 API 或授權受限權重」的自主性痛點。** 舊方法：頂級 agentic 能力鎖在閉源 API（資料外流＋帳單失控）；開源權重則多半欠缺原生多模態與長程工具調用能力。甜點區：開放權重＋原生四模態輸入＋1M 上下文＋官方 agentic 基準驗證，BF16／NVFP4 雙精度釋出，SGLang、vLLM、TensorRT-LLM、llama.cpp 生態支援。極度適合**自建 coding agent 與長程自動化系統的團隊**、**需要本地部署頂級推理能力的研究機構**，以及**做合成資料生成與 LLM-as-a-judge 評測的開發者**。硬體門檻誠實揭露：NVFP4 需 700GB VRAM、BF16 需 2TB，官方稱兩台 M5 Ultra Mac Studio 可用 MLX 本地運行。
  * **資源**：[🤗 Hugging Face 模型卡](https://huggingface.co/meta-models/Muse-Spark-Open-816B-A42B)（BF16／NVFP4 權重，需登入接受授權） | [📄 官方評測技術報告](https://research.meta.ai) | [📖 開發者部署文件](https://dev.meta.ai) | [💬 模型問題回饋](mailto:museoss@meta.com)
  * **⚠️ 授權注意**：採 Meta 自訂 Muse Model License（非 OSI 開放授權）：產品／服務 UI 須標示 "Built with Muse Spark Open"；年營收逾 2000 萬美元的 Model-as-a-Service 需另與 Meta 簽約；未滿 18 歲不得使用。商用採用前請自行確認條款。
  * **附註（未獨立查證）**：媒體報導的部署數字（兩台 M5 Ultra Mac Studio、BF16 約 1.6TB／NVFP4 約 530GB）與官方模型卡（700GB／2TB VRAM）不一致，條目採官方數字；Helion kernel、TorchTitan 微調支援、AMD／Intel／Unsloth 更小格式等僅見媒體報導，未在官方模型卡親驗。

### 🆕 新模型快訊：端側 Agent 推理模型

* **[LFM2.5-24B-A2B (Liquid AI)](https://huggingface.co/LiquidAI/LFM2.5-24B-A2B)** `[2026-10-13]` 🔥 `[端側Agent]` `[MoE]` `[純推理模型]` `[工具調用]`
  * **核心優勢**：**24B 總參數、每 token 僅 2.45B 運算：專為端側 Agent 打造的純推理模型。** 架構沿 LFM2 路線：40 層（30 層雙門控短卷積＋10 層 GQA）、每 MoE 塊 64 experts、top-4 路由；上下文 32K→131K、詞表 65K→128K（非拉丁語系分詞更好）；預訓練拉到約 33T tokens。後訓練五階段是關鍵：SFT→教師專家化→非 Agent／Agent 兩輪多領域在線蒸餾→直接在 OpenClaw、Hermes Agent、Pi、OpenCode 裡做 Agentic RL，讓模型學會各 harness 的工具與互動模式。客觀指標：16 項基準對打 Qwen3.6-35B-A3B／Gemma-4-26B-A4B-it／Nemotron-3.5-Lightning，工具調用類拿下 5 項第一（AutomationBench 27.69 對次佳 8.72、LiveClaw 48.09 對 38.19、BFCLv4 65.01、ToolSandbox 80.71），三項指令遵循基準全拿第一；推理速度 M5 Max 達 184 tok/s、單張 B300 達 21K tok/s。
  * **解決痛點 / 推薦場景**：**完美解決了「想在本地跑 Agent，卻被迫把資料送上雲端 API」的隱私與成本痛點。** 舊方法：雲端大模型 API 又貴、資料又外流；本地小模型則不會用工具、推理慢到不能當 Agent 用。甜點區：純推理架構（每次回答必先顯式思考）、工具調用原生（Pythonic 函數調用格式）、端側極速（筆電等級硬體互動式調度）。極度適合**隱私敏感的本地自動化 Agent**（在 MacBook／工作站上全天跑 OpenClaw／Hermes）、**斷網或內網環境的智能助手**，以及**不想付雲端 token 帳單的個人開發者**。
  * **資源**：[🤗 Hugging Face 模型卡](https://huggingface.co/LiquidAI/LFM2.5-24B-A2B)（另有 Base 版／FP8／GGUF／ONNX／MLX-4bit 權重，DSpark 草稿模型即將推出） | [🌐 官方發布部落格](https://www.liquid.ai/blog/lfm2-5-24b-a2b) | [📄 LFM2 架構技術報告 (arXiv:2511.23404)](https://arxiv.org/abs/2511.23404) | [📖 本地 Agent 部署指南](https://docs.liquid.ai)
  * **⚠️ 授權注意**：open-weight 但採 Liquid 自訂 LFM 1.0 授權（HF 模型卡標示 license:other，非 OSI 開放授權），商用採用前請自行確認條款。

### 🧠 核心概念與必讀文章：看懂 AI Agent 與 Agentic AI

在開發智能代理之前，理解底層邏輯與安全邊界至關重要。以下文獻涵蓋了從概念釐清、工作流設計到資安防護的必備知識：

* **[Agentic AI 與 AI Agents 的概念差異解析](https://www.alphaxiv.org/abs/2505.10468)**
  * **必讀原因**：釐清業界最容易混淆的兩個名詞。探討「AI 代理 (AI Agents)」作為單一執行體，與「代理式人工智慧 (Agentic AI)」作為系統性架構的分類學、應用場景與未來挑戰。
* **[Agentic AI 的資安威脅與緩解策略 (OWASP 官方指南)](https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations/)**
  * **必讀原因**：AI 失控怎麼辦？國際資安權威 OWASP 針對代理式 AI 可能面臨的 Prompt Injection (提示詞注入) 與權限濫用，提供了系統性的防禦與緩解架構 (Mitigations)。
* **[AI 搜尋引擎的致命傷：引用來源問題 (Citation Problem)](https://www.cjr.org/tow_center/we-compared-eight-ai-search-engines-theyre-all-bad-at-citing-news.php)**
  * **必讀原因**：當 AI 代理負責搜尋與總結時，如何避免侵權與幻覺？本文評測了八大 AI 搜尋引擎，揭露其在新聞與來源引用上的缺陷，是開發檢索代理 (Search Agent) 的重要借鏡。
* **[VISTA: 給多模態 Agent 裝上可回看的無損視覺記憶](https://arxiv.org/abs/2610.02200)** `[2026-10]` 🔥 `[AI Agent]` `[視覺推理]` `[ARC-AGI-3]` `[無損視覺記憶]` `[多模態]`
  * **核心優勢**：**不改模型、只改 Harness：ARC-AGI-3 從 40.68 直達滿分 100.00。** MIT 何愷明團隊的三件套：視覺觀察（直接看渲染畫面而非文字網格）、無損視覺記憶（每一幀原始保存、獨立於模型上下文之外）、視覺檢查（模型自主決定回看哪一幀、放大哪個區域，另有 read_pixels 可讀像素 RGB 值）。Claude Opus 5.0 在 25 款公開遊戲全通關，行動數比首玩人類少 57.4%；GPT-5.6 Sol 也達 99.00。論文稱這是首個不靠程序合成、僅憑視覺輸入就達滿分的系統。
  * **解決痛點 / 推薦場景**：**一次性視覺編碼丟掉的細節，長程推理時要不回來。** 傳統 VLM 把圖編碼一次就丟掉原圖，上下文一滿早期觀察還會被壓縮或刪掉；VISTA 讓模型按需回看、按需放大，把「看什麼、何時回看」變成可推理的動作。消融實驗顯示無損記憶加視覺檢查是最大功臣（70.05 → 94.10）。同一套 Harness 幾乎零改動遷移到 GameWorld（成功率 63.3%，超越新手人類）、BabyVision（41.0% → 63.2%），開源模型 GLM-5.3 Flash 也從 1.89 拉到 66.93。適合**長程交互式視覺任務**、**具身智能**、**遊戲與 GUI Agent** 的 Harness 設計參考。
  * **資源**：[📄 論文](https://arxiv.org/abs/2610.02200) | [🐙 GitHub](https://github.com/joshhhhhan/VISTA)


---

### 🔄 Agent 工作流 (Workflow) 入門指南
AI Agent 的強大不在於單打獨鬥，而在於流程設計。以下精選教學幫助您從零建構多智能體系統：
* **基礎掃盲**：[萬字長文綜觀 Agent 發展史](https://zhuanlan.zhihu.com/p/29833831482) | [Agentic AI 的核心區別](https://zhuanlan.zhihu.com/p/705935464)
* **實戰架構**：[從單一 Agent 到複雜 Workflow 的演進](https://zhuanlan.zhihu.com/p/32491596217) | [什麼是 Agentic 工作流程？](https://zhuanlan.zhihu.com/p/32709535995)

---

### 💼 領域專用 Agent 實戰案例 (Finance & Coding)

* [CADDesigner](https://github.com/NiJingzhe/SimpleCADAPI) [2026] 🔥 [CAD建模] [AI智慧體] [ECIP範式] [計算機輔助設計]
  * **核心優勢**：**首創由 LLM 驅動的概念 CAD 設計智慧體與顯式上下文命令式範式 (ECIP)，透過一致性 API 設計、聲明式約束與智慧錯誤回饋機制，在概念 CAD 模型生成任務上超越代表性基線。**
  * **解決痛點**：傳統 LLM 生成 CAD 腳本常面臨微調成本高昂、API 狀態複雜容易產生幻覺，以及空間坐標計算與對象尋找困難的問題；改善方式是透過中間層智慧體範式，讓模型僅聲明設計意圖與功能標籤，由 SDK 自動處理幾何計算與自診斷修復，實現意圖驅動的參數化設計。

* [text-to-cad](https://github.com/earthtojake/text-to-cad) [2026-07-22] 🔥 [CAD建模] [Agent技能] [build123d] [硬體設計]
  * **核心優勢**：**首創面向 CAD、機器人與硬體設計的 Agent 技能集合，透過整合 LLM、build123d 與 OpenCascade 內核，實現自然語言一鍵生成工業級 STEP、STL 與 DXF 檔案，並具備 Python 源碼可見與 git diff 可追溯性。**
  * **解決痛點**：傳統 CAD 軟體需繁瑣手動點擊且學習曲線陡峭，而學術界 Text-to-CAD 模型往往停留在實驗室階段、缺乏工程工作流閉環；改善方式是將其封裝為 Codex 與 Claude Code 的本地 Agent 技能插件，由 LLM 生成可控的參數化原始碼，結合工業級幾何內核與本地預覽工具，實現從設計描述到製造輸出的無縫工程閉環。

* **[FinRobot (開源金融 AI 代理)](https://deepwiki.com/AI4Finance-Foundation/FinRobot)**
  * **應用場景**：專為金融分析打造的 Agent 框架，支援最新 Gemini 2.5 模型，能自動化執行財報分析、市場預測等量化任務。[👉 AlphaXiv 論文解析](https://www.alphaxiv.org/zh/overview/2405.14767)
* **[Jupyter-AI (程式碼編寫代理)](https://deepwiki.com/jupyterlab/jupyter-ai)**
  * **應用場景**：將生成式 AI 原生接入 Jupyter Notebook，支援 Gemini 2.5，能理解您的數據上下文並自動生成、除錯 Python 程式碼，是數據科學家的最強副駕。

---

### 🧩 2026 必備 AI Agent 開源框架與開發工具 (依據應用場景分類)

在 Agentic AI 時代，選擇正確的框架能讓開發事半功倍。以下依據「應用場景」精選目前 GitHub 上最活躍、最具生產力的 AI Agent 開源專案：

* **[Harness² (Google Research)](https://github.com/google-research/harness2)** `[2026-10]` 🔥 `[Agent自我優化]` `[Harness工程]` `[遞歸自我改進]` `[無需Grader]` `[Apache 2.0]`
  * **核心優勢**：**模型權重不動，效能照樣漲：把「調 harness」本身變成一條會學習的管線。** Harness 是包在模型外的整層配置：system prompt、工具、記憶、編排與護欄。Harness² 的任務級遞歸走對比式 Propose–Probe–Compose：editor 對八個可編輯元件（system prompt、guardrails、memory、tool guidance、subagents、skills、scripts、plugins）提出候選改法，probe 把候選實際在同一任務上跑一遍，composer 從執行行為的差異中挑出真改進、合成新 harness，全程不需要標準答案或外部評分器。第二層 harnessing 級遞歸把每個任務定稿的 harness 與站得住腳的 lessons 存進常駐的 improvement harness，成為下一個任務的編輯起點。遞歸預算用 --k 控制：parallel 同時探 K 個通用加 K 個領域候選，sequential 串行精煉 K 步；執行器預設 OpenCode，可換 Codex。
  * **解決痛點 / 推薦場景**：**生產環境的任務大多沒有標準答案，傳統獎勵訊號拿不到，harness 只能靠人肉試錯。** 論文（arXiv:2610.14224）與官方實測：GLM-5 與 Gemini 3.5 Flash、四種模型與 harness 配置、對照各自的原廠預設 harness，單步遞歸即全面提升：WorkBuddy-Bench 最高 +11.5 分、JobBench +4.5 分、法律 LAB 部分通過率 +11.8 個百分點，加大 --k 還能再漲。極度適合**企業 Agent 平台的 harness 自動調校**、**無 grader 場景的持續優化**、**研究「配置與權重何者決定 Agent 上限」**。⚠️ 官方 README 自己寫明：執行器網路存取不受限、Codex 沙箱預設關閉、公開 benchmark 的評分 rubric 在網路上可及，評測前須自行加網路限制，否則分數可能被「上網查答案」灌水；且 guardrails 本身就是可編輯元件之一，被污染的 memory 或 skill 等於改寫 Agent 的判斷邏輯，harness 檔案必須進版控並審計每次 diff；repo 亦聲明非 Google 官方支援產品、不在 Google 開源漏洞獎勵範圍。
  * **資源**：[🐙 GitHub](https://github.com/google-research/harness2) | [📄 論文 (arXiv:2610.14224)](https://arxiv.org/abs/2610.14224) | [🌐 專案頁](https://harness2.github.io)

#### 1. 個人全自動化助理與通用 Agent (Personal & General Assistants)

* **[nanoMuse](https://github.com/nano-muse/nanoMuse)** `[2026-09]` 🔥 `[個人智能體]` `[跨裝置協作]` `[開源Muse路線]` `[Goals+Routines]` `[Hands螢幕操作]`
  * **核心優勢**：**手機一句話，電腦接著做：開源個人智能體第一次把「多設備」做成一等公民。** 浙大三位作者發起的獨立社群專案（與 Meta 無關），致敬 Meta Muse 路線：手機 App、桌面端、瀏覽器與中繼全部開源（GPL-3.0）。手機上 `@Mac 編譯一下項目` 就能把任務丟給在線電腦，執行結果與審批卡片送回手機；對話預設跨設備同步（只同步主對話）；Goals＋Routines 做長期目標追蹤與定時任務，每天還生成 Feed。模型可換：社區中繼免費額度（每帳號 ¥10 用量）或自帶 20 家服務商 Key，中繼也可自托管。18 天破千星，最新 1.0.5。
  * **解決痛點 / 推薦場景**：**雲端 Agent 夠不著你自己的設備，單機 Agent 又走不出那台手機。** Meta Muse 跑在雲 VM，OpenMinis 只活在一台手機；nanoMuse 讓每台設備各跑一個 Agent，經中繼互相委託。沒有 API 的 App 就用 Hands 直接操作螢幕（Android／桌面可，iOS 系統不允許）；刪檔、發送、付款三級審批，密碼驗證碼一律交給用戶。極度適合**手機指揮電腦跑編譯與長任務**、**跨設備的個人自動化**、**想自托管整套個人智能體的人**。
  * **資源**：[🐙 GitHub](https://github.com/nano-muse/nanoMuse) | [📄 論文](https://arxiv.org/abs/2610.08699) | [🌐 官網](https://nanomuse.cn) | [📖 隱私說明](https://github.com/nano-muse/nanoMuse/blob/main/docs/privacy.md)
  * **⚠️ 隱私注意**：社區中繼 0.9 起新帳號預設開啟「幫助改進 AI 模型」（保留部分聊天文字與工具調用做訓練），與對話同步是兩個獨立開關，都可在設定裡關閉並刪除已保留數據。

* **[Meta Muse](https://ai.meta.com/)** `[2026-09-08]` 🔥 `[目標驅動個人Agent]` `[Muse Secure VM]` `[Sentinel安全守衛]` `[跨端硬體延展]` `[Agentic Commerce]`
  * **核心優勢**：**打破「對話框諮詢顧問＋人工手動執行」的舊範式，Meta 正式發布以獨立數位身份長程接管系統與商業交易的個人 AI Agent 系統！** 核心架構捨棄傳統輕量 API 函數掛載，為每個智能體在雲端分配獨立高隔離度的 **Muse Secure VM**（配備專屬檔案系統、無頭瀏覽器、Bash 終端與網路棧），並引入獨立安全監視體 **Sentinel** 對網路出站流量與高危調用進行即時硬體級攔截與注入防護。在交互端由「提示詞問答」躍遷至「宏觀目標驅動」，獲取授權後可直接穿透 macOS 底層檔案系統、Mail 客戶端、行事曆與備忘錄；並在 Meta Connect 大會上延伸至 Ray-Ban 智慧眼鏡與 Muse Charm 便攜硬體，建構全域無所不在的 Agent 交互層。此外，系統賦予 Agent 專屬電子郵件地址，串接 Walmart、Best Buy、Sephora 等零售通路並綁定 Shop Pay 與 PayPal 實現代客自動化結帳。
  * **解決痛點 / 推薦場景**：徹底解決傳統 LLM+RAG 模式「無狀態單次請求銷毀、僅依賴文字 Guardrail 無法抵禦多步越權攻擊」以及「使用者必須在十幾個視窗間手動切換比對與填單」的工程痛點。 展現了 Agent Runtime 在沙盒隔離、狀態持久化與多步回滾上的生產級架構。同時成為探討「使用者授權不等於平台准入（遭遇 Amazon.com 平台防火牆封鎖阻斷）」 以及「高權限客戶端 0-day 導致權限放大效應（Privilege Amplification）」的指標性案例。極度適合作為**個人全自動化數位管家與長程目標託管系統**、**跨桌面系統原生應用深度整合中樞**，以及**次世代環境式穿戴裝置（智慧眼鏡/便攜硬體）的統一代理層參考實現**。
  * **資源**：[🌐 Meta AI 官方平台](https://ai.meta.com/) | [📱 Meta Connect 產品發布](https://about.meta.com/) | [🛡️ Patrick Wardle 0-day 漏洞揭露研究](https://objective-see.org/)

* **[OpenMuse](https://github.com/CopilotKit/OpenMuse)** `[2026-09-22]` 🔥 `[Meta Muse開源平替]` `[自託管個人助理]` `[常開瀏覽器會話]` `[背景非同步任務]` `[寫操作人機確認]` `[MIT協議]`
  * **核心優勢**：**打破商業閉源 Agent 數據壟斷，CopilotKit 開源首個支援完全二次開發與自託管的個人 AI 助理系統！** 專案採 MIT 協議開源，iOS、Android 與 Web 三端共用單一程式碼庫。系統核心搭載三大生產級基建：**常開 Chromium 瀏覽器**（保留網站登入態無須反覆驗證，並內建「Take control」一鍵人工即時接管機制）、**持久化後台任務引擎**（任務在伺服器端維持進度與執行紀錄，即使關閉應用程式或伺服器重啟也能無痛斷點續傳，避免重複執行）、以及**隔離 Linux 容器終端**（指令上限 30 秒、終端本體不直連外網且全量記錄輸出）。整合 Gmail 與 Google 日曆，原生落實「寫操作強制人機確認」原則；並具備 PDF 表單智慧欄位解析、周期性去重網頁監控與 CSV 帳單支出分析等多任務處理能力。
  * **解決痛點 / 推薦場景**：**完美解決了 Meta Muse 等商業雲端 Agent「資料與控制權完全受制於大公司、無法客製化二次開發」，以及傳統對話機器人「關掉網頁任務即中斷、涉及發信改日曆等寫操作容易誤動作脫韁」的致命痛點。** 提供 Render 與 Railway 一鍵部署模板，大幅簡化自架伺服器門檻。極度適合**注重資料主權與隱私的技術團隊自託管專屬私人助理**、**開發者研究 Agent 中斷恢復與操作審批確認流架構**，以及作為**個人自動化網頁監控、信件檢索與文件處理的開源原型基底**。
  * **資源**：[🐙 GitHub 官方倉庫](https://github.com/CopilotKit/OpenMuse)

* **[OpenBot (CopilotKit)](https://github.com/CopilotKit/OpenBot)** `[2026-08]` 🔥 `[企業AI同事]` `[Agent治理]` `[審計]` `[AG-UI]` `[自建部署]`
  * **核心優勢**：**開源 AI 同事，但先回答安全評審的三個問題：數據去了哪、誰能看什麼、Agent 動過哪些手。** CopilotKit 出品（MIT），每個 Agent 配一台獨立電腦（獨立容器、獨立瀏覽器登錄態、獨立檔案），所有動作只走一個網關：先裁定、再記錄、最後才執行。預設帶通用助理加公司知識問答兩個同事（配置而非代碼），另有 10 個金融崗位角色範本。任意 AG-UI Agent（LangGraph、Mastra、CrewAI、Pydantic AI、Google ADK）都能接入成同事。跑在你自己的機房：Docker Compose 起步，生產用 Helm chart；官方明說這是模板不是產品，無託管版。
  * **解決痛點 / 推薦場景**：**Agent 進公司最大的阻力不是聰明不聰明，是出了事查不清。** OpenBot 把治理做進底座：策略按工具、意圖、發起人、頁面 URL、命令、檔案等欄位裁定，fail-closed（規則缺失或寫錯一律拒絕）；審計不留「發生了但沒記錄」的路徑；密钥加密保存且永不進日誌；撞上登錄牆可人工接管。它是 OpenMuse 的同門兄弟（個人版走手機 App），兩者共用 AG-UI 協議與 Intelligence 記憶底座，未來可能拼在一起：個人端在手機上跑，重活兒丟給公司這套有治理的機器。極度適合**要在內網落地的企業 Agent 專案**、**需要完整審計軌跡的金融與合規場景**。
  * **資源**：[🐙 GitHub](https://github.com/CopilotKit/OpenBot) | [🌐 官方頁](https://copilotkit.ai/openbot)
  * **⚠️ 落地成本**：對話持久化、記憶與自動學習技能來自獨立服務 CopilotKit Intelligence，不在 MIT 許可內；本地 Mac 有免費開發者計畫（30 天許可可續）。Alpha 階段，官方提醒預期粗糙與 bug。

* **[DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness)** `[2026-08-13]` 🔥 `[Agent作業系統]` `[一切皆插件]` `[Cordis內核]` `[受控執行流水線]` `[多提供方接入]`
  * **核心優勢**：**打破 Agent 應用產品思維，DeepSeek 釋出首個以「一切皆插件 (Everything is a Plugin)」為核心哲學的開源 Agent 基礎設施底座！** 其設計思想源自論文《A Programming Paradigm for Spatiotemporal Composability》，底層依托 Cordis 共享上下文，將模型適配器、工具註冊表、會話日誌、Agent 循環、檔案系統、沙箱、審批策略與 Web UI 全部插件化解耦。系統提供 `web` 與 `headless` 兩種 Profile，僅需 78 行配置即可定義完整運行時；前端憑證採只寫與脫敏引用架構（支援 DeepSeek、Anthropic、OpenAI 及自建 Gateway 多提供方接入），工具呼叫皆經過權限與審批流水線，並支援五級目錄掃描的任務專用指令（Skill）按需動態載入。
  * **解決痛點 / 推薦場景**：完美解決了傳統成品 Agent 工具「與特定模型/用戶端深度綁定、內部黑盒無法更換底層檔案系統與沙箱，以及全量載入提示詞導致 Token 冗餘浪費」的架構性痛點。 透過將模型視為可替換能力，賦予開發者自由替換模型、檔案系統與沙箱的極致可定製性。極度適合**自建企業內部私有化 Agent 基礎設施與作業系統級工作區**、**需跨模型（DeepSeek/Claude/GPT）無縫切換的進階開發者**，以及**打造受嚴格安全策略與權限審批控制的自動化任務工作流**。
  * **資源**：[🐙 GitHub 官方倉庫](https://github.com/deepseek-ai/deepseek-harness) | [📖 官方文件站](https://deepseek-harness.github.io/deepseek-harness/) | [📦 npm 套件 (@deepseek-ai/dsh)](https://www.npmjs.com/package/@deepseek-ai/dsh) | [🌐 官方產品頁](https://www.deepseek.com/harness/)

* **[Resource2Skill](https://github.com/microsoft/Resource2Skill)** `[2026-06]` 🔥 `[Skill工廠]` `[多模態經驗蒸餾]` `[分層Skill-Wiki]` `[動態缺口補全]` `[微軟開源]`
  * **核心優勢**：**打破 Agent 技能（Skill）依賴人工手寫的產能瓶頸，微軟聯手 UCSC 與上交大開源首個將多模態人類資源「煉」成可執行技能的自動化工廠！** 論文（arXiv:2606.29538）建立「發現資源 ➔ 經驗蒸餾 ➔ 組織成 Wiki ➔ 選擇組合 ➔ 執行補缺」五步標準流水線；透過 `yt-dlp`、`ffmpeg` 結合 Gemini 提取教學影片的時間序列操作、代碼模式與視覺關鍵幀，組織成結合結構化文字、代碼、視覺範例與來源追溯的分層多模態 Skill Wiki（Hierarchical Multimodal Skill Wiki）。主實驗橫跨 Web、Excel、PPT、Blender、CAD、UE5 與 Reaper 七大領域 28 個比較單元，平均任務成功率從 45.0% 提升至 56.8%（GPT-5.4 於 UE5 任務暴漲 38.2 個百分點，人類盲測偏好率達 85.5%）；更具備在線能力缺口自適應獲取機制，在新能力任務上帶來 21.6 個百分點的增益。
  * **解決痛點 / 推薦場景**：完美解決了企業與團隊在構建 Agent 時「人工編寫與維護 SKILL.md 成本高昂、散落在教學影片與代碼庫的隱性經驗無法直接復用」，以及「全量注入知識導致上下文爆炸與檢索噪聲干擾」的致命痛點。 實現將成熟操作經驗轉化為可檢索、組合與評測的可執行資產，並在執行時透過層級瀏覽縮小範圍以極致壓縮上下文。極度適合**需持續生產與維運多 Agent 技能庫的平台團隊**、**沉澱海量歷史教學影片與專案資產的企業組織**，以及**高度依賴複雜 GUI/工具鏈與程序性步驟的軟體工程團隊**。
  * **資源**：[🐙 GitHub 官方倉庫](https://github.com/microsoft/Resource2Skill) | [📄 arXiv 論文 (2606.29538)](https://arxiv.org/abs/2606.29538) | [🌐 官方專案頁](https://microsoft.github.io/Resource2Skill/) | [🤗 Hugging Face 資料集](https://huggingface.co/datasets/microsoft/RESOURCE2SKILL) | [🎬 官方專案影片](https://www.youtube.com/watch?v=03gtIwEZX7s)

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
* **[Microsoft Agensh（無中央編排、1,024 個 coding agent 自組織框架）](https://github.com/microsoft/Agensh)** `[2026-10-24]` 🔥 `[多智能體]` `[無編排]` `[Coding Agent]` `[MIT]` `[ProgramBench]` `[自組織]`
  * **核心優勢**：**把多智能體協調從「主管 agent」搬進基礎設施：沒有中央編排者，1,024 個 worker 照同一條五步迴圈自認領、自驗證、自合併，agent 數量本身成為新的擴展維度。** 每個 worker 非同步跑同一迴圈：蒐集上下文、認領子任務（發 CLAIM、重疊用私訊協調）、動手並及早分享發現、按驗收標準驗證、合併進共享 repo 再重複；迴圈寫在提示詞裡而非執行期程式碼，每個 worker 除 ID 外拿同一份提示。支撐三件套：Gitea 共享工作區（分支、PR、合併衝突）、Mattermost 團隊頻道＋私訊、源自 DeLM 的共享情境板（OBSERVED、FACT、FAIL、CLAIM、PATCH_SUMMARY 五類筆記）。底層接單 agent 框架，實驗用 GitHub Copilot CLI（ACP 會話），論文稱可用輕量轉接器接 Claude Code 等框架。預設單節點 Docker Compose 跑 8 個 worker，6 小時一任務；1,024 agent 實驗為 16 節點 × 64 agent，每 worker 上限輸入 272,000 token、輸出 128,000 token、記憶體 64 GiB。MIT 授權。
  * **解決痛點 / 推薦場景**：**解決了「主管 agent 成為多智能體瓶頸：規劃、派工、合併全卡在一個人身上，agent 一多就塞車」的痛點。** 舊方法：Claude Code agent teams、Codex 子 agent、Copilot fleet、Kimi Agent Swarm 皆由主管拆解派工，規模一拉大協調成本先爆。甜點區：ProgramBench 最難 5 題（FFmpeg、gromacs、pandoc、PHP-src、ctags，離線從行為重建程式、6 小時預算），GPT-5.6-sol 高推理 effort 下 5 題平均測試通過率從 1 agent 的 19.31% 升到 128 agent 的 28.78%（相對提升約 49%）；pandoc 單題從 33.89%（1 agent）升到 55.06%（1,024 agent），且 128 agent 在 30 分鐘就通過 30%，32 agent 需 60 分鐘、8 agent 需 90 分鐘。極度適合**有硬性時限、任務夠大值得上百 agent 分工的重建／重構任務**，以及**研究「agent 數量擴展律」的團隊**（實驗還觀察到未寫死的自發分工：8 agent 自行協調介面、32 agent 同儕審查、128 agent 固定整合流程、1,024 agent 出現整合者角色並接手失敗任務）。小任務別硬上：1 agent 到 8 agent 平均只加 1.37 點，划不來。
  * **資源**：[🐙 GitHub 官方倉庫（MIT）](https://github.com/microsoft/Agensh) | [🌐 官方專案頁](https://agens-harness.github.io/project/) | [📄 arXiv 論文 (2609.26781)](https://arxiv.org/abs/2609.26781)
  * **附註（未獨立查證）**：論文發表於 9 月 22 日，程式碼首版發布於 10 月 24 日（Microsoft Research 作者 Furu Wei 當日 LinkedIn 公告），昨日簡報漏收、本日補登，日期如實標示為 2026-10-24，不偽稱 10 月 25 日發布；MarkTechPost 報導刊於 10 月 24 日（UTC 時間戳為 10 月 25 日凌晨，屬昨日簡報開工後才上線，故漏收）。GPT-6.1-sol 的 pandoc 數字（1 agent 56.19% → 32 agent 79.59%）只出現在 README，不在論文 v1 版內，引用時要分開標示。Token 成本未公布；實跑另需模型 API token 與 ProgramBench v1.2.5，Linux＋Docker Engine＋Compose v2＋systemd＋cgroup v2＋Python 3.11 以上。

* **[DeerFlow 2.0 (字節跳動)](https://github.com/bytedance/deer-flow/blob/main/README_zh.md)** `[2026-03-26]`：從 Deep Research 升級的 Super Agent Harness，將 sub-agents、memory 和 sandbox 有機組織，能處理極度複雜任務。
* **[Agno](https://zread.ai/agno-agi/agno/)** `[2025-11]`：專注於高效能的多智能體 (Multi-agent) 系統框架。
* **[Microsoft Agent Framework](https://github.com/microsoft/agent-framework)** `[2025-08-29]`：微軟官方開發套件，專為 .NET 和 Python 開發者設計的企業級工作流。
* **[Agent-Squad (AWS Labs)](https://deepwiki.com/awslabs/agent-squad)** `[2025-05-18]`：輕量級的開源多智能體框架。
* **[FlowGram (字節跳動)](https://github.com/bytedance/flowgram.ai)** `[2025-05-10]`：開源版的 Coze 核心視覺化工作流引擎。
* **[Agent Development Kit (ADK)](https://github.com/google/adk-python)** `[2025-04-03]`：Google 官方釋出的智能體開發工具包。

---

#### 3. 深度研究與開源知識庫 (Deep Research & RAG)

* **[DeepTutor](https://github.com/HKUDS/DeepTutor)** `[2026-04]` 🔥 `[Agent原生工作區]` `[終身個性化學習]` `[三層可審計記憶]` `[多引擎RAG]`
  * **核心優勢**：**打破多工具切換的學習孤島，港大 HKUDS 團隊開源首個將 Chat、Quiz、Research 等六大模式裝進單一運行的 Agent 原生終身學習工作區！** 論文（arXiv:2604.26962）提出結合引用基礎問題輔導與難度校準問題生成的統一框架，並建立 TutorBench 基準。在混合個性化引擎驅動下，平均提升個性化指標 10.8%，加強基礎模型代理推理能力 29.4%。系統搭載可審計的三層記憶架構（L1 Trace / L2 Surface Summary / L3 Synthesis 及 Memory Graph 證據溯源），同時整合 LlamaIndex、PageIndex、GraphRAG 與 LightRAG 等多檢索引擎，支援隨時召喚 CLI 子 Agent（Claude Code/Gemini/Codex 等）與 EduHub 技能擴展。
  * **解決痛點 / 推薦場景**：**完美解決了自學者與研究人員在 ChatGPT、Notion、刷題 App 與學術搜尋間來回切換導致「學習進度碎片化、上下文斷裂且工具缺乏長期記憶」的致命痛點。** 讓學習從「切換工具」升級為「同一個 AI 內切換模式（Chat / Quiz / Research / Visualize / Solve / Mastery Path）」，並支援直連 Obsidian Vault。極度適合**系統化學習新領域的自學者**、**需自動化文獻調研與論文協作 (Co-Writer) 的研究生/學者**，以及**打造自適應學習路徑的教育者與開發者**。
  * **資源**：[🐙 GitHub 官方開源](https://github.com/HKUDS/DeepTutor) | [📄 arXiv 論文 (2604.26962)](https://arxiv.org/abs/2604.26962) | [🌐 官方網站](https://deeptutor.info) | [📖 官方文檔](https://docs.deeptutor.info)

* **[Scholar Loop](https://github.com/renee-jia/scholar-loop)** `[2026-06-15]` 🔥 `[自主科研閉環]` `[8專職Agent小隊]` `[防獎勵黑客]` `[單GPU預算]` `[隨時間衰減技能庫]`
  * **核心優勢**：**打破傳統 AI 只會「讀論文復讀」的局限，首創將博士研究員「讀文獻➔提假設➔跑實驗➔反思➔寫論文」完整循環工程化的自主科研架構！** 系統將科研流程拆解為 Director、Lit Scout、Reasoner、Debate Panel、Funnel、Runner、Reflector、Advisor 及 Writer+Reviewer 等 8 個專職智能體，透過 typed JSON-schema 與共享稽核軌跡（audit trace）協作。底層由平行人口漏斗（Parallel Population Funnel）、自動停止治理器（Self-stopping Governor）、預測-驗證校準（CalibrationLog）與相關性排序情境注入（SkillLibrary）四大確定性支柱支撐。更首創兩階段凍結評分、編輯允許列表、VerifiedRegistry 數字可溯源機制及對抗性作弊引擎（Cheater Engine），在代碼層面徹底杜絕 AI 相互打勾與獎勵黑客（Reward Hacking）作弊問題。
  * **解決痛點 / 推薦場景**：完美解決了現有 AI 科研助手「僅能單次摘要、缺乏假設驗證與反思閉環」、以及讓 AI 評判 AI 導致「幻覺數據與指標作弊層出不窮」的致命痛點。 內建預算感知的「三層篩選漏斗（Smoke ➔ Verify ➔ Full Run）」讓壞想法在低成本推理階段即被淘汰，並搭配隨時間衰減的技能庫避免過度固守歷史偏見。原生支援真實 PyTorch 運行、提供 108 個單元測試與免 GPU/API Key 的 MockLLM 快速驗證環境。極度適合**算力預算受限但需持續探索新假設的科研團隊與實驗室**、**演算法工程師進行自動化 Baseline 驗證與消融實驗**，以及**打造具備嚴格確定性紀律的次世代 AI 科研 Agent 管線**。
  * **資源**：[🐙 GitHub 官方開源](https://github.com/renee-jia/scholar-loop)

* **[autoarxiv](https://autoarxiv.org)** `[2026-06]` 🔥 `[一鍵論文復現]` `[autoresearch]` `[最小化實驗]` `[環境自動修復]` `[算力成本預估]`
  * **核心優勢**：**打破「讀論文容易、跑論文崩潰」的落地高牆，alphaXiv 首創「改一個 URL」即可全自動修復環境並完成單卡最小化復現的 Agent 服務！** 奠基於 Paper2Agent 框架（arXiv:2509.06917），只需將 arXiv 網址中的 `arxiv` 替換為 `autoarxiv`，系統即可自動定位 GitHub 開源代碼庫。AI 智能體能自主閱讀 `README.md` 並分析實驗依賴，將原本需 4 張 H100 等龐大硬體條件自主壓縮為單卡可執行的「最小化復現」方案（包含模型降級、限制訓練步數為 40 步、開啟 LoRA、自動編寫啟動腳本 `run.sh` 與評估摘要 `summarize_eval.py`）。系統即時同步損失曲線與指標面板，驗證初始 Claim 並精準估算完整復現所需的算力與時間成本，更支援用戶接入自有算力基礎設施與自定義 Agent。
  * **解決痛點 / 推薦場景**：完美解決了機器學習領域中「依賴版本漂移、路徑硬編碼、多卡硬體假設與隱性預處理，導致大量研究代碼在 Setup 階段即報錯死亡、無人能驗證數值」的骨灰級痛點。 實測可將手動排查環境與復現實驗的數小時工作量壓縮至十餘分鐘。極度適合**需快速評估論文代碼真實可用性的科研人員與演算法工程師**、**進行 Baseline 快速初篩與復核的學術團隊**，以及**預先進行 GPU 算力預算評估的企業研發實驗室**。
  * **資源**：[🌐 autoarxiv 服務入口](https://autoarxiv.org) | [🤖 alphaXiv 官方助手](https://www.alphaxiv.org/assistant) | [📄 Paper2Agent 論文 (arXiv:2509.06917)](https://arxiv.org/abs/2509.06917) | [📝 官方發布公告](https://x.com/askalphaxiv/status/2067593673072877833)

* **[Polaris](https://github.com/ZJU-REAL/Polaris)** `[2026-06]` 🔥 `[全流水線AI科研]` `[Voyage可恢復架構]` `[Human-Gated]` `[ResearchWiki]` `[Elo辯論評審]`
  * **核心優勢**：**打破問答工具的零碎輔助，浙江大學 ZJU-REAL Lab 開源首個將「文獻調研➔想法生成➔想法評審➔實驗執行➔論文寫作➔論文評審」六階段串聯的端到端科研流水線！** 架構將重活交由確定性代碼（PyMuPDF/pgvector），LLM 僅負責判斷與評審；首創 **Voyage（航程）** 長任務機制，由 Navigator 規劃、Helm 執行與 Sextant 自驗證三循環驅動，支援 Worker 崩潰斷點續傳與預算熔斷。系統整合四大核心模組：**Research Wiki**（每日增量讀取 arXiv、概念網狀鏈接並支援一鍵導出 Obsidian）、**Idea Forge**（多信號差距分析與四維評分）、**Elo Debate**（多 AI 評審員正反辯論錦標賽排序）與 **Experiment Lab**（Fernet 加密 SSH 連接遠端 GPU 自動規劃除錯，GSM8K 實測節省約 68% 上下文 Token）。後端寫作強制對賬真實實驗指標，並在評審端逐條校驗引文存在性，偽造引用直接打回。
  * **解決痛點 / 推薦場景**：**完美解決了科研人員在「文獻讀不完、實驗調參反覆、論文修改繁瑣」且現有 AI 科研助手「缺乏長流程推進能力、互相打勾造假、崩潰無法恢復」的致命痛點。** 嚴格遵循「流程交接處設置 Human-Gated 人閘」機制，從想法晉級、動用 GPU 預算到確認投稿，關鍵決定權始終留在研究者手中。支援團隊多租戶文獻共享與用量透明管控，並透過 MCP 協議對外暴露文獻與實驗資產。極度適合**高校與科研機構課題組打造可審計、自動化的 AI-for-Science 科研實驗室**、**演算法工程師進行自動化 Baseline 復現與消融實驗**，以及**需高可靠文獻追蹤與論文寫作審核的科研團隊**。
  * **資源**：[🐙 GitHub 官方開源](https://github.com/ZJU-REAL/Polaris) | [📖 產品與文檔站](https://zju-real.github.io/Polaris/) | [🌐 在線體驗 (訪客模式)](http://101.37.174.109:8080)

* [Arbor](https://ruc-nlpir.github.io/Arbor/)] [2026-06-11] 🔥 [自主科研] [Agent框架] [Hypothesis-Tree] [Autonomous Optimization]
  * **核心優勢**：**首創基於假設樹精煉 (HTR) 與洞察回傳的自主科研架構，在六個真實自主優化 (AO) 任務上取得超過基線 2.5 倍的相對增益，並在 MLE-Bench Lite 上以 GPT-5.5 創下 86.36% Any Medal 的 SOTA 成績。**
  * **解決痛點**：傳統 LLM Agent 隨著任務變長容易退化為線性的局部盲目試錯，缺乏結構化的研究狀態與經驗沉澱；改善方式是透過長期 Coordinator 與短期 Executor 分離架構、外化 Hypothesis Tree，並將實驗洞察沿樹狀結構反向回傳與使用 held-out 驗證閘門，實現知識的結構化積累、長期規劃與防止過擬合。

* **[[OpenWorker]](https://github.com/andrewyng/openworker)** `[2026-07-23]` 🔥 `[開源智能體桌面應用]` `[本地優先]` `[模型隨你挑]` `[無人值守]`
  * **核心優勢**：**由吳恩達 (Andrew Ng) 與 Rohit Prasad 聯手打造的桌面級 AI 同事開源神作，喊出「交給你的是成品，而不是待辦清單」！** 徹底打破傳統智能體只能在對話框流連的侷限，將研究端的抽象能力（規劃、工具調用）翻譯成桌面上一個具備分層風險模型、無人值守 inbox、self-wake 喚醒機製與 25+ 連接器的可信賴同事。支援跨檔案、終端與主流企業應用的端到端自動化執行，並原生對接 aisuite 基礎庫與 Claude Desktop/Cursor 的 MCP 生態。
  * **解決痛點 / 推薦場景**：**完美解決了使用者「敢不敢讓 AI 自作主張在電腦上跑」的信任危機，並免除被單一閉源模型綁定的遷移成本。** 透過四級風險防護、運行模式約束與任務級常駐規則，將失敗的爆炸半徑壓到最低；同時藉由 ProviderRouter 支援 30+ 企業級模型與 Ollama 本地部署，實現零摩擦的模型切換。是打造**桌面級個人助理**、**自動化文件交付**與**長時程知識工作無人化代理**的工業級參考實現。
  * **資源**：[🐙 GitHub 專案](https://github.com/andrewyng/openworker) | [🌐 官方網站](https://openworker.com) | [📦 基礎庫 aisuite](https://github.com/andrewyng/aisuite)

* **[AnySearch (AI Agent 專屬跨域搜尋基礎設施)](http://www.anysearch.com)** `[2026-05]` 🔥
  * **核心優勢**：**打破大模型「表層網路」的資訊盲區，專為 AI Agent 打造的真實世界搜尋基礎設施！** 徹底拋棄傳統面向人類的網頁搜尋引擎 (SERP)。AnySearch 透過統一的 API、MCP Server 或 Agent Skill 介面，讓 AI 能直接穿透「深網 (Deep Web)」。它內建強大的智慧意圖路由 (Intent Classifier)，精準跨域抓取 GitHub 生產級程式碼、即時金融數據、法院裁決書與威脅情報等異質資料；並透過 RRF 融合與多維品質重排序過濾雜訊，直接回傳高資訊密度的結構化 Markdown，實測可大幅省下 60~70% 的 Token 消耗。
  * **解決痛點 / 推薦場景**：**完美解決了傳統 RAG 與 AI 搜尋「充斥 SEO 垃圾農場、無法穿透專業資料庫」，以及「多源 API 串接維護成本過高與 Token 嚴重浪費」的致命痛點。** 具備零保留 (Zero Retention) 隱私保護架構，查詢即焚、不留痕跡。極度適合**企業開發者**與**資安/金融分析團隊**打造**高可靠性的 Deep Research Agent (深度調研智能體)**、**跨域威脅情報 (IOC) 分析大腦**，以及**自動化競品與法務盡職調查副駕**。
  * **資源**：[🌐 官方網站](http://www.anysearch.com) | [🐙 GitHub 官方組織](https://github.com/anysearch-ai) 
  <br>`[Agent基礎設施]` `[DeepResearch]` `[MCP原生支援]` `[穿透深網]`

* **[LLM Wiki (自主學習的個人知識庫)](https://github.com/nashsu/llm_wiki)** `[持續更新]` 🔥
  * **核心優勢**：**將 Andrej Karpathy 的 AI 知識庫理念完美落地的神作！從被動 RAG 檢索進化為具備「深度研究 (Deep Research)」與「視覺化知識圖譜」的自主學習大腦。** 徹底顛覆傳統 RAG 每次查詢都要重新檢索比對的低效模式。透過獨創的「兩步鏈式思考錄入（先分析後生成）」機制，大語言模型會先完整「吃透」您的文件，再自動提煉並建構出具備交叉引用的 Wiki 頁面與動態知識圖譜。內建 SHA256 增量快取與持久化佇列，確保海量文件處理不中斷，且檔案結構完全相容於 Obsidian。
  * **解決痛點 / 推薦場景**：**完美解決了傳統 RAG 系統「跨文件推理能力極差」、「無法察覺知識盲區」的致命痛點。** 最強大的殺手鐧在於其「知識缺口洞察」功能，能透過圖譜演算法找出孤立頁面，並自動觸發 **Deep Research (深度研究)** 機制，自主呼叫網路搜尋引擎 (如 Tavily API) 抓取資料來補全知識庫。極度適合研究人員、學術界與重度知識工作者用來打造**專屬的第二大腦 (Second Brain)**、**企業級私有化本地知識庫**，或是進行長篇文獻的深度整理與洞察。
  * **資源**：[🐙 GitHub 官方開源](https://github.com/nashsu/llm_wiki) | [📦 軟體安裝包下載 (v0.3.13)](https://github.com/nashsu/llm_wiki/releases/tag/v0.3.13)
  `[第二大腦]` `[Deep Research]` `[視覺化知識圖譜]` `[Obsidian相容]`

* **[Academic-Search (科研智能體專屬文獻檢索技能)](https://github.com/ustc-ai4science/academic-search)** `[2026-05]` 🔥
  * **核心優勢**：**打破大模型學術檢索的資訊孤島，專為 AI Agent 打造的跨平台文獻調研「外掛技能 (Skill)」！** 由中科大 (USTC) 認知智能全國重點實驗室開源。它將文獻檢索從粗糙的「網頁爬蟲」升級為結構化的智慧工作流，一鍵整合 arXiv、Google Scholar、Semantic Scholar 等七大主流學術平台。內建「查詢自動擴展」與貼近人類閱讀節奏的「兩遍精讀策略」，能自動過濾冗餘並優先呈現 SOTA 論文，直接輸出完美適配 LLM 閱讀的 JSON/Markdown 格式（含 BibTeX 與開源程式碼連結）。
  * **解決痛點 / 推薦場景**：**完美解決了傳統 RAG 系統在進行學術調研時，因檢索源單一、關鍵字過窄導致「文獻漏檢」，以及「大模型難以解析非結構化網頁」的致命痛點。** 採用標準化封裝，原生支援無縫接入 AutoGPT、LangChain 等 Agentic AI 框架。極度適合學術機構與企業研發團隊打造**全自動文獻綜述大腦 (Deep Research Agent)**、**前沿技術熱點追蹤系統**，以及**論文 Baseline 自動對比與彙整副駕**。
  * **資源**：[🐙 GitHub 官方開源](https://github.com/ustc-ai4science/academic-search)
  `[科研 Agent]` `[DeepResearch]` `[跨平台檢索]` `[Agent Skill]`

* **[DeepXiv (科研 Agent 的文獻基建)](https://github.com/DeepXiv/deepxiv_sdk)** `[2026-05]` 🔥
  * **核心優勢**：**終結 AI 硬啃 PDF 的低效窘境，將 2 億篇科技文獻轉化為 Agent「隨插即用」的結構化數據基建！** 智源研究院 (BAAI) 領銜開源，徹底顛覆依賴 GUI 搜尋引擎與 PDF 爬蟲的傳統流程。首創「分層數據消費」機制，Agent 可透過 `--brief` (摘要速覽)、`--head` (章節概覽) 到 `--section` (章節精讀)，像人類學者一樣將運算資源 (Tokens) 集中在關鍵實驗數據上，並直接輸出原生 JSON 或 Markdown 格式。
  * **解決痛點 / 推薦場景**：**完美解決了傳統 RAG 系統「強行塞入整份 PDF 導致上下文溢出、幻覺嚴重與算力浪費」的致命痛點。** 內建專屬搜索引擎與深度調研 Agent，更原生支援 CLI、Python SDK 與 MCP 協議。極度適合學術機構與企業研發團隊打造**全自動深度調研大腦 (Deep Research Agent)**、**Baseline 對比數據自動彙整副駕**，以及**前沿技術熱點追蹤流水線**。
  * **資源**：[🐙 GitHub 官方開源](https://github.com/DeepXiv/deepxiv_sdk) | [📄 官方技術報告](https://arxiv.org/abs/2603.00084) | [🌐 API 開發文檔](https://data.rag.ac.cn/api/docs)
  `[科研 Agent]` `[DeepResearch]` `[MCP支援]` `[文獻解析自動化]`

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

* **[DeepCode](https://github.com/HKUDS/DeepCode)** `[2026-08]` 🔥 `[Paper2Code]` `[Agentic Coding]` `[V2中央廚房]` `[Text2Web/Text2Backend]`
  * **核心優勢**：**打破「任務流水線」壁壘，港大 HKUDS 團隊升級開源首個打通「論文到生產」的 Agentic Coding 中央廚房！** 專注於結構化文檔適配與「資訊過載 vs. 上下文瓶頸」的信道優化問題，提出 Blueprint 藍圖蒸餾、CodeMem 狀態化代碼記憶、CodeRAG 與 Verification 閉環糾錯四維架構。在 PaperBench 評測上，科研編碼（73.5%）超越 PaperCoder（51.1%），商用 Agent 子集達 84.8%（超越同底座 Cursor/Claude Code 58.7%）。v1.3.0 V2 架構全面統一 Agent 內核與事件協議，支援 CLI/Web/Headless 模式、企業級權限沙箱、專案記憶及多代理並行協作。
  * **解決痛點 / 推薦場景**：完美解決了開發者在「閱讀複雜論文、寫網頁前端、寫後端服務」時，因各工具管線獨立導致上下文斷裂、以及論文動輒幾十頁造成 LLM 信道飽和「細節錯、接口斷、跑不通」的致命痛點。 實測僅需 15 分鐘即可將 arXiv 論文演算法還原為含測試的可執行 Python 套件，5 分鐘生成能跑的 React + Tailwind 前端後台。極度適合**需將學術論文快速轉化為生產級代碼的研究人員與演算法工程師**、**全端自動化開發團隊**，以及**打造全場景 AI 編程環境的開發者**。
  * **資源**：[🐙 GitHub 官方倉庫](https://github.com/HKUDS/DeepCode) | [📄 arXiv 論文 (2512.07921)](https://arxiv.org/abs/2512.07921) | [📦 v1.3.0 Release Notes](https://community.qtorque.io/HKUDS/DeepCode/releases)

* **[deepagents](https://github.com/langchain-ai/deepagents)** `[2026-04]` 🔥 `[ClaudeCode開源版]` `[AgentHarness]` `[LangGraph上層封裝]` `[免模型綁定]`
  * **核心優勢**：**打破 Claude Code 封閉綁定與模型鎖定，LangChain 團隊打造首個開箱即用的「Batteries-included Agent Harness」開放框架！** 建立於 LangGraph 之上，將規劃（Planning/`write_todos`）、子代理隔離（Sub-agents/`task`）、檔案系統抽象（Filesystem）、上下文管理、持久化記憶、MCP 接入、人機協作（HITL）、Shell 與技能載入（Skills）等九大能力完全封裝進單一 `create_deep_agent()` 函式中。官方實證僅透過系統提示、工具與 middleware 調優的 Harness 工程（固定 `gpt-5.2-codex` 模型），便讓 CLI 在 Terminal Bench 2.0 基準從 52.8% 提升至 66.5%（排名衝入 Top 5）。支援 Python 與 JS/TS 雙端，並自帶終端程式設計子專案 `dcode`，可無縫介接 GPT-5.5、Claude Sonnet 4.5、Qwen3-Coder 或本地 Ollama。
  * **解決痛點 / 推薦場景**：**完美解決了開發者想使用類似 Claude Code/Cursor 的全自動終端編程與多代理協作體驗，卻受限於閉源 SaaS 綁定 Claude 模型、無法自訂 Middleware/日誌/沙箱、以及從頭手寫 LangGraph 複雜狀態機耗時費力的致命痛點。** 實測僅需 5 行代碼即可啟動自主規劃、調工具、讀寫檔案與摘要反饋的閉環 Agent，比從頭搭建節省 80% 工作量。極度適合**已在使用 LangGraph 的團隊進行零成本升級**、**自研企業內部私有化 Coding Agent 的工程師**，以及**評估開源替代方案以符合資安合規的技術決策者**。
  * **資源**：[🐙 GitHub 官方倉庫](https://github.com/langchain-ai/deepagents) | [📦 Python 官方文檔](https://docs.langchain.com/oss/python/deepagents/overview) | [💻 Deep Agents Code 文檔](https://docs.langchain.com/oss/javascript/deepagents/code/overview) | [📝 Harness 工程方法論](https://langchain.com/blog/improving-deep-agents-with-harness-engineering)

* **[NVIDIA NeMo Switchyard](https://github.com/NVIDIA-NeMo/Switchyard)** `[2026-03]` 🔥 `[LLM智慧路由層]` `[Rust高效代理]` `[多協議翻譯]` `[CodingAgent解耦]` `[成本驟降74%]`
  * **核心優勢**：**打破編碼代理對單一閉源模型的深度綁定，NVIDIA NeMo 團隊開源首個 Rust 打造的「鐵路編組站」式 LLM 智慧路由調度層！** 論文（arXiv:2603.20895）提出學習式 Prefill 路由器（Learned Prefill Router），結合 Provider 無關的中性類型與三層抽象（LLM Client / Target / Route），實現 OpenAI Chat、Anthropic Messages 與 OpenAI Responses 三大協議雙向互轉。內建 Random、LLM Classifier、Stage Router（階段路由，依工具 activity 判斷能力級別）與 Escalation Router 四種路由演算法，提供獨立 HTTP 代理（`switchyard-server`）與嵌入式庫（`switchyard-libsy`）雙形態。實測在 LangChain 145 個多輪 Agent 任務中，於 Nemotron 3.5 Lightning 與 Claude Opus 間動態升級，**成本暴力降低 74%**（僅 7% 呼叫打到旗艦模型）；在 Cognition Devin 基準測試中，於 Opus 與 Kimi 間動態分流，準確率維持 2.8% 誤差內且**成本降低 28%**。
  * **解決痛點 / 推薦場景**：完美解決了 Claude Code、Codex、OpenClaw 等編碼代理「因 API 方言不通被迫綁定閉源高價模型」、「每一步工具呼叫/探索都打到旗艦模型導致速度慢且 Token 成本爆炸」，以及「企業敏感程式碼/IP/主機名容易洩漏出境」的三大落地痛點。 讓 Agent 在本地「說母語 API」，底層卻能無縫將流量路由至本地 vLLM、NVIDIA NIM 或 Ollama。極度適合**自建企業內部私有化 Coding Agent 的基礎設施工程師**、**需大幅壓低多步驟 Agent 工作流 Token 成本的技術團隊**，以及**進行多模型 A/B 測試與效能成本權衡的 AI 系統架構師**。
  * **資源**：[🐙 GitHub 官方倉庫](https://github.com/NVIDIA-NeMo/Switchyard) | [📄 arXiv 論文 (2603.20895)](https://arxiv.org/abs/2603.20895) | [📝 NVIDIA 官方技術部落格](https://developer.nvidia.com/blog/route-ai-agent-workloads-across-models-with-nvidia-nemo-switchyard) | [📖 NeMo Relay 整合文檔](https://docs.nvidia.com/nemo/relay/dev/configure-plugins/switchyard/about)

* **[[google-colab-cli]](https://github.com/googlecolab/google-colab-cli)** `[2026-06-05]` 🔥
  * **核心優勢**：**Google 官方重磅發布！將 Colab 雲端算力原生注入本地終端機與 AI Agent 核心工作流的破局神作！** 徹底擺脫瀏覽器 GUI 的笨重束縛，透過極簡的 CLI 命令，即可直接調度遠端 T4/L4/H100 GPU 與新一代 TPU 算力資源。其最驚豔的 **Shebang 魔法寫法 (`#!/usr/bin/env -S colab run --gpu L4`)**，能讓任何普通的本地 Python 腳本瞬間退化為「自帶 L4 GPU 的可執行檔」，實現本地撰寫、遠端核心（Kernel）狀態持久化執行的絲滑體驗。
  * **解決痛點 / 推薦場景**：**完美解決了傳統網頁版 Colab「網頁重新整理狀態全毀」、「CI/CD 自動化難以非互動式租借 GPU」，以及「Claude Code/Gemini CLI 等終端 AI Agent 無法跨越 GUI 點擊連接 runtime」的致命痛點。** 內建背景 keep-alive 守護行程，且異常退出碼（Exit Code）與標準輸出（stdout）皆能完美對齊。是 **Mac 本地缺乏獨顯的 ML 實驗工程師**、**需要自動化進行 QLoRA 微調的技術團隊**，以及**打造全自動化終端 Agentic 運作管線**的工業級必備基建。*(⚠️ 註：目前僅原生支援 Linux 與 macOS，不支援 Windows。)*
  * **資源**：[🐙 GitHub](https://github.com/googlecolab/google-colab-cli) | [📝 官方發佈公告](https://developers.googleblog.com/2026/06/introducing-the-google-colab-cli.html) | [📦 PyPI 套件頁](https://pypi.org/project/google-colab-cli/) | [📊 微調範例資料集](https://huggingface.co/datasets/philschmid/gretel-synthetic-text-to-sql) | [🤖 Gemma 3-1B 模型基座](https://huggingface.co/google/gemma-3-1b-it)

* **[Hugging Face ml-intern](https://github.com/huggingface/ml-intern)** `[2026-04]` 🔥
  * **核心優勢**：**重新定義「AI 幫我做研究」！能自主讀論文、找資料、寫腳本並提交 GPU 訓練的開源 ML 實習生。** 建立在 `smolagents` 框架之上，它打破了傳統 AI 只能「寫程式碼」的局限。透過內建的三階段閉環迭代（Research -> Plan & Validate -> Implement），它能自主爬取 arXiv 論文、追溯引用圖譜、篩選或合成 Hugging Face 數據集，甚至在遇到 reward collapse 時自主排查問題並重新訓練，完成真正意義上的端對端機器學習研究工作流。
  * **解決痛點 / 推薦場景**：**完美解決了 AI 研究員在進行模型微調或 RLHF 時，需要耗費數天在環境配置、數據清洗與反覆調整參數的「煉丹」苦工。** 實測在 PostTrainBench 基準上，僅用 Qwen3-1.7B 模型就能在 10 小時內達成 32% 的驚人成績，甚至超越了 Claude Code。極度適合**AI 實驗室/研究員**進行模型後訓練探索，或**開發者**用來自動化合成邊緣案例資料集。支援 CLI 與具備視覺化進度的 Web UI 雙重部署。
  * **資源**：[🐙 GitHub 官方源碼](https://github.com/huggingface/ml-intern) | [🌐 線上立即體驗 (Spaces)](https://huggingface.co/spaces/smolagents/ml-intern) | [📖 smolagents 底層文件](https://huggingface.co/docs/smolagents)
  `[自主ML代理]` `[自動化微調]` `[HuggingFace生態]` `[取代煉丹師]`

* **[Phi-Ground-Any-4B (微軟)](https://huggingface.co/microsoft/Phi-Ground-Any)** `[2025-07]` 🔥
  * **核心優勢**：**專為 AI Agent 打造的「精準點擊」視覺定位神作，徹底打通電腦控制的最後一哩路！** 微軟重磅釋出的 40 億參數輕量級 GUI Grounding 模型，採 MIT 完全開源。它打破了傳統視覺模型在螢幕截圖上容易「眼花」的缺陷，首創 Text-first 輸入架構（先給指令再看圖，帶著目標掃描），能將自然語言直接轉化為精確的螢幕像素座標。在難度極高的 ScreenSpot-Pro 基準測試中強勢刷新 10B 以下模型 SOTA，其底層核心技術更已被整合進 Windows Copilot 之中。
  * **解決痛點 / 推薦場景**：**完美解決了傳統 AI Agent 能理解工作流，卻經常因為「點不準按鈕」而導致任務全面崩潰的致命痛點。** 由於擁有極低的運算延遲與高達 1680×1008 的螢幕解析度支援，極度適合開發者用來打造**高可靠性的電腦操作智能體 (Computer Use Agent)**、**自動化 RPA 軟體測試腳本**，以及**複雜網頁導航副駕 (Web Agent)**，是讓矽基生命真正具備精確動手能力的工業級視覺感知模組。
  `[ComputerUse]` `[GUI定位]` `[Agent視覺核心]` `[微軟開源]`

* **[OpenCLI (網頁與私域數據 CLI 化神器)](https://github.com/jackwener/OpenCLI)** `[持續更新]` 🔥
  * **核心優勢**：**終結 Agent 視覺解析的高昂成本，將全網與本地應用直接化為 AI 專屬的「命令行 API」神作！** 徹底顛覆傳統 Browser-use 依賴大模型「看截圖、猜座標」的笨重模式。OpenCLI 透過自動化適配器，將 Bilibili、小紅書等百大網站，甚至是微信 (WeChat)、Notion、Cursor 等本地 Electron 應用程式，直接封裝成標準、確定性的 CLI 指令。
  * **解決痛點 / 推薦場景**：**完美解決了傳統 AI Agent 網頁自動化「Token 消耗極大、極易點錯」，以及「難以無縫提取私有通訊紀錄」的致命痛點。** 由於操作指令直接在本地瀏覽器或系統環境執行，達成了驚人的「零 Token 消耗」與 100% 執行確定性。極度適合開發者用來打造**極低成本的自動化 RPA 智能體**、**私域知識庫 (如微信對話/飛書) 的 RAG 語料抓取**，或是作為取代純視覺 Web Agent 的高效底層控制中樞。
  * **資源**：[🐙 GitHub 官方開源](https://github.com/jackwener/OpenCLI)
  `[Agent自動化]` `[零Token消耗]` `[私域數據提取]` `[Web-to-CLI]`

* **[Awesome-Design-MD (AI 視覺設計說明書)](https://github.com/VoltAgent/awesome-design-md)** `[2026-03-31]` 🔥
  * **核心優勢**：**終結 AI 生成 UI「千篇一律」的痛點，用純文字 Markdown 讓 AI 秒懂大廠級設計規範的開源神作！** 徹底拋棄繁瑣的 Figma 匯出與複雜的 JSON 設定檔。基於 Google Stitch 提出的全新標準，只要將一個 `DESIGN.md` 檔案放入專案根目錄，AI 程式設計助手（如 Cursor、Claude Code、v0 等）就能直接讀取包含色彩、字體、元件樣式與陰影深度的完整設計系統，並輸出視覺高度統一的精緻前端程式碼。
  * **解決痛點 / 推薦場景**：**完美解決了傳統 AI 寫扣時「懂語法卻不懂美學」、反覆微調前端樣式導致開發效率低下的致命痛點。** 專案內建超過 60 款全球頂尖科技與消費品牌（如 Stripe、Linear、Vercel、Apple、Claude 等）的開箱即用設計規範。極度適合**全端工程師**、**獨立開發者 (Indie Hacker)** 與 **新創團隊**，在缺乏專業 UI/UX 設計師的場景下，利用 Agentic Workflow 零成本、極速打造具備商業級質感的現代化 Web 應用介面。
  * **資源**：[🐙 GitHub 官方開源](https://github.com/VoltAgent/awesome-design-md) | [📝 Tenten 深度解讀與實戰](https://tenten.co/learning/awesome-designmd/)
  `[前端生成神器]` `[DESIGN.md]` `[Agent開發副駕]` `[UI設計自動化]`

* **[ai-website-cloner-template (AI 網頁逆向與生成神器)](https://github.com/JCodesMore/ai-website-cloner-template)** `[持續更新]` 🔥
  * **核心優勢**：**徹底顛覆前端切版與逆向工程的繁瑣流程，一鍵將任何網站轉化為生產級 Next.js 程式碼！** 它不僅僅是暴力的 HTML 爬蟲，而是一個結合了 AI 代理（支援 Cursor、Claude Code、Windsurf 等十餘種工具）的全自動化前端產線。透過獨創的「五階段工作流」（偵察設計系統、初始化配置、撰寫元件規格、平行建置、組裝與視覺品檢），能精準還原目標網站的互動邏輯與響應式佈局，並輸出高品質的 TypeScript + Tailwind CSS 專案。
  * **解決痛點 / 推薦場景**：**完美解決了開發者在看到精美網站想「致敬學習」、或是需要極速構建 MVP (最小可行性產品) 時，手刻前端介面極度耗時的痛點。** 讓 AI 代理接管繁瑣的 CSS 數值計算與元件切割，開發者只需專注於後端架構與業務邏輯。極度適合**全端工程師**、**獨立開發者 (Indie Hacker)** 進行**快速商業點子驗證 (Rapid Prototyping)**，或是企業接案團隊打造自動化建站流水線。
  * **資源**：[🐙 GitHub 官方開源](https://github.com/JCodesMore/ai-website-cloner-template)
  `[網頁逆向工程]` `[Next.js實戰]` `[Agent前端副駕]` `[自動化建站]`

* **[Skyvern (視覺化網頁自動化 Agent)](https://github.com/Skyvern-AI/skyvern)** `[持續更新]` 🔥
  * **核心優勢**：**顛覆傳統爬蟲與 RPA，用一句自然語言指令搞定全自動網頁操作的視覺智能體！** 徹底拋棄脆弱且易失效的 XPath、CSS 選擇器與 DOM 解析。Skyvern 結合了大語言模型與電腦視覺技術，直接「看懂」並理解網頁佈局，讓 AI 能像真人一樣進行邏輯推斷（如比對不同網站的同款商品）、填寫複雜表單、處理 2FA 雙重驗證，甚至編排多步驟的商業工作流。
  * **解決痛點 / 推薦場景**：**完美解決了傳統網頁自動化腳本「網站一改版，程式碼就報廢」的致命痛點。** 由於無需預先適配特定網站結構，極度適合企業與獨立開發者打造**跨平台電商價格監控系統**、**自動化求職與表單填寫機器人**，以及建構**發票批次下載與報表整理的 RPA 助手**。這款開箱即用的開源神器將大幅降低自動化系統的維護成本。
  * **資源**：[🐙 GitHub 官方開源](https://github.com/Skyvern-AI/skyvern) | [🌐 官方網站](https://www.skyvern.com/) | [📊 WebBench 基準測試論文參考](https://arxiv.org/abs/2403.04121)
  `[視覺Agent]` `[免寫選擇器]` `[RPA自動化]` `[網頁操作]`

* **[CLI-Anything (Agent 專屬軟體 CLI 生成器)](https://github.com/HKUDS/CLI-Anything)** `[2026-05]` 🔥
  * **核心優勢**：**徹底終結 GUI 自動化的脆弱惡夢，一鍵將「任何」開源軟體轉化為 AI Agent 可直接驅動的穩定 CLI 工具！** 港大 HKUDS 團隊的革命性專案。透過 Claude Code 插件執行一條指令，即可全自動掃描 GIMP、Blender 或 LibreOffice 等龐大軟體的原始碼庫，並生成包含 REPL 互動模式、標準 JSON 輸出與 100% 測試覆蓋率的生產級命令列介面 (CLI)。它不是模擬滑鼠點擊，而是真實呼叫軟體底層 API。
  * **解決痛點 / 推薦場景**：**完美解決了傳統電腦操作 Agent (如 RPA) 高度依賴截圖辨識，導致「按鈕位置一變就報廢」的致命痛點。** 賦予 Agent 像資深工程師一樣精準、穩定控制專業軟體的能力。極度適合企業用來打造**自動化影音/3D渲染流水線**、**文件批次處理 Agent**，或是將現有開源專案無痛升級為「Agent-Native (智能體原生)」的基礎設施。
  * **資源**：[🐙 GitHub 官方開源](https://github.com/HKUDS/CLI-Anything)
  `[電腦操作]` `[Agent基礎設施]` `[GUI轉CLI]` `[零妥協自動化]`

* **[Vercel Agent Browser (AI 原生瀏覽器自動化引擎)](https://github.com/vercel-labs/agent-browser)** `[2026-05-18]` 🔥
  * **核心優勢**：**專為 AI Agent 量身打造的革命性瀏覽器自動化工具，上下文 Token 消耗暴力銳減 93%！** 傳統 Playwright 框架強制 AI 吞下數萬行的混亂 HTML DOM 樹，一次登入即燒掉 20,000 個 Token。Vercel Labs 另闢蹊徑，透過 Rust CLI 將網頁精簡重構為 AI 專用的「無障礙樹」，自動過濾裝飾性元素，並為每個可互動元件指派穩定的 Ref 編號（如 `@e1`, `@e2`）。AI 看到的不再是天書，而是極簡清單，實現「指哪打哪」的極致效能。
  * **解決痛點 / 推薦場景**：**徹底終結傳統自動化腳本「因前端改版、CSS 選擇器變動而集體報廢」的易碎惡夢，並斬斷高昂的 Token 呼叫成本。** 只要網頁互動結構不變，Ref 編號便具備極強的抗改版魯棒性。原生適配 Claude Code 與 Cursor 等 AI 編程代理，是打造**工業級智慧網頁爬蟲**、**自動化資料採集智能體**，以及免程式碼快速原型驗證（MVP）的 AI-First 首選基礎設施。
  * **資源**：[🐙 GitHub 官方開源](https://github.com/vercel-labs/agent-browser) | [🌐 專案主頁](https://www.skyvern.com/) *(註：官方源碼與技術說明依據 Vercel Labs 最新發布頁面為準)*

* **[OpenHarness (港大 HKUDS)](https://github.com/HKUDS/OpenHarness)** `[2026-04]` 🔥
  * **核心優勢**：**將 Agent 從「黑盒」變「白盒」的極致輕量框架**。僅用 1.1 萬行 Python 程式碼，就完美復刻了 Anthropic 官方 Claude Code（高達 51 萬行 TypeScript）的核心架構。內建引擎循環、MCP 協議支援、多代理協作與三級權限沙箱，並**完全相容 Claude 官方的 Skills 與 Plugins 生態**。
  * **解決痛點 / 推薦場景**：完美解決了商業 Agent 框架過於臃腫、開發者難以窺探底層邏輯與二次開發的痛點。無論你是想從零拆解學習 Agent 的運作機制，還是需要一個能直接在終端機 (CLI) 執行檔案讀寫、Bash 腳本、Git 操作與 PR 審查的專屬 AI 開發副駕，這都是目前最具啟發性的開源平替神作。
  * **資源**：[🐙 GitHub](https://github.com/HKUDS/OpenHarness)
  * **⚠️ 關鍵警告 (PR 156, 159 中修復)**：[CVE-2026-6819] 遠端插件管理漏洞 (CVSS: 8.8 High)、[CVE-2026-40515] 權限繞過漏洞 (CVSS: 8.7 High)、[CVE-2026-6729] 對話劫持漏洞 (CVSS: 9.x Critical)
    <br>`[ClaudeCode平替]` `[白盒框架]` `[開發者副駕]` `[極易擴展]`

* **[OpAgent](https://github.com/codefuse-ai/OpAgent)** `[2026-02-20]` 🔥
  * **核心優勢**：**視覺驅動的 Web 智能體霸主，WebArena 成功率 71.6% 榮登榜首。** 由螞蟻集團研發，打破傳統對 HTML 代碼的過度依賴，改採網頁截圖直接進行空間佈局理解。結合線上強化學習（Online RL）與「規劃、執行、反思、總結」四位一體的協作架構，賦予 AI 像真人一樣在複雜網頁中試錯與導航的能力。
  * **解決痛點 / 推薦場景**：**完美解決了傳統網頁腳本因 UI 改版就失效、以及無法處理跨頁面複雜邏輯的問題。** 無需預設腳本，僅憑一條指令即可在亞馬遜（Amazon）等真實電商平台自主完成搜尋、識別與加購操作，是建構自動化電商助理與 RPA 流程的頂級引擎。
  * **資源**：[🐙 GitHub](https://github.com/codefuse-ai/OpAgent) | [🤗 HuggingFace](https://huggingface.co/codefuse-ai/OpAgent-32B) | [📄 Technical Report](https://arxiv.org/pdf/2602.13559) | [🌐 線上 Demo](https://huggingface.co/spaces/exias/OpAgent)

* **[[Heretic]](https://github.com/p-e-w/heretic)** `[2025-01-01]` 🔥 `[安全去對齊]` `[機械可解釋性]` `[自動參數優化]` `[開源平替]`
  * **核心優勢**：**打破大模型安全對齊的黑箱神話，首創將「拒絕方向消融 (Abliteration)」與 Optuna TPE 自動搜索完美封裝的去審查工業級利器！** 這款在 GitHub 狂攬 2.5 萬 Stars 的現象級開源黑科技，徹底顛覆了過往「去對齊必須深入理解 Transformer 殘差流與內部機制」的高難度學術門檻。Heretic 透過自動定位拒絕方向並執行權重正交化，在將有害提示拒答率壓至 3/100 的同時，對原模型能力與分佈的損害（KL 散度低至 0.16）降到歷史新低。
  * **解決痛點 / 推薦場景**：**完美解決了開發者在本地部署開源大模型時，常因「大廠過度審查（Over-censorship）導致正常指令頻頻遭拒」，而手動修改權重程式碼繁瑣且易導致模型崩潰的痛點。** 專案內建殘差向量投影與層間動畫分析，對研究者而言是探討模型內省機制的「手術刀」；對產品開發者而言，則是執行 `pip install` 就能一鍵移除安全對齊的「工業級拆卸標準件」。極度適合用於**本地私有化模型去審查**、**機械可解釋性研究**，以及需要極端模型自主權的開發場景。

* **[Gemini Computer Use](https://github.com/google-gemini/computer-use-preview)** `[2025-10]`：Google 預覽版框架，讓 AI 直接操作網頁介面。

* **[WebDancer](https://www.alphaxiv.org/zh/overview/2505.22648)** `[2025-05-30]`：Alibaba 開源的 WebAgent，專精於網頁資料的自主瀏覽與操作。

* **[OpenHands (Devin 平替)](https://github.com/All-Hands-AI/OpenHands)** `[2025-05-25]`：具備完整沙盒執行環境，能自主寫 Code、修 Bug。

* **[Deepsite](https://huggingface.co/spaces/enzostvs/deepsite)** `[2025-04-03]`：基於 DeepSeek 的網頁開發智能體。

* **[DeepGemini](https://github.com/sligter/DeepGemini)** `[2025-03-30]`：被譽為 AI 界搭積木神器。

* **[autoMate](https://github.com/yuruotong1/autoMate)** `[2025-03-11]`：基於 OmniParser 的 AI 自動化 GUI 助手。

* **[OmniParser](https://github.com/microsoft/OmniParser)** `[2024-10-26]`：微軟開源的核心技術，將純視覺輸入轉化為可操作的 UI 元素。

* **[context-mode](https://github.com/mksglu/context-mode)** `[2026-10-12]` 🔥 `[ContextWindow優化]` `[MCP伺服器]` `[CodingAgent]` `[會話記憶]`
  * **核心優勢**：**把 MCP 工具的原始輸出擋在 context window 之外：AI coding agent 的「上下文節流閥」。** 機制四招：沙箱工具只回傳結果摘要（官方宣稱 315 KB → 5.4 KB，98% 縮減）；SQLite 追蹤所有檔案編輯、git 操作、任務、錯誤與使用者決策，會話壓縮後用 FTS5＋BM25 只取回相關片段；「Think in Code」典式：讓模型寫程式做分析，而非把 50 個檔案讀進 context（官方例：47 次 Read＝700 KB → 1 次 ctx_execute＝3.6 KB）；刻意不強制簡潔寫作風格（官方引 Moonshot 研究：激進的簡潔提示會傷害 coding／reasoning 基準）。客觀指標：GitHub 27,383 star、1,950 fork、2,230 commits，10-12 登上 GitHub trending daily 第 3 名（AI 相關僅次於 REA），支援 Claude Code、Codex、Cursor、GitHub Copilot 等 17 個平台。
  * **解決痛點 / 推薦場景**：**完美解決了 AI coding agent「用越久越笨」的上下文失血痛點。** 舊方法：每個 MCP 工具呼叫都把原始資料傾倒進 context（一個 Playwright 快照 56 KB、20 個 GitHub issue 59 KB），30 分鐘燒掉 40% 上下文；會話一壓縮，agent 連自己在改哪些檔案都忘了。甜點區：工具輸出沙箱化、會話記憶外置索引、資料處理交給程式碼而非模型閱讀。極度適合**長時間多輪的 AI 結對編程**、**大型 monorepo 的 agent 重構任務**，以及**被 token 帳單刺痛的團隊**。
  * **資源**：[🐙 GitHub 官方倉庫](https://github.com/mksglu/context-mode)（倉庫根目錄另有 BENCHMARK.md，數字未獨立驗證）
  * **⚠️ 授權注意**：README 徽章標示 Elastic License v2，但 GitHub 倉庫頁顯示 License: Other（NOASSERTION），兩者不一致，商用採用前請自行確認。

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

* **[Scientific Agent Skills (K-Dense)](https://github.com/K-Dense-AI/scientific-agent-skills)** `[2026-10-14]` 🔥
  * **核心優勢**：**把通用 AI Agent 直接升級成「AI 科學家」：177 個經過 CI 測試的科學研究程序知識技能，全部 MIT 開源。** 每個技能是一個「程序知識」目錄：版本化、可讀的指令檔＋參考資料＋可執行腳本，Agent 只在任務需要時才載入。覆蓋生物資訊、化學資訊與藥物研發、臨床研究、材料科學、實驗室自動化等 20 個領域，對接 100+ 科學資料庫。遵循 open Agent Skills 標準，支援 Cursor、Claude Code、Codex、Google Antigravity、Pi，也可打包成 Agent Plugin。客觀指標：repo 抓取當日 49,462 star／4,427 fork，CI 對每個技能跑 skill tests＋security scan。
  * **解決痛點 / 推薦場景**：**完美解決了「通用模型給你能跑的程式碼，卻不保證分析方法在該領域站得住腳」的科學研究痛點。** 舊方法：Agent 自行寫的分析腳本選錯統計檢定、用錯識別碼命名空間、沒附必要免責聲明：看似能跑，實則同行一翻就倒。甜點區：生物資訊、基因組學、藥物虛擬篩選、質譜蛋白質體、臨床證據工作流：技能把「該領域認可的程序選擇」直接寫成可載入的知識。極度適合**做科學計算的個人研究者**（把 Claude Code／Cursor 變成會做 single-cell RNA-seq 或分子對接的助手）、**藥物研發團隊的自動化管線**，以及**需要可重現、可引用分析流程的實驗室**。
  * **資源**：[🐙 GitHub 官方開源](https://github.com/K-Dense-AI/scientific-agent-skills) | [📄 論文《Scientific Agent Skills: A Library of Procedural Knowledge for Research Agents》(arXiv:2609.00065)](https://arxiv.org/abs/2609.00065)
`[AI科學家]` `[Agent技能]` `[科學計算]` `[藥物研發]` `[生物資訊]`

* **[[Huobao Drama]](https://github.com/chatfire-AI/huobao-drama)** `[2026-05]` 🔥
  * **核心優勢**：**打破傳統影視製作高牆，首款將「創意劇本➔分鏡➔音效➔成片」全流程打通的開源自動化短劇生產線！** 基於 Mastra AI 框架自主編排 5 大工程智能體（劇本改寫、角色場景提取、分鏡拆解、音色分配、提示詞生成），後端採用 Hono 與 Drizzle ORM，極速驅動 SQLite、Sharp 與 FFmpeg 進行視訊、音訊、字幕的單鏡高能合成與整集拼接。模型層採多廠商解耦設計，支援隨時切換 MiniMax、OpenAI、Gemini、火山等最新影音大模型，開創了「人還在，只是從拍一條變成調一條流水線」的工業化新範式。
  * **解決痛點 / 推薦場景**：完美攻克短劇小團隊與個人創作者在內容生產中「中間碎活無窮無盡、跨工具鏈協同成本極高」的焦慮死結。 繞開學術界過度糾結的「單鏡頭完美幾何檢索」，從產品通量出發，將「霸總出現 7 次自動合併人物卡」等實用去重做到極致。實測在 GitHub 狂攬 11.3k Stars 與 2.1k Forks，極度適合自媒體團隊進行**模板化劇情批量生產**、**低成本爆款素材矩陣測試**，或開發者直接打包成 **SaaS 影音短劇生成平台**進行商業變現。
  * **資源**：[🐙 GitHub](https://github.com/chatfire-AI/huobao-drama) | [📄 深度解讀](https://deepwiki.com/chatfire-AI/huobao-drama)

* **[Claude for Legal (Anthropic)](https://github.com/anthropics/claude-for-legal)** `[2026]` 🔥
  * **核心優勢**：**Anthropic 官方開源的法律業專屬 Agent 智慧體全家桶，無縫接入 20+ 專業系統的自動化法務大腦！** 採用高度模組化的設計，將法律實務精準拆解為 12 個垂直領域與 70+ 個專業 Agent（定時任務與技能）。最大亮點是內建強大的 MCP (Model Context Protocol) 連接器，能直接打通 iManage、Ironclad、DocuSign 等法務標準資料庫。開發者無需撰寫複雜程式碼，僅透過編輯 Markdown 與 JSON (`CLAUDE.md`) 即可零門檻定製團隊專屬的法務 Playbook。
  * **解決痛點 / 推薦場景**：**完美解決了傳統法務工作「繁瑣合約比對耗時」、「法規追蹤易漏」與「跨系統資料孤島」的三大致命痛點。** 系統能自動執行 NDA 風險分級、供應商合約紅線標註 (Redline) 以及 GDPR 隱私合規 (DSAR) 的標準回應。極度適合**大型律師事務所**、**跨國企業法務部門**建構專屬的 AI 法律工作流 (Workflow)，讓律師從重複性的審閱泥淖中徹底解放，專注於高階決策。
  * **資源**：[🐙 GitHub 官方源碼](https://github.com/anthropics/claude-for-legal)
  `[法務Agent]` `[MCP生態系]` `[工作流自動化]` `[Anthropic官方]`

* **[Remotion Skills (AI 代碼驅動影片框架)](https://github.com/remotion-dev/skills)** `[持續更新]` 🔥
  * **核心優勢**：**顛覆「黑盒文生影片」，用 AI 寫 React 程式碼來「精確渲染」影片的工程化革命！** 建立在知名的 React 影片框架 Remotion 之上，將影片視為「隨時間變化的 UI」。它內建專為大模型設計的動畫模式庫與 MCP 協議，讓 AI 代理能直接聽懂自然語言指令（如：做一個 30 秒科技風產品介紹），並自動輸出 100% 確定性、可編輯、支援版本控制的 TypeScript/React 影片代碼。
  * **解決痛點 / 推薦場景**：**完美解決了主流生成式 AI 影片無法精確控制排版、無法修改錯字，以及傳統圖形化剪輯軟體無法自動化批量生產的痛點。** 告別手動拖曳時間軸，極度適合企業開發者打造**自動化 RPA 影片生產工廠 (如每日新聞摘要、電商財報可視化)**、**社群媒體短影音批量生成**，是將影片製作從「手工藝」升級為「軟體工程」的開源首選。
  * **資源**：[🐙 Remotion 主專案](https://github.com/remotion-dev/remotion) | [🐙 Remotion Skills (AI技能包)](https://github.com/remotion-dev/skills)
`[程式碼生影片]` `[Agent原生支援]` `[零誤差渲染]` `[自動化剪輯工廠]`

* **[OpenMontage (代理式 AI 影片全自動生產系統)](https://github.com/calesthio/OpenMontage)** `[持續更新]` 🔥
  * **核心優勢**：**號稱全球首款開源的「代理式影片製作系統 (Agentic Video Production)」，將影片剪輯從「手工藝」徹底升級為「軟體工程」！** 顛覆傳統 AI 生成影片需反覆人工微調的碎裂流程。它放棄了死板的 Python 狀態機，首創「Agent-First」架構，利用 YAML 定義管線與 Markdown 撰寫高達 500+ 個智能體操作技能 (Skills)。開發者只需在 Claude Code 或 Cursor 中輸入一句自然語言指令，系統便能自主完成調研、寫稿、呼叫生成 API (如 Kling/FLUX)、配樂及字幕合成。
  * **解決痛點 / 推薦場景**：**完美解決了傳統 AI 影片製作中「工具過於碎片化」以及「缺乏敘事邏輯與時間軸管理」的致命痛點。** 內建 12 條實戰級生產流水線（涵蓋動畫解說、虛擬主播、播客轉影片、多語言本地化等），且具備斷點續傳 (Checkpoint) 與審批閘門機制。極度適合**自媒體與內容創作者**以極低成本（實測 60 秒高畫質短片僅需 $1.33）打造**全自動化短影音工廠**，也是企業與研發團隊研究複雜 Agent 工作流編排的頂級開源教材。
  * **資源**：[🐙 GitHub 官方開源](https://github.com/calesthio/OpenMontage) | [🌐 官方網站與 DEMO](https://openmontage.dev) | [📝 AISignal 深度架構分析](https://www.aisignal.dev/analysis/calesthio-openmontage)
  `[Agentic Video]` `[自動化剪輯工廠]` `[Markdown技能驅動]` `[全自動生產線]`

* **[HyperFrames (HeyGen 代碼驅動影片渲染框架)](https://github.com/heygen-com/hyperframes)** `[2026-05]` 🔥
  * **核心優勢**：**顛覆「提示詞生影片」的盲盒模式，讓 AI Agent 透過編寫 HTML/CSS 來「精準剪輯」影片的工業級神作！** 由全球知名 AI 視覺公司 HeyGen 開源。它徹底拋棄了傳統的圖形化剪輯軟體，底層結合 Node.js、Puppeteer 與 FFmpeg，實現了「Write HTML, Render Video」的新範式。最驚豔的是，它原生內建了專為 Claude、Cursor 等 AI 代理設計的技能包，讓 AI 能直接理解並輸出結構化代碼，達成 100% 確定性、零誤差的影片渲染。
  * **解決痛點 / 推薦場景**：**完美解決了傳統生成式 AI 影片「難以精確控制轉場與排版」、「無法保證每次輸出一致」以及「難以大規模批量自動化生產」的致命痛點。** 支援 WebGL Shader 轉場特效、導入 CSV 數據自動生成動態圖表，甚至能輸入 URL 將整個網頁轉化為影片演示。極度適合**自媒體團隊打造自動化短影音流水線工廠 (RPA)**、**企業批量生產數據可視化報表影片**，以及開發者建構**端到端的全自動影片製作智能體 (Video Agent)**。
  * **資源**：[🐙 GitHub 官方開源](https://github.com/heygen-com/hyperframes) | [📝 官方介紹與實作案例](https://github.com/heygen-com/hyperframes%3Ftab%3Dreadme-ov-file%23examples)
  `[代碼驅動影片]` `[Agent原生支援]` `[自動化剪輯工廠]` `[HeyGen開源]`

* **[Paper2Poster](https://paper2poster.github.io/)** `[2025-06-02]`：學術利器，自動為 PDF 論文產生精美的發表海報。

* **[MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo)** `[2025-02-28]`：自媒體神器，AI 自動生成高清短影音工作流。

---

## Tools
**🛠️ 開發工具 (Tools & Protocols)**

標準化開發工具鏈能解決 80% 的模型部署相容性問題。 導入 vLLM 或 Ollama 等引擎，可將 API 響應時間從 2000ms 壓縮至 300ms 以下，並節省 50% 記憶體開銷。統一協議能無縫介接上層 Agent，實現底層模型熱抽換。

### 🔍 RAG 檢索增強生成：從入門到次世代架構 (Retrieval-Augmented Generation)

傳統的 RAG (文本切塊 + 向量檢索) 已無法滿足企業對複雜排版、長文本與精準推理的需求。以下精選 2025-2026 年最具突破性的 RAG 開源框架，依據「技術流派與解決痛點」為您分類：

#### 1. 顛覆傳統：無切塊與 Agentic RAG 架構
放棄傳統向量資料庫，運用 AI 推理能力進行導航，解決長文檔檢索破碎的問題。

* **[PageIndex](https://zread.ai/VectifyAI/PageIndex)** `[2026-03-01]` | 授權：MIT
  * **技術突破**：UCL 團隊開發的 Agentic RAG 革命性開源專案。完全拋棄「向量庫」與「文本切片 (Chunking)」，改用大模型進行推理導航。
  * **解決痛點**：在超長文檔檢索中達到 98% 的驚人準確率，徹底重塑 RAG 的底層邏輯。[🌐 線上體驗](https://chat.pageindex.ai/) | [📝 公眾號教學](https://mp.weixin.qq.com/s/iivoQtqzLhFA69N5iaOvzQ) | [📝 深度解讀](https://mp.weixin.qq.com/s/wwRJYvRl_jFaiiJkdrJdgw)

* **[PixelRAG](https://github.com/StarTrail-org/PixelRAG)** `[2026]` 🔥 `[視覺RAG]` `[多模態檢索]` `[幻覺剋星]` `[Qwen3-VL底座]`
  * **核心優勢**：**徹底顛覆傳統文本 RAG 的「視覺派」檢索框架，問答準確率飆升 18.1% 且 Token 成本狂降 10 倍！** 由 UC Berkeley SkyLab 與 BAIR 聯合研發，完全拋棄傳統「抽文本 → 切片段」導致圖表與排版全毀的落後套路。PixelRAG 直接透過 Playwright 引擎將網頁與 PDF 渲染成高清視覺瓦片 (Tiles)，並利用專屬微調的 Qwen3-VL-Embedding-2B 視覺大模型進行特徵萃取。它讓 AI 真正「看懂」文檔的表格結構、流程圖邏輯與版面配置，完美實現「以圖搜圖、以文搜圖」的雙向多模態檢索。
  * **解決痛點 / 推薦場景**：**完美解決了傳統 RAG 系統在處理「財報表格、工程圖紙、學術論文圖表」時，因強行剝離純文本導致結構錯亂、資訊遺失與嚴重幻覺的致命痛點。** 官方霸氣開源 828 萬筆維基百科視覺索引，並支援無 GPU 環境的本地私有化建庫。極度適合用於打造**企業級高保真多模態知識庫**、**醫療與金融複雜報表解析系統**，以及需要精準視覺溯源的**大模型幻覺治理 (Hallucination Mitigation)** 工業級場景。
  * **資源**：[🐙 GitHub 官方開源](https://github.com/StarTrail-org/PixelRAG)

* **[[DCI-Agent-Lite (Direct Corpus Interaction)]](https://github.com/DCI-Agent/DCI-Agent-Lite)** `[2026-05]` 🔥
  * **核心優勢**：**拋棄 Embedding 與向量庫，讓 Agent 直接用 Bash 指令「裸搜」語料的 RAG 顛覆神作！** 這篇頂會級別的研究首創 DCI (Direct Corpus Interaction) 範式。它完全省去了傳統 RAG 耗時的文本切片、向量化與 Top-k 固定過濾流程，直接賦予 AI Agent 使用 `grep`、`find` 等終端機指令的能力，讓 AI 能像真人工程師一樣與原始文件進行高解析度的自由互動與多步查證。
  * **解決痛點 / 推薦場景**：**完美解決了傳統向量 RAG 「先壓縮再檢索」導致關鍵細節流失、無法處理精確字彙比對與複雜多跳推理 (Multi-hop Reasoning) 的致命痛點。** 實測在 BrowseComp-Plus 基準上準確率暴漲 11%，且 API 呼叫成本反降 30%。極度適合企業打造**無索引即時檢索 (Zero-index retrieval)**、**動態程式碼庫/Log 檔分析**與**高價值的 Agentic Search (代理式檢索) 深度研究大腦**。
  * **資源**：[🐙 GitHub 官方開源](https://github.com/DCI-Agent/DCI-Agent-Lite) | [📄 arXiv 論文 (2605.05242)](https://arxiv.org/abs/2605.05242) | [🤗 Hugging Face 討論區](https://huggingface.co/papers/2605.05242)
  `[無索引檢索]` `[終端互動]` `[RAG顛覆者]` `[高解析度介面]`

* **[LinearRAG](https://github.com/DEEP-PolyU/LinearRAG)** `[2025-11-20]`
  * **技術突破**：全新的高效 RAG 框架，主打「無需進行複雜的關係抽取 (Relation Extraction)」，大幅降低構建知識庫的算力與時間成本。[📝 知乎解讀](https://zhuanlan.zhihu.com/p/1975321777342260763)

#### 2. 資料清洗與多模態解析 (Data Parsing & Multi-modal)
RAG 的成敗取決於資料輸入的品質。這些工具專精於處理複雜表格、圖片與數學公式。

* **[MinerU-Popo (Universal Post-Processing Model for Structured Document Parsing)](https://github.com/opendatalab/MinerU-Popo)** `[2026-05-24]` 🔥 `[RAG前處理]` `[文件級OCR後處理]` `[跨頁結構重建]` `[動態分塊同步]`
  * **核心優勢**：**打破單頁 OCR 解析的資訊孤島，地表首個專為 RAG 打造的文件級「跨頁結構與邏輯重建」後處理黑科技模型！** 當前 MinerU、PaddleOCR、GLM-OCR 等模型已成為頁面解析的標準，但下游 RAG 應用常因頁面邊界導致文字截斷、表格斷裂、標題層次遺失及圖文語意關聯中斷（四大缺口）[cite: 1]。由 OpenDataLab 團隊打造的 MinerU-Popo 另闢蹊徑，複用現有 ASR/OCR 輸出，以極輕量的後處理成本重構文件級邏輯[cite: 1]。基於 Qwen3-VL-4B 進行垂直微調，內建標籤歸一化、四子任務推理（文字/表格截斷、標題層次、圖文關聯）、重疊分塊偏差校準及文件樹構建管線[cite: 1]，以 0.37 doc/s 的極速推理解鎖文件級大一統解析，標題層次 TEDS 精度狂飆至 **90.6%**[cite: 1]！
  * **解決痛點 / 推薦場景**：**完美解決企業建置 RAG 私有知識庫時，因 PDF 雙欄排版、跨頁表格被機械式切片（Chunking）導致格式破碎、長代碼斷裂及上下文明顯丟失的致命痛點[cite: 1]。** 系統最硬核的突破在於「表格截斷分析」，能透過 6 項啟發式預篩選精準判斷同表性，並預測列級合併策略（`cell_list`），自動處理跨頁邊界行中不同列的單元格狀態[cite: 1]。其首創的「重疊分塊 + 偏差校準」同步機制，讓長文件解析在維持 4B 微型參數的硬體優勢下[cite: 1]，於下游 ViDoRe V3 基準評測中大獲全勝，**最高將 RAG 下游查詢延遲暴力壓低 70%**[cite: 1]。極度適合用於**大型法律合規合約解析**、**理工 STEM 理工論文高保真 Markdown 清洗**，以及**高併發、低算力成本的企業級大模型預訓練語料準備管線**[cite: 1]。
  * **資源**：[🐙 GitHub 官方開源](https://github.com/opendatalab/MinerU-Popo) | [📄 論文 (arXiv:2605.24973)](https://arxiv.org/abs/2605.24973) | [🤗 HuggingFace 權重下載](https://huggingface.co/DreamEternal/MinerU-Popo)

* **[OpenDataLoader](https://github.com/opendataloader-project/opendataloader-pdf)** `[2026-03-20]`
  * **核心優勢**：在極度困難的「表格擷取」任務中拿下 0.93 的超高準確率。主打「不追求極限速度，但精準度無可挑剔」的穩健策略，是企業處理 PDF 財報與數據報表的神兵利器。[📝 公眾號解讀](https://mp.weixin.qq.com/s/mPjH0dTyAMLKL5Hq5KPqCw)

* **[RAG-Anything](https://github.com/HKUDS/RAG-Anything)** `[2025-07-02]`
  * **核心優勢**：港大 HKUDS 團隊打造的「全能多模態 RAG 系統」。能一鍵自動解析 PDF、Word、PPT 中的文字、圖片、複雜表格與公式，並無縫映射到知識圖譜 (KG) 中。極度適合金融財報、醫療病歷或科研文獻的深度推理。[📄 論文](https://arxiv.org/pdf/2510.12323) | [📝 36Kr 解讀](https://m.36kr.com/p/3358608090400776) | [📝 Milvus 實戰解析](https://milvus.io/zh-hant/blog/multimodal-rag-made-simple-rag-anything-milvus-instead-of-20-separate-tools.md)

#### 3. 圖譜增強與全局語意 (Graph-RAG)
解決傳統 RAG「只見樹木，不見森林」的問題，強化實體之間的邏輯關聯。

* [[HyGRAG](https://www.google.com/search?q=%E9%80%A3%E7%B5%90)] [2026-06-18] 🔥 [GraphRAG] [多跳推理] [知識融合] [動態更新]
  * **核心優勢**：**首創融合上下文（Chunk）與顯式關係（Entity Triplet）的層級圖索引與雙通道檢索架構，在多跳推理基準上平均提升 9.7% 準確率，並在推理階段顯著節省 Token 消耗。**
  * **解決痛點**：舊方法面臨實體抽取累積錯誤與丟失上下文（Entity-centric）或不擅長跨片段顯式關係（Chunk-centric）的兩難困境；改善方式是透過混合圖建構、Cleora 結構感知嵌入與 LLM 社區摘要合成超越源文檔的新興知識表示，並設計 attachment-based update 機制支援局部動態更新，避免全圖重建的高昂運算開銷與延遲。

* **[FlowRAG](https://arxiv.org/abs/2606.17856)** `[2026-06]` 🔥
  * **核心優勢**：**打破傳統 GraphRAG「實體稀疏」與「噪聲擴散」的致命缺陷，首創四層異構圖與頻率感知加權流的 RAG 新範式！** FlowRAG 放棄了單純的相似度比對，轉而建構「段落 ↔ 摘要 ↔ 句子 ↔ 實體」的四層緊密架構。透過「雙粒度實體激活」（摘要層處理抽象轉述、句子層精確命中）加上「頻率感知加權流」主動剪除低置信度的錯誤關聯。將無序的文本塊升級為一條條「可追蹤的顯式邏輯骨架」，在多跳推理基準 (如 HotpotQA, 2Wiki) 準確率強勢碾壓 LightRAG 與 HippoRAG。
  * **解決痛點 / 推薦場景**：**完美解決傳統 RAG 面對「抽象提問」時找不到檢索入口，以及「複雜多跳推理」時中間證據鏈斷裂、被錯誤資訊帶偏導致嚴重幻覺的痛點。** 更驚人的是，其輕量化的抽取式建圖讓索引時間比 LightRAG 狂飆快 14 倍，LLM Token 消耗驟降近 47 倍！極度適合打造**企業級高精度多跳問答知識庫**、**醫療/法律等垂直領域的嚴謹邏輯推理系統**，以及需要**強可解釋性證據鏈**的高階 AI Agent。

* **[Hyper-Extract (開源強類型全場景知識圖譜提取框架)](https://github.com/yifanfeng97/Hyper-Extract)** `[2026-05-17]` 🔥
  * **核心優勢**：**打破「先壓縮再過濾」的黑盒限制，首創「八大強類型結構」與「知識增量演進」的 Graph-RAG 前處理終極神作！** 採用 Pydantic 與強類型驗證機制，能一鍵將雜亂的非結構化文件（如財報、法務合約、醫療病歷）轉化為可序列化、持久化的知識摘要。除了傳統的二元關係圖譜 (AutoGraph) 外，更原生支援多方複雜關係的**超圖 (AutoHypergraph)**、以及融合時間與地理空間維度的**時空圖 (AutoSpatioTemporalGraph)**，並內建 GraphRAG、LightRAG 等十餘種開源提取引擎。其最強大的設計在於「知識的增量演進」，允許持續餵入新文件並於原有圖譜上智慧擴展更新，無需每次從頭跑完訓練流程。
  * **解決痛點 / 推薦場景**：**完美解決了傳統 Graph-RAG 在建置知識圖譜時「實體關係容易斷裂、座標漂移」以及「新文件移入必須全量重練導致算力爆表」的致命痛點。** 框架內建 80+ 款開箱即用的領域模板（涵蓋金融、法律、醫學等），提供極簡的 CLI 與 Python SDK 雙模式驅動。極度適合**企業建構私有化高價值知識管理大腦**、**算法團隊準備指令微調數據集**，以及需要細粒度證據追蹤與時空線索拼接的**深度產業研究與智慧體搜尋 (Agentic Search)** 場景。
  * **資源**：[🐙 GitHub 官方儲存庫](https://github.com/yifanfeng97/Hyper-Extract) | [📄 arXiv 技術報告](https://arxiv.org/abs/2605.05242) | [📝 模板設計與決策樹指南](https://www.google.com/search?q=https://github.com/yifanfeng97/Hyper-Extract/blob/main/DESIGN_GUIDE.md)
  `[Graph-RAG]` `[知識圖譜自動生成]` `[超圖與時空圖]` `[零代碼YAML驅動]`

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

### 🔧 開發者與個人資訊自動化 (Personal Automation & Dev Tools)
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

### 🎨 視覺化畫布與 AI 創作引擎 (Visual Canvas & Creation)
打破傳統 ChatGPT「單線對話框 (Chat UI)」的限制，提供全局鳥瞰的空間思維，適合複雜企劃與長篇寫作。

* **[Refly (畫布式 AI 創作引擎)](https://github.com/refly-ai/refly)** `[持續更新]`
  * **核心優勢**：一款極具創新力的「無限畫布式 (Canvas)」開源 AI 原生創作引擎。內建整合 13+ 主流大語言模型，提供類似 Miro 結合 Notion AI 的白板工作流。
  * **解決痛點**：解決使用 AI 進行深度寫作或腦力激盪時「上下文容易丟失、邏輯難以串聯」的痛點。開發者與創作者可以在畫布上自由展開節點、對比多個模型的生成結果，是個人與團隊進行複雜 AI 內容協作的完美開源平替方案。[📖 官方中文文檔](https://docs.refly.ai/zh)

---

## World Models
**🌍 World Models (世界模型)**

世界模型透過物理法則學習，大幅提升空間與時序預測能力。 整合 SORA 等空間預測架構，機器人與自駕決策的模擬誤差率可降低 60% 以上，數據採集成本減少十倍。這是從純文本邁向通用具身智能 (Embodied AI) 的關鍵路徑。如果說傳統 LLM 是「文字接龍」，那世界模型 (World Models) 就是讓 AI 具備「物理法則與常識預測能力」。透過預測環境的下一步變化，這是通往通用人工智慧 (AGI) 與具身智能 (Embodied AI) 的關鍵拼圖。

* **[Genie 4（Google DeepMind：原生音訊＋即時轉向的世界模型，Gemini 在迴圈內導引）](https://deepmind.google/blog/genie-4-a-new-generation-of-world-simulation/)** `[2026-10-28]` 🔥 `[世界模型]` `[原生音訊]` `[即時轉向]` `[Gemini導引]` `[研究預覽]` `[SynthID]`
  * **核心優勢**：**世界模型第一次同時做到「看得到、聽得到、改得到」：畫面即時算、聲音原生出、場景中途還能用一句話改寫。** Genie 4 是 Google DeepMind 的新一代世界模型：輸入一句話或一張圖，即時生成可走進去探索的互動世界，而非一段播完就結束的影片。三大升級皆來自官方部落格：第一，原生音訊，DeepMind 首款即時世界模型原生生成聲音，環境音、音樂與角色即時對話皆與畫面同步生成；第二，即時轉向，模擬進行中可用自然語言改天氣、移鏡頭、加入人物或物件，Gemini 會按場景脈絡調整指令，兩次輸入之間 Gemini 也持續監看並推動場景；第三，Gemini 進迴圈，Gemini Omni 負責錨定真實外觀與物理行為，Gemini 3.8 Flash 擔任迴圈內導引 Agent，逐格觀察、把目標拆成步驟、驗證每步是否完成，遇使用者介入即時改計畫，讓多步驟事件具備因果連貫性；另與 Gemini 4 Argon 連動做機器人模擬實驗（Apptronik Apollo 人形機器人下西洋跳棋的步驟拆解）。
  * **解決痛點 / 推薦場景**：**解決了「影片生成只能看、世界模型只能靜默探索、想改場景就得重算整段」的痛點。** 舊方法：影片模型產出固定片段，導演想換鏡頭或天氣只能重抽；早期世界模型無聲、人物動作僵硬、場景稍長就失憶。甜點區：影視前期視覺化（同一場景即時多拍、隨改鏡頭與對白）、遊戲與互動體驗原型（有想法先走進可玩原型、再寫引擎程式碼）、歷史照片與災害情境的沉浸式重現、機器人與 Agent 的訓練場景生成（先在想像世界測一遍再上真機）。官方也明言用途邊界：目前是研究預覽，僅受信任測試者可用，之後先到 Google AI Ultra 訂閱戶的 Project Genie 與 Gemini API／AI Studio 早期夥伴，一般使用者需排候補；所有生成影音皆帶 SynthID 浮水印。
  * **量化基準（官方部落格未給解析度、幀率與基準分數，以下數字來自次級報導，僅供參考）**：據 TechCrunch 報導，場景維持一致的時間約 2 分鐘，為 Genie 3 的約 2 倍（Genie 3 為 1 分鐘、720p、24fps，見次級對照）；官方部落格僅稱「短時間 session 內可維持連貫」，未承諾具體分鐘數。官方坦承的限制比數字更重要：模擬越久、多輪複雜改寫後、或在場景中長途移動時，視覺細節與物件恆存性仍會漂移；複雜物理互動、即時音訊準確度、畫面中可讀文字、空間準確度與長期一致性皆列為持續研究項目。
  * **資源**：[🌐 Google DeepMind 官方部落格](https://deepmind.google/blog/genie-4-a-new-generation-of-world-simulation/)
  * **附註（未獨立查證）**：日期認定是本則最容易踩錯的邊界，特此標明：官方部落格標示 2026-10-27（美國日期），其 UTC 戳記 10-27 16:00 換算台北時間恰為 10-28 00:00，屬本日窗口起點，故本日收錄、不提前、不延後；頁面另有 10-28 12:01 UTC 的更新紀錄，那是頁面更新不是改寫發布日。無權重、無開源程式碼、無技術報告論文號，不可寫成開源模型；「最逼真、最互動」為執行長 Sundar Pichai 的公開說法，非評測結論。昨日晚間的使用者指定試作（口播稿、封面圖、TTS 音檔）已先行產出，本日正式條目沿用其已查證事實並補上官方部落格親驗細節，試作媒體不另登記台帳。

* **[H-JEPA (LeCun AMI 世界模型)](https://github.com/kevinghst/H-JEPA)** `[2026-10]` 🔥 `[世界模型]` `[JEPA]` `[分層規劃]` `[視覺規劃]` `[具身智能]`
  * **核心優勢**：**LeCun 2022 年畫的分層 JEPA 藍圖，第一次端到端跑通了。** AMI 聯合 NYU、INRIA Paris、Brown：多個動作條件 JEPA 逐層堆疊，每層在自己的表徵空間預測更遠的未來（高層一步對應低層兩步）。規劃由上而下：高層先定粗略路線，預測的中間狀態變成低層的子目標，低層接力細化成原始動作。每層三件套（狀態編碼器、動作編碼器、預測器）端到端共同訓練，用 LeJEPA 的 SIGReg 防表徵坍塌。Visual AntMaze 三層成功率 73%，單層只有 18%，而且規劃算量更少。
  * **解決痛點 / 推薦場景**：**單一表徵空間伺候不了兩種活：低層控制要細節，長程規劃要抽象。** 四足機器人腿姿不同、位置對了，平坦模型會誤判「離目標還很遠」；H-JEPA 的高層自動丟掉腿部姿態這類快變細節、只保留位置與迷宮佈局，目標比對回到對的抽象層級。代碼（MIT）與 84 個預訓練 checkpoint 全開源。極度適合**長程視覺規劃**、**機器人操作**、**世界模型研究**。⚠️ 分層不是越多越好：Push-T 兩層最佳，三四層因短軌跡餓死高層訓練數據反而下降；目前全是仿真加 DROID 離線評測，無真機閉環成績。
  * **資源**：[🐙 GitHub](https://github.com/kevinghst/H-JEPA) | [📄 論文](https://arxiv.org/abs/2610.06805) | [🌐 專案頁](https://h-jepa.com)

* **[WorldScape 0.2]** `[2026-03]` 🔥 `[具身世界模型]` `[MoE 架構]` `[物理可信]`
  * **核心優勢**：**打破物理與視覺的次元壁，參數僅競品 10% 卻稱霸全球的世界模型霸主！** 由 Manifold AI (流形空間) 研發，採用突破性的多專家協同 (MoE) 架構。它將幾何拓撲、語意理解與物理規律在統一的隱式元空間中完美對齊，不僅在 3D/4D 視覺生成上保持極高的一致性，更在 WorldArena 與 WorldScore 兩大權威具身智能 (Embodied AI) 基準評測中，強勢擊敗國際巨頭穩居雙榜全球第一。
  * **解決痛點 / 推薦場景**：**徹底終結傳統影片生成模型常見的「空間扭曲」、「穿模」與「無視重力」等不符物理常識的致命缺陷。** 憑藉極高的空間智能密度與極速的即時推理能力，它是打造**具身智能機器人**動作規劃器 (Action Planning)、**自動駕駛虛擬模擬環境**，以及需要將高階物理 AI 落地至**邊緣運算設備 (Edge AI)** 的頂級世界大腦。
  * **資源**：[📊 WorldArena 基準榜單](https://huggingface.co/spaces/WorldArena/WorldArena) | [📄 WorldArena 論文](https://arxiv.org/abs/2602.08971) | [📊 WorldScore 基準榜單](https://huggingface.co/spaces/Howieeeee/WorldScore_Leaderboard)

* **[Code World Model (Meta Yann LeCun 團隊)](https://zread.ai/facebookresearch/cwm/1-overview)** `[2025-09-25]`
  * **核心優勢**：AI 教父 Yann LeCun 領軍發布的 320 億參數開源世界模型。有別於生成式 AI，它採用 JEPA (聯合嵌入預測架構)，專注於理解系統的內部邏輯與預測代碼執行的結果，是 AI Agent 進行複雜規劃 (Planning) 的終極大腦。[📝 新浪深度報導](https://t.cj.sina.com.cn/articles/view/1746173800/68147f6801901e2wa)

---

## MoE
**🧠 MoE (Mixture of Experts 混合專家模型)**

MoE 架構在不增加推論成本的前提下，實現參數規模的指數級擴張。 採用 8x7B 的稀疏激活機制，僅需 14B VRAM 即可達到 70B 稠密模型的生成品質，運算效率提升 300%。為邊緣伺服器部署千億參數模型提供最佳解法。MoE 架構是目前突破大模型「算力牆」的唯一解方。它的核心概念是「術業有專攻」：模型可能擁有千億參數，但每次回答問題時，只會啟動（激活）最相關的幾個「專家神經網路」，從而在極低的推論成本下，展現出超越稠密模型 (Dense Model) 的極致效能。

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

* **[Hy3-preview](https://github.com/Tencent-Hunyuan/Hy3-preview)** `[2026-04-23]` 🔥 `[快慢思考融合]` `[Agent實用霸主]` `[超長上下文256K]`
  * **核心優勢**：**騰訊混元重建後的首款開源巨獸！總參數 295B (激活 21B) 完美融合快慢思考的 MoE 模型。** 徹底拋棄「為刷榜而生」的盲點，主打真實業務場景的「全面實用性」。在複雜邏輯推理（如清華數學博資考）與程式碼生成上表現驚人。其原生支援快思考（直接響應）與慢思考（深度推論）動態切換，首 token 延遲大幅降低 54%，整體推理效率更提升了 40%。
  * **解決痛點 / 推薦場景**：**完美解決了傳統大模型在執行「超長複雜工作流」時容易斷片、忘記指令的致命痛點。** 實測可穩定支援高達 495 步的 Agent 自動化腳本（如文件處理、工具鏈編排）。官方提供極其完善的 vLLM / SGLang 部署腳本與 LLaMA-Factory 微調指南，是企業打造**高併發複雜智能體 (Agentic AI)**、**超長文本檢索 (RAG)** 以及**程式碼開發副駕 (Code Copilot)** 的工業級基礎模型首選。
  * **資源**：[🐙 GitHub 官方開源](https://github.com/Tencent-Hunyuan/Hy3-preview) | [🤖 ModelScope 模型下載](https://www.modelscope.cn/collections/Tencent-Hunyuan/Hy3-preview)

* **[Hunyuan-Large (騰訊混元最大 MoE)](https://github.com/Tencent/Hunyuan-Large)** `[2024-11-06]`
  * **核心優勢**：在中文互聯網資料的理解上具備極大優勢，且針對 RAG 檢索任務進行了深度最佳化。[🤗 線上 DEMO](https://huggingface.co/spaces/tencent/Hunyuan-Large) | [🤗 模型下載](https://huggingface.co/tencent/Hunyuan-Large) | [📝 機器之心報導](https://www.jiqizhixin.com/articles/2024-11-06-6)


---

## SLM
**📱 SLM (Small Language Models 小型語言模型)**
### 🧠 次世代 LLM：小型語言模型，邊緣運算首選：Small Language Models (SLM)

SLM 是實現數據絕對隱私與端側斷網運行的首選。 在 8GB 記憶體的設備上，7B 級別模型的量化版 (4-bit) 可達到每秒 25 tokens 的生成速度，滿足 90% 邊緣運算需求。有效規避雲端 API 的隱私外洩風險與高昂訂閱費。隨著端側算力提升，2025 年的 AI 戰場已從雲端燒向邊緣設備。小型語言模型 (SLM) 通常指參數在 8B 以下的模型，主打「低功耗、保護隱私、無網連線」。以下是專為手機與物聯網 (IoT) 設計的開源王者：

#### 📊 端側 SLM 快速比較表
| 模型名稱 | 開發團隊 | 💡 核心優勢與解決痛點 | 🚀 推薦適用場景 & 規格標籤 |
| :--- | :--- | :--- | :--- |
| **Phi-4** | 🇺🇸 **Microsoft** | **以小博大的教科書**。微軟 Phi 家族最新力作，透過高品質合成數據訓練，在各項 Benchmark 上經常越級打怪，擊敗百億參數模型。 | 本地筆電開發、離線文件摘要<br>`[微軟生態]` `[高CP值]` |
| **Llama 3.2 (1B/3B)** | 🇺🇸 **Meta** | **專為端側與手機設計**。Meta 官方釋出的輕量版本，完美適配行動裝置的記憶體限制，並保持強大的指令跟隨能力。 | iOS/Android APP 內建 AI、物聯網<br>`[Edge AI]` `[手機可跑]` |
| **SmolLM2** | 🌐 **Hugging Face** | **為極端環境打造的極小模型**。極致壓縮體積，專門針對運算資源極度受限的環境進行最佳化。 | 穿戴式裝置、超低功耗設備<br>`[極小體積]` `[極低功耗]` |

#### 📂 核心模型下載與資源

* **[[ELF (Embedded Language Flows)]](https://github.com/lillian039/ELF)** `[2026-05]` 🔥 `[擴散語言模型]` `[何愷明團隊]` `[非自迴歸]`
  * **核心優勢**：**打破 GPT 自迴歸霸權的連續擴散語言模型神作，僅 105M 參數達成驚人生成品質！** 由何愷明團隊重磅推出，徹底捨棄傳統 Next-token prediction 路線，首創將文字 Token 映射為連續 Embedding 並採用 Flow Matching 技術進行去噪。它完美融合了圖像生成領域的 CFG (Classifier-Free Guidance) 技術，在僅需 45B 訓練 Token 與 32 步極速採樣的條件下，生成困惑度壓低至 24，效能強勢輾壓傳統離散擴散模型。
  * **解決痛點 / 推薦場景**：**完美解決了傳統大模型「逐字生成延遲高」與「極度依賴海量訓練資料 (通常需 500B+)」的致命痛點。** 透過「連續到底、最後一步離散化」的極簡架構，大幅降低了訓練算力與推論開銷。極度適合部署於**資源受限的邊緣運算設備 (Edge AI)**，並在**機器翻譯**與**文本摘要**等條件生成 (Conditional Generation) 任務中，作為低算力、高效能的次世代微型語言模型 (SLM) 首選。
  * **資源**：[🐙 GitHub](https://github.com/lillian039/ELF) | [📄 論文](https://arxiv.org/pdf/2605.10938)

* **[Phi-4](https://huggingface.co/NyxKrage/Microsoft_Phi-4)** `[2024-12-13]`：微軟 Phi-4 正式發表，以小博大效能驚人。[📝 公眾號解析](https://mp.weixin.qq.com/s/uny1VUt7vk_ZU6hCH0EDGg)

* **[SmolLM2](https://github.com/huggingface/smollm/)** `[2024-11-04]`：Hugging Face 官方推出的手機執行小型語言模型。[📝 iThome 報導](https://www.ithome.com.tw/news/165832)

* **[Llama 3.2 (1B/3B)](https://ai.meta.com/blog/llama-3-2-connect-2024-vision-edge-mobile-devices/)** `[2024-09-25]`：Meta 震撼開源的端側邊緣運算 (Edge AI) 專屬模型。

---
## Reasoning
**🤔 Reasoning Models (深度推理模型)**

強化思維鏈 (CoT) 的推理模型徹底改變了複雜邏輯任務的解決率。 實測如 DeepSeek-R1 或 OpenAI o1 架構，在進階數學與程式碼基準 (MATH/HumanEval) 上突破 85% 準確率。透過隱藏推理過程，大幅降低幻覺並提升可靠度。自從 OpenAI 的 o 系列問世後，「Chain of Thought (思考鏈)」與「強化學習 (RL)」成為激發大模型數理運算與邏輯推理的標準配備。以下精選具備頂尖思考能力的開源推理模型：

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

* **[GPT-6.1 Terra (OpenAI)](https://openai.com)** `[2026-10-26]` 🔥 `[電腦操作]` `[視覺推理]` `[閉源API]` `[成本效率]` `[ChatGPT Work]` `[Codex]`
  * **核心優勢**：**OpenAI 中階主力換代：把電腦操作與視覺推理做成「日常高用量工作」的可負擔選項，旗艦級任務表現、不到旗艦的價格與速度。** 接替 GPT-5.6 Terra，定位在 Luna／Terra／Sol／Astra 產品線的中段：看懂螢幕、跨應用操作、寫提案、讀技術圖、填表單、剪影片。API 模型 id 為 `gpt-6.1-terra`，上下文 1.05M tokens、最大輸出 128K tokens、知識截止 2026-06-01，輸入文字與圖像、輸出文字。標準 API 價為每百萬 tokens 輸入 1 美元、快取輸入 0.05 美元、輸出 5 美元，OpenAI 稱比 GPT-5.6 Terra 與 GPT-6.1 Sol 的標準價低 50%；輸入超過 272K tokens 的請求適用較高的長上下文費率。
  * **解決痛點 / 推薦場景**：**解決了「旗艦模型做日常電腦雜活又貴又慢、小模型又做不穩」的甜點區問題。** 舊方法：高用量任務（讀發票入帳、跨表單填寫、技術圖判讀）全打到旗艦模型，成本與等待時間隨量暴漲；或用上一代 Terra，錯誤率高、終端任務成功率低。OpenAI 自測數字：Terminal-Bench 4.0 最高推理強度下 50.3%，對比 GPT-5.6 Terra 的 21.5%；Agents' Last Exam 中等強度下比前代高約 15 個百分點，且 OpenAI 稱其表現追平 GPT-6 Astra、每 token 價格僅約十分之一、任務完成速度快 3 倍以上；內部困難提示事實錯誤率從低強度的 53.6% 降到 16.7%，最高強度降到 4.3%。極度適合**ChatGPT Work 與 Codex 裡的高用量日常電腦工作**、**要把 Agent 任務成本壓到可規模化的團隊**。但 OpenAI 自己也劃線：最複雜的程式任務仍建議用 GPT-6.1 Sol 或 Astra，Terra 不是旗艦替代品。
  * **資源**：[🌐 OpenAI 官方發布（2026-10-26，經多家報導引述）](https://siliconangle.com/2026/10/26/openai-launches-gpt-6-1-terra-for-faster-better-performing-ai-agents-at-half-the-price/) | [📝 價格與基準整理](https://aiweekly.co/alerts/openai-ships-gpt-61-terra-at-15-per-million-half-of-sol) | [📝 報導：Agents' Last Exam 與 Terminal-Bench](https://www.digitaltrends.com/computing/openais-new-gpt-6-1-terra-model-gets-astra-like-results-at-a-fraction-of-the-cost/)
  * **附註（未獨立查證）**：以上基準皆為 OpenAI 自測，尚未有獨立複現；「快 3 倍以上」為 OpenAI 自家計時結果。可用範圍：ChatGPT Work 與 Codex 的 Plus、Pro、Business、Enterprise、Edu 方案，不在一般 ChatGPT 對話提供；GitHub 另於 UTC 10-26 宣布 Copilot 全面上線，換算台北時間為 10-27 凌晨，不計入本日窗口主項。本條目為閉源 API 模型，不適用「新模型快訊：前沿開源權重模型」H3，故改插頂級閉源商業模型小節。

* **[Gemini 4 Carbon(Google DeepMind：資安＋長程工程最強前沿模型，首批只給資安防禦者)](https://deepmind.google/blog/gemini-4-carbon-our-next-frontier-model/)** `[2026-10-29]` 🔥 `[閉源前沿]` `[資安防禦]` `[長程Agent]` `[Intelligence Index 59]` `[Fairwind限定]` `[對齊強化]`
  * **核心優勢**：**Google 兩週內第二款 Gemini 4 前沿模型，這次主攻「又長又硬的工程任務＋資安防禦全流程」：找漏洞、驗證可利用性、修到根因三段全拿當下最佳，長程 Agent 可連續跑數天咬住大型程式碼庫的疑難雜症。** 接續兩週前發布的 Gemini 4 Argon，官方定位為「我們最強的模型」；綜合指標 Artificial Analysis Intelligence Index v5.0 以 59 分居首；網頁開發 WebDev Arena 較 Argon 提升 89 Elo、以 1,768 分居第 4。內部團隊實測：生成安全程式碼的成功率較 Argon 提升超過 2 倍；Chrome 團隊稱其生成高品質修補的表現超過另一家實驗室的大型前沿模型 10 倍以上；Wiz 亦稱其在網頁滲透測試基準領先。
  * **解決痛點 / 推薦場景**：**解決了「資安防禦三段式工作長期斷鏈：找得到漏洞、驗不出能不能利用、修補只貼表面」的痛點。** 舊方法：三段各用不同工具與人力接力，驗證與修補最花時間、且修補常未觸及根因。甜點區：受信資安防禦團隊的漏洞發現、利用驗證與根因修補，以及需連續數天追蹤的大型程式碼庫除錯(官方稱內部團隊已見其跨數天、穿越死胡同持續推進的案例)。但注意取得門檻：本週起僅先開放給一小部分資安防禦者，再逐步擴大到 Fairwind Program 的受信夥伴(該計畫逾 650 個夥伴)；開發者、企業與一般消費者何時可用官方未給日期，僅稱在回饋與護欄迭代後盡快開放。Google 同時參與美國政府的自願性發布前模型測試流程。價格與 Argon 相同：入門價每百萬 token 輸入 2 美元、輸出 10 美元，快取輸入打 95 折；入門期結束後調為 4 美元／20 美元(入門期結束日未公布)。
  * **量化基準(皆 Google 官方自報，資安三項經官方註明為無護欄下評測，尚未有獨立複現)**：SEC-bench Pro(真實軟體中自主找複雜漏洞)88.2%；ExploitGym(把已揭露漏洞轉為可用 exploit 以驗證風險)54.8%；Collinear CWE-bench(修補到根因)71.0%，三項皆為當下最佳。對齊與誠實面(皆官方內部測試)：Terminal-Bench 4.0 作弊成功率降至 0.0%、作弊嘗試率 0.4%；即時編碼環境中高嚴重度不對齊警示減少近 80%；無根據主張較 Argon 約減半；過度越權減少 26%、服務不足減少 29%；Gray Swan 間接提示注入(IPI)基準攻擊成功率 0.0%(Argon 為 0.7%)。
  * **資源**：[🌐 Google DeepMind 官方部落格](https://deepmind.google/blog/gemini-4-carbon-our-next-frontier-model/)
  * **附註(未獨立查證)**：日期邊界特別說明：DeepMind 官方頁面僅標示 2026-10-28(美國日期)，未給精確時刻；次級追蹤站記載該頁發布時刻為 UTC 10-28 17:00、另有 20:03 的說法，換算台北時間皆為 10-29 凌晨約 01:00 至 04:03，落在台北 10 月 29 日窗口，故本日收錄，不提前歸入 10 月 28 日。閉源模型、無權重、無模型卡：查證時 Google 模型卡索引仍列 Argon、公告連結的安全報告亦為 Argon 的 10 月報告(次級報導 mlq.ai 指明)，Carbon 專屬卡片與報告尚未見到，條目不寫成已有。所有基準皆為 Google 自報，跨家數字宜打折看；Chrome「10 倍」與 Wiz 領先皆為官方引述的內部觀察，非公開可複現基準。

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
* **[Carbon-X (Hugging Face 開放 DNA 對話模型：14.8B／DNA＋文字單一解碼器)](https://huggingface.co/HuggingFaceBio/Carbon-X)** `[2026-10-22]` 🔥 `[DNA]` `[基因變異效應]` `[BioAI]` `[Apache 2.0]` `[6-mer tokenizer]`
  * **核心優勢**：**第一個能用日常語言跟 DNA 聊天的開源模型：14.8B decoder-only，從 Qwen3-14B 起手，DNA 與文字共用單一 token 流。** hybrid tokenizer：Qwen3 BPE＋5,515 DNA tokens（4,096 個 6-mer＋1,364 尾段 token＋`<dna></dna><oov>` 標記），DNA 自動偵測標記。302B tokens mid-training（DNA 55%＋英文 20%＋生物文本 15%＋指令 10%），再經 SFT＋兩輪非同步 GRPO（verifiable rewards）。五項 DNA 基準平均 66.7%（無思考模式），比起點 Qwen3-14B 高 27 個百分點、領先所有開源對比模型；逼近 GPT-6.1 Sol（67.5%），推論成本約 1/1,800。編碼區變異效應（BioReason Coding）74.9、下一個鹼基預測（NextBase）39.4 兩項領先全場。bf16 單張 80GB GPU（vLLM）可跑，基因敏感資料可留本地。
  * **解決痛點 / 推薦場景**：**解決了「基因資料敏感不能上雲、開源模型又看不懂 DNA」的痛點。** 舊方法：frontier API 模型分析 ClinVar 240 萬個未定變異估計 $32K–$4M，且病人基因資料得送出境；通用開源模型在 DNA 任務上幾乎隨機猜。甜點區：Apache 2.0 商用友善，適合**做變異效應判讀、基因功能註解的研究團隊**，以及**想把 DNA 能力包成 agent 工具的人**（官方附 Claude Code／Codex CLI 現成技能＋Inspect 整合）。
  * **資源**：[🤗 HF 模型卡](https://huggingface.co/HuggingFaceBio/Carbon-X) | [🚀 官方發布頁（訓練配方＋Space）](https://huggingface.co/spaces/HuggingFaceBio/Carbon-X-Release)
  * **附註（未獨立查證）**：五基準中 FrontierVEP、NextBase 為 HF 自建；模型卡明言**未經濕實驗室驗證、不可用於臨床決策**；會算錯鹼基座標、會虛構序列功能；splice site（29.8%）與 histone mark（34.6%）仍弱；長 DNA 生成品質退化；llama.cpp／GGUF 不支援（DNA tokenizer 為自訂 Python 程式碼）。

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

### 📈 專用預測基礎模型（時間序列）

* **[TimeH2O-v1 (H2O.ai)](https://huggingface.co/h2oai/timeh2o-v1)** `[2026-10-26]` 🔥 `[時間序列預測]` `[零樣本]` `[基礎模型]` `[非商業授權]` `[fev-bench]` `[機率預測]`
  * **核心優勢**：**第一個在 fev-bench 拿下第一名的 108M 參數時間序列基礎模型：不針對你的序列訓練，就能直接給出帶不確定性的預測。** 預測時只讀序列歷史，不做訓練或微調，權重不變；支援單變量與帶外生變量（價格、促銷、天氣等會影響序列的外部訊號）的序列，涵蓋金融、醫療、供應鏈、能源等領域。使用方式極輕：`pip install h2ofm` 後 `TimeH2O.from_pretrained("h2oai/timeh2o-v1")`，一次預測同時給中位數點預測與 0.1 至 0.9 共 9 檔分位數，方便直接做區間決策。
  * **解決痛點 / 推薦場景**：**解決了「每個序列各養一個模型、資料一漂移就得重訓」的預測老問題。** 舊方法：需求、庫存、現金流、能源負載、病患量各建專用模型，維護與重訓成本隨序列數量線性膨脹；新方案：一個預訓練好的通用預測模型零樣本上線，之後有需要再針對自家領域微調成專用版。fev-bench（100 個真實序列預測任務、與季節性 naive 基準比機率準確度）成績：勝率 91.9%、32 個模型中第一，技能分 50.8（預測誤差比基準低 50.8%），領先 Timestral-209M（89.6%）、t0-gamma（88.1%）、TimesFM-3 與 Chronos-2。極度適合**要快速上線多序列預測、又需要不確定性區間的團隊**，以及**想把預測餵給 Agent 當決策依據、而非只給點估計的場景**。
  * **資源**：[🤗 Hugging Face 模型（h2oai/timeh2o-v1）](https://huggingface.co/h2oai/timeh2o-v1) | [🌐 H2O.ai 官方新聞稿（BusinessWire，2026-10-26）](https://www.businesswire.com/news/home/20261026408387/en/H2O.ais-TimeH2O-Beats-Mistral-Google-and-Amazon-in-Time-Series-Forecasting)
  * **附註（未獨立查證）**：授權是關鍵差異，務必不要寫成開源模型：HF 模型卡明載 Non-commercial（非商業授權），僅允許內部基準測試，商業預測用途需洽 H2O.ai；新聞稿標題所稱 open-weight 指權重可取得，不等於可商用。時間點：新聞稿發布為 UTC 2026-10-26 15:29，換算台北時間 10-26 23:29，落在昨日窗口內；但 fev-bench 榜單快照日期為 10-23，早於正式發布，代表模型在正式發布前已上榜，榜單時間與發布時間不要混為同一天。所有成績為 H2O.ai 引用的榜單數字，未經獨立複現；訓練資料已排除與 fev-bench、GIFT-Eval、TIME 重疊的資料集，此說法取自 HF 模型卡，未獨立驗證。本檔既有章節無時間序列類別，故以「建議新增章節」方式放在 LLM 小節末，批次合併時再確認位置。

---

## Embedding
**🔎 Embedding & Reranker (向量嵌入與重排序模型)**

在構建 RAG 系統時，如果檢索到的參考資料不準，再強的 LLM 也會產生幻覺 (Hallucination)。目前業界的黃金標準是採用「雙層檢索架構」：先用 **Embedding** 模型進行海量初篩，再用 **Reranker** 模型進行精準的二次排序。以下精選目前最具代表性的表徵模型：

* [LEANN](https://github.com/yichuan-w/LEANN) [2026-03-09] 🔥 [低存儲向量索引]
  * **核心優勢**：**首創「基於圖的選擇性重計算 (Graph-based Selective Recomputation)」與高階節點保留剪枝，將 ANN 索引存儲開銷壓到原始資料的 5% 以下！** 該項發表於 MLSys 2026 的工作透過拋棄冗餘嵌入向量並利用壓縮稀疏行 (CSR) 格式，比標準 HNSW 索引縮小最高達 50 倍，同時在真實 QA 基準上維持 90% 的 top-3 召回率，搜尋延遲保持在 2 秒以內。
  * **解決痛點 / 描述**：傳統向量索引（如 HNSW、DiskANN）會帶來原始資料 1.5 到 7 倍的龐大存儲開銷，使個人設備與筆電難以執行本地端 RAG 與隱私保護資料檢索。LEANN 透過「搜尋時按需重算嵌入」與貼合 RAG 「LLM 生成主導」的延遲權衡，成功推倒「存儲之牆」，並支援 Apple Mail、瀏覽器歷史及 Claude Code MCP 等豐富的本地數據源。
  * **資源**：[📄 論文 (arXiv:2506.08276)](https://arxiv.org/abs/2506.08276) | [🐙 GitHub 專案](https://github.com/yichuan-w/LEANN) | [📄 MLSys 2026](https://doi.org/10.48550/arXiv.2506.08276)

* **[Kanana-2-Embedding(Kakao：韓語檢索專用雙模型，3B＋蒸餾 1.3B，MRL 可調維度)](https://biz.heraldcorp.com/article/10919060)** `[2026-10-29]` 🔥 `[韓語檢索]` `[Embedding]` `[開源權重]` `[MRL可調維度]` `[知識蒸餾]` `[個人化Agent檢索]`
  * **核心優勢**：**韓語 RAG 終於有同級開源檢索模型可用：Kakao 把自家個人化 Agent 的檢索底座一次開源兩顆，韓語同級最強、英語不掉隊，向量維度還能隨服務現場伸縮。** 兩款皆已上架 Hugging Face：Kanana-2-3B-Embedding(3B，由自家小型語言模型 Kanana-2-SLM 轉訓為檢索用途)與 Kanana-2-1.3B-Embedding(1.3B，由 3B 知識蒸餾而來)。兩款皆採用 Matryoshka Representation Learning(MRL)，向量維度可依服務的儲存空間與處理速度放大縮小，開發者不必為不同場景各建一套索引。定位是個人化 Agent 的檢索基礎技術：理解使用者提問意圖與過往對話脈絡，即使關鍵字不完全相同也能找回相關資訊。授權為 Kanana Open License，依授權條款允許商用與研發。
  * **解決痛點 / 推薦場景**：**解決了「韓語 RAG 檢索先天吃虧：西方通用 embedding 在韓語語意上不夠準，固定維度向量又逼你在儲存成本與檢索精度之間二選一」的痛點。** 舊方法：直接套用英文為主的通用 embedding，韓語查詢召回率偏低；或自建檢索模型，成本與資料門檻都高。甜點區：韓語個人化 Agent 與語意搜尋(客服、內容推薦、企業內部知識庫)、需要同時顧及儲存與速度的檢索服務(MRL 先低維粗篩、再高維精排的管線)。與同節既有的 Qwen3 Embedding(中文生態)互補，不重複。
  * **量化基準(Kakao 官方說法，查證時未見可引用的數字基準表，詳見附註)**：與同級開源模型(Meta llama-nemotron-embed-1b-v2、阿里 Qwen3-Embedding-4B)對比，兩款在韓語表現為同級最佳、英語表現與對手相當；推論效率高於 Qwen3-Embedding；相較上一代 Kanana embedding 系列，搜尋表現提升、記憶體用量與推論速度皆有數十倍以上的效率進步(官方說法，未給可核對的測試條件)。
  * **資源**：[📰 韓國先驅報報導(Herald Business，含 Kakao 官方效能圖)](https://biz.heraldcorp.com/article/10919060) | [📰 朝鮮日報英文報導](https://biz.chosun.com/en/en-it/2026/10/29/RCY64EEJIRD4XN4M3AQGDIT5XI/)
  * **附註(未獨立查證)**：日期以韓媒報導戳記為準：朝鮮日報刊出 2026-10-29 10:00(韓國時間)，換算台北時間同日 09:00，落在台北 10 月 29 日窗口；先驅報韓國時間戳記為 13:05，同日。基準誠實說明：本次查證多家韓媒報導皆只載定性結論(韓語最佳、英語相當、效率數十倍)，未見 MTEB 或韓語檢索基準的數字表，條目不編造分數；使用者若要精確數字，需等 Kakao 模型卡或技術報告公開後補。與台帳既有項目去重說明：2026-10-22 已上線的 Kanana-2-Vision Encoder 是視覺編碼器(426M／98M)，與本則文字檢索 embedding 為不同產品線，不算重複。Hugging Face 模型頁連結查證時未逐字回傳，故資源欄僅列已驗證的報導連結，模型名稱以報導所載為準(Kanana-2-3B-Embedding、Kanana-2-1.3B-Embedding)，批次合併時再補模型卡直連。

### 1. 網頁級巨量檢索與搜尋引擎架構 (Web-Scale Retrieval)
想要打造媲美 AI 搜尋引擎的檢索準確度？直接使用目前地表最強搜尋引擎團隊的底層技術。

* **[Jina Embeddings V5 Omni](https://huggingface.co/jinaai/jina-embeddings-v5-omni-small)** `[2026-05]` 🔥
  * **核心優勢**：**打破模態孤島的全模態向量化霸主，真正實現圖、文、音、影「大一統」且完全相容舊有文字索引！** 創新採用凍結文字主幹、僅訓練 0.35% 輕量跨模態投影層的黑科技。它不僅單一模型就能原生支援四種模態的混合編碼（如：一句話+一張圖生成單一向量），更做到與前代 `v5-text` 逐位一致 (bit-identical)，讓老用戶升級時**完全免重建龐大的向量資料庫**。
  * **解決痛點 / 推薦場景**：**完美解決傳統多模態 RAG 系統必須同時維護 CLIP (處理圖片) 與 Text Embedding 兩套獨立編碼器及向量空間的致命痛點，大幅降低硬體與維運成本。** 內建 4 種任務 LoRA 適配器（檢索、分類、聚類、匹配），並支援 MRL (Matryoshka) 動態降維技術，允許開發者實作「低維粗篩 → 高維精排」的極致省流管線。是打造**企業級全模態 RAG 知識庫**、**電商跨模態搜圖/搜片系統**，以及支援高併發 **vLLM 部署**的工業級大腦。
  * **資源**：[🐙 HuggingFace 模型權重](https://huggingface.co/jinaai/jina-embeddings-v5-omni-small) | [📄 arXiv 官方論文]()
  `[全模態向量化]` `[免重建索引]` `[Matryoshka降維]` `[vLLM原生支援]`

* **[pplx-embed-v1 系列 (Perplexity 出品)](https://research.perplexity.ai/articles/pplx-embed-state-of-the-art-embedding-models-for-web-scale-retrieval)** `[2026-02-28]`
  * **核心優勢**：Perplexity AI 官方釋出的尖端文本嵌入模型。包含 `pplx-embed-v1` 與 `pplx-embed-context-v1`。
  * **解決痛點**：專為「真實世界、充滿雜訊的 Web 級別檢索任務」所最佳化。如果您需要處理極度龐大、非結構化的網路抓取資料，這是目前最推薦的 RAG 檢索底座。[🤗 HuggingFace 權重](https://huggingface.co/collections/perplexity-ai/pplx-embed)

### 2. 中文生態系與私有化開源首選 (Chinese & Open Source)
針對繁簡中文語意理解優化，適合需要將資料留在本地端（Data Privacy）的企業內部知識庫。

* **[jina-reranker-v3.5](https://huggingface.co/jinaai/jina-reranker-v3.5)** `[2026-07]` 🔥 `[0.6B極致輕量]` `[3L2G混合注意力]` `[結構化數據理解]` `[長列表顯存優化]` `[垂直領域增強]`
  * **核心優勢**：**打破 0.6B 小模型性能天花板，Jina AI 推出以「3L2G 混合注意力架構」與三階段自蒸餾徹底重構的列表式（Listwise）重排序神作！** 論文（arXiv:2607.18152）指出其延續 LBNL 一次前向傳播整批文件的特性，將局部滑動窗口（w=1024）與週期性全局注意力結合，使長列表計算複雜度降至線性級 $O(L \cdot w)$，支援 131K 超長上下文，在長文本場景推理速度狂飆 56%。搭配 Struct-IR 數據擾動與 EUR-Lex/AILA 等權威庫補強，在 BEIR 基準拿下 63.20 (nDCG@10) 越級擊敗 7 倍參數量的 Qwen3-Reranker-4B（62.28）；結構化數據理解（Struct-IR）暴漲 24.8%，法律檢索（AILA）指標大幅飆升 11–14 個點。
  * **解決痛點 / 推薦場景**：**完美解決了傳統 Reranker 面對「長列表全注意力導致顯存爆炸與延遲失控」、「垂直領域（法律/金融/醫療）語言模式特殊導致排序失效」，以及「不懂 JSON 與表格中價格/規格等數值邏輯約束」的三大工業落地致命痛點。** 原生支援 Jina API、Elasticsearch EIS 託管調用，並提供 Docker 一鍵私有化部署與 CC BY-NC 4.0 開源權重。極度適合**企業級 RAG 知識庫長列表精準二階段重排**、**電商/履歷等帶有強數值約束的結構化多條件搜尋**，以及**法律合規與金融醫療垂直檢索管線**。
  * **資源**：[🤗 Hugging Face 模型合集](https://huggingface.co/jinaai/jina-reranker-v3.5) | [📄 技術報告 (arXiv:2607.18152)](https://arxiv.org/abs/2607.18152) | [💻 Jina AI API](https://jina.ai/reranker/) | [🧙 魔搭 ModelScope](https://modelscope.cn/models/jinaai/jina-reranker-v3.5)

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

* **[Audio Flamingo Next (AF-Next)](https://github.com/NVIDIA/audio-flamingo)** `[2026-04-13]` 🔥
  * **核心優勢**：**NVIDIA 次世代全開源語音大模型，首創「時間錨定推理鏈 (Temporal Audio CoT)」。** 採用 Qwen-2.5-7B 為語言骨幹，透過百萬小時網際網路規模數據訓練。其最大創舉是捨棄傳統 RoPE，改用 **RoTE (旋轉時間嵌入)** 來直接建模音訊時間語意，將上下文一舉擴展至 128K。在長音訊理解與多模態推理指標上，強勢擊敗 Gemini-2.5-Pro 與 Phi-4-mm。
  * **解決痛點 / 推薦場景**：**徹底終結傳統模型「無法跨時間段聚合證據」與「長音訊泛化力差」的痛點。** 官方貼心釋出三大特化變體：**Instruct** (適合通用對話 QA)、**Think** (適合高難度音訊邏輯推理，能精準給出推理時間戳) 以及 **Captioner** (適合精細字幕與長摘要)。是企業建構 Podcast 深度分析系統、智慧會議大腦、與複雜音樂/聲學事件理解 Agent 的最強開源底座。
  * **資源**：[🐙 GitHub](https://github.com/NVIDIA/audio-flamingo) | [📄 論文](https://arxiv.org/abs/2604.10905) | [🌐 專案主頁](https://afnext-umd-nvidia.github.io/) | [🤗 HF 權重 (Instruct版)](https://huggingface.co/nvidia/audio-flamingo-next-hf)
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
**👁️ Vision-Language Model (視覺多模態大模型)**

視覺大模型 (VLM) 正在從龐大的雲端叢林，逐步走向邊緣運算 (Edge AI) 與行動裝置。

* **[Seed1.5-VL (ByteDance)](https://github.com/ByteDance-Seed/Seed1.5-VL)** `[2025-05-20]`
  * **解決痛點**：具有視覺增強多模態能力的高階語言模型。在處理複雜圖表、多圖對比等高難度視覺推理任務上表現優異。[📄 AlphaXiv 論文](https://www.alphaxiv.org/zh/overview/2505.07062) | [📝 知乎解讀](https://zhuanlan.zhihu.com/p/1905914968433497765)
* **[nanoVLM (HuggingFace)](https://deepwiki.com/huggingface/nanoVLM)** `[2025-05-12]`
  * **解決痛點**：解決 VLM 難以在端側部署的痛點。專為邊緣運算與 IoT 裝置設計的微型視覺模型，具備極低的運算資源門檻。

---

## Multimodal
**🌌 多模態大模型與語音硬體終端 (Multimodal & Edge AI)**

> 2025 至 2026 年，大語言模型正式長出「眼睛」與「嘴巴」。本區塊不僅收錄了能看懂複雜圖表的多模態基礎模型 (Vision-Language Models)，更為創客與物聯網 (IoT) 開發者整理了最齊全的語音硬體開源解決方案。
>
> 隨著模型能力的進化，單一模態（純文字、純視覺）已無法滿足複雜的應用場景。新一代的基礎大模型原生支援視覺、語音與工具呼叫，是開發自動化 AI Agent 的核心大腦。

### 1. 頂尖多模態與視覺推理 (Vision & Complex Parsing)
需要讓 AI 看懂工程圖紙、財報表格或進行深度邏輯推理？這些是目前的開源王者：

* **[Qwen3.5-Omni](https://modelscope.cn/studios/Qwen/Qwen3.5-Omni-Demo)** `[2026-04]` 🔥
  * **核心優勢**：**首款實現「視聽直覺編程」的原生全模態統一體**。採用 Hybrid Attention MoE 架構，支援 256k 超長上下文，能一次吞下 10 小時音訊或 400 秒影片。
  * **解決痛點 / 推薦場景**：打破了傳統 Agent 「只能看文字」或「音畫不同步」的限制。模型能邊看影片邊聽需求，直接寫出對應的自動化程式碼，是開發**工業級多模態自主代理程式**的首選。
  * **資源**：[🐙 ModelScope](https://modelscope.cn/studios/Qwen/Qwen3.5-Omni-Demo) | [📄 論文](https://arxiv.org/abs/2604.15804v1) | [📝 官方解讀](https://arxiv.org/abs/2604.15804v1)

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

* **[LiteRT-LM](https://github.com/google-ai-edge/LiteRT-LM)** `[2026-04]` 🔥 `[Google端側編排層]` `[跨平台LLM Runtime]` `[MTP解碼加速]` `[WebGPU/NPU支援]` `[多模態輸入]`
  * **核心優勢**：**打破單機極限與平台碎片化，Google 正式開源經 Chrome 與 Pixel 產品線規模化驗證的端側 LLM 生產級編排層！** 基於 LiteRT（前身 TensorFlow Lite）深度打造，作為統一調度 CPU / GPU / NPU 的 Runtime Orchestrator。系統採用專用 `.litertlm` 格式，結合 XNNPACK、MLDrift kernel 與先進量化（Gemma 4 E2B 靠權重快取在 Apple CPU 上實體記憶體佔用僅 607MB）；更透過 MTP drafter 與主模型共享硬體 IP 執行推測解碼，在 S26 Ultra 上解碼速度達 52 tok/s（加速最高 2.2 倍），WebGPU（M4 Max）達 76 tok/s。原生支援視覺與音訊多模態、OpenAI 風格的 Function Calling 與約束解碼（Constrained Decoding）防止 JSON 解析崩潰，並提供 Python、Kotlin、C++、Swift 及 Web JS 全平台語言綁定。
  * **解決痛點 / 推薦場景**：完美解決了企業在開發端側 AI 時「同一個模型需為 Android、iOS、瀏覽器 Web 與物聯網樹莓派各自養一支推理工程隊伍維護」、以及「端側小模型多模態與工具調用生態零散」的架構痛點。 克服了以往純推理引擎缺乏生產級編排與約束解碼的限制。極度適合**需將單一模型一次部署至手機 (Android/iOS)、瀏覽器 (WebGPU)、桌面及嵌入式 IoT (如 Raspberry Pi 5) 的跨平台邊緣 AI 應用**、**對資料隱私有嚴格要求的端側多模態離線推論**，以及**打造低延遲端側 Agent 工具調用與結構化輸出管線**。
  * **資源**：[🐙 GitHub 官方倉庫](https://github.com/google-ai-edge/LiteRT-LM) | [🌐 產品官方首頁](https://ai.google.dev/edge/litert-lm) | [🤗 HuggingFace 社群預轉模型庫](https://huggingface.co/litert-community) | [📝 MTP 與跨平台技術部落格](https://ai.google.dev/edge/litert-lm/blog/blazing-fast)

* **[Mistral Small 3.1](https://huggingface.co/mistralai/Mistral-Small-3.1-24B-Instruct-2503)** `[2025-03-18]`
  * **核心優勢**：歐洲 AI 巨頭的逆襲！具備 128K 超長上下文，在 24B 的輕量級體積下，各項基準測試效能直接碾壓 GPT-4o Mini，是性價比極高的商用 API 替代品。
* **[Phi-4 Family (Microsoft)](https://huggingface.co/collections/microsoft/phi-4-677e9380e514feb5577a40e4)** `[2025-02-27 更新]`
  * **核心優勢**：「小身材大智慧」的代名詞。最新的 Phi-4 Multimodal 版本以僅 56 億的參數規模，在多項任務中展現越級打怪的實力，是微軟在端側 AI 佈局的核心武器。[📝 效能評測](https://zhuanlan.zhihu.com/p/26984226500)
* **[MiniCPM 家族 (面壁智能)](https://github.com/OpenBMB)** `[2025-01-16 更新]`
  * **核心優勢**：端側開源模型的驕傲！最新發布的 MiniCPM-o 2.6 與 3.0 版本，不僅支援 Ollama 一鍵部署，更是少數能真正在手機端流暢運行並具備優秀視覺能力 (MiniCPM-V) 的模型。[📝 魔改教學](https://mp.weixin.qq.com/s/DjDznmtKZoJNKXYz0X4zog)

* **[AirLLM](https://github.com/lyogavin/airllm)** `[2023]` 🔥 `[分層推理Layer-wise]` `[4GB顯存跑70B]` `[零精度損失]` `[端側大模型推理]` `[mmap按需載入]`
  * **核心優勢**：**打破大模型顯存硬體高牆，首創「分層推理（Layer-wise Inference）」讓 4GB 消費級顯卡即可運行 70B 全精度大模型！** 在不做量化、蒸餾或剪枝的前提下聲稱模型效能零損失，將多層 Transformer 切分為磁碟分片（Layer Shards），推論時依序「載入第 1 層 ➔ 計算 ➔ 從顯存釋放」。70B 模型單層參數約 1.6GB 加上約 30MB KV 快取，全程顯存佔用控制在 4GB 以內；結合 Flash Attention 與記憶體映射檔案（mmap）優化 I/O 與 CUDA 記憶體存取，最高支援在 8GB 顯存跑 405B Llama 3.1、12GB 顯存跑 671B DeepSeek-V3。提供與 Hugging Face Transformers 一致的簡潔呼叫介面。
  * **解決痛點 / 推薦場景**：完美解決了個人開發者與小團隊「沒有雙 A100 GPU 叢集，完全無法在本地端運行 70B 乃至 671B 旗艦大模型」以及「依賴雲端 API 造成機密資料外流」的致命痛點。 本質上以時間換取空間（NVMe SSD 上推理速度約 1–3 tokens/sec），大幅降低 70B 級別模型的落地門檻。極度適合**個人開發者在單卡遊戲卡或筆電顯卡上進行離線研究與測試**、**小團隊低成本驗證 70B 量級實驗**，以及**重視隱私、無需高頻即時互動的本機批次推理場景**。
  * **資源**：[🐙 GitHub 官方倉庫](https://github.com/lyogavin/airllm) | [📦 PyPI 套件](https://pypi.org/project/airllm) | [📄 相關經典論文 FlexGen (ICML 2023)](https://arxiv.org/abs/2303.06865) | [📝 BAAI 技術介紹](https://hub.baai.ac.cn/view/33278)

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


---

## FAQ
**❓ LLM 開發常見問題解答 (FAQ)**

**Q1: 企業應如何選擇合適的微調工具？**
A: 建議首選 LLaMA Factory，其可視化介面能減少 50% 環境配置時間，並廣泛支援主流開源模型與訓練演算法。

**Q2: 解決模型幻覺最有效的方法是什麼？**
A: 結合 RAG (檢索增強生成) 技術，導入外部驗證過的向量知識庫，實測可將企業內部問答的錯誤率壓低至 15% 以下。

**Q3: 該使用雲端 API 還是地端部署開源模型？**
A: 具備高度機密數據（如醫療、金融）建議採用地端 SLM (7B-14B)，其餘超過 80% 的通用業務則使用雲端 API 成本最低。

**Q4: AI Agent 框架哪個最適合新手？**
A: Dify 提供直觀的拖曳式工作流，無須寫程式即可串接 API，是目前降低非工程師開發門檻 60% 的最佳入門選擇。

**Q5: 評估模型效能需要看哪些指標？**
A: 勿僅看跑分基準，應自建 100-200 筆符合企業真實情境的測試集，並關注 Token 生成速度 (TPS) 以確保使用體驗。

**Q6: 開源 LLM 該怎麼選？**
A: 先看場景：中文 RAG 優先 Qwen3，需要地端部署與可控性選 Llama 3.3，預算與速度優先則考慮 Gemini Flash 這類託管 API。細節見本頁上方快速選型結論。

**Q7: RAG 場景選哪個模型？**
A: Embedding 與 Reranker 的影響往往大於生成模型本身。中文場景建議 Qwen3-Embedding 搭配 Qwen3-Reranker，生成端再依延遲與成本需求挑選。

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "TechArticle",
      "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "https://deep-learning-101.github.io/Large-Language-Model"
      },
      "headline": "2026 大語言模型 (LLM) 與 AI Agent 開源資源選型指南",
      "description": "2026 最強大語言模型與 AI Agent 開發指南。彙整 RAG 防幻覺實作、vLLM 推理框架選型、SLM 端側小模型與 LLaMA Factory 零程式碼微調資源。",
      "image": "https://raw.githubusercontent.com/Deep-Learning-101/TonTon/refs/heads/main/_includes/DL101-Logo.jpg",
      "author": {
        "@type": "Person",
        "name": "TonTon Huang Ph.D.",
        "url": "https://twman.org/"
      },
      "publisher": {
        "@type": "Organization",
        "name": "Deep Learning 101, Taiwan",
        "url": "https://deep-learning-101.github.io/"
      },
      "datePublished": "2026-03-29",
      "dateModified": "2026-07-28"
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "地端部署 8B LLM，該如何選擇推論框架以節省 VRAM？",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "針對中小型企業併發需求，選用具備 PagedAttention 技術的 vLLM 或 SGLang 推論框架，能將 8B 模型記憶體需求精準控制在單張 24GB 顯卡，大幅降低硬體採購成本。"
          }
        },
        {
          "@type": "Question",
          "name": "企業地端微調 (Fine-tuning) 開源大模型有哪些推薦工具？",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "推薦採用 LLaMA Factory 或 Unsloth 等零程式碼/高效能微調工具，結合 LoRA 或 QLoRA 技術，能以極低的算力成本完成特定業務語境的模型對齊。"
          }
        }
      ]
    }
  ]
}
</script>