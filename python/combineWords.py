readerG = open('/home/gianfranco//Desktop/Nachrichten')
readerE = open('/home/gianfranco//Desktop/Notes')
readerGE = open('/home/gianfranco//Desktop/NachNot','w')


wordsG = readerG.readlines()
wordsE = readerE.readlines()


myIterator = 0

for wordG in wordsG:
   readerGE.write(wordG[:-1] + ',' + wordsE[myIterator])
   myIterator+=1

try:

	print ("File found!")

    	# Further file processing goes here
finally:
    	readerG.close()





print ("Hello World!")
