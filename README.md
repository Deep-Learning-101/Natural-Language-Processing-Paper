#
https://www.twman.org/AI/NLP

https://huggingface.co/DeepLearning101
#

---

<details>
<summary>手把手帶你一起踩 AI 坑</summary>

<h3><a href="https://blog.twman.org/p/deeplearning101.html" target="_blank">手把手帶你一起踩 AI 坑</a>：<a href="https://www.twman.org/AI" target="_blank">https://www.twman.org/AI</a></h3>

<ul>
  <li>
    <b><a href="https://blog.twman.org/2025/03/AIAgent.html" target="_blank">避開 AI Agent 開發陷阱：常見問題、挑戰與解決方案</a></b>：<a href="https://deep-learning-101.github.io/agent" target="_blank">探討多種 AI 代理人工具的應用經驗與挑戰，分享實用經驗與工具推薦。</a>
  </li>
  <li>
    <b><a href="https://blog.twman.org/2024/08/LLM.html" target="_blank">白話文手把手帶你科普 GenAI</a></b>：<a href="https://deep-learning-101.github.io/GenAI" target="_blank">淺顯介紹生成式人工智慧核心概念，強調硬體資源和數據的重要性。</a>
  </li>
  <li>
    <b><a href="https://blog.twman.org/2024/09/LLM.html" target="_blank">大型語言模型直接就打完收工？</a></b>：<a href="https://deep-learning-101.github.io/1010LLM" target="_blank">回顧 LLM 領域探索歷程，討論硬體升級對 AI 開發的重要性。</a>
  </li>
  <li>
    <b><a href="https://blog.twman.org/2024/07/RAG.html" target="_blank">檢索增強生成(RAG)不是萬靈丹之優化挑戰技巧</a></b>：<a href="https://deep-learning-101.github.io/RAG" target="_blank">探討 RAG 技術應用與挑戰，提供實用經驗分享和工具建議。</a>
  </li>
  <li>
    <b><a href="https://blog.twman.org/2024/02/LLM.html" target="_blank">大型語言模型 (LLM) 入門完整指南：原理、應用與未來</a></b>：<a href="https://deep-learning-101.github.io/0204LLM" target="_blank">探討多種 LLM 工具的應用與挑戰，強調硬體資源的重要性。</a>
  </li>
  <li>
    <b><a href="https://blog.twman.org/2023/04/GPT.html" target="_blank">解析探索大型語言模型：模型發展歷史、訓練及微調技術的 VRAM 估算</a></b>：<a href="https://deep-learning-101.github.io/GPU" target="_blank">探討 LLM 的發展與應用，強調硬體資源在開發中的關鍵作用。</a>
  </li>
  <li>
    <b><a href="https://blog.twman.org/2024/11/diffusion.html" target="_blank">Diffusion Model 完全解析：從原理、應用到實作 (AI 圖像生成)</a></b>；<a href="https://deep-learning-101.github.io/diffusion" target="_blank">深入探討影像生成與分割技術的應用，強調硬體資源的重要性。</a>
  </li>
  <li>
    <b><a href="https://blog.twman.org/2024/02/asr-tts.html" target="_blank">ASR/TTS 開發避坑指南：語音辨識與合成的常見挑戰與對策</a></b>：<a href="https://deep-learning-101.github.io/asr-tts" target="_blank">探討 ASR 和 TTS 技術應用中的問題，強調數據質量的重要性。</a>
  </li>
  <li>
    <b><a href="https://blog.twman.org/2021/04/NLP.html" target="_blank">那些 NLP 踩的坑</a></b>：<a href="https://deep-learning-101.github.io/nlp" target="_blank">分享 NLP 領域的實踐經驗，強調數據質量對模型效果的影響。</a>
  </li>
  <li>
    <b><a href="https://blog.twman.org/2021/04/ASR.html" target="_blank">那些語音處理踩的坑</a></b>：<a href="https://deep-learning-101.github.io/speech" target="_blank">分享語音處理領域的實務經驗，強調資料品質對模型效果的影響。</a>
  </li>
  <li>
    <b><a href="https://blog.twman.org/2020/05/DeepLearning.html" target="_blank">手把手學深度學習安裝環境</a></b>：<a href="https://deep-learning-101.github.io/101" target="_blank">詳細介紹在 Ubuntu 上安裝深度學習環境的步驟，分享實際操作經驗。</a>
  </li>
</ul>

</details>

---

# Natural Language Processing (NLP)

<details close> 
   
<summary>自然語言處理</summary>

### ** 2018/07/15-2020/02/29 開發心得：**

自然語言處理（英語：Natural Language Processing，縮寫作 NLP）是人工智慧和語言學領域的分支學科。此領域探討如何處理及運用自然語言；自然語言處理包括多方面和步驟，基本有認知、理解、生成等部分。 自然語言認知和理解是讓電腦把輸入的語言變成有意思的符號和關係，然後根據目的再處理。自然語言生成系統則是把計算機數據轉化為自然語言。最後，放眼望去想入門 Attention、Transformer、Bert 和 李宏毅老師的教學影片等，絕對不能錯過。
雖然分享這些踩過的坑還有免費DEMO跟API其實我想不到有啥好處，但至少不用為了要營利而去亂喊口號也更不用畫大餅，能做多少就是說多少；如同搞 Deep Learning 101 搞那麼久，搬桌椅、直播場佈其實比想像中麻煩，只希望讓想投入的知道 AI 這個坑其實很深，多分享總是比較好 ! 

