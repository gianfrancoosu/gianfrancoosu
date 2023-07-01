import requests
from bs4 import BeautifulSoup

def news(word, linee_definizione, non_trovate):
	# the target we want to open	
	url='https://www.wordreference.com/deen/' + word
	print(url)
	
	#open with GET method
	resp=requests.get(url.rstrip())
	
	#http_respone 200 means OK status
	if resp.status_code==200:
		# print("Successfully opened the web page")
		# print("The news are as follow :-\n")
	
		# we need a parser,Python built-in HTML parser is enough .
		soup=BeautifulSoup(resp.text,'html.parser')
		#print(soup.get_text())
		
		linee = soup.get_text().split("\n")
		definizione_iniziata = False
		definizione_finita = False
		for linea in linee:
			#print(linea)
			if linea.startswith("WordReference English-German Dictionary"):
				definizione_iniziata = True
			else:
			        if "auch in diesen Einträgen gefunden:" in linea:
			               definizione_finita = True
			        if definizione_iniziata and not definizione_finita and len(linea) > 1 and not linea.startswith("Fehlt etwas Wichtiges?"):
			               linee_definizione.append(linea)
		# for linea in linee_definizione:
		# 	print(linea)
		if not definizione_iniziata:
			non_trovate.append(url)
			non_trovate.append("=================================================================\n")	
			non_trovate.append(linee)		
				
                
		# l is the list which contains all the text i.e news
		#l=soup.find("ul",{"class":"searchNews"})
	
		#now we want to print only the text part of the anchor.
		#find all the elements of a, i.e anchor
		#for i in l.findAll("a"):
			#print(i.text)
	else:
		print("Error")

def read_words():

	# Using readlines()
	file1 = open('TEDESCO', 'r')
	Lines = file1.readlines()
	file1.close()

	linee_definizione = []		
	not_trovate = []		
	count = 0
	# Strips the newline character
	for line in Lines:
		count += 1
		print(count)
		linee_definizione.append("=================================================================\n")		
		linee_definizione.append("Line{}: {}".format(count, line.strip()))
		linee_definizione.append("=================================================================\n")		
		linee_definizione.append("\n")		
		linee_definizione.append("\n")		
		news(line, linee_definizione, not_trovate)

	# for linea in linee_definizione:
	# 	print(linea)
		
	# writing to file
	file1 = open('DEFINIZIONI', 'w')
	file1.writelines(linee_definizione)
	file1.close()

	# writing to file
	file1 = open('DEFINIZIONI_NOT_TROVATE', 'w')
	file1.writelines(not_trovate)
	file1.close()

# linee_definizione = []		
# news('niedrigen', linee_definizione)
read_words()
