from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.utils.config import get_default_config
import telebot

config_dict = get_default_config()
config_dict['language'] = 'ru'
config_dict['language'] = 'en'
owm = OWM('742d980924df3fa9a64c3ea9cccbcc55')
mgr = owm.weather_manager()
bot = telebot.TeleBot("1958896867:AAE-I0ng2BtrtGDQsv4ydcLraDOl6PEE8yU")

@bot.message_handler(content_types=['text'])
def send_echo(message):
    try: 
     observation = mgr.weather_at_place( message.text )
     w = observation.weather
     temp = w.temperature('celsius')["temp"]
    
     answer = "В городе " + message.text + " сейчас " + w.detailed_status + "\n"
     answer += "Температура сейчас в районе " + str(temp) + "\n\n"

     if temp < 10:
          answer += "Сейчас холодно, одевайся тепло!"         
     elif temp < 20:
          answer += "Сейчас более менее тепло, но все равно что-нибудь накинь сверху!"
     else:
          answer += "Температура прекрасная, сейчас уж точно не замерзнешь!"  

     bot.send_message(message.chat.id, answer)
    except:
     bot.send_message(message.chat.id,'Ошибка! Город не найден.')
bot.polling( none_stop = True)
input()