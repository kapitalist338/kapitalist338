import speech_recognition as sr
import os
import webbrowser
import sys

def talk(words):
	print(words)
	os.system("say " + words)

talk("hello boss how can i help you")

def listen_Command():
	r = sr.Recognizer()

	with sr.Microphone() as inputSource:
		print("Im listenning ...")
		r.pause_threshold = 0.5
		r.adjust_for_ambient_noise(inputSource, duration = 1)
		voice = r.listen(inputSource)

	try:
		LC = r.recognize_google(voice).lower()
		print("You said:  " + LC)
	except sr.UnknownValueError:
		talk("i didnt understand you...")
		LC = listen_Command()

	return LC

def doSomeMagic(LC):
	if "hello" in LC:
		print("hello Boss ...")
		talk("hello Boss ...")

	elif "youtube" in LC:
		url = "https://youtube.com"
		webbrowser.open(url)

	elif "goodbie" in LC:
		talk("goodbie")
		sys.exit()

while True:
	doSomeMagic(listen_Command())
