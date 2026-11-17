from openai import OpenAI
from django.conf import settings
class contentClient():  #هنا بدي امرق الAPI Key
    def __init__(self):
        self.client = OpenAI(api_key=settings.OPENAI_APIKEY)

    def generate(self, prompt, system=None):
        messages=[]
        if system:
            messages.append({"role": "system","content": system})
        messages.append({"role": "user","content": prompt}) #الفرق ما بين system prompt انه هي عبارة عن تعليمات للنظام ممنوع يتجاوزها زي مثلا انه تكون الاجابة 50 كلمة بينما ال user prompt هاي المستخدمين اللي بطلبوها يعني مثلا اكتبلي موضوع عن شيء معين هنا ممكن يتجاوزها
        response=self.client.chat.completions.create(
            model=settings.OPENAI_MODEL,
            messages=messages,
        )
        return response.choices[0].message.content

