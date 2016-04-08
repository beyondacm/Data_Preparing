# Generate the qapair.txt 
# File qapair.txt is in this format : 
# Question_id , Answer0_vote , Answer1_vote , ... , NumOfAnswer

import re

def generate_qapair(PATH_IN, PATH_OUT):

	f_in  = open(PATH_IN + 'answer.json', 'r')
	f_out = open(PATH_OUT + 'qapair.txt', 'w') 

	line1 = f_in.readline()
	info1 = line1.split('"')
	pre_qid = info1[3]
	pre_vote = info1[-2]
	f_out.write(pre_qid+','+pre_vote)

	num_vote = 0
	for line in f_in:
		info = line.split('"')
		cur_qid = info[3]
		print cur_qid
		cur_vote = info[-2]
		if cur_qid == pre_qid :
			f_out.write(','+cur_vote)
			num_vote = num_vote + 1
		else :
			f_out.write(','+str(num_vote + 1))
			num_vote = 0
			f_out.write('\n'+cur_qid+','+cur_vote)
		pre_qid = cur_qid

	f_out.flush()
	f_in.close()
	f_out.close()












