import os
import random
import datetime


commands = {
	"hello": ["привет", "здорово"],
	"time": ["время", "времени", "который час"],
	"joke": ["смеши", "шути", "анекдот", "шутк"],
	"weather": ["погод"],
	"processor": ["процессор"]
}


def play_voiceline(name):
	os.system(f"aplay ./voicelines/{name}.wav")


def answer(request):
	def command_for(type):
		return any(i in request for i in commands[type])
	if command_for("hello"):
		hello()
	elif command_for("time"):
		get_current_time()
	elif command_for("joke"):
		joke()
	elif command_for("weather"):
		weather()
	elif command_for("processor"):
		print(cpu_temperature())
	else:
		did_not_understand()

#==========================================================#
def number_decay(num):
	num = str(num)
	result = []
	for i in range(len(num)):
		if len(num) - i - 1 == 1:
			result.append(int(num[i]+num[i+1]))
			break
		result.append(int(num[i])*(10**(len(num) -i - 1)))
	return result

def get_current_time():
	now = datetime.datetime.now()
	print(number_decay(now.hour), "часов")
	print(number_decay(now.minute), "минут")

def hello():
	print("ну привет")

def joke():
	os.system("cd Anekdoter; sudo python3 main.py")


def weather():
	os.system("cd weather; sudo python3 weather.py")


def cpu_temperature():
	res = os.popen("sudo vcgencmd measure_temp").readline()
	res = res.replace("temp=", "").replace("'C", "")
	return res


def did_not_understand():
	print("Ничё не понял")

