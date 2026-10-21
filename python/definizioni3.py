
import requests
from bs4 import BeautifulSoup


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
}


def news(word, linee_definizione, non_trovate):
	# the target we want to open	
	url='https://en.wiktionary.org/wiki/' + word.rstrip() +"#GERMAN" 
#	url='https://dictionary.cambridge.org/dictionary/german-english/' + word.rstrip()
	print(url)


	
	#open with GET method
	resp=requests.get(url.rstrip(), headers=headers)
	
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
			#print(linea + "\n")
			if linea.startswith("Verb[edit]") or linea.startswith("Noun[edit]") or linea.startswith("Adjective[edit]"):
				definizione_iniziata = True
			else:
			        if "Conjugation[edit]" in linea or "Declension[edit]" in linea :
			               definizione_finita = True
			        if definizione_iniziata and not definizione_finita and len(linea) > 1 and not linea.startswith("Fehlt etwas Wichtiges?"):
			               linee_definizione.append(linea)
			               linee_definizione.append("<br>")
		# for linea in linee_definizione:
		#   print(linea)
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
		print(resp.status_code)

def read_words():

	# Using readlines()
	file1 = open('TEDESCO', 'r')
	Lines = file1.readlines()
	file1.close()

	linee_definizione = []		
	not_trovate = []		
	count = 0
	# Strips the newline character
	linee_definizione.append("<table>")	
	for line in Lines:
		count += 1
		print(count)
		linee_definizione.append("<tr>\n")	
		linee_definizione.append("<td>\n")	
		linee_definizione.append(line.strip())
		linee_definizione.append("<td>\n")	
		news(line, linee_definizione, not_trovate)
		linee_definizione.append("</td>\n")	
		linee_definizione.append("</tr>\n")	

	# for linea in linee_definizione:
	# 	print(linea)
		
	linee_definizione.append("</table>")	
	# writing to file
	file1 = open('DEFINIZIONI.html', 'w')
	file1.writelines(linee_definizione)
	file1.close()

	# writing to file
	file1 = open('DEFINIZIONI_NOT_TROVATE', 'w')
	file1.writelines(not_trovate)
	file1.close()

# linee_definizione = []		
# news('niedrigen', linee_definizione)
read_words()
