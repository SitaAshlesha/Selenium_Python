file =  open('test.txt')
#print(file.read())
for i in file.readlines():
    print(i)



file.close()
