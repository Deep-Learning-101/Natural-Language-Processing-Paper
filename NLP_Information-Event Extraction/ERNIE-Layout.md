---
layout: default
title: ERNIE-Layout 視覺豐富文件理解 | 實戰心得與論文資源
description: 百度提出的 ERNIE-Layout 文件預訓練模型架構與資訊抽取案例分享。探討在處理發票、收據等視覺豐富文件 (VRD) 時的實測效果與依賴 OCR 的技術瓶頸。
permalink: /NLP/ERNIE-Layout
lang: zh-Hant
schema_type: article
---

{% include header.html %}

---

{% include ai-share.html %}

---

# 📄 ERNIE-Layout：版面知識增強的文件理解模型

在處理如發票、收據、報表等「視覺豐富文件 (Visually-rich Document, VRD)」時，純文字的 NLP 模型往往會失效，因為文字的空間排版 (Layout) 蘊含了極重要的語義。百度的 **ERNIE-Layout** 就是為了解決這個痛點而誕生的架構。

> 💡 **2023/07/24 實測心得**：
> 經過實際測試，效果不算非常好。**最主要的瓶頸在於它依然高度依賴前端 OCR (光學字元辨識) 的精準度**。此外，當面對同一份文件中存在多個實體時，無法一次性全部擷取，必須特別設計 Prompt 並分開進行多次擷取，在實務流程上稍嫌繁瑣。

---

## 📄 學術文獻
[Qiming Peng, Yinxu Pan, Wenjin Wang, Bin Luo, Zhenyu Zhang, Zhengjie Huang, Teng Hu, Weichong Yin, Yongfeng Chen, Yin Zhang, Shikun Feng, Yu Sun, Hao Tian, Hua Wu, Haifeng Wang, "ERNIE-Layout: Layout Knowledge Enhanced Pre-training for Visually-rich Document Understanding", arXiv preprint, arXiv:2210.06155, 2022](https://arxiv.org/pdf/2210.06155.pdf)

## 🔗 實用開源資源與社群探討

* 💻 [**GitHub 專案源碼**](https://github.com/PaddlePaddle/PaddleNLP/blob/develop/model_zoo/ernie-layout/README_ch.md) (基於 PaddleNLP)
* 🎮 [**Huggingface 線上 DEMO**](https://huggingface.co/spaces/PaddlePaddle/ERNIE-Layout)

**社群深度解讀：**
* [知乎：ERNIE-Layout 筆記](https://zhuanlan.zhihu.com/p/580997246)
* [知乎：ERNIE-Layout & UIE-X 的多方案學術論文信息抽取](https://zhuanlan.zhihu.com/p/596776604)
* [老劉說NLP：再談文檔信息抽取的開源技術方案：ERNIE-Layout 文檔預訓練模型架構及信息抽取案例](https://mp.weixin.qq.com/s/tcqqZThDNUovj8fJ1f4Z-A)