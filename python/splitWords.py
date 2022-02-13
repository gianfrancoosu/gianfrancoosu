readerG = open('/home/gianfranco//Desktop/Nachrichten')
writerG = open('/home/gianfranco//Desktop/NachNot','w')


linesG = readerG.readlines()


for lineG in linesG:
         words = lineG.split()
         for word in words:
              writerG.write(word + "\n")

try:

	print ("File found!")

    	# Further file processing goes here

finally:
    	readerG.close()
 #      writerG.close()
 #     print ("Hello World!")
