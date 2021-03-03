import datetime
import time 
import webbrowser as w
import wikipedia as wiki
from pytube import YouTube
from pytube import Playlist

def he():
	a=input("Enter Your Q.\n")
	a=a.lower()
	if "download" and "youtube" and "video" in a:
		
		url=input("Please Enter the video url here\n")
		print("\nDownloading...\nPlease Wait..\n")
		try:
			m=YouTube(url).streams.first().download()
			print("\n"+m+"Downloaded\n")
			he()
		except:
			print("Video Not available...\nCheck the  url again\n")
			he()
	elif "open youtube and search" in a:
		b=a.replace("open youtube and search ","")
		w.open("https://m.youtube.com/results?search_query="+b)
		he()
	elif "weather today" in a:
		a=w.open("https://www.google.com/search?q=how+is+the+weather+today")
		print("Please wait...")
		he()
	elif "weather today." in a:
		a=w.open("https://www.google.com/search?q=how+is+the+weather+today")
		print("Please wait...")
		he()
	elif "todays weather" in a:
		a=w.open("https://www.google.com/search?q=how+is+the+weather+today")
		print("Please wait...")
		he()
	elif "todays weather." in a:
		a=w.open("https://www.google.com/search?q=how+is+the+weather+today")
		print("Please wait...")
		he()
	elif "today weather" in a:
		a=w.open("https://www.google.com/search?q=how+is+the+weather+today")
		print("Please wait...")
		he()
	elif "today weather." in a:
		a=w.open("https://www.google.com/search?q=how+is+the+weather+today")
		print("Please wait...")
		he()
	elif "todays date" in a:
		a=time.strftime("%d %m %y")
		print(a+" is the date today")
		he()
	elif "todays date." in a:
		a=time.strftime("%d %m %y")
		print(a+" is the date today")
		he()
	elif "date today" in a:
		a=time.strftime("%d %m %y")
		print(a+" is the date today")
		he()
	elif "date today." in a:
		a=time.strftime("%d %m %y")
		print(a+" is the date today")
		he()
	elif "time" in a:
		a=time.strftime("%I:%M %p")
		print("The time is "+a)
		he()
	elif "time." in a:
		a=time.strftime("%I:%M %p")
		print("The time is "+a)
		he()
	elif "/0" in a:
		print("Answer is:Not defined")
		he()
	elif "-" in a:
		a=eval(a)
		print(a)
		he()
	elif "*" in a:
		a=eval(a)
		print(a)
		he()
	elif "/" in a:
		a=eval(a)
		print(a)
		he()
	elif "+" in a:
		a=eval(a)
		print(a)
		he()
	elif "day today" in a:
		try:
			date=time.strftime("%d %m %Y")
			day_name= ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']
			day = datetime.datetime.strptime(date, '%d %m %Y'). weekday()
			print("Today is "+day_name[day]+" "+date)
			he()
		except:
			print("Sorry I didn't get that\nTry Again")
			he()
	elif "add" in a:
		a=a.replace(" with ","+")
		a=a.replace("add ","")
		b=eval(a)
		print(b)
		he()
	elif "add" in a:
		a=a.replace(" in ","+")
		a=a.replace("add ","")
		b=eval(a)
		print(b)
		he()
	elif "what is the sum of" in a:
		a=a.replace(" and ","+")
		a=a.replace("what is the sum of ","")
		b=eval(a)
		print(b)
		he()
	elif "add" in a:
		a=a.replace(" and ","+")
		a=a.replace("add ","")
		b=eval(a)
		print(b)
		he()
	elif "open youtube" in a:
		a=w.open("https://www.youtube.com")
		he()
	elif "open instagram" in a:
		a=w.open("https://www.instagram.com")
		he()
	else:
		print("Sorry I didn't get that\nTry Again")
		he()	
he()