# Generate the qapair.txt 
# Display the Question-Answer_Vote-NumOfAnswer

import re

f1 = open('answer.json', 'r')
f2 = open('qapair.txt', 'w')
#f2 = open('answer_vt_vtnum.txt', 'w')

line1 = f1.readline()
info1 = line1.split('"')
pre_qid = info1[3]
pre_vote = info1[-2]
f2.write(pre_qid+','+pre_vote)
#line = f1.readline()

#while line :
num_vote = 0
example = 0     #number_question wihch num of answers > 3 

for line in f1:
    info = line.split('"')
    cur_qid = info[3]
    print cur_qid
    cur_vote = info[-2]
    if cur_qid == pre_qid :
        f2.write(','+cur_vote)
        num_vote = num_vote + 1
    else :
        f2.write(','+str(num_vote + 1))
        num_vote = 0
        f2.write('\n'+cur_qid+','+cur_vote)
    pre_qid = cur_qid

    
#f2.flush()
f1.close()
f2.close()

f = open('qapair.txt', 'r')
examples = 0

for line in f:
    info = line.split(',')
    qid = info[1]
    num_a = info[-1]
    if num_a >= 3:
        examples = examples + 1        
        print qid

print examples
f.close()












