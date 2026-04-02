---
layout: default
title: NLP 自然語言處理資源懶人包 | Transformers, BERT & RAG | Deep Learning 101
description: 2026 NLP 技術與論文資源彙整。從基礎的 Transformers、BERT 到最新的 RAG (檢索增強生成) 技術架構解析，提供研究人員與開發者最紮實的自然語言處理指南。
permalink: /Natural-Language-Processing
lang: zh-Hant
schema_type: service
service_type: AI Consulting
---

{% include header.html %}

# 📝 NLP 自然語言處理・實戰血淚與必讀資源總整理

> **編者按：** 本頁面專注於自然語言處理的核心技術架構。從基礎的 Transformers、BERT 模型，到進階的檢索增強生成、命名實體識別與文本分類技術，提供開發者紮實的理論與實戰資源。
>
> 如果您想尋找更詳細的論文筆記，歡迎訪問 **GitHub Repository**：
> 👉 [**GitHub: Natural-Language-Processing-Paper**](https://github.com/Deep-Learning-101/Natural-Language-Processing-Paper) (歡迎 Star ⭐)

---

{% include ai-share.html %}

---

## 🧠 NLP 自然語言處理 (Natural Language Processing)

關於自然語言處理，如果你在臺灣，那你第一時間應該會想到俗稱 Chatbot 的聊天機器人（就是要人工維運關鍵字跟正規表示式的機器人）吧？

從最早的中英文的情感分析，我們陸續接觸過文本糾錯(校正)、文本分類、文本相似度、命名實體識別、文本摘要、機器閱讀理解等，當然自然語言處理其實博大精深，還有像是分詞、詞性標註、句法分析、語言生成等，傳說中的知識圖譜 (Ontology？) 更是大魔王了。

這邊僅先匯整接觸過的做說明，當然在深度學習還未爆紅前，已經有非常多的演算法，未來也盡量針對各個項目與領域持續更新簡單介紹，就當近幾次專題演講的摘要，也算是這幾年跟小夥伴們奮鬥 NLP 充滿血與淚的回憶。

### 💡 給開發者的落地忠告
根據經驗，論文當然要追，更要實作跟實驗，**但算法模型其實效果已經都差不多，如果你想將算法實際落地，別懷疑，請好好的處理你的數據，這會是蠻關鍵的地方**。

另外，你一定也要知道 BERT 家族，早在 2018 年 11 月，Google 大神釋出 BERT 後，就差不多屌打各種自然語言處理應用（在這之前，你想搞自然語言處理，勢必用到騰訊所開源需要 16GB 記憶體的 `Tencent_ChineseEmbedding`），再後來還有像 Transformer 跟 Huggingface，所以你一定要花點時間瞭解。

當然，如果你真的沒太多時間投入去換跟處理數據然後重新訓練，那歡迎聯絡一下，用我們還持續迭代開發的**臺灣深度大師**啦！不然公開數據都是對岸用語或簡體跟英文，還要擠 GPU 計算資源，你會很頭痛！對啦，你也可以試試 NVIDIA GTC 2021 介紹的 Jarvis 等對話式 AI 等東西，但我想你還是會覺得不容易上手就是，除非你想自己從頭硬幹去瘋狂的標註適合自己場景的數據，然後瞭解怎樣重新訓練模型。

---

### 🗓️ 2018/07/15-2020/02/29 開發心得總結
自然語言處理是人工智慧和語言學領域的分支學科。此領域探討如何處理及運用自然語言；自然語言處理包括多方面和步驟，基本有認知、理解、生成等部分。自然語言認知和理解是讓電腦把輸入的語言變成有意思的符號和關係，然後根據目的再處理。自然語言生成系統則是把計算機數據轉化為自然語言。

最後，放眼望去想入門 Attention、Transformer、Bert 和 **李宏毅老師的教學影片**等，絕對不能錯過。

雖然分享這些踩過的坑還有免費 DEMO 跟 API 其實我想不到有啥好處，但至少不用為了要營利而去亂喊口號，也更不用畫大餅，能做多少就是說多少；如同搞 Deep Learning 101 搞那麼久，**搬桌椅、直播場佈其實比想像中麻煩，只希望讓想投入的知道 AI 這個坑其實很深，多分享總是比較好！**

<ul>
<li><b><a href="https://mp.weixin.qq.com/s/SJXxeTsqn9RoaVu66MISXQ">這麼多年，終於有人講清楚Transformer了</a></b></li>
<li><b><a href="https://zhuanlan.zhihu.com/p/411311520">我從零實現了Transformer模型，把代碼講給你聽</a></b></li>
<li><b><a href="https://easyai.tech/ai-definition/attention/">Attention 機制</a></b></li>
<li><b><a href="https://zhuanlan.zhihu.com/p/410776234">超詳細圖解Self-Attention</a></b></li>
<li><b><a href="https://huggingface.co/learn/nlp-course/zh-TW/chapter1/1">NLP Course @ HuggingFace</a></b></li>
</ul>

---

## 🛠️ 核心任務實戰解析與資源 (點擊展開)

<details>
  <summary><b>🔍 Information / Event Extraction (資訊與事件擷取)</b></summary>
  <br>
  <ul>
    <li><b><a href="https://github.com/Deep-Learning-101/Natural-Language-Processing-Paper/blob/main/HugNLP.md">HugNLP</a></b>：<a href="https://blog.twman.org/2023/07/HugIE.html">以 MRC 為核心的統一信息抽取框架，支援醫療應用如診斷書與醫囑擷取。</a></li>
    <li><b><a href="https://github.com/Deep-Learning-101/Natural-Language-Processing-Paper/blob/main/DeepKE.md">DeepKE</a></b>：<a href="https://github.com/zjunlp/DeepKE/blob/main/README_CN.md">支援中文知識圖譜抽取，包含 DeepKE-LLM 與 KnowLM 擴展模組。</a></li>
    <li><b><a href="https://github.com/Deep-Learning-101/Natural-Language-Processing-Paper/blob/main/ERNIE-Layout.md">ERNIE-Layout</a></b>：<a href="https://arxiv.org/abs/2210.06155">增強視覺結構理解的預訓練模型，提升文件排版感知能力。</a></li>
    <li><b><a href="https://huggingface.co/spaces/DeepLearning101/PaddleNLP-UIE">UIE @ PaddleNLP</a></b>：<a href="https://github.com/PaddlePaddle/PaddleNLP/tree/develop/model_zoo/uie">支援任意類型信息抽取任務的通用開源工具。</a></li>
  </ul>
</details>

<details> 
  <summary><b>📖 Machine Reading Comprehension (機器閱讀理解 MRC)</b></summary>
  <br>
  <blockquote>
    <b>🗓️ 2018/10/15–2019/02/10 開發心得</b><br>
    投入約 120 天，開發用於博物館與展場導覽機器人的問答系統。當時缺乏中文資料集，無法直接套用英文 SQuAD 1.0/2.0。初期需自行翻譯資料、自建標註系統，並標註維基百科語料以彌補在地語言差異。挑戰包含多篇文章處理、跨文件推理，以及中英文格式差異與語境適配。
  </blockquote>
  <ul>
    <li><a href="https://www.twman.org/AI/NLP/MRC">中文機器閱讀理解</a></li>
    <li><a href="https://zhuanlan.zhihu.com/p/80905984">機器閱讀理解綜述(一)</a> | <a href="https://zhuanlan.zhihu.com/p/80980403">(二)</a> | <a href="https://zhuanlan.zhihu.com/p/81126870">(三)</a></li>
    <li><a href="https://zhuanlan.zhihu.com/p/109309164">機器閱讀理解探索與實踐</a></li>
  </ul>  
</details>    

<details>
  <summary><b>🏷️ Named Entity Recognition (命名實體識別 NER)</b></summary>
  <br>
  <blockquote>
    <b>🗓️ 2019/12/02-2020/02/29 開發心得</b><br>
    記得前後兩次陸續投入總計約 100 天。<br><br>
    或許有人會發現為何在分享這幾篇自然語言會強調中文數據？最好理解的說法就是中文是基於字表示再加上中文斷詞的效果，比起每個單詞只需空格來表示的英文硬是麻煩點。命名實體識別 (NER) 是指將語句中的元素分成預先定義的類別（開放域來說包括實體、時間和數字3個大類，人名、地名、組織名、機構名、時間、日期、數量和名字等7個小類，特定領域就像是藥名、疾病等類別）。要應用在那方面？像是關係抽取、對話意圖理解、輿情分析、對話 NLU 任務等等都用得上，更廣義的就屬填槽 (Slot-Filling) 了。<br><br>
    最早 (2019/08時) 我們需處理的場景是針對電話助理的對話內容 (就是APP幫你接電話跟對方對話) 在語音識別後跟語音合成前的處理，印像中沒做到非常深入；後來剛好招聘到熟悉 NER 這部份的小夥伴們，剛好一直想把聊天對話做個流程處理 (多輪對話的概念) ，就再花了點時間當做上手。<br><br>
    因為不想依賴大量關鍵字和正規表示式做前處理，中間試了不少數據集，還做了像是用拼音、注音等，或者品牌定義等超多的實驗，甚至還一度想硬整合 RASA 等等的開源套件，也嘗試用了 "改寫" 來修正對話內容，去識別出語句中的重點字。至於這個的數據標據就真的更累人，意外找到一個蠻好用的標註系統 <code>ChineseAnnotator</code>，然後我們就瘋狂開始標註！
  </blockquote>
  <ul>
    <li><a href="https://www.twman.org/AI/NLP/NER">中文命名實體識別</a></li>
  </ul> 
</details>

<details>
  <summary><b>✍️ Correction (文本糾錯)</b></summary>
  <br>
  <blockquote>
    <b>🗓️ 2019/11/20-2020/02/29 開發心得</b><br>
    投入約 100 天，早期上線成本資源頗高，現在就沒這問題；這個項目堪稱是在 NLP 這個坑裡投入第二多的。<br><br>
    記得當時的場景是機器人在商場裡回答問題所顯示出來的文字會有一些 ASR 的錯字，但是問題一樣卡在數據集，還因此讓小夥伴們花了好長時間辛苦去標註 XD，但看看現在效果，我想這是值得的！記得一開始是先依賴 <code>pycorrector</code>，然後再換 <code>ConvSeq2Seq</code>，當然 bert 也做了相關優化實驗。<br><br>
    <b>中間一度被那三番二次很愛嗆我多讀書，從 RD 轉職覺得自己很懂做產品的 PM 拿跟百度對幹，從一開始的看實驗結果輸，到後來贏了，卻又自己亂測說還是不夠好之類的叭啦叭啦，說實話，你最後不也人設垮了然後閃人 ~ 攤手 ~</b><br><br>
    現在看看這截圖效果，不是蠻勵害的嗎？真的想說這社會真的充滿一堆人設嚇死人的人，無敵愛嘴砲！搞的為了滿足那位人設比天高的需求，真的是想了像是用拼音還兼 NER 來整合的好幾種方法！<br><br>
    那文本糾錯會有什麼坑呢？：數據啊、格式啊 !!! 還有幾個套件所要處理的目標不太一樣，有的可以處理疊字有的可以處理連錯三個字，還有最麻煩的就是斷字了，因為現有公開大家最愛用的仍舊是 <code>Jieba</code>，即便它是有繁中版，當然也能試試 <code>pkuseg</code>，但就是差了點感覺。
  </blockquote>
  <ul>
    <li><a href="https://www.twman.org/AI/NLP/Correction">中文文本糾錯</a></li>
    <li><a href="https://huggingface.co/spaces/DeepLearning101/Corrector101zhTW">HuggingFace Space 線上體驗</a></li>  
  </ul> 
</details>

<details>
  <summary><b>📂 Classification (文本分類)</b></summary>
  <br>
  <blockquote>
    <b>🗓️ 2019/11/10-2019/12/10 開發心得</b><br>
    最早我們是透過 Hierarchical Attention Networks for Document Classification (HAN) 的實作，來修正並且以自有數據進行訓練；但是這都需要使用到騰訊放出來的近 16 GB 的 embedding：<code>Tencent_AILab_ChineseEmbedding_20190926.txt</code>，如果做推論，這會是個非常龐大需載入的檔案。<br><br>
    直到後來 Huggingface 橫空出世，解決了 bert 剛出來時，很難將其當做推論時做 embedding 的 service (最早出現的是 <code>bert-as-service</code>)；同時再接上 BiLSTM 跟 Attention。CPU (Macbook pro)：平均速度：約 0.1 sec/sample，總記憶體消耗：約 954 MB (以 BiLSTM + Attention 為使用模型)。<br><br>
    引用 Huggingface transformers 套件 <code>bert-base-chinese</code> 模型作為模型 word2vec (embedding) 取代騰訊 pre-trained embedding。<br>
    <b>優點：</b> API 上線時無須保留龐大的 Embedding 辭典，避免消耗大量記憶體空間，但 BERT 相較於傳統辭典法能更有效處理同詞異義情況，更簡單且明確的使用 BERT 或其他 Transformers-based 模型。<br>
    <b>缺點：</b> Embedding 後的結果不可控制，BERT Embedding 維度較大，在某些情況下可能造成麻煩。
  </blockquote>
  <ul>
    <li><a href="https://www.twman.org/AI/NLP/Classification">中文文本分類</a></li>
  </ul> 
</details>


<details>
  <summary><b>🔗 Similarity (文本相似度)</b></summary>
  <br>
  <blockquote>
    <b>🗓️ 2019/10/15-2019/11/30 開發心得</b><br>
    投入約 45 天，那時剛好遇到 albert，但最後還是被蒸溜給幹掉；<br><br>
    會做文本相似度主要是要解決當機器人收到 ASR 識別後的問句，在進到關鍵字或正規表示式甚至閱讀理解前，藉由 80/20 從已存在的 Q&A 比對，然後直接解答；簡單來說就是直接比對兩個文句是否雷同，這需要準備一些經典/常見的問題以及其對應的答案，如果有問題和經典/常見問題很相似，需要可以回答其經典/常見問題的答案。<br><br>
    畢竟中文博大精深，想要認真探討其實非常難，像是<b>廁所在那裡</b>跟<b>洗手間在那</b>，兩句話的意思真的一樣，但字卻完全不同；至於像是<b>我不喜歡你</b>跟<b>你是個好人</b>，這就是另一種相似度了 ~ xDDD !<br><br>
    那關於訓練數據資料，需要將相類似的做為集合，這部份就需要依賴文本分類；你可能也聽過 TF-IDF 或者 n-gram 等，這邊就不多加解釋，建議也多查查，現在 github 上可以找到非常的範例程式碼，建議一定要先自己動手試試看！
  </blockquote>
  <ul>
    <li><a href="https://www.twman.org/AI/NLP/Similarity">中文文本相似度</a></li>
  </ul> 
</details>  

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "TechArticle",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://deep-learning-101.github.io/Natural-Language-Processing"
  },
  "headline": "從傳統 NLP 到大模型時代：機器閱讀理解、文本糾錯與實戰血淚史",
  "description": "整合 2018 至今的 NLP 開發心得與最新技術。涵蓋機器閱讀理解(MRC)、命名實體識別(NER)、文本糾錯、Transformer 架構解析與中文 NLP 實戰資源總整理。",
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
  "datePublished": "2026-04-02",
  "dateModified": "2026-04-02",
  "keywords": "自然語言處理, NLP, 機器閱讀理解, MRC, 文本糾錯, NER, 命名實體識別, Transformer, BERT, HuggingFace, 文本分類, 文本相似度, 中文 NLP",
  "about": [
    {
      "@type": "Service",
      "name": "傳統 NLP 技術開發與心得分享"
    }
  ]
}
</script>