
Hi this is my program made with chatgpt that can extract pictures of every animal on earthand here is how to do it:

first and the most important, you need to have python installed, you can get it from https://python.org.
important when istalling you need to check the "Add python to PATH" option, so it works

then when you installed python you dont have to do this ever again its just a one time thing

okay, now the tutorial on how to use this program 
open cmd, by pressing "start" + "R" and writng cmd then "enter", so if you did it you write this command "pip install requests" and click enter, then you wirte "cd your_drive:\path\to\the\downloaded\folder",
you need to write your path to this folder you downloaded, so for example: cd C:\Images\fetch by taxon

then you copy and paste this command:
	python fetch_by_taxon.py --taxon /taxa/3 --count 20 --output "H:\fetch by taxon"

there are few things that you want to customize before you enter the command, first the --taxon, you want to write /taxa/ and after that a number of your taxon on the inaturalist website,
if you cant find it in this folder there is a png, called "Where_to_find_the_taxa.png" that shows where you can find it.

the next thing that you can change is the --count option, it basicly tells the program how many pictures you want to fetch, so if you need a 300 pictures or 5 just write number here.

last option is the --output, you put the direction to the folder you want the pictures to end up in.

Thats all and thank you for installing my program!
									 

