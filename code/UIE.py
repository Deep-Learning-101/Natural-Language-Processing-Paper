# -*- coding:utf-8 -*-
from paddlenlp import Taskflow
from hanziconv import HanziConv
import time, json
import gradio as gr


def medicalpaddle(text): 

    schema = {"门诊触发词": ["门诊起讫日", "门诊次数"], "住院触发词": ["住院起始日", "住院终止日", "住院天数"], "手术触发词": ["手术起讫日", "手术项目", "手术次数"], "急诊触发词": ["急诊起始日", "急诊终止日", "急诊起始时间", "急诊终止时间"], "加护病房触发词": ["加护病房起始日", "加护病房终止日"], "烧烫伤触发词": ["烧烫伤病房起始日", "烧烫伤病房终止日"], "癌症化疗触发词": ["癌症化疗起讫日", "癌症化疗次数"], "癌症放射线触发词": ["癌症放射线次数", "癌症放射线起讫日"], "罹癌触发词": ["罹癌起讫日"]}

    ie = Taskflow('information_extraction', task_type="event_extraction", schema=schema, model='uie-base', schema_lang="ch", from_hf_hub=True, task_path='DeepLearning101/Medical-Advice', position_prob=0.87)
    output = ie(HanziConv.toSimplified(text))
    return HanziConv.toTraditional(json.dumps(output, indent = 4, ensure_ascii = False))

examples = [
    ["病患因上述診斷，於民國108年12月03日15時10分至本院急診就診，於12月03日23時18分住入院，於12月05日接受左側腦室旁腫瘤切除術及腦室外引流管置放術，術後於12月05日入住加護病房，目前於加護病房住院治療中。"],
    ["病患曾於108-12-17至本院門診手術室接受右側經皮穿腎引留管換管手術治療，病患曾於108-12-17至本院門診治療"],
    ["於108/12/07日因破水入院，待產過程中發生上述情形，故行剖腹生產，產出壹名男嬰，體重3285公克．產後情況穩定，應於產後六週門診複查．"],    
    ["病患因上述原因，於2019年1月4日來院門診，2019年1月11日施行子宮鏡子宮黏膜下肌瘤及子宮內膜瘜肉切除手術，2019年1月23日回診"],
    ["患者因上述原因曾於108年06月03日，12月06日，在本院門診接受子宮頸抹片追蹤檢查，建議返回長庚醫院後續癌症追蹤。"],
    ["病人因上述疾病，於2019年11月06日來門診就診，宜持續於門診追蹤治療"],
    ["病患曾於108年11月10日12：08~108年11月11日19：41至本院急診治療，於民國108年11月11日住院，住院中持續接受內科治療與氧氣治療，於108年11月21日出院，出院後需使用居家呼吸器以及製氧機，宜門診追蹤治療"],
    ["病人於民國108年09月14日從門診入院，住普通病房，於民國108年12月06日出院，特此證明。"],
    ["該病患因上述疾病於民國108年5月18日至本院急診室就診，經傷口護理及診療後於當天出院，應於門診持續追蹤治療。"],
    ["病人因上述疾病於2019年12月11日入院接受治療，於2019年12月16日出院，共住院6日，宜門診繼續追蹤治療"],
    ["病人因上述症狀，於民國108年12月16日住院，接受自費欣普尼注射治療，並於民國108年12月17日出院，須門診追蹤治療。"],
    ["病人外傷來院就診時間108.11.11-108.11.29共9次。"],
    ["該員於108年10月16日，因上述病情，入院施行治療，期間須使用呼吸器及氣墊床。於108年11月26日出院。"],
    ["患者自108.03.14~108.11.20於本院診療"],
    ["1.108年8月02日，10月04日，10月11於本院門診治療。"],
    ["民國108年11月25日門診手術局部麻醉，左側乳房腫瘤核心粗針穿刺手術。"],
    ["病患因上述病因於107年03月21日接受鼻咽切片手術"],
    ["患者於108年12月19日住院接受針劑注射化學藥物及標靶藥物治療，於108年12月20日出院"],
    ["患肢不宜負重．宜休養3個月．宜使用三角巾固定．患者於民國108年01月23日至108年04月18日共至門診4次"],
    ["病人於108-12-13接受左腎結石體外震波碎石手術。"],
    ["病人因上述病症，於108年04月07日住入本院，接受支持性照護。108年04月10日出院於狀況穩定下予以出院。已安排後續放射線及化學治療。"],
    ["病人因上述病症及化學藥物治療後白血球低下，於108年05月07日入院，現完成化學藥物治療及放射線治療於108年06月08日予以出院，已安排門診後續追蹤複查。"],
    ["病人因上述病情於108年05月25日入院至加護病房，於108年05月30日轉至普通病房，於108年06月03日出院。"],
    ["病患於108年5月01日被送至本院急診就診，同日住院入加護病房，108年5月01日自動出院並轉他院."],
    ["病人因上述病症，自108年05月14日住入本院，病人於108年05月15日轉入加護病房，於108年05月24日轉入一般病房，至108年06月05日出院，宜繼續門診追蹤治療。"],
    ["病人因上述原因，於民國108年05月28日14:14來本院急診，經診斷後轉燒燙傷普通病房住院治療，民國108年06月03日接受清創手術，於民國108年6月14日自燒燙傷普通病房出院，宜於門診持續追蹤治療"],
    ["病人因上述原因，於民國108年6月26日至燒燙傷病房住院，民國108年6月27日接受頸部疤痕放鬆及全層皮膚移植手術，於民國108年7月9日自燒燙傷病房出院，宜於門診持續追蹤治療"],
    ["病患曾於108年09月19日20:32~108年09月20日08:41至本院急診治療，於108年09月20日住院抗生素治療，108年09月26日出院．一週門診追蹤．"],  
]
    
demo = gr.Interface(
    fn=medicalpaddle,
    inputs=gr.inputs.Textbox(label="醫療診斷書之醫囑原始內容"),
    outputs=gr.outputs.Textbox(label="醫療診斷書之醫囑擷取結果"),
    examples=examples,
    title="<p style='text-align: center'><a href='https://www.twman.org/AI' target='_blank'>醫囑分析：PaddleNLP 的 UIE</a>",
    description=(
        "這是將命名實體識別應用在醫囑分析，使用的是 PaddleNLP的UIE，並搭配 doccano 另外自行標註了數據，fine-tuning 前的結果；但只用CPU，所以有點慢"
    ),    
)

demo.launch(debug=True)