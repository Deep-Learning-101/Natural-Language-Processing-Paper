import openai
from hanziconv import HanziConv
openai.api_key = 'sk-KEY'

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {
    "role": "user",
    "content": "病人因上述病癥，自108年12月06日住院治療檢查，接受化學藥物治療至108年12月07日出院，宜繼續門診追蹤治療。上面是一段醫囑，請幫我找出以下資訊：住院與否、住院起迄日、燒燙傷與否、燒燙傷起迄日、加護病房與否、加護病房起迄日、門診與否、門診起迄日、門診次數、手術與否、手術名稱、手術起迄日、急診與否、急診起迄日、急診起始日時分秒、急診終止日時分秒、癌症化療與否、癌症化療起迄日、罹癌與否、罹癌起迄日、癌症放射線與否、癌症放射線起迄日"
}
        ]
    )
print(completion.choices[0].message['content']) 



# export OPENAI_API_KEY=sk-KEY
#這是用API直接呼叫
# curl -w "time_total:%{time_total}" https://api.openai.com/v1/chat/completions \
#  -H "Authorization: Bearer $OPENAI_API_KEY" \
#  -H "Content-Type: application/json" \
#  --insecure -d '{
#  "model": "gpt-3.5-turbo",
#  "messages": [{"role": "user", "content": "1.108年8月02日，10月04日，10月11於本院門診治療。上面是一段醫囑，請幫我找出以下資訊：住院與否、住院起迄日、燒燙傷與否、燒燙傷起迄日、加護病房與否、加護病房起迄日、門診與否、門診起迄日、門診次數、手術與否、手術名稱、手術起迄日、急診與否、急診起迄日、急診起始日時分秒、急診終止日時分秒、癌症化療與否、癌症化療起迄日、罹癌與否、罹癌起迄日、癌症放射線與否、癌症放射線起迄日"}]}'