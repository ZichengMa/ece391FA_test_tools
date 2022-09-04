import random
import os
import linecache
test_num = 100
wrong_num = 0
error_message = open('error.txt','wr')
for i in range(0,test_num):
    size1 = random.randint(1,11)
    size2 = random.randint(1,11)
    content1 = [str(random.randint(1,11)) for k in range(0,size1)]
    content2 = [ str(random.randint(1,11)) for k in range(0,size2)]
    content1 = "\n".join(content1)
    content2 = "\n".join(content2)
    f=open('test1.txt','w')
    f.write(str(size1)+"\n")
    f.write(content1)
    f.close()
    f=open('test2.txt','w')
    f.write(str(size2)+"\n")
    f.write(content2)
    f.close()
    os.system("./edit_dist ./test1.txt ./test2.txt > result.txt")
    f = open('result.txt','rb')
    result = f.readlines()
    c_result = result[8].replace('\n','')
    asm_result = result[11].replace('\n','')

    if  c_result!=asm_result:
        wrong_num=wrong_num+1
        error_message.write("Test"+str(i)+" fails. "+"C result is "+c_result+" while asm result is "+asm_result +". Details are shown below:\n")
        error_message.write("List 1:\n"+content1)
        error_message.write("\nList 2:\n"+content2)
        error_message.write("\n--------------------\n")
os.remove('test1.txt')
os.remove('test2.txt')
os.remove('result.txt')
error_message.close()
print( str(test_num-wrong_num)+' of '+str(test_num)+' tests have passed.')
if wrong_num==0:
    os.remove('error.txt')