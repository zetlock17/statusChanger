import telebot
import json
from datetime import datetime

# for Telegram
bot = telebot.TeleBot('6060977596:AAEPniJwXd3n1U7KLhedQdX9Luiq6Uk6Wuo')

data = {}

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
	if message.text == 'sleep':

		now = datetime.now()

		# data['startSleep'] = str(datetime.now())
		# data['startSleepYear'] = now.strftime("%y")
		data['startSleepMonth'] = now.strftime("%m")
		data['startSleepDay'] = now.strftime("%d")
		data['startSleepHour'] = now.strftime("%H")
		data['startSleepMinute'] = now.strftime("%M")
		data['startAwakeHour'] = 0
		data['startAwakeMinute'] = 0
		data['startAwakeMonth'] = 0
		data['startAwakeDay'] = 0
		data['sleep'] = True
		data['awake'] = False

		with open("data.json", "w") as write_file:
   			json.dump(data, write_file)

	elif message.text == 'awake':

		now = datetime.now()	

		# data['startAwake'] = str(datetime.now())
		# data['startAwakeYear'] = now.strftime("%y")
		data['startAwakeMonth'] = now.strftime("%m")
		data['startAwakeDay'] = now.strftime("%d")
		data['startAwakeHour'] = now.strftime("%H")
		data['startAwakeMinute'] = now.strftime("%M")
		data['startSleepHour'] = 0
		data['startSleepMinute'] = 0 
		data['startSleepMonth'] = 0
		data['startSleepDay'] = 0
		data['awake'] = True
		data['sleep'] = False

		with open("data.json", "w") as write_file:
   			json.dump(data, write_file)

bot.polling(none_stop=True, interval=0)
