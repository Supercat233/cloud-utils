from googletrans import Translator

translator = Translator()

def translate_text(text, dest='zh-cn'):
    result = translator.translate(text, dest=dest)
    return result.text

if __name__ == "__main__":
    print("🌐 Translator Tool - 输入英文或日文（回车退出）")
    while True:
        text = input("🔤 输入原文: ")
        if not text:
            break
        translated = translate_text(text)
        print("✅ 翻译结果:", translated)
        print("-" * 30)