[Transformer - Attention is all you need](https://zhuanlan.zhihu.com/p/311156298)

[這麼多年，終於有人講清楚Transformer了](https://mp.weixin.qq.com/s/SJXxeTsqn9RoaVu66MISXQ)

[我從零實現了Transformer模型，把代碼講給你聽](https://zhuanlan.zhihu.com/p/411311520)

[Attention 機制](https://easyai.tech/ai-definition/attention/)

[超詳細圖解Self-Attention](https://zhuanlan.zhihu.com/p/410776234)

[NLP Course @ HuggingFace](https://huggingface.co/learn/nlp-course/zh-TW/chapter1/1)

關於自然語言處理，如果你在臺灣，那你第一時間應該會想到俗稱Chatbot的聊天機器人 (就是要人工維運關鍵字跟正規表示式的機器人)吧？從最早的中英文的情感分析，陸續接觸過文本糾錯(校正)、文本分類、文本相似度、命名實體識別、文本摘要、機器閱讀理解等，當然自然語言處理其實博大精深，還有像是分詞、詞性標註、句法分析、語言生成等，傳說中的知識圖譜 (Ontology？) 更是大魔王了；這邊僅先匯整接觸過的做說明，當然在深度學習還未爆紅前，已經有非常多的演算法，未來也盡量針對各個項目與領域持續更新簡單介紹，就當近幾次專題演講的摘要，也算是這幾年跟小夥伴們奮鬥NLP充滿血與淚的回憶；另外，根據經驗，論文當然要追，更要實作跟實驗，但算法模型其實效果已經都差不多，如果你想將算法實際落地，別懷疑，請好好的處理你的數據，這會是蠻關鍵的地方。另外，你一定也要知道 BERT家族，早在2018年11月，Google 大神釋出 BERT 後，就差不多屌打各種自然語言處理應用 (在這之前，你想搞自然語言處理，勢必用到騰訊所開源需要16GB記憶體的Tencent_ChineseEmbedding)，再後來還有像 transformer 跟 huggingface，所以你一定要花點時間瞭解；當然，如果你真的沒太多時間投入去換跟處理數據然後重新訓練，那歡迎聯絡一下，用我們還持續迭代開發的臺灣深度大師啦，不然公開數據都是對岸用語或簡體跟英文還要擠GPU計算資源，你會很頭痛 ! 對啦，你也可以試試 NVIDIA GTC 2021 介紹的Javis等對話式AI等東西，但我想你還是會覺得不容易上手就是，除非你想自己從頭硬幹去瘋狂的標註適合自己場景的數據，然後瞭解怎樣重新訓練模型。

<details close>
   
<summary>Information/Event Extraction (資訊/事件擷取)</summary>
     
  - [HugNLP](https://github.com/Deep-Learning-101/Natural-Language-Processing-Paper/blob/main/HugNLP.md)
     - [Jianing Wang, Nuo Chen, Qiushi Sun, Wenkang Huang, Chengyu Wang, Ming Gao, "HugNLP: A Unified and Comprehensive Library for Natural Language Processing", arXiv preprint, 	arXiv:2302.14286, 2023](./HugNLP.md)
     - [基於機器閱讀理解(MRC)的指令微調(Instruction-tuning)的統一信息抽取框架之診斷書醫囑擷取分析](https://blog.twman.org/2023/07/HugIE.html)
  - [DeepKE](https://github.com/Deep-Learning-101/Natural-Language-Processing-Paper/blob/main/DeepKE.md)
     - [Ningyu Zhang, Xin Xu, Liankuan Tao, Haiyang Yu, Hongbin Ye, Shuofei Qiao, Xin Xie, Xiang Chen, Zhoubo Li, Lei Li, Xiaozhuan Liang, Yunzhi Yao, Shumin Deng, Peng Wang, Wen Zhang, Zhenru Zhang, Chuanqi Tan, Qiang Chen, Feiyu Xiong, Fei Huang, Guozhou Zheng, Huajun Chen, "DeepKE: A Deep Learning Based Knowledge Extraction Toolkit for Knowledge Base Population", arXiv preprint, arXiv:2201.03335, 2022](./DeepKE.md)
     - [基於深度學習的開源中文知識圖譜抽取框架](https://github.com/zjunlp/DeepKE/blob/main/README_CN.md)
     - [DeepKE-LLM: A Large Language Model Based Knowledge Extraction Toolkit](https://github.com/zjunlp/DeepKE/blob/main/example/llm/README_CN.md)
     - [知識增強的開源語言大模型框架](https://github.com/zjunlp/KnowLM/blob/main/README_ZH.md)
  - [ERINE-Layout](https://github.com/Deep-Learning-101/Natural-Language-Processing-Paper/blob/main/ERNIE-Layout.md)
     - [Qiming Peng, Yinxu Pan, Wenjin Wang, Bin Luo, Zhenyu Zhang, Zhengjie Huang, Teng Hu, Weichong Yin, Yongfeng Chen, Yin Zhang, Shikun Feng, Yu Sun, Hao Tian, Hua Wu, Haifeng Wang, "ERNIE-Layout: Layout Knowledge Enhanced Pre-training for Visually-rich Document Understanding", arXiv preprint, arXiv:2210.06155, 2022](./ERNIE-Layout.md)
  - [UIE @ PaddleNLP](https://huggingface.co/spaces/DeepLearning101/PaddleNLP-UIE)
    - https://github.com/PaddlePaddle/PaddleNLP/tree/develop/model_zoo/uie
</details>

<details close>
   
### ** 2018/10/15-2019/02/10 開發心得：**
投入約120天，早期想上線需要不少計算資源 (沒有昂貴的GPU想上線簡直是難如登天，好險時代在進步，現在CPU就能搞定)。記得我2018從老闆口中第一次聽到新項目是機器閱讀理解時，一頭霧水不知道是在幹麼，Google後突然發現這還真是它X的超級難的東西，而當時落地場景是要解決機器人在博物館或者展場的Q&A，不想再預先建一堆關鍵字與正規表示式來幫相似度和分類做前處理。
但機器閱讀理解坑真的不小，首先當然是數據，公開數據有SQuAD 1.0和2.0，但這是英文，你想用在中文 ? 你可以自己試試啦，再來有了個中文的CMRC，但用得是對岸用語跟簡體中文，而且數據格式不太一樣；後來台達電放出了DRCD還有科技部辦的科技大擂台，依然有格式不同的問題，數據量真的不太夠，所以想要落地你真的得要自己標註。
為了解決像是多文章還有問非文章內問題，還有公開數據要嘛英文不然就是簡體中文或對岸用語，然後本地化用語的數據實在不足的狀況，小夥伴們真的很給力，我們也用機器翻譯SQuAD 1.0和2.0還有自己手工爬維基百科跟開發了數據標註系統自己標註 ! 不得不說小夥伴們真的是投入超多精神在機器閱讀理解，更在Deep Learning 101做了分享。

  <summary>Machine Reading Comprehension (機器閱讀理解)</summary>

  - [中文機器閱讀理解](https://www.twman.org/AI/NLP/MRC)
    - [機器閱讀理解綜述(一)](https://zhuanlan.zhihu.com/p/80905984)
    - [機器閱讀理解綜述(二)](https://zhuanlan.zhihu.com/p/80980403)
    - [機器閱讀理解綜述(三)](https://zhuanlan.zhihu.com/p/81126870)
    - [機器閱讀理解探索與實踐](https://zhuanlan.zhihu.com/p/109309164)
    - [什麼是機器閱讀理解？跟自然語言處理有什麼關係？](https://communeit.medium.com/%E4%BB%80%E9%BA%BC%E6%98%AF%E6%A9%9F%E5%99%A8%E9%96%B1%E8%AE%80%E7%90%86%E8%A7%A3-%E8%B7%9F%E8%87%AA%E7%84%B6%E8%AA%9E%E8%A8%80%E8%99%95%E7%90%86%E6%9C%89%E4%BB%80%E9%BA%BC%E9%97%9C%E4%BF%82-b02fb6ccb6e9)
</details>

<details close>
   
### ** 2019/12/02-2020/02/29 開發心得：**
記得前後兩次陸續投入總計約100天。或許有人會發現為何在分享這幾篇自然語言會強調中文數據？最好理解的說法就是中文是基於字表示再加上中文斷詞的效果，比起每個單詞只需空格來表示的英文硬是麻煩點。命名實體識別 (Named Entity Recognition, NER) 是指將語句中的元素分成預先定義的類別 (開放域來說包括實體、時間和數字3個大類，人名、地名、組織名、機構名、時間、日期、數量和名字等7個小類，特定領域就像是藥名、疾病等類別)。要應用在那方面？像是關係抽取、對話意圖理解、輿情分析、對話NLU任務等等都用得上，更廣義的就屬填槽 (Slot-Filling) 了。
最早 (2019/08時) 我們需處理的場景是針對電話助理的對話內容 (就是APP幫你接電話跟對方對話) 在語音識別後跟語音合成前的處理，印像中沒做到非常深入；後來剛好招聘到熟悉NER這部份的小夥伴們，剛好一直想把聊天對話做個流程處理 (多輪對話的概念) ，就再花了點時間當做上手，因為不想依賴大量關鍵字和正規表示式做前處理，中間試了不少數據集，還做了像是用拼音、注音等，或者品牌定義等超多的實驗，甚至還一度想硬整合 RASA 等等的開源套件，也嘗試用了 "改寫" 來修正對話內容，去識別出語句中的重點字。至於這個的數據標據就真的更累人，意外找到一個蠻好用的標註系統 ChineseAnnotator，然後我們就瘋狂開始標註 !

  <summary>Named Entity Recognition (命名實體識別)</summary>

  - [中文命名實體識別](https://www.twman.org/AI/NLP/NER)

</details>

<details close>

### ** 2019/11/20-2020/02/29 開發心得：**
投入約100天，早期上線成本資源頗高，現在就沒這問題；這個項目堪稱是在NLP這個坑裡投入第二多的，記得當時的場景是機器人在商場裡回答問題所顯示出來的文字會有一些ASR的錯字，但是問題一樣卡在數據集，還因此讓小夥伴們花了好長時間辛苦去標註 XD，但看看現在效果，我想這是值得的 ! 記得一開始是先依賴 pycorrector，然後再換 ConvSeq2Seq，當然 bert 也做了相關優化實驗，中間一度被那三番二次很愛嗆我多讀書，從RD轉職覺得自己很懂做產品的PM拿跟百度對幹，從一開始的看實驗結果輸，到後來贏了，卻又自己亂測說還是不夠好之類的叭啦叭啦，說實話，你最後不也人設垮了然後閃人 ~ 攤手 ~ 
現在看看這截圖效果，不是蠻勵害的嗎 ? 真的想說這社會真的充滿一堆人設嚇死人的人，無敵愛嘴砲 ! 搞的為了滿足那位人設比天高的需求，真的是想了像是用拼音還兼NER來整合的好幾種方法 ! 那文本糾錯會有什麼坑呢？：數據啊、格式啊 !!! 還有幾個套件所要處理的目標不太一樣，有的可以處理疊字有的可以處理連錯三個字，還有最麻煩的就是斷字了，因為現有公開大家最愛用的仍舊是Jieba，即便它是有繁中版，當然也能試試 pkuseg，但就是差了點感覺。

  <summary>Correction (糾錯)</summary>

  - [中文文本糾錯](https://www.twman.org/AI/NLP/Correction)

</details>

<details close>

### ** 2019/11/10-2019/12/10 開發心得：**
最早我們是透過 Hierarchical Attention Networks for Document Classification (HAN) 的實作，來修正並且以自有數據進行訓練；但是這都需要使用到騰訊放出來的近16 GB 的 embedding：Tencent_AILab_ChineseEmbedding_20190926.txt，如果做推論，這會是個非常龐大需載入的檔案，直到後來 Huggingface 橫空出世，解決了 bert 剛出來時，很難將其當做推論時做 embedding 的 service (最早出現的是 bert-as-service)；同時再接上 BiLSTM 跟 Attention。CPU (Macbook pro)：平均速度：約 0.1 sec/sample，總記憶體消耗：約 954 MB (以 BiLSTM + Attention 為使用模型)。
引用 Huggingface transformers 套件 bert-base-chinese 模型作為模型 word2vec (embedding) 取代騰訊 pre-trained embedding
優點：API 上線時無須保留龐大的 Embedding 辭典,避免消耗大量記憶體空間，但BERT 相較於傳統辭典法能更有效處理同詞異義情況，更簡單且明確的使用 BERT 或其他 Transformers-based 模型
缺點：Embedding後的結果不可控制，BERT Embedding 維度較大,在某些情況下可能造成麻煩

  <summary>Classification (分類)</summary>

  - [中文文本分類](https://www.twman.org/AI/NLP/Classification)

  </details>

  <details close>

### ** 2019/10/15-2019/11/30 開發心得：**
投入約45天，那時剛好遇到 albert，但最後還是被蒸溜給幹掉；會做文本相似度主要是要解決當機器人收到ASR識別後的問句，在進到關鍵字或正規表示式甚至閱讀理解前，藉由80/20從已存在的Q&A比對，然後直接解答；簡單來說就是直接比對兩個文句是否雷同，這需要準備一些經典/常見的問題以及其對應的答案，如果有問題和經典/常見問題很相似，需要可以回答其經典/常見問題的答案；畢竟中文博大精深，想要認真探討其實非常難，像是廁所在那裡跟洗手間在那，兩句話的意思真的一樣，但字卻完全不同；至於像是我不喜歡你跟你是個好人，這就是另一種相似度了 ~ xDDD ! 那關於訓練數據資料，需要將相類似的做為集合，這部份就需要依賴文本分類；你可能也聽過 TF-IDF 或者 n-gram 等，這邊就不多加解釋，建議也多查查，現在 github 上可以找到非常的範例程式碼，建議一定要先自己動手試試看 !

  <summary>Similarity (相似度)</summary>

  - [中文文本相似度](https://www.twman.org/AI/NLP/Similarity)

  </details>

</details>

#
# LLM  

> 📚 LLM 大語言模型・必讀資源總整理
> **編者按：** 本頁面彙整目前最主流的 LLM 排行榜、開源模型、推論與微調工具，以及相關學術論文。

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
- [🛠️ 微調蒸餾技術與資源 (Fine-tuning)](#fine-tuning)
- [🧩 AI Agent 開源框架](#ai-agent)
- [🛠️ 開發工具 (Tools & Protocols)](#tools)
- [🌍 World Models (世界模型)](#world-models)
- [🧠 MoE (混合專家模型)](#moe)
- [📱 Small Language Models (小型語言模型)](#slm)
- [🤔 Reasoning Models (推理模型)](#reasoning)
- [🏛️ Large Language Models (大型語言模型)](#llm-1)
- [🔎 Embedding & Reranker](#embedding)
- [🔊 Speech-to-Speech LLM (語音大模型)](#speech)
- [👁️ Vision-Language Model (視覺大語言模型)](#vision)
- [🌌 Multimodal LLM (多模態大語言模型)](#multimodal)

---

## Leaderboards
**🏆 排行榜 (Leaderboards)**

- [**AlpacaEval Leaderboard**](https://tatsu-lab.github.io/alpaca_eval/)
- [**Open LLM Leaderboard**](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
- [**Big Code Models Leaderboard**](https://huggingface.co/spaces/bigcode/bigcode-models-leaderboard)
- [**Awesome-Chinese-LLM**](https://github.com/HqWu-HITCS/Awesome-Chinese-LLM)

---

## Fine-tuning
**🛠️ 微調蒸餾技術與資源 (Fine-tuning)**

### 顯存估算 (VRAM)
- **大模型所需 GPU 記憶體筆記**
  - 資源：[📝 微信公眾號](https://mp.weixin.qq.com/s/M_hdtR7mVq14MnaaL0MAUw)
- **不同參數規模在微調方法下所需的顯存總結**
  - 資源：[📝 DataLearner](https://www.datalearner.com/blog/1051703254378255)

### 微調/蒸餾技術教學
- **微調技術全解**
  - 說明：SFT、LoRA、P-tuning v2、Freeze 監督微調方法
  - 資源：[📝 知乎專欄](https://zhuanlan.zhihu.com/p/643941480)
- **LoRA vs 完全微調**
  - 說明：MIT 21頁論文講懂了
  - 資源：[📝 機器之心](https://www.jiqizhixin.com/articles/2024-11-11-5)
- **大模型微調 (Fine-tuning) 全解**
  - 資源：[📝 53AI](https://www.53ai.com/news/finetuning/2025022604125.html)
- **Unsloth 官方微調技巧**
  - 說明：初學者必看指南
  - 資源：[📝 微信公眾號](https://mp.weixin.qq.com/s/COZfH_h36nX33TZGBVn0rg)
- **零代碼一站式微調**
  - 說明：從資料集準備到模型微調全流程
  - 資源：[📝 知乎專欄](https://zhuanlan.zhihu.com/p/1906670241645322809)
- **DeepSeek-R1 微調指南**
  - 說明：微調為領域專家
  - 資源：[📝 知乎專欄](https://zhuanlan.zhihu.com/p/25054526736)
- **EasyDistill**  
  - 說明：知識蒸餾不再難！阿里開源EasyDistill及DistilQwen模型家族，開源即用、效能強勁！
  - 資源：[🐙 GitHub](https://github.com/modelscope/easydistill) | [📄 AlphaXiv](https://www.alphaxiv.org/abs/2505.20888)  
- **NVIDIA NeMo**
  - 說明：模型剪枝和知識蒸餾
  - 資源：[📝 NVIDIA Blog](https://developer.nvidia.com/zh-cn/blog/llm-model-pruning-and-knowledge-distillation-with-nvidia-nemo-framework/)

### 微調框架 (Frameworks)
- **LLaMA Factory**
  - 資源：[🐙 GitHub](https://github.com/hiyouga/LLaMA-Factory) | [🤗 Demo](https://huggingface.co/spaces/hiyouga/LLaMA-Board)
  - 延伸：[📝 中文文檔](https://github.com/hiyouga/LLaMA-Factory/blob/main/README_zh.md) | [📝 架構解析 (2024-09-13)](https://mp.weixin.qq.com/s/eJqKc_2nHBYzDFAp2AYdWQ) | [📝 單卡訓練 Agent 實戰](https://zhuanlan.zhihu.com/p/678989191)

- **Torchtune**
  - 資源：[🐙 GitHub](https://github.com/pytorch/torchtune) | [📖 官方文件](https://pytorch.dev.org.tw/torchtune/stable/index.html)
  - 延伸：[📝 Llama3.1 知識蒸餾實戰](https://pytorch.ac.cn/torchtune/stable/tutorials/llama_kd_tutorial.html)

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
> 完整列表請見：[避開 AI 代理 (AI Agents) 與 代理式人工智慧 (Agentic AI) 開發陷阱](https://deep-learning-101.github.io/agent)

### 核心概念與必讀文章
- **AI Search Has A Citation Problem**
  - 資源：[📝 CJR](https://www.cjr.org/tow_center/we-compared-eight-ai-search-engines-theyre-all-bad-at-citing-news.php)
- **Agentic AI vs AI Agents**
  - 說明：A Conceptual Taxonomy, Applications and Challenges
  - 資源：[📄 AlphaXiv](https://www.alphaxiv.org/abs/2505.10468)
- **OWASP Agentic AI**
  - 說明：Threats and Mitigations
  - 資源：[🛡️ OWASP](https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations/)
- **Agent 工作流入門**
  - 資源：[📝 從 Agent 到 Workflow](https://zhuanlan.zhihu.com/p/32491596217) | [📝 萬字長文綜觀 Agent](https://zhuanlan.zhihu.com/p/29833831482) | [📝 什麼是 Agentic 工作流程？](https://zhuanlan.zhihu.com/p/32709535995) | [📝 Agentic AI 區別](https://zhuanlan.zhihu.com/p/705935464)
- **FinRobot**
  - 資源：[📄 AlphaXiv](https://www.alphaxiv.org/zh/overview/2405.14767) | [📚 DeepWiki](https://deepwiki.com/AI4Finance-Foundation/FinRobot) (支援 Gemini 2.5)
- **Jupyter-AI**
  - 資源：[📚 DeepWiki](https://deepwiki.com/jupyterlab/jupyter-ai) (支援 Gemini 2.5)

### Agent 框架列表 (按時間排序)

- 2026-01-20 | **OpenClaw(MoltBot/Clawdbot)**  
  - 說明：一個跑在你自己電腦上的 AI 助手平台。 | [👉 點此看深度技術分析 ](https://deep-learning-101.github.io/LLM/OpenClaw-Moltbot-Clawdbot)
  - 資源： [🌐 官網](https://openclaw.ai/) | [🐙 GitHub](https://github.com/NVIDIA/personaplex) | [📝 官方文件](https://docs.openclaw.ai/) | [[📝 DeepWiki](https://deepwiki.com/openclaw/openclaw) | [[📝 Zread](https://zread.ai/openclaw/openclaw) | [📝 公眾號解讀](https://mp.weixin.qq.com/s/yFi8lWLWp7NPDO-zD6QW_Q) | [📝 公眾號解讀](https://mp.weixin.qq.com/s/1ikfiU_eGnL5FRaPRddA2Q) | [📝 公眾號解讀](https://mp.weixin.qq.com/s/WDEYhOG2tGYau0VAOc_y7A) | [📝 知乎解讀](https://zhuanlan.zhihu.com/p/1999109634909303005)

- 2025-11-15｜**Agno**
  - 說明：高效能 Multi-agent 系統框架
  - 資源：[🌐 官網](https://zread.ai/agno-agi/agno/) | [📝 架構深度解析](https://zhuanlan.zhihu.com/p/1945395802844410466)

- 2025-10-28｜**Tongyi DeepResearch**
  - 說明：通義全面開源，超越 OpenAI 閉源框架
  - 資源：[📝 DeepResearch](https://zread.ai/Alibaba-NLP/DeepResearch) | [📝 中文解讀](https://zhuanlan.zhihu.com/p/1951785880655209261)

- 2025-10-28｜**DeepAgent**
  - 說明：首個全自主深度推理智能體
  - 資源：[📝 RUC-NLPIR](https://zread.ai/RUC-NLPIR/DeepAgent) | [📝 中文解讀](https://zhuanlan.zhihu.com/p/1966457879335798713)

- 2025-10-19｜**Gemini Computer Use**
  - 說明：Google 推出讓 AI 代理操作網頁介面
  - 資源：[📖 官方文件](https://ai.google.dev/gemini-api/docs/computer-use) | [📝 iThome 報導](https://www.ithome.com.tw/news/171579) | [🐙 GitHub](https://github.com/google-gemini/computer-use-preview)

- 2025-10-10｜**SurfSense**
  - 說明：GitHub 萬星王炸，整合 Slack/Notion/Jira
  - 資源：[📝 MODSetter](https://zread.ai/MODSetter/SurfSense) | [📝 中文解讀](https://mp.weixin.qq.com/s/za_ZQ7OWuvYaN2f0Ml0AgA)

- 2025-08-29｜**Microsoft Agent Framework**
  - 說明：開放原始碼開發套件，用於建置 .NET 和 Python 的 AI 代理程式 和 多代理程式工作流程 。
  - 資源：[🐙 GitHub](https://github.com/microsoft/agent-framework) | [📝 官方文件](https://learn.microsoft.com/zh-tw/agent-framework/overview/agent-framework-overview)

- 2025-08-29｜**MiroThinker**
  - 說明：開源的深度研究代理，針對研究和預測進行了最佳化。
  - 資源：[🐙 GitHub](https://github.com/MiroMindAI/MiroThinker) | [📝 公眾號解讀](https://mp.weixin.qq.com/s/gRvKoSTpelsDLaUQJb0F3w)

- 2025-07-03｜**multi-modal-researcher**
  - 資源：[🐙 GitHub](https://github.com/langchain-ai/multi-modal-researcher)

- 2025-06-25｜**Gemini CLI**
  - 說明：你的開源 AI 代理
  - 資源：[🐙 GitHub](https://github.com/google-gemini/gemini-cli) | [📝 Google Blog](https://blog.google/intl/zh-tw/products/cloud/gemini-cli-your-open-source-ai-agent/)

- 2025-06-06｜**PandaWiki**
  - 說明：新一代 AI 大模型驅動的開源知識庫
  - 資源：[🐙 GitHub](https://github.com/chaitin/PandaWiki) | [📝 中文解讀](https://zhuanlan.zhihu.com/p/1916981702733039060)

- 2025-06-03｜**Gemini Fullstack LangGraph**
  - 說明：開源版 Perplexity
  - 資源：[📚 DeepWiki](https://deepwiki.com/google-gemini/gemini-fullstack-langgraph-quickstart) | [🌐 DEMO](https://deep-learning-101.github.io/gemini-fullstack-langgraph/FinGenAI) | [📝 53AI 報導](https://www.53ai.com/news/OpenSourceLLM/2025060431620.html)

- 2025-06-03｜**Perplexica**
  - 說明：Perplexity AI 開源替代品
  - 資源：[🐙 GitHub](https://github.com/ItzCrazyKns/Perplexica) | [📝 53AI 報導](https://www.53ai.com/news/qianyanjishu/2394.html)

- 2025-06-02｜**Paper2Poster**
  - 說明：自動為論文產生海報
  - 資源：[🌐 Project](https://paper2poster.github.io/) | [📝 中文解讀](https://zhuanlan.zhihu.com/p/1912838595510776080)

- 2025-06-01｜**Agent Zero**
  - 說明：全能 AI 代理（產生APP、程式碼、RAG）
  - 資源：[🐙 GitHub](https://github.com/frdel/agent-zero) | [🌐 官網](https://agent-zero.ai/) | [📝 騰訊雲文章](https://cloud.tencent.com/developer/article/2472836)

- 2025-05-30｜**WebDancer**
  - 說明：Alibaba 開源 WebAgent
  - 資源：[📄 AlphaXiv](https://www.alphaxiv.org/zh/overview/2505.22648) | [📚 DeepWiki](https://deepwiki.com/Alibaba-NLP/WebAgent)

- 2025-05-28｜**Lemon AI**
  - 說明：全球首款全端開源通用 AI Agent
  - 資源：[🐙 GitHub](https://github.com/hexdocom/lemonai) | [📝 53AI 報導](https://www.53ai.com/news/OpenSourceLLM/2025052883904.html)

- 2025-05-25｜**OpenHands**
  - 資源：[🐙 GitHub](https://github.com/All-Hands-AI/OpenHands) | [🌐 Demo](https://app.all-hands.dev/)

- 2025-05-18｜**Agent-Squad**
  - 說明：輕量級開源 AI 多智能體框架 (AWS Labs)
  - 資源：[📚 DeepWiki](https://deepwiki.com/awslabs/agent-squad) | [📝 中文解讀](https://mp.weixin.qq.com/s/5Y23EhpHb2_pBOY8XrkMNw)

- 2025-05-10｜**FlowGram (ByteDance)**
  - 說明：字節跳動開源 Coze 核心工作流引擎
  - 資源：[🐙 GitHub](https://github.com/bytedance/flowgram.ai) | [📝 公眾號解讀](https://mp.weixin.qq.com/s/EOtp8j67G5xd6H0qVfOhcw) | [📚 DeepWiki](https://deepwiki.com/search/-dify-n8n_a61d08fd-2089-4cf3-9253-3275a54b54fa)

- 2025-05-10｜**DeerFlow**
  - 說明：字節跳動 DeerFlow 解析
  - 資源：[🐙 GitHub](https://github.com/bytedance/deer-flow/blob/main/README_zh.md) | [📝 深度解析](https://www.53ai.com/news/LargeLanguageModel/2025061552389.html) | [📚 DeepWiki](https://deepwiki.com/search/_78a54d18-9132-44eb-920a-98618b505c9f)

- 2025-05-09｜**OpenDeepWiki**
  - 說明：加入 MCP，讓 AI 掌握開源專案文件
  - 資源：[🐙 GitHub](https://github.com/AIDotNet/OpenDeepWiki) | [📝 公眾號解讀](https://mp.weixin.qq.com/s/Ux1-cpXdOSnjBrxCslHjtw) | [📚 如何使用](https://deepwiki.com/search/_f9b90674-c6d9-4999-8a72-49cf28a30dca)

- 2025-05-07｜**AI Manus**
  - 資源：[📚 DeepWiki](https://deepwiki.com/Simpleyyt/ai-manus)

- 2025-04-24｜**suna**
  - 說明：Manus 開源平替
  - 資源：[🐙 GitHub](https://github.com/kortix-ai/suna) | [📝 機器之心](https://www.jiqizhixin.com/articles/2025-04-23-6)

- 2025-04-22｜**釦子空間 (Coze Space)**
  - 說明：字節版 Manus
  - 資源：[🌐 官網](https://space.coze.cn/) | [📝 知乎解讀](https://zhuanlan.zhihu.com/p/1896900788091090915)

- 2025-04-03｜**AutoAgent**
  - 說明：港大打造開源最強 Deep Research
  - 資源：[🐙 GitHub](https://github.com/HKUDS/AutoAgent) | [📝 公眾號解讀](https://mp.weixin.qq.com/s/oATCuzI4BJ6JcwJkazinCA)

- 2025-04-03｜**Agent Development Kit (ADK)**
  - 說明：Google 智能體開發工具包
  - 資源：[🐙 GitHub](https://github.com/google/adk-python) | [📝 53AI 報導](https://www.53ai.com/news/OpenSourceLLM/2025041012369.html)

- 2025-04-03｜**Deepsite**
  - 說明：基於 DeepSeek 的網頁開發智能體
  - 資源：[🤗 Space](https://huggingface.co/spaces/enzostvs/deepsite) | [📝 知乎推薦](https://zhuanlan.zhihu.com/p/1890332067411243826)

- 2025-03-30｜**DeepGemini**
  - 說明：AI 界搭積木神器
  - 資源：[🐙 GitHub](https://github.com/sligter/DeepGemini) | [📝 公眾號推薦](https://mp.weixin.qq.com/s/F2U7rWOMvfTyiRai-kfL_A)

- 2025-03-24｜**AgenticSeek**
  - 說明：Manus 完全本地化替代品
  - 資源：[🐙 GitHub](https://github.com/Fosowl/agenticSeek) | [📝 公眾號推薦](https://mp.weixin.qq.com/s/tRZNgG2trzRxScP_fJ29JQ)

- 2025-03-20｜**DeepSearcher**
  - 說明：私有資料 + Deepseek 打造本地 Deep Research
  - 資源：[📝 DeepSearcher](https://zread.ai/zilliztech/deep-searcher) | [📝 知乎解讀](https://zhuanlan.zhihu.com/p/24273636289)

- 2025-03-11｜**autoMate**
  - 說明：基於 OmniParser 的 AI 自動化助手
  - 資源：[🐙 GitHub](https://github.com/yuruotong1/autoMate) | [📝 公眾號推薦](https://mp.weixin.qq.com/s/7W0xL3EBJM9mmNZbdZCiiQ)

- 2025-03-10｜**OpenManus**
  - 資源：[🐙 GitHub](https://github.com/mannaandpoem/OpenManus) | [📝 一文讀懂](https://zhuanlan.zhihu.com/p/30090038284)

- 2025-02-28｜**MoneyPrinterTurbo**
  - 說明：AI 自動生成高清短視頻
  - 資源：[🐙 GitHub](https://github.com/harry0703/MoneyPrinterTurbo) | [📝 知乎推薦](https://zhuanlan.zhihu.com/p/27043978423)

- 2024-02-01｜**MobileAgent**
  - 說明：多模態手機助理
  - 資源：[🐙 GitHub](https://github.com/X-PLUG/MobileAgent/blob/main/README_zh.md) | [📝 知乎解讀](https://zhuanlan.zhihu.com/p/680871671)

- 2025-01-03｜**smolagents**
  - 說明：Hugging Face 開源 Agent 框架
  - 資源：[🐙 GitHub](https://github.com/huggingface/smolagents) | [📝 CSDN 介紹](https://blog.csdn.net/m0_59163425/article/details/144917058)

- 2024-10-26｜**OmniParser**
  - 說明：微軟開源，控制電腦手機的智能體
  - 資源：[🐙 GitHub](https://github.com/microsoft/OmniParser) | [📝 知乎解讀](https://zhuanlan.zhihu.com/p/3343331861)

- 2024-09-23｜**STORM**
  - 說明：基於 LLM 的知識整理系統 (Stanford)
  - 資源：[🐙 GitHub](https://github.com/stanford-oval/storm) | [📝 公眾號介紹](https://mp.weixin.qq.com/s/x72eW958UbhrscvKghO6og)

---

## Tools
**🛠️ 開發工具 (Tools & Protocols)**

### MCP (Model Context Protocol)
- 2025-08-20｜**FastAPI-MCP**
  - 說明：將 FastAPI 介面升級為 MCP 工具服務
  - 資源：[📝 zread](https://zread.ai/tadata-org/fastapi_mcp) | [📝 公眾號教學](https://mp.weixin.qq.com/s/L568EP2tl2zwmC8vxz8s7w)
- 2025-04-15｜**automcp**
  - 說明：秒設定 MCP 伺服器
  - 資源：[🐙 GitHub](https://github.com/NapthaAI/automcp) | [📝 公眾號介紹](https://mp.weixin.qq.com/s/x-aZEhtnRYPFno81Fb9ttw)
- 2025-04-10｜**line-bot-mcp-server**
  - 資源：[🐙 GitHub](https://github.com/line/line-bot-mcp-server)
- 2025-04-05｜**GitMCP**
  - 說明：讓 AI 秒懂 GitHub 項目
  - 資源：[🐙 GitHub](https://github.com/idosal/git-mcp) | [📝 53AI 報導](https://www.53ai.com/news/RAG/2025040590146.html)
- 2025-03-14｜**playwright-mcp**
  - 說明：AI 自動化神器
  - 資源：[🐙 GitHub](https://github.com/microsoft/playwright-mcp) | [📝 知乎解讀](https://zhuanlan.zhihu.com/p/30178146112)

### Browser Automation (瀏覽器自動化)
- **Browser-use**
  - 資源：[🐙 GitHub](https://github.com/browser-use/browser-use)
  - 2025-06-04：[workflow-use](https://github.com/browser-use/workflow-use) (一次錄製，永久使用)
  - 2025-04-16：[web-ui](https://github.com/browser-use/web-ui) | [📚 如何使用](https://deepwiki.com/search/_bfd33aa8-cd79-4f1d-a1e8-5620d4374329)
  - 2025-03-28：[browser-use-webui](https://github.com/browser-use/web-ui)
  - 2025-02-16：[webui 部署教學](https://zhuanlan.zhihu.com/p/24116360552)
  - 2025-01-23：[讓 AI 像人類一樣使用瀏覽器](https://zhuanlan.zhihu.com/p/20038156945)


### 效率工具 (Efficiency Tools)
- 2025-12-20｜**NVIDIA Nemotron-3-Nano**
  - 資源：[🤗 HuggingFace](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-Base-BF16) | [🌐 OpenRouter](https://openrouter.ai/nvidia/nemotron-3-nano-30b-a3b:free)
- 2025-11-20｜**LinearRAG**
  - 說明：全新 RAG 框架，無需關係抽取
  - 資源：[🐙 GitHub](https://github.com/DEEP-PolyU/LinearRAG) | [📝 知乎解讀](https://zhuanlan.zhihu.com/p/1975321777342260763)
- 2025-09-11｜**DeepMCPAgent**
  - 說明：教你讓模型自己「找工具」
  - 資源：[📝 zread](https://zread.ai/cryxnet/DeepMCPAgent) | [📝 公眾號解讀](https://mp.weixin.qq.com/s/Sj_7i1mTJ9WYaTlCzIqCFA)
- 2025-07-30｜**LangExtract**
  - 說明：Gemini 驅動的資訊擷取庫
  - 資源：[🐙 GitHub](https://github.com/google/langextract) | [📝 Google Developers](https://developers.googleblog.com/zh-hans/introducing-langextract-a-gemini-powered-information-extraction-library/)
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
  - 說明：自然語言驅動的智慧爬蟲
  - 資源：[🐙 GitHub](https://github.com/ScrapeGraphAI/Scrapegraph-ai) | [📝 公眾號推薦](https://mp.weixin.qq.com/s/lQukAy12V5K1cH6rTkqxaA)
- 2025-04-15｜**stagehand**
  - 說明：AI 驅動的下一代瀏覽器自動化框架
  - 資源：[🐙 GitHub](https://github.com/browserbase/stagehand) | [📝 公眾號推薦](https://mp.weixin.qq.com/s/KF-z67kn4rTjcIBmTvj3nA)
- 2025-04-11｜**nanobrowser**
  - 說明：AI 驅動的瀏覽器自動化神器
  - 資源：[🐙 GitHub](https://github.com/nanobrowser/nanobrowser) | [📝 公眾號推薦](https://mp.weixin.qq.com/s/65SwCtDta1cKvx1_BbaoHQ)
- 2025-04-10｜**DevDocs**
  - 說明：開發者的文檔收割機
  - 資源：[🐙 GitHub](https://github.com/cyberagiinc/DevDocs) | [📝 公眾號推薦](https://mp.weixin.qq.com/s/k5fG_L1q_19ylKIJD6PXmw)
- 2025-04-06｜**sqlchat**
  - 說明：讓資料庫管理像聊天一樣簡單
  - 資源：[🐙 GitHub](https://github.com/sqlchat/sqlchat) | [📝 公眾號推薦](https://mp.weixin.qq.com/s/kieSzWn3QDYvZ5Zx35hr1A)
- 2025-03-26｜**pdf-craft**
  - 說明：PDF 秒轉 Markdown/EPUB
  - 資源：[🐙 GitHub](https://github.com/oomol-lab/pdf-craft) | [📝 知乎推薦](https://zhuanlan.zhihu.com/p/1888288260171744707)
- 2025-03-25｜**OCRmyPDF**
  - 說明：能力分析
  - 資源：[🐙 GitHub](https://github.com/ocrmypdf/OCRmyPDF) | [📝 知乎分析](https://www.zhihu.com/tardis/zm/art/32745781279?source_id=1003)
- 2025-03-12｜**AingDesk** (同上)
  - 資源：[📚 DeepWiki](https://deepwiki.com/aingdesk/AingDesk) | [📝 知乎解讀](https://zhuanlan.zhihu.com/p/29773848356)
- 2025-03-08｜**composio**
  - 說明：AI 助理效率神器，整合 200+ 工具
  - 資源：[🐙 GitHub](https://github.com/ComposioHQ/composio) | [📝 公眾號推薦](https://mp.weixin.qq.com/s/rRPOmihGzcIXx0HQc3pdoA)
- 2025-02-25｜**PySpur**
  - 說明：拖曳式開發 AI 工作流程
  - 資源：[🌐 官網](https://www.pyspur.dev/) | [📝 知乎解讀](https://zhuanlan.zhihu.com/p/26161709083)
- 2025-01-13｜**DocAligner**
  - 說明：拍照文件復原 (校正、版面定位)
  - 資源：[🐙 GitHub](https://github.com/ZZZHANG-jx/DocAligner) | [📝 公眾號推薦](https://mp.weixin.qq.com/s/Bra9h3ExddB5NiH1g4uk1g)
- 2025-01-07｜**activepieces**
  - 說明：開源 AI 自動化工作流程工具
  - 資源：[🐙 GitHub](https://github.com/activepieces/activepieces) | [📝 公眾號推薦](https://mp.weixin.qq.com/s/Z17KtGyAH5YI4R-VY1fgng)
- 2024-12-19｜**LightRAG**
  - 資源：[🐙 GitHub](https://github.com/HKUDS/LightRAG) | [📝 技術框架解讀](https://zhuanlan.zhihu.com/p/13261291813)
- 2024-12-15｜**markitdown**
  - 資源：[🐙 GitHub](https://github.com/microsoft/markitdown)

---

## AI PTT
**🌍 AI PPT (用AI做PPT)**

- 2026-01-04 | **LangChat Slides**
  - 說明：基於生成式AI 的智慧幻燈片生成工具，由LangChat 團隊開發。
  - 資源：[🐙 GitHub](https://github.com/langchat/langchat-slides) | [DEMO](https://slides.langchat.cn/) | [掘金解讀](https://juejin.cn/post/7591861857465778214)
- 2025-12-13 | **banana-slides**
  - 說明：基於nanobananapro🍌的原生AI PPT生成應用，邁向真正的「Vibe PPT」。
  - 資源：[🐙 GitHub](https://github.com/Anionex/banana-slides) | [📝 公眾號推薦](https://mp.weixin.qq.com/s/XXyCnEdrTVoK-m-EAW69nA)
- 2025-07-26｜**presenton**
  - 說明：本地部署一鍵生成精美 PPT
  - 資源：[🐙 GitHub](https://github.com/presenton/presenton) | [📝 公眾號推薦](https://mp.weixin.qq.com/s/QTMVGD_aP41qrwtbjLxV8Q)
- 2025-07-03｜**MultiAgentPPT**
  - 說明：多智能體並發產生 PPT
  - 資源：[🐙 GitHub](https://github.com/johnson7788/MultiAgentPPT) | [📝 知乎解讀](https://zhuanlan.zhihu.com/p/1920611446007497267)
  - 2025-01-13｜**PPTAgent**
  - 說明：中科院開源 AI 工具，文件轉高品質 PPT
  - 資源：[🐙 GitHub](https://github.com/icip-cas/PPTAgent) | [📝 知乎推薦](https://zhuanlan.zhihu.com/p/18105237248)

---

## NotebookLM 平替
**🌍 NotebookLM 平替**

- 2026-01-04 | **Notex**
- 說明：一個開源 NotebookLM 替代方案的實現
  - 資源：[🐙 GitHub](https://github.com/smallnest/notex) | [📝 公眾號推薦](https://mp.weixin.qq.com/s/65epWwIC7Lqalwh-WuoP3Q)
  - [DEMO](https://notex.rpcx.io/)

- 2025-12-06 | **Open NoteBook**
- 說明：一個開源的、注重隱私的Google Notebook LM 替代方案
  - 資源：[🐙 GitHub](https://github.com/smallnest/notex) | [📝 知乎解讀](https://zhuanlan.zhihu.com/p/1980701578559234518) | [📝 公眾號解讀](https://mp.weixin.qq.com/s/Kncslf0XL1ucdPpQX_-a1g)

- 2025-12-06 | **Auto-Slides**
- 說明：不只是幫你寫，還能幫你講。它讓論文第一次有機會“開口說話”
  - 資源：[🐙 GitHub](https://github.com/Westlake-AGI-Lab/Auto-Slides) | [📝 知乎解讀](https://zhuanlan.zhihu.com/p/1953393379334391701)

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

- 2025-01-07｜**Smolagents**
  - 說明：Hugging Face 全新 AI 智能體框架
  - 資源：[🐙 GitHub](https://github.com/huggingface/smolagents) | [📝 知乎解讀](https://zhuanlan.zhihu.com/p/16417392406)

- 2024-12-13｜**Phi-4**
  - 說明：微軟 Phi-4 正式發表，以小博大
  - 資源：[🤗 HuggingFace](https://huggingface.co/NyxKrage/Microsoft_Phi-4) | [📝 公眾號](https://mp.weixin.qq.com/s/uny1VUt7vk_ZU6hCH0EDGg)

- 2024-11-18｜**MobileLLM-1.5B**
  - 說明：Meta 打造行動裝置超強語言模型
  - 資源：[🤗 HuggingFace](https://huggingface.co/facebook/MobileLLM-1.5B) | [📝 公眾號](https://mp.weixin.qq.com/s/hjY6L69pqN4GvybCuHesTA)

- 2024-11-04｜**SmolLM2**
  - 說明：手機執行的小型語言模型
  - 資源：[🤗 HuggingFace](https://github.com/huggingface/smollm/) | [📝 iThome](https://www.ithome.com.tw/news/165832)

- 2024-09-25｜**Llama 3.2**
  - 說明：1B/3B 端側模型 (Edge AI)
  - 資源：[📝 Meta Blog](https://ai.meta.com/blog/llama-3-2-connect-2024-vision-edge-mobile-devices/)

---

## Reasoning
**🤔 Reasoning Models (推理模型)**

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

- 2025-08-05｜**Claude Opus 4.1**
  - 資源：[📝 機器之心](https://www.jiqizhixin.com/articles/2025-08-06-4)

- 2024-11-23｜**Ai2 Tülu 3**
  - 說明：真・開源模型，公開「後訓練」一切
  - 資源：[🐙 GitHub](https://github.com/allenai/open-instruct) | [🌐 Playground](https://playground.allenai.org/) | [🤗 Model](https://huggingface.co/allenai) | [📝 機器之心](https://www.jiqizhixin.com/articles/2024-11-23-5)

- 2024-11-09｜**Ai2 OpenScholar**
  - 資源：[📝 Blog](https://allenai.org/blog/openscholar) | [🌐 Project](https://openscholar.allen.ai/)

- 2024-09-25｜**Llama 3.2 90b/11b**
  - 資源：[📝 Meta Blog](https://ai.meta.com/blog/llama-3-2-connect-2024-vision-edge-mobile-devices/)

---

## Embedding
**🔎 Embedding & Reranker**

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


## **相關論文**

- UnIVAL: Unified Model for Image, Video, Audio and Language Tasks：https://arxiv.org/pdf/2307.16184.pdf
    *  https://unival-model.github.io
      
- Revisiting Relation Extraction in the era of Large Language Models：https://arxiv.org/abs/2305.05003
    * [用LLM(大模型)進行關係抽取](https://mp.weixin.qq.com/s/eQL-yvz7JIuObY1CUe2gsw)
      
- [A Survey on Language Models for Code](https://arxiv.org/abs/2311.07989)
    * [首篇程式碼產生大模型論文綜述](https://zhuanlan.zhihu.com/p/667402546)
    * [涵蓋500多項研究、50多個模型，代碼大模型綜述來了](https://www.jiqizhixin.com/articles/2023-11-22-8)
      
- [Source Code Data Augmentation for Deep Learning: A Survey](https://arxiv.org/abs/2305.19915)
    * [Data Augmentation Approaches for Source Code Models](https://github.com/terryyz/DataAug4Code)
    * [歷數5年89篇研究，這篇綜述告訴我們深度學習中的程式碼資料增強怎麼樣了](https://www.jiqizhixin.com/articles/2023-11-23-3)

## **相關連結**
   
* [transformers_tasks](https://github.com/HarderThenHarder/transformers_tasks/tree/main/LLM)
  
* [超級AI助理：全新提升！中文NLP訓練框架，快速上手，海量訓練數據，ChatGLM-v2、中文Bloom、Dolly助您實現更智能的應用！](https://zhuanlan.zhihu.com/p/652256798)
  
### RAG
   
* [Graph RAG：知識圖譜結合LLM 的檢索增強](https://siwei.io/graph-rag/)
  
* [一文讀懂RAG和LLM微調，教你結合業務場景落地LLM應用](https://mp.weixin.qq.com/s/NcWyI00m2RrnibdzXqy_qQ)
  
* [LangChain - RAG：線上系統多文檔要頻繁更新](https://mp.weixin.qq.com/s/Klz0ddtqa08_5q7MqX8HXg)
  
### LangChain

* [LangChain 入門：構建LLM 支持的應用程序的初學者指南](https://zhuanlan.zhihu.com/p/631948940)
* [LangChain中文入門教程](https://github.com/liaokongVFX/LangChain-Chinese-Getting-Started-Guide)
* [大語言模型集成工具LangChain](https://zhuanlan.zhihu.com/p/599688026)
* [LangChain-ChatGLM-Webui](https://github.com/thomas-yanxin/LangChain-ChatGLM-Webui)
* [Langchain-Chatchat/Langchain-ChatGLM](https://github.com/chatchat-space/langchain-ChatGLM)
* [基於本地知識的問答機器人langchain-ChatGLM](https://zhuanlan.zhihu.com/p/622717995)
* [LlamaIndex：輕鬆構建索引查詢本地文檔的神器](https://zhuanlan.zhihu.com/p/638827267)
* [LlamaIndex——与LangChain类似但更专注于数据处理的LLM框架](https://cloud.tencent.com/developer/article/2333511)
* [langchain大模型外掛知識庫問答系統核心部件：如何更好地解析、分割複雜非結構化文本](https://mp.weixin.qq.com/s/rOWfCQuUPohatMF_dU2nIA)
* [一文詳解最熱的LLM 應用框架LangChain](https://zhuanlan.zhihu.com/p/651151321)
* [LangChain：打造自己的LLM 落地場景實作！](https://zhuanlan.zhihu.com/p/651150077)
* [langchain+xray，好玩起来了](https://mp.weixin.qq.com/s/qKFkUdvNWumanqGE6s6jUw)
* [利用LangSmith和Lilac微調你的大模型](https://mp.weixin.qq.com/s/zOM_5kpkjApDTqt9IcXstA)

### LLM 部署開發相關

* [**AutoGen / AutoGen Studio**](https://github.com/microsoft/autogen)
    * https://microsoft.github.io/autogen/blog/2023/12/01/AutoGenStudio/
    * [微軟Agent框架AutoGen論文及原理解讀](https://mp.weixin.qq.com/s/HgdAn2Bp10T7jCf5nZhdkw)
    * [AutoGen Studio 與本機Mistral AI 模型](https://mp.weixin.qq.com/s/VyOvf2guWH1AXrtVeQ8oYQ)
    * [AutoGen Studio UI 2.0 : Step By Step Installation Guide](https://gptpluginz.com/autogen-studio-ui/)
    * [體驗AutoGen Studio - 微軟推出的友善多智能體協作框架](https://zhuanlan.zhihu.com/p/678244812)
    * [逐步掌握最佳Ai Agents框架-AutoGen](https://juejin.cn/post/7305230279812218890)：https://github.com/sugarforever/AutoGen-Tutorials
    * [微軟AutoGen框架太火了，智能體聊聊天就把問題解決了](https://www.jiqizhixin.com/articles/2023-10-16-11)
    * autogen-ui：https://github.com/victordibia/autogen-ui
    * [我打通了Autogen和Bing搜尋| AutoGen系列第二篇](https://mp.weixin.qq.com/s/O8s_3K6yRB597i5swCV2Ew)
    * [Streamlit + AutoGen = 基於LLM的多代理網頁應用開發](https://mp.weixin.qq.com/s/nT55YPBviAiU3OWvdnLjjQ)
    * [使用Streamlit建立AutoGen使用者介面](https://zhuanlan.zhihu.com/p/665636978) 
* [AnythingLLM](https://github.com/Mintplex-Labs/anything-llm)：https://github.com/Mintplex-Labs/anything-llm
* [ollama](https://github.com/ollama/ollama)：https://ollama.ai
* [Flowise ——通過拖放界面構建定制的LLM流程](https://cloud.tencent.com/developer/article/2296201)
    * [Flowise｜無代碼ChatBot 構建平台｜LangChain](https://zhuanlan.zhihu.com/p/635304135) 
* [QAnything, Question and Answer based on Anything](https://github.com/netease-youdao/QAnything/blob/master/README_zh.md)：https://github.com/netease-youdao/QAnything
    * [開源、可本地部署的AI知識問答庫來了！有道出品：QAnything](https://new.qq.com/rain/a/20240117A00JGT00)
* [CrewAI](https://github.com/joaomdmoura/crewAI)：[CrewAI與AutoGen相比](https://zhuanlan.zhihu.com/p/681218725)
* [Phidata](https://github.com/phidatahq/phidata)：[Phidata補齊大模型短板，輕鬆建構RAG AI助理！](https://zhuanlan.zhihu.com/p/682123580)
* [**NVIDIA AI Foundation Models**](https://developer.nvidia.com/nemotron-3-8b)
    * [NVIDIA AI Foundation Models：使用生產就緒型LLM 建置自訂企業聊天機器人和智慧副駕](https://zhuanlan.zhihu.com/p/667838746)
    * [NVIDIA 透過企業級生成式人工智慧微服務為聊天機器人、Copilot 和摘要工具帶來商業智慧](https://blogs.nvidia.com.tw/2023/11/29/nemo-retriever-generative-ai-microservice/)
* [**TensorRT-LLM**](https://github.com/NVIDIA/TensorRT-LLM)
    * [NVIDIA TensorRT-LLM 增強了 NVIDIA H100 GPU 上大型語言模型的推論能力](https://blogs.nvidia.com.tw/2023/09/11/nvidia-tensorrt-llm-supercharges-large-language-model-inference-on-nvidia-h100-gpus/)
    * [Nvidia開源TensorRT-LLM函式庫強化H100 GPU大型語言模型推論效能](https://www.ithome.com.tw/news/158687)
* [**FastGPT**](https://fastgpt.run)
    * https://doc.fastgpt.run/docs/intro/
    * [利用Docker Compose快速部署FastGPT知识库问答](https://mp.weixin.qq.com/s/wkQuYtK8iEI-SzHn9ihUKQ)
* [**XAgent**](https://github.com/OpenBMB/XAgent)：https://github.com/OpenBMB/XAgent
    * [全面超越AutoGPT，面壁智慧聯合清華NLP實驗室開源大模型「超級英雄」XAgent](https://www.jiqizhixin.com/articles/2023-10-17-7)
    * [驕傲！清華XAgent完勝ChatGPT4.0！](https://www.wehelpwin.com/news/91)
* [**Dify**](https://dify.ai/)
    * https://github.com/langgenius/dify
    * https://docs.dify.ai/v/zh-hans/
    * [這支十餘人的年輕創業團隊如何在2 個月做出一個 LLMOps 平台](https://zhuanlan.zhihu.com/p/666614787)    
* [**HuggingChat**](http://hf.co/chat)：Powered by Open Assistant's latest model – the best open source chat model right now – and Hugging Face Inference API.
    * [chat ui](https://github.com/huggingface/chat-ui)
    * [非工程師指南: 訓練LLaMA 2 聊天機器人](https://huggingface.co/blog/zh/Llama2-for-non-engineers)
* [JittorLLMs：計圖大模型推理庫-沒有顯示卡也能跑大模型](https://github.com/Jittor/JittorLLMs/blob/main/README.md)：https://github.com/Jittor/JittorLLMs
* [PromptFlow — 微軟最新開源的基於LLM的開發工具集](https://zhuanlan.zhihu.com/p/666139473)：https://github.com/microsoft/promptflow
* [用bitsandbytes、4 位元量化和QLoRA 打造親民的LLM](https://huggingface.co/blog/zh/4bit-transformers-bitsandbytes)
* [用LLaMA 2.0, FAISS and LangChain實現基於知識問答](https://zhuanlan.zhihu.com/p/651428758)
* [LMDeploy](https://github.com/InternLM/lmdeploy/blob/main/README_zh-CN.md)：[使用LMDeploy 輕鬆部署Llama-2 系列模型！](https://zhuanlan.zhihu.com/p/645877584)
* [LLMStack：一個用於構建生成式AI 應用、聊天機器人、智能體的無代碼平台](https://mp.weixin.qq.com/s/YhIQJhafdglPLirJBi6LLg)
    * https://github.com/trypromptly/LLMStack
* [LLaMA2-Accessory](https://github.com/Alpha-VLLM/LLaMA2-Accessory)
* [AutoChain : LangChain 的替代品](https://mp.weixin.qq.com/s/v4c4JzXiVEJfwi9CQbJ2Tg)
* [LangFlow：一款可輕鬆實驗和原型化 LangChain 模擬的 AI 項目](https://mp.weixin.qq.com/s/omHZ_IqjISphmdGz3tiMnQ)


### LLM 模型匯整

* [大型語言模型綜述全新出爐：從T5到GPT-4最全盤點！](https://zhuanlan.zhihu.com/p/619526209)
* [現有開源中文LLM整理](https://zhuanlan.zhihu.com/p/630577059)
* [大模型LLM-微調經驗分享&總結](https://zhuanlan.zhihu.com/p/620885226)
* [Hugging Face 的文本生成和大語言模型的開源生態](https://huggingface.co/blog/zh/os-llms)
* [構建能夠使用CPU 運行的MetaAI LLaMA2 中文大模型](https://zhuanlan.zhihu.com/p/645426799)
* [復旦NLP團隊發表80頁大模型Agent綜述，一文綜觀AI智能體的現況與未來](https://www.jiqizhixin.com/articles/2023-09-19-8)

### Code LLM 代碼大模型介紹

* [個人程式設計助理: 訓練你自己的編碼助手](https://huggingface.co/blog/zh/personal-copilot)
* [Code Llama](https://huggingface.co/codellama/CodeLlama-70b-hf)：https://github.com/facebookresearch/codellama
    * [Introducing Code Llama, a state-of-the-art large language model for coding](https://ai.meta.com/blog/code-llama-large-language-model-coding/)
    * [Meta 公佈最新大型開源程式碼模型 Code Llama 70B！能力直逼 GPT-4](https://www.inside.com.tw/article/34063-meta-releases-code-llama-70b-an-open-source-behemoth-to-rival-private-ai-development)
* DeepSeek Coder：https://huggingface.co/deepseek-ai
    * [深度求索發布67B 大模型，以「開源」加速AGI 時代到來](https://zhuanlan.zhihu.com/p/669595851)
    * [可能是最強的開源程式碼大模型！深度求索發布DeepSeek Coder](https://zhuanlan.zhihu.com/p/664849454)
* CodeShell：https://huggingface.co/WisdomShell
    * [CodeShell-7B：北大開源70億參數代碼大模型，效能領先，IDE插件全面開源](https://zhuanlan.zhihu.com/p/670151914)

### LLM 模型介紹

* [Gemma: Google 最新推出開放大語言模型](https://huggingface.co/models?search=google/gemma)
    * [Gemma: Google 最新推出開放大語言模型](https://huggingface.co/blog/zh/gemma)
* [**Mistral**](https://huggingface.co/mistralai/Mistral-7B-v0.1)
    * [混合式專家模型(MoE) 詳解](https://huggingface.co/blog/zh/moe)
    * [Mixtral - 目前 Hugging Face 上最先進的 MoE 模型](https://huggingface.co/blog/zh/mixtral)
    * [Mistral 7B 開箱 — 真正意義上的開源 LLM 模型](https://blog.infuseai.io/mistral-7b-introduction-2f6857f6982b)
    * [Mistral AI：歐洲最強模型團隊，打造開源輕量LLM](https://new.qq.com/rain/a/20231123A08N4100)
* [**Xwin-LM**](https://github.com/Xwin-LM/Xwin-LM)
    * [首次擊敗GPT-4？700億參數Xwin-LM登頂史丹佛AlpacaEval，13B模型吊打ChatGPT](https://www.kuxai.com/article/1449)
    * [Xwin-LM-7B-V0.2](https://huggingface.co/Xwin-LM/Xwin-LM-7B-V0.2)
    * [Xwin-LM-13B-V0.2](https://huggingface.co/Xwin-LM/Xwin-LM-13B-V0.2)
* [**Zephyr**](https://huggingface.co/HuggingFaceH4)
    * [最好7B模型再易主！打敗700億LLaMA2，蘋果電腦就能跑，還開源免費](https://zhuanlan.zhihu.com/p/663816617)
    * [實戰｜如何低成本訓練一個可以超越70B Llama2 的模型Zephyr-7B](https://zhuanlan.zhihu.com/p/663782256)
    * [使用者意圖對齊，無需人工標註，Zephyr-7B 超越Llama2-Chat-70B](https://cloud.tencent.com/developer/article/2354363)
    * [Zephyr-7B-β：類GPT高性能LLM大模型](https://zhuanlan.zhihu.com/p/664820726)：https://huggingface.co/spaces/HuggingFaceH4/zephyr-chat
* [neural-chat-7b-v3@INTEL](https://huggingface.co/Intel/neural-chat-7b-v3)
    * [Efficient LLM inference on CPUs](https://hackmd.io/@VitasLu/r1BoroKVa)
    * [Intel® Extension for Transformers](https://github.com/intel/intel-extension-for-transformers)
    * [Intel-Optimized Llama.CPP](https://medium.com/@NeuralCompressor/llm-performance-of-intel-extension-for-transformers-f7d061556176)
* [**Baichuan**](https://github.com/Baichuan-inc/Baichuan-13B)：https://huggingface.co/baichuan-inc
    * https://huggingface.co/baichuan-inc/Baichuan-13B-Base
    * https://huggingface.co/baichuan-inc/Baichuan-13B-Chat
    * [實戰！私有化部署RAG大模型，ChatGLM2-6B還是Baichuan2-13B](https://www.luxiangdong.com/2023/10/09/ragllm/#/%E8%AF%95%E7%94%A8Baichuan2-13B)
    * [Baichuan2-13B 量化及 API 部署](https://mp.weixin.qq.com/s/7qf4ncRLfdvjpfhKNgqEow)
    * [百川智能發表Baichuan2大模型：全面領先Llama2，訓練切片也開源了](https://www.jiqizhixin.com/articles/2023-09-06-6)
* [**01-ai/Yi**](https://huggingface.co/01-ai)
    * [零一萬物Yi-34B-Chat 微調模型及量化版正式上線](https://zhuanlan.zhihu.com/p/668635998)
    * [零一萬物發布大模型Yi-34B，李開復：堅定進軍全球第一梯隊目標](https://www.mittrchina.com/news/detail/12627)
    * [李開復：用大模型創造Super APP是最大的商機](https://www.mittrchina.com/news/detail/12642)
    * [基於LLaMA卻改張量名，李開復公司大模型開源行為引發爭議，官方回應來了](https://www.jiqizhixin.com/articles/2023-11-14-4)
* [**Fengshenbang-LM(封神榜大模型)**](https://github.com/IDEA-CCNL/Fengshenbang-LM)：https://huggingface.co/IDEA-CCNL
    * [Ziya2: Data-centric Learning is All LLMs Need](https://arxiv.org/pdf/2311.03301.pdf)
    * [Ziya2-13B-Base](https://huggingface.co/IDEA-CCNL/Ziya2-13B-Base)
    * [社群動態| 封神榜團隊揭秘大模型訓練秘密：以資料為中心](https://hub.baai.ac.cn/view/32516)
    * [IDEA研究院Ziya2-13B首发魔搭社区（含社区推理微调最佳实践教程）](https://zhuanlan.zhihu.com/p/661623603)
    * [Never Lost in the Middle: Improving Large Language Models via Attention Strengthening Question Answering](https://arxiv.org/abs/2311.09198)
    * [多項長篇文本任務第一，揭秘Ziya-Reader 訓練技術：注意力增強](https://hub.baai.ac.cn/view/32706)
* [**Chat GLM**](https://github.com/THUDM/ChatGLM3)
    * [ChatGLM3 使用Demo及效果測試](https://zhuanlan.zhihu.com/p/664036961)
    * [當ChatGLM3能用搜尋引擎時](https://mp.weixin.qq.com/s/FAhPO_3hWOdOssssRmVFUQ)
* [Falcon 180B Demo](https://huggingface.co/spaces/tiiuae/falcon-180b-demo)
    * [Falcon 180B Model](https://huggingface.co/tiiuae/falcon-180B)
    * [Falcon 180B 目前最強大的開源模型](https://zhuanlan.zhihu.com/p/655709522)    
* [天工@崑崙萬維](https://github.com/SkyworkAI/Skywork)
    * [崑崙萬維發布「天工SkyAgents」平台，零程式碼打造AI智能體](https://www.jiqizhixin.com/articles/2023-12-01)
    * [天工Skywork-13B開源模型的煉成與思考](https://zhuanlan.zhihu.com/p/664985891)
    * [崑崙萬維開源百億級大語言模型，配套150B開源中文資料集](https://36kr.com/p/2496563965695876)
    * [中文最強開源大模型來了！130億參數，0門檻商用，來自崑崙萬維](https://zhuanlan.zhihu.com/p/664108647)
* [Meta Llama 2](https://ai.meta.com/llama)：https://github.com/facebookresearch/llama
    * [Llama 2：開放式基礎和微調聊天模型](https://zhuanlan.zhihu.com/p/648030318)
    * [Llama 2 來襲 - 在 Hugging Face 上玩轉它](https://huggingface.co/blog/zh/llama2)
    * [使用PyTorch FSDP 微調Llama 2 70B](https://huggingface.co/blog/zh/ram-efficient-pytorch-fsdp)
    * [中文LLaMA模型和指令精調的Alpaca大模型：中文數據進行二次預訓練](https://cloud.tencent.com/developer/article/2306028)
    * [千元預算半天訓練，效果媲美主流大模型，開源可商用中文LLaMA-2](https://www.jiqizhixin.com/articles/2023-09-25-16)
    * [所有基準測試都優於Llama 2 13B，最好的7B模型來了，免費用](https://www.jiqizhixin.com/articles/2023-09-29-2)
* [MOSS](https://github.com/OpenLMLab/MOSS)
    * https://txsun1997.github.io/blogs/moss.html
* Bloom：
    * https://huggingface.co/spaces/sambanovasystems/BLOOMChat
    * [176B竟然可以辣麼快，效果直逼chatgpt-4直接hf在線體驗，還可以商用](https://mp.weixin.qq.com/s/9ero7t8WRyehpVRdD0rZWA)
    * [逼近GPT-4！BLOOMChat: 开源可商用支持多语言的大语言模型](https://zhuanlan.zhihu.com/p/631036519)    
* [Dolly](https://github.com/databrickslabs/dolly)
    * [Databricks公布生成性AI模型Dolly，強調比ChatGPT更容易訓練](https://www.ithome.com.tw/news/156128)
    * [全球首個完全開源的大語言模型Dolly，性能堪比 GPT3.5！](https://www.techbang.com/posts/105519-open-source-dolly-gpt)
    * [世界首款真開源類ChatGPT大模型Dolly 2.0，可隨意修改商用](https://zhuanlan.zhihu.com/p/621655147)
    * [Databricks開源可商用的指令遵循大型語言模型Dolly 2.0](https://www.ithome.com.tw/news/156407)
* [XVERSE](https://github.com/xverse-ai/XVERSE-13B)
    * [130億參數大模型免費商用！性能超Llama2-13B，支持8k上下文](https://zhuanlan.zhihu.com/p/649643798)
    * [國內最大開源模型發布，無條件免費商用！參數650億，基於2.6兆token訓練](https://zhuanlan.zhihu.com/p/665270135)    
* [MPT-7B](https://www.mosaicml.com/blog/mpt-7b)：A New Standard for Open-Source, Commercially Usable LLMs
    * https://huggingface.co/mosaicml/mpt-7b
    * https://huggingface.co/spaces/mosaicml/mpt-7b-instruct
    * [MosaicML 推出70 億參數模型MPT-7B-8，號稱一次處理8000 字長文本、可商用](https://mp.weixin.qq.com/s/ZLotkvr9IEl91cLeu6jC6w)
    * [最新發布！截止目前最強大的最高支持65k輸入的開源可商用AI大模型：MPT-7B！](https://www.datalearner.com/blog/1051683422426508)
* [OpenBMB]
    * [清華係發布國產Mistral僅2B，老手機都帶得動，GitHub一天斬獲300+星](https://zhuanlan.zhihu.com/p/681116159)：https://github.com/OpenBMB/MiniCPM
    * [CPM-Bee](https://github.com/OpenBMB/CPM-Bee)
    * [VisCPM：SOTA 開源中文多模態大模型](https://zhuanlan.zhihu.com/p/640750889)
* [Open Assistant](https://projects.laion.ai/Open-Assistant/)
    * [Open Assistant： 創造一場開源革命](https://zhuanlan.zhihu.com/p/62259607)
    * [AI趨勢周報第208期：AI趨勢周報第208期：AI社群發起Open Assistant專案，要打造與第三方互動的AI助理](https://www.ithome.com.tw/news/155472)
    * [OpenAssistant 12B(pythia-based)本地部署快速體驗(ChatGPT開源、可商用的平替)](https://zhuanlan.zhihu.com/p/622358878)
    * [OpenAssistant  對話- 民主化大型語言模型對齊（Open-Assistant）](https://zhuanlan.zhihu.com/p/624051115)
    * [全球最大ChatGPT開源平替來了！支持35種語言，寫代碼、講笑話全拿捏](https://zhuanlan.zhihu.com/p/616917667)
* [Cerebras-GPT](https://github.com/Cerebras/modelzoo)
    * [免費可商用開源GPT模型來了，50G權重直接下載，性能不輸GPT-3](https://zhuanlan.zhihu.com/p/618893184)
    * [Open Compute-Optimal Language Models Trained on the Cerebras Wafer-Scale Cluster](https://www.cerebras.net/blog/cerebras-gpt-a-family-of-open-compute-efficient-large-language-models/)
* OpenBuddy
    * [OpenBuddy - 面向全球用户的开源多语言聊天机器人](https://github.com/OpenBuddy/OpenBuddy/blob/main/README.zh.md)
    * [OpenBuddy 發布基於Llama 2 的新一代跨語言對話模型，開源可商用](https://www.oschina.net/news/250986)
    * [OpenBuddy發布650億參數的大型跨語言對話模型](https://mp.weixin.qq.com/s/xZ0ejXwLcjGTurQFOws8lQ)
* h2oGPT：https://github.com/h2oai/h2ogpt
    * [基於H2O.ai生態系統的開源可商用大語言模型](https://zhuanlan.zhihu.com/p/645600655)
* 文心@百度：
    * https://wenxin.baidu.com
* 混元@騰訊：
    * https://cloud.tencent.com/product/hunyuan    
* 通義千問(QWEN)@阿里：
    * https://huggingface.co/Qwen/Qwen-72B
    * https://github.com/QwenLM/Qwen-7B
    * https://tongyi.aliyun.com/
    * [720億參數大模型都拿來開源了！通義千問開源全家桶，最小18億模型端側都能跑](https://www.jiqizhixin.com/articles/2023-12-01-5)
    * [免費、可商用，阿里雲開源70億參數通義千問大模型](https://www.jiqizhixin.com/articles/2023-08-04-6)
    * [開源語音大語言模型來了！阿里基於Qwen-Chat提出Qwen-Audio!](https://zhuanlan.zhihu.com/p/668608727)

</details>
