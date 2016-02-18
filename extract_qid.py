# calculate the number of examples in the training set

import re

f_in = open('qapair.txt', 'r')
f_out = open('qid_ex.txt', 'w')

examples = 0
for line in f_in:
    info = line.split(',')
    qid = info[0]
    num_a = info[-1]
    if int(num_a) >= 3:
        print num_a
        examples = examples + 1        
        f_out.write(qid+'\n')
        print qid
            
print examples

f_in.close()
f_out.close()
