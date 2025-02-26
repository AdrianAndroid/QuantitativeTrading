import requests
import json

# 替换为你自己的飞书Webhook地址
webhook_url = "https://open.feishu.cn/open-apis/bot/v2/hook/ef773d85-bdef-44f9-b022-3272e1bfd368"

# 构建文本消息内容
message = {
    "msg_type": "text",
    "content": {
        "text": "量化交易的学习：这是一条来自Python的飞书文本消息。"
    }
}

# 将消息内容转换为JSON格式
message_json = json.dumps(message)

# 设置请求头
headers = {
    "Content-Type": "application/json"
}

# 发送POST请求
response = requests.post(webhook_url, data=message_json, headers=headers)

# 检查响应状态
if response.status_code == 200:
    print("消息发送成功")
else:
    print(f"消息发送失败，错误码：{response.status_code}，错误信息：{response.text}")