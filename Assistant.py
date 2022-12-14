import webbrowser as web 
import pyttsx3
import datetime as dt
import math
import random
import win10toast
import folium
import requests
import json

	
x = dt.datetime.now()
print(x)

spk = pyttsx3.init()

def funct():
	pass

def ip():
	def GIBI(ip = '127.0.0.1'):
		try:
			res = requests.get(url=f"http://ip-api.com/json/{ip}").json()
			print(res)
		except requests.exceptions.connectionError:
			print('Error')

	def main():
		spk.say('enter ip')
		spk.runAndWait()
		ip = input('pls enter your ip here: ')

		GIBI(ip=ip)

	if __name__ == '__main__':
		main()


def push():
	toast = win10toast.ToastNotifier()

	x = input('Enter the title: ')
	y = input('Now massage: ')
	z = int(input('enter the duration: '))

	toast.show_toast(title=x, msg=y, duration=z)

def rand():
	print(random.random())

def MC():
	print('number PI:', math.pi)
	print('number E:', math.e)
	print('number "Tau":', math.tau)


def spik():
	engine = pyttsx3.init()
	d = str(input('what I will say?: '))
	engine.say(d)
	engine.runAndWait()


def ser():
	spk.say('What I will search')
	spk.runAndWait()
	b = str(input('what I will search? :  '))
	web.open_new_tab("https://www.google.com/search?q=" + b)

def cal():
	num1 = float(input('Please enter the first num: '))
	act = str(input('Please enter the action: '))
	num2 = float(input('Please enter the second num: '))
	if act == '+':
		print(num1 + num2)

	if act == '-':
		print(num1 - num2)

	if act == '*':
		print(num1 * num2)

	if act == ':' or act == '/':
		print(num1 / num2)



while True:
	spk.say('what do you want?')
	spk.runAndWait()
	a = str(input('what do you want?:'))

	if a == 'CP':
		break

	if a == 'search':
		ser()
	if a == 'cal':
		cal()
	if a == 'sp' or a == 'speak':
		spik()
	if a == 'MC' or a == 'MK':
		MC()
	if a == 'random' or a == 'rand':
		rand()
	if a == 'push' :
		push()

	if a == 'ip':
		ip()
