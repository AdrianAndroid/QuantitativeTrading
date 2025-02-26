import requests
import json

# 替换为你自己的飞书Webhook地址
webhook_url = "https://open.feishu.cn/open-apis/bot/v2/hook/ef773d85-bdef-44f9-b022-3272e1bfd368"

# 模拟量化交易信息
strategy_name = "双均线策略"
current_positions = [
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "AAPL", "quantity": 100, "cost_price": 150.0},
    {"symbol": "GOOG", "quantity": 50, "cost_price": 2500.0}
]
today_trades = [
    {"symbol": "AAPL", "action": "买入", "quantity": 20, "price": 152.0},
    {"symbol": "GOOG", "action": "卖出", "quantity": 10, "price": 2510.0}
]
total_profit = 5000.0
daily_profit = 200.0

# 构建持仓信息字符串
position_str = ""
for position in current_positions:
    position_str += f" - 股票代码：{position['symbol']}，持仓数量：{position['quantity']}，成本价：{position['cost_price']}\n"

# 构建今日交易记录字符串
trade_str = ""
for trade in today_trades:
    trade_str += f" - 股票代码：{trade['symbol']}，操作：{trade['action']}，数量：{trade['quantity']}，价格：{trade['price']}\n"

# 构建卡片消息内容
message = {
    "msg_type": "interactive",
    "card": {
        "elements": [
            {
                "tag": "div",
                "text": {
                    "content": f"**交易策略名称**：{strategy_name}",
                    "tag": "lark_md"
                }
            },
            {
                "tag": "div",
                "text": {
                    "content": f"**当前持仓情况**：\n{position_str}",
                    "tag": "lark_md"
                }
            },
            {
                "tag": "div",
                "text": {
                    "content": f"**今日交易记录**：\n{trade_str}",
                    "tag": "lark_md"
                }
            },
            {
                "tag": "div",
                "text": {
                    "content": f"**总收益**：{total_profit} 元\n**今日收益**：{daily_profit} 元",
                    "tag": "lark_md"
                }
            }
        ],
        "header": {
            "title": {
                "content": "量化交易信息报告",
                "tag": "plain_text"
            }
        }
    }
}

message_json = json.dumps(message)

headers = {
    "Content-Type": "application/json"
}

response = requests.post(webhook_url, data=message_json, headers=headers)

if response.status_code == 200:
    print("消息发送成功")
else:
    print(f"消息发送失败，错误码：{response.status_code}，错误信息：{response.text}")