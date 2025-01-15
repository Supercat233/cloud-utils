from google.cloud import texttospeech

client = texttospeech.TextToSpeechClient()

# 设置语言代码，例如 "en-US", "ja-JP"
language_code = "en-US"

response = client.list_voices(language_code=language_code)

print(f"可用声音列表（{language_code}）:")
for voice in response.voices:
    name = voice.name
    gender = texttospeech.SsmlVoiceGender(voice.ssml_gender).name
    natural = "✅ WaveNet" if "WaveNet" in name else ""
    print(f"- {name} ({gender}) {natural}")
