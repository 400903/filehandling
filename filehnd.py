#FILE HANDLING-------------------------------
''''
file paths are 2 typees
1.absolute psth-router folder
2.relative path-currnt working folder
'''

#('X') TO CREATE A FILE------------------------------------------'''
# f1=open('filehandling.txt','x')
# f1.close() # txt file is created in user/user/pythonfiles



'''1.access mode 'w' is overwritting'''

#TO INSERT DATA INTO A FILE------------------------------------
#SYNTAX:
''' 
VARIABLE=OPEN(FILENAME.FORMAT,'W')
VARIABLE.WRITE('ELABORATE HERE')
VARIABLE.CLOSE()
'''
#FILE EXIST--------------------------------
'''BELOW FILE OVERWRITE WITH THE LOWER BELOW FILE'''

# f1=open('filehandling.txt','w')
# f1.write("my rahul i am from narayanaet") #1st step ceated file in above commaand now we inserted into that
# f1.close()

# f1=open('filehandling.txt','w')
# f1.write("my rahul i am from narayanaet i enrolled python coarse")
# f1.close()# again we insert some txt on top of above  step so it overwriting

#FILE DOESN'T EXIST--------------------
'''IF FILE IS NOT PRESENT, NEW FILE IS CREATED AND DATA INSERTED'''

# f1=open('filehand.txt','w')
# f1.write("on monday i need to discuss binary data types")
# f1.close() # here new created new file and stored data at once (single) instead of create file nd write a data into that

#EXMPALE=1
# FRONTEND=['HTML','CSS', 'JAVA','PYTHON', 'SQL']
# f1=open('javafiles.txt','w')
# f1.writelines(FRONTEND)
# f1.close()
# #output= HTMLCSSJAVAPYTHONSQL

# FRONTEND=['HTML'," ",'CSS'," ",'JAVA'," ",'PYTHON'," ",'SQL']
# f1=open('javafiless.txt','w')
# f1.writelines(FRONTEND)
# f1.close()
#answer is= HTML CSS JAVA PYTHON SQL (with space come)



''' access mode 'r' ''' 
# this for show or reading the data ======================================

# # f1=open('filehand.txt','r')
# print(f1.read())
# # f1.close()

# read() takes parameter-------------------------------------------


# f1=open('filehand.txt','r')#we are reading here using print so read 5 positions only
# print(f1.read(5))

# f1=open('filehand.txt','r')#we are reading here using print so read 5 positions only
# print(f1.read(8))
# print(f1.read(11))
# print(f1.read(14))
# f1.close()


#readlines()will not take parameter------------------------------------------

# f2=open('expehand.txt','r')
# print(f2.readline())# answer is this['bangalore is a big city'] but if u re run it changes see
# print(f2.readline())
# print(f2.readline())
# f2.close()


''' access mode 'a'  is appending''' 

# @file exist------------------------------------

# k1=open('appendfile.txt','w')
# k1.write("today ipl match is chennai super kings vs mumbai,")#normal file created till here
# k1.close() 

# k2=open('appendfile.txt','a') # for same file we are appending some txt
# k2.write(" " "here toss was won by csk") #here i given space so it will append with space with earlier data
# k2.close()

#@file doesn't exist--------------------------------

# f1=open('newfilecreate.txt','a')
# f1.write('korra')
# f1.close()



'''  'R+'  (read nd write) -------------------------------'''

j1=open('appendfile.txt','r+')
print(j1.read)
j1.write("mumbai loss the match")
print(j1.read)
j1.close()