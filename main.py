import telegram
from datetime import datetime

# ✅ Telegram Bot Token 및 Chat ID
bot = telegram.Bot(token='YOUR_BOT_TOKEN')
chat_id = 'YOUR_CHAT_ID'

# ✅ 예측 종목 리스트 (예시)
predicted_stocks = [
    {'name': '알체라', 'entry': 12000, 'target': 13500, 'cut': 11500},
    {'name': '랩지노믹스', 'entry': 2900, 'target': 3300, 'cut': 2700}
]

# ✅ 메시지 생성
message = f"📈 [주식 급등 예상 알리미]\n🕖 {datetime.now().strftime('%Y-%m-%d')} 기준\n\n"
for stock in predicted_stocks:
    message += (
        f"🔹 {stock['name']}\n"
        f"   ▪️ 매수가: {stock['entry']:,}원\n"
        f"   ▪️ 목표가: {stock['target']:,}원\n"
        f"   ▪️ 손절가: {stock['cut']:,}원\n\n"
    )

# ✅ 메시지 전송
bot.send_message(chat_id=chat_id, text=message)
