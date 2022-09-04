import random
import os
test_num = 100
wrong_num = 0
error_message = open('error.txt','wr')

for i in range(0,test_num):
    content = [str(random.randint(1,40)) for k in range(0,2)]
    content = ' '.join(content)
    f=open('test.txt','w')
    f.write(content)
    f.close()
    os.system("./mystery ./test.txt > result.txt")
    f = open('result.txt','rb')
    result = f.readlines()
    c_result = result[2].replace('\n','')
    asm_result = result[5].replace('\n','')

    if  c_result!=asm_result:
        print((str(i)+'is wrong'))
        wrong_num=wrong_num+1
        error_message.write("Test"+str(i)+" fails. "+"C result is "+c_result+" while asm result is "+asm_result+".")
        error_message.write("\n----------------------------------------------------------------\n")
        
os.remove('test.txt')
os.remove('result.txt')
error_message.close()
print( str(test_num-wrong_num)+' of '+str(test_num)+' tests have passed.')
if wrong_num==0:
    os.remove('error.txt')