import requests
import json

# 从 config.json 读取 token
with open("config.json", "r") as f:
    config = json.load(f)

ACCESS_TOKEN = config["access_token"]
DROPBOX_PATH = config["dropbox_path"]  # 上传后保存到的路径

def upload_file(local_path):
    with open("config.json", "r", encoding="utf-8") as f:
        file_data = f.read()

    url = "https://content.dropboxapi.com/2/files/upload"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Dropbox-API-Arg": json.dumps({
            "path": f"{DROPBOX_PATH}/{local_path}",
            "mode": "add",
            "autorename": True,
            "mute": False
        }),
        "Content-Type": "application/octet-stream"
    }

    response = requests.post(url, headers=headers, data=file_data)

    if response.status_code == 200:
        print(f"✅ 上传成功: {local_path}")
    else:
        print(f"❌ 上传失败: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    print("📤 Dropbox Uploader")
    local_file = input("📄 输入要上传的文件名: ").strip()
    upload_file(local_file)
