from google.cloud import texttospeech
import os

# 设置 GOOGLE_APPLICATION_CREDENTIALS 环境变量（改成你的 key 路径）
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "textreader-key.json"

def gcloud_tts(text, lang="en", speaking_rate=1.0, pitch=0.0):
    client = texttospeech.TextToSpeechClient()

    # 设置语音参数
    voice = texttospeech.VoiceSelectionParams(
        language_code=lang,
        name="en-US-Wavenet-F"  # 👈 可以替换为其他音色
    )

    # 设置音频输出格式与风格参数
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3,
        speaking_rate=speaking_rate,
        pitch=pitch
    )

    # 合成请求
    synthesis_input = texttospeech.SynthesisInput(text=text)
    response = client.synthesize_speech(
        input=synthesis_input,
        voice=voice,
        audio_config=audio_config
    )

    # 保存音频
    with open("output.mp3", "wb") as out:
        out.write(response.audio_content)
    print("✅ Google Cloud TTS 合成完成！文件已保存为 output.mp3")

# ---------- 主程序 ----------
if __name__ == "__main__":
    print("🎤 Google Cloud Text-to-Speech Reader")

    # 获取语速
    rate_input = input("🎶 请输入语速 (默认 1.0，推荐范围 0.8 ～ 1.2): ").strip()
    speaking_rate = float(rate_input) if rate_input else 1.0

    # 获取音高
    pitch_input = input("🎼 请输入音高 (默认 0.0，推荐范围 -5.0 ～ 5.0): ").strip()
    pitch = float(pitch_input) if pitch_input else 0.0

    # 获取文字
    text_input = input("📝 输入文字（或输入 .txt 文件名）: ").strip()

    if text_input.lower().endswith(".txt") and os.path.exists(text_input):
        with open(text_input, "r", encoding="utf-8") as f:
            text = f.read()
    else:
        text = text_input

    gcloud_tts(text, lang="en-US", speaking_rate=speaking_rate, pitch=pitch)
