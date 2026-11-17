from ..client import contentClient

def validate_text_input(text: str, min_length: int =20, field_name: str="Content") -> str:
    if not text or not text.strip():
        raise ValueError(f'{field_name} cannot be empty or whitespace')
    cleaned_text=text.strip()
    if(len(cleaned_text)<min_length):
        raise ValueError(f'{field_name} must be at least {min_length} characters long')
    return cleaned_text

def validate_title(title: str , min_length: int = 5) -> str:
    return validate_text_input(title, min_length, field_name="Title")
def generate_ai_content(prompt: str , system: str = None) -> str:
    client = contentClient()
    result=client.generate(prompt, system=system)
    print("result:" ,result)

    cleaned_result=result.strip()
    print("cleaned_result:" ,cleaned_result)
    if not cleaned_result:
        raise ValueError('Model output was empty or invalid')
    return cleaned_result
#ملف ال utils بنستخدمه لما تكون في خدمة مشتركة على سبيل المثال في عنا خدمة توليد نصوص ال utils بعمل validate للعنوان هل هو صحيخ او لا وبعدين بعمل توليد لل content وطبعا لازم نعمل clean للنتيجة لانه ممكن يكون مش مرتب

