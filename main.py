import vk_api, json
from datetime import datetime
import time as t

import os
os.system(f"python {'tgBotConnection.py'} &")

# for VK
user_id = ''
token = ''

def calculationTime(iMinute, iHour, iDay, iMonth, startMinute, startHour, startDay, startMonth):

	iMinutes = int(iMonth) * 43200 + int(iDay) * 1440 + int(iHour) * 60 + int(iMinute)
	startMinutes = int(startMonth) * 43200 + int(startDay) * 1440 + int(startHour) * 60 + int(startMinute)

	deltaMinutes = iMinutes - startMinutes

	hours = deltaMinutes / 60

	return round(hours, 1)

while True:

	with open("data.json", "r") as read_file:
		data = json.load(read_file)

	# print(data)

	now = datetime.now()
	vk = vk_api.VkApi(token=token)

	iterationHour = now.strftime("%H")
	iterationMinute = now.strftime("%M")
	iterationDay = now.strftime("%d")
	iterationMonth = now.strftime("%m")
	# iterationYear = now.strftime("%y")

	if data['sleep']:

		timeSleep = calculationTime(iterationMinute, iterationHour, iterationDay, iterationMonth, data['startSleepMinute'], data['startSleepHour'], data['startSleepDay'], data['startSleepMonth'])

		vk.method("status.set", {"text":'сплю ' + str(timeSleep) + 'ч'})

	elif data['awake']:

		timeAwake = calculationTime(iterationMinute, iterationHour, iterationDay, iterationMonth, data['startAwakeMinute'], data['startAwakeHour'], data['startAwakeDay'], data['startAwakeMonth'])

		vk.method("status.set", {"text":'не сплю ' + str(timeAwake) + 'ч'})

	t.sleep(30)



# phrases = [
# 	'status 1', 
# 	'status 2', 
# 	'status 3',
# ]

# while True:
# 	vk = vk_api.VkApi(token=token)
# 	vk.method("status.set", {"text":random.choice(phrases)})
# 	time.sleep(30)
