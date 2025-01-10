import requests
import json

# 读取 API key
with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)
    api_key = config["api_key"]

def get_weather(city):
    url = (
        f"https://api.openweathermap.org/data/2.5/weather?"
        f"q={city}&appid={api_key}&units=metric&lang=zh_cn"
    )
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temp = data["main"]["temp"]
        description = data["weather"][0]["description"]
        print(f"🌡️ 当前温度：{temp}°C")
        print(f"🌤️ 天气状况：{description}")
    else:
        print("❌ 查询失败，请检查城市名称是否正确。")

if __name__ == "__main__":
    while True:
        city = input("请输入城市名（按回车退出）：")
        if not city:
            break
        get_weather(city)
        print("-" * 40)
