import time
import speech_recognition as sr

from response import answer


def listen(recognizer, audio):
	try:
		voice = recognizer.recognize_google(audio, language='ru-RU').lower()
		print('[log] Распознано: ' + voice)

		if voice.startswith("прав"):
			answer(voice)

	except sr.UnknownValueError:
		print('[log] Голос не распознан!')
	except sr.RequestError as e:
		print('[log] Проблема с подключением')


r = sr.Recognizer()
m =  sr.Microphone(device_index=2)

with m as source:
	r.adjust_for_ambient_noise(source)

stop_listening = r.listen_in_background(m, listen)

import os
os.system('clear') #lots of ALSA's error info, which don't prevent work of program


while True:
	time.sleep(0.01)
