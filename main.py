import flet as ft

def main(page: ft.Page):
    page.title = "آلة حاسبة"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # عناصر واجهة المستخدم
    result = ft.TextField(label="النتيجة", read_only=True, width=200)
    
    # أزرار الآلة الحاسبة
    buttons = [
        "7", "8", "9", "/",
        "4", "5", "6", "*",
        "1", "2", "3", "-",
        "0", ".", "=", "+"
    ]

    # دالة للتعامل مع النقرات على الأزرار
    def on_button_click(e):
        if e.control.text == "=":
            try:
                # حساب النتيجة
                result.value = str(eval(result.value))
            except Exception as ex:
                result.value = "خطأ"
        else:
            result.value += e.control.text
        
        page.update()

    # إنشاء الأزرار
    button_list = [
        ft.ElevatedButton(text=button, on_click=on_button_click) for button in buttons
    ]

    # تنظيم العناصر في واجهة المستخدم
    page.add(
        result,
        ft.Row([button_list[0], button_list[1], button_list[2], button_list[3]]),
        ft.Row([button_list[4], button_list[5], button_list[6], button_list[7]]),
        ft.Row([button_list[8], button_list[9], button_list[10], button_list[11]]),
        ft.Row([button_list[12], button_list[13], button_list[14], button_list[15]]),
    )

# تشغيل التطبيق
ft.app(target=main)
