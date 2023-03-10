import requests
from datetime import datetime
import telebot
from auth_data import token


def get_data():
    req = requests.get("https://yobit.net/api/3/ticker/btc_usd")
    response = req.json()
    print(response)
    sell_price = response["btc_usd"]["sell"]
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell BTC price: {sell_price}")
 
def telegram_bot(token):
    bot = telebot.TeleBot(token)
    
    @bot.message_handler(commands=['start'])
    def start_message(message):
        bot.send_message(message.chat.id, "Hallo friend! Write the 'price' to find out the cost of BTC!")
     
    bot.polling()


if __name__ == '__main__':
   # get_data()
 telegram_bot(token)