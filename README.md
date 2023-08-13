# Natural Language Processing (自然語言處理)

[那些自然語言處理 (Natural Language Processing, NLP) 踩的坑](https://blog.twman.org/2021/04/NLP.html)

### **開發心得：**

關於自然語言處理，如果你在臺灣，那你第一時間應該會想到俗稱Chatbot的聊天機器人 (就是要人工維運關鍵字跟正規表示式的機器人)吧？目前為止 (2018/07/15-2020/02/29)，從最早的中英文的情感分析，陸續接觸過文本糾錯(校正)、文本分類、文本相似度、命名實體識別、文本摘要、機器閱讀理解等，當然自然語言處理其實博大精深，還有像是分詞、詞性標註、句法分析、語言生成等，傳說中的知識圖譜 (Ontology？) 更是大魔王了；這邊僅先匯整接觸過的做說明，當然在深度學習還未爆紅前，已經有非常多的演算法，未來也盡量針對各個項目與領域持續更新簡單介紹，就當近幾次專題演講的摘要，也算是這幾年跟小夥伴們奮鬥NLP充滿血與淚的回憶；另外，根據經驗，論文當然要追，更要實作跟實驗，但算法模型其實效果已經都差不多，如果你想將算法實際落地，別懷疑，請好好的處理你的數據，這會是蠻關鍵的地方。另外，你一定也要知道 BERT家族，早在2018年11月，Google 大神釋出 BERT 後，就差不多屌打各種自然語言處理應用 (在這之前，你想搞自然語言處理，勢必用到騰訊所開源需要16GB記憶體的Tencent_ChineseEmbedding)，再後來還有像是 transformer 跟 huggingface，所以你一定要花點時間瞭解；當然，如果你真的沒太多時間投入去換跟處理數據然後重新訓練，那歡迎聯絡一下，用我們還持續迭代開發的臺灣深度大師啦，不然公開數據都是對岸用語或簡體跟英文還要擠GPU計算資源，你會很頭痛 ! 對啦，你也可以試試 NVIDIA GTC 2021 介紹的Javis等對話式AI等東西，但我想你還是會覺得不容易上手就是，除非你想自己從頭硬幹去瘋狂的標註適合自己場景的數據，然後瞭解怎樣重新訓練模型。

https://www.twman.org/AI/NLP

https://huggingface.co/DeepLearning101

## HugNLP
[Jianing Wang, Nuo Chen, Qiushi Sun, Wenkang Huang, Chengyu Wang, Ming Gao, "HugNLP: A Unified and Comprehensive Library for Natural Language Processing", arXiv preprint, 	arXiv:2302.14286, 2023](./HugNLP.md)

[基於機器閱讀理解(MRC)的指令微調(Instruction-tuning)的統一信息抽取框架之診斷書醫囑擷取分析](https://blog.twman.org/2023/07/HugIE.html)

![醫囑分析v4@JugIE@HugNLP](./images/CathayIE.gif)

## DeepKE
[Ningyu Zhang, Xin Xu, Liankuan Tao, Haiyang Yu, Hongbin Ye, Shuofei Qiao, Xin Xie, Xiang Chen, Zhoubo Li, Lei Li, Xiaozhuan Liang, Yunzhi Yao, Shumin Deng, Peng Wang, Wen Zhang, Zhenru Zhang, Chuanqi Tan, Qiang Chen, Feiyu Xiong, Fei Huang, Guozhou Zheng, Huajun Chen, "DeepKE: A Deep Learning Based Knowledge Extraction Toolkit for Knowledge Base Population", arXiv preprint, arXiv:2201.03335, 2022](./DeepKE.md)

## ERNIE-Layout
[Qiming Peng, Yinxu Pan, Wenjin Wang, Bin Luo, Zhenyu Zhang, Zhengjie Huang, Teng Hu, Weichong Yin, Yongfeng Chen, Yin Zhang, Shikun Feng, Yu Sun, Hao Tian, Hua Wu, Haifeng Wang, "ERNIE-Layout: Layout Knowledge Enhanced Pre-training for Visually-rich Document Understanding", arXiv preprint, arXiv:2210.06155, 2022](./ERNIE-Layout.md)

## PaddleNLP
https://github.com/PaddlePaddle/PaddleNLP

醫囑分析v1@UIE-PaddleNLP
![醫囑分析v1@UIE-PaddleNLP](./images/Medical-Advice_PaddleNLP-UIE.gif)

#
# 大語言模型 (Large Language Model)

[大型語言模型(Large Language Model，LLM)，想要嗎？](https://blog.twman.org/2023/04/GPT.html)

### **相關論文**

[UnIVAL: Unified Model for Image, Video, Audio and Language Tasks](https://unival-model.github.io/)：https://arxiv.org/pdf/2307.16184.pdf

[Revisiting Relation Extraction in the era of Large Language Models](https://arxiv.org/abs/2305.05003)
* [用LLM(大模型)進行關係抽取](https://mp.weixin.qq.com/s/eQL-yvz7JIuObY1CUe2gsw)

### **相關連結**

#### LLM 部署相關
* [LMDeploy](https://github.com/InternLM/lmdeploy/blob/main/README_zh-CN.md)：[使用LMDeploy 輕鬆部署Llama-2 系列模型！](https://zhuanlan.zhihu.com/p/645877584)

* [LLaMA2-Accessory](https://github.com/Alpha-VLLM/LLaMA2-Accessory)
* [AutoChain : LangChain 的替代品](https://mp.weixin.qq.com/s/v4c4JzXiVEJfwi9CQbJ2Tg)
* [LangFlow：一款可輕鬆實驗和原型化 LangChain 模擬的 AI 項目](https://mp.weixin.qq.com/s/omHZ_IqjISphmdGz3tiMnQ)
* [Flowise ——通過拖放界面構建定制的LLM流程](https://cloud.tencent.com/developer/article/2296201)
* [Dify](https://dify.ai/)
    * https://github.com/langgenius/dify
    * https://docs.dify.ai/v/zh-hans/getting-started/intro-to-dify


#### LLM 模型匯整
* [大型語言模型綜述全新出爐：從T5到GPT-4最全盤點！](https://zhuanlan.zhihu.com/p/619526209)

* [現有開源中文LLM整理](https://zhuanlan.zhihu.com/p/630577059)

* [大模型LLM-微調經驗分享&總結](https://zhuanlan.zhihu.com/p/620885226)

* [Hugging Face 的文本生成和大語言模型的開源生態](https://huggingface.co/blog/zh/os-llms)

#### LLM 模型介紹
* [Meta Llama 2](https://ai.meta.com/llama)：https://github.com/facebookresearch/llama
    * [Llama 2：開放式基礎和微調聊天模型](https://zhuanlan.zhihu.com/p/648030318)

* Chinese Llama 2 7B：https://github.com/LinkSoul-AI/Chinese-Llama-2-7b
    * [中文版開源Llama 2同時有了語言、多模態大模型，完全可商用](https://developer.aliyun.com/article/1301101)

* 通義千問：https://github.com/QwenLM/Qwen-7B
    * [免費、可商用，阿里雲開源70億參數通義千問大模型](https://www.jiqizhixin.com/articles/2023-08-04-6)

* XVERSE：https://github.com/xverse-ai/XVERSE-13B
    * [130億參數大模型免費商用！性能超Llama2-13B，支持8k上下文](https://zhuanlan.zhihu.com/p/649643798)

* [MPT-7B](https://www.mosaicml.com/blog/mpt-7b)：A New Standard for Open-Source, Commercially Usable LLMs
    * https://huggingface.co/mosaicml/mpt-7b
    * https://huggingface.co/spaces/mosaicml/mpt-7b-instruct
    * [MosaicML 推出70 億參數模型MPT-7B-8，號稱一次處理8000 字長文本、可商用](https://mp.weixin.qq.com/s/ZLotkvr9IEl91cLeu6jC6w)
    * [最新發布！截止目前最強大的最高支持65k輸入的開源可商用AI大模型：MPT-7B！](https://www.datalearner.com/blog/1051683422426508)

* [HuggingChat](http://hf.co/chat)：Powered by Open Assistant's latest model – the best open source chat model right now – and Hugging Face Inference API.

* [Open Assistant](https://projects.laion.ai/Open-Assistant/)：https://github.com/LAION-AI/Open-Assistant
    * [Open Assistant： 創造一場開源革命](https://zhuanlan.zhihu.com/p/62259607)
    * [AI趨勢周報第208期：AI趨勢周報第208期：AI社群發起Open Assistant專案，要打造與第三方互動的AI助理](https://www.ithome.com.tw/news/155472)
    * [OpenAssistant 12B(pythia-based)本地部署快速體驗(ChatGPT開源、可商用的平替)](https://zhuanlan.zhihu.com/p/622358878)
    * [OpenAssistant  對話- 民主化大型語言模型對齊（Open-Assistant）](https://zhuanlan.zhihu.com/p/624051115)
    * [全球最大ChatGPT開源平替來了！支持35種語言，寫代碼、講笑話全拿捏](https://zhuanlan.zhihu.com/p/616917667)

* [Dolly](https://github.com/databrickslabs/dolly)
    * [Databricks公布生成性AI模型Dolly，強調比ChatGPT更容易訓練](https://www.ithome.com.tw/news/156128)
    * [全球首個完全開源的大語言模型Dolly，性能堪比 GPT3.5！](https://www.techbang.com/posts/105519-open-source-dolly-gpt)

* OpenBuddy
    * [OpenBuddy - 面向全球用户的开源多语言聊天机器人](https://github.com/OpenBuddy/OpenBuddy/blob/main/README.zh.md)
    * [OpenBuddy 發布基於Llama 2 的新一代跨語言對話模型，開源可商用](https://www.oschina.net/news/250986)
    * [OpenBuddy發布650億參數的大型跨語言對話模型](https://mp.weixin.qq.com/s/xZ0ejXwLcjGTurQFOws8lQ)

* h2oGPT：https://github.com/h2oai/h2ogpt
    * [基於H2O.ai生態系統的開源可商用大語言模型](https://zhuanlan.zhihu.com/p/645600655)