from venv import logger

from .utils import validate_title, generate_ai_content


def _build_generate_prompt(title:str, tone:str = None) -> str:
    prompt = f"write a short blog post about {title}"
    if tone:
        prompt += f"write it in a {tone}"
    prompt += f"keep the total output under 500 characters"
    return prompt
#هنا انشأنا البروميت حسب العنوان اللي بدي يفوته المستخدم وال tone هي بمعنى النغمة او النبرة هل بطريقة غاضبة او عصبية او الخ ايضا اضفنا شرط انه يكون الاوتبوت اقل من 500 حرف
def _generate_post(title:str, tone:str = None) -> dict:
    cleaned_title=validate_title(title, min_length=5)
    prompt=_build_generate_prompt(cleaned_title, tone)
    try:
        cleaned_content=generate_ai_content(prompt)
    except Exception :
        logger.error(f"faild to generate {cleaned_title}")
        raise
    if len(cleaned_content)>500:
        cleaned_content=cleaned_content[:500]
    return{
        "title":cleaned_title,
        "content":cleaned_content,
        "length":len(cleaned_content)
    }
#احنا بعد ما انشانا البرومبت الان بدنا ننشأ البوست اول اشي بنعمل clean للعنوان يعني نخلي بس النص بدون ايموجيات وققص زي هيك وبعدين نعملvalidate للعنوان بعد هيك بنبعت العنوان للفنكشن تبع البروميت ويغد ما يتم انشاء البرومبت بتعمل انشاء للبوسا وطبعا بنحط شرط للتاكيد مرة تانية في حال ما التزم ال ai انه يكون النص اقل من 500 وبنقطعه وبعد هيك بنحط البوست والعنوان وطول البوست
