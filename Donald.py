# hello this is my first real project in python I have been writing it for about 3 days but
# I will make this program better, stronger and so all. Im writing it in 2022 on december
# 15-18th. after a few weeks there will be the new 2023 year.
# Now about programm this code can 1) search everything in youtube, Wikipedia and google
# 2) (my favorite) donald can get the information about a person with his IP adress its
# cool, isnt it?
# 3) speak - Donald can tell you about everything if this information 
# available in Wikipedia.
# 4) He can say you 3 math constants Pi = 3.14... , e = 2.7..., and tau heah its little 
# thing but it can be helpful in moments
# 5) Donald can send push notifications in your windows its pretty cool!
# 6) Donald can open youtube, VK and other sytes!
# 7) Donald can creat a .txt files in your PC!!!

# I also could add a function that let you to command to Donald by the voice but Ive no 
# microphone

#youtube - KAPITALIST


# goodbye! 
# Sergey, 12/18/2022 , 13 years

# Donald

import webbrowser as web # for working with browser
import pyttsx3 # for speaking
import datetime as dt
import math # for math constants
import random
import win10toast # for push
import folium # idk why 
import requests # for IP
import json
import wikipedia # for work with wikipedia
from colorama import Fore, Back, Style

print(Fore.RED + 'Hello boss I am Donald how can I help you?')
spk = pyttsx3.init() # function that make python to speak
spk.say('Hello boss Im donald how can I help you?')
spk.runAndWait()

def greeting():
	print('Hello boss Im Donald your assistant')
	spk.say('Hello boss Im Donald your assistant')
	spk.runAndWait()

def Help():
	spk.say('This is my functions')
	spk.runAndWait()
	print('My functions:')
	print('0) CP - close program')
	print('1) txt, file - create file ')
	print('2) sy - search video on youtube')
	print('3) yt - open youtube')
	print('4) Wiki - search in Wikipedia')
	print('5) music - listen a music')
	print('6) ip -  search about person by ip')
	print('7) push - send push')
	print('8) rand - randon float number')
	print('9) MC - math consts')
	print('10) search - search in youtube')
	print('11) cal - calculator')

def ff():
	po = input('enter the name of the txt file:')
	file = open( po + '.txt' , 'w' ) 
	kl = input('enter the text:')
	file.write(kl)
	file.close()

def SIYT(): # SIYT - Search In YouTube
	spk.say('what do you want to search in youtube?:')
	dj = str(input('what do you want to search in youtube?:'))
	web.open_new_tab('https://www.youtube.com/results?search_query=' + dj)

#wikipedia.set_language('en-US')

def yt(): #youtube
	web.open_new_tab('https://youtube.com') # open youtube in new tab

def vk(): # vkontakte
	web.open_new_tab('https://vk.com') # open vk in  new tab

def Wiki(): # searching in Wikipedia

	if __name__ == '__main__':
		text_W = input('what do you want to search:')
		Search_W = wikipedia.search(text_W, results=5) # searching in Wikikpedia

		if len(Search_W) == 0:
			print(f'Error the "{text_W} not exist in Wikipedia!') # this works if ther are
			# nothing with the name text_W in Wikipedia.com
			exit() # print error and close the program


		for index, result in enumerate(Search_W):
			print(f'{index}) {result}')
		get_one = input("number of result:")
		TexT = wikipedia.summary(Search_W[int(get_one)])
		print(TexT)
		spk.say(TexT)
		spk.runAndWait()
	
x = dt.datetime.now()
print(x)



def mus():
	spk.say('Wats music do you want:')
	spk.runAndWait()
	k = str(input('Wats music do you want:'))
	if k == 'slipknot' or k == 'Slipknot':
		p = str(input('what song of SLIPKNOT do you want to listen?:'))
		web.open_new_tab('https://www.youtube.com/results?search_query=slipknot+' + p)

	if k == 'acdc' or k == 'AC/DC':
		n = str(input('What song of AC/DC do you want to listen?:'))
		web.open_new_tab('https://www.youtube.com/results?search_query=AC%2FDC' + n)
	if k == 'music' or 'Music':
		spk.say('What music do you want to listen:')
		hj = str(input('What music do you want to listen'))
		web.open_new_tab('https://www.youtube.com/results?search_query=' + hj)

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
	spk.say('what do you want?:')
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

	if a == 'music' or a == 'mus':
		mus()

	if a == 'search in wikipedia' or a == 'wikipedia' or a == 'wiki':

		Wiki()

	if a == 'yt':

		yt()

	if a == 'vk': 

		vk()

	if a == 'search in youtube' or a == "sy":

		SIYT()

	if a == 'file' or a == 'File' or a == 'txt':
		ff()

	if a == 'help' or a == 'Help':
		Help()
		
	if a == 'hi' or a == 'hello':
		greeting()

	#end of code
	#goodbie
