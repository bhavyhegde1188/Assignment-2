
ifile = open('text.txt')  
   ofile = open('otext.txt', mode = 'w')  
  sentence = ifile.read()  
  
 words sentence.split()  
 words.sort()  
 print (words)  
  
 for word in words:  
  ofile.write(word + " ")  
 ofile.close()
