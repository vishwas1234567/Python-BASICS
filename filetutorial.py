import random
text = "Hello people we are the gen 2 of the technoids for the sessions we will also take sessions"
file1 = open("myfile.txt","r") #the file one opened as the read mode for the
#the creatin of the new file
file1.close()
file2 = open("filetexted.txt","w")
file2.write("this is the first session that we will be taing"+"\n\n")
file2.write(text)#here we write the data of the text
file2.close()

for i in range(100):
    file3 = open("fieltexted.txt","a")
    file3.write(str(i)+'\n')
    file3.close()
for i in range(200):
    file3 = open("fieltexted.txt","a")#here we define the opened file for the acess
    file3.write(str(i)+'\n')
    file3.close()
    pass
file4 = open("mynativefile.txt","w")
file4.write(text)
file4.close()
for i in range(1000):
    with open("mynativefile.txt",'a') as file5:
        file5.write(str(i*10)+'\n')
        file5.close()#even without this the file will work
for i in range(1000):
    with open("mynativefile1.txt",'a') as file6:
        file6.write(str(i*10)+'\n')

        




    

