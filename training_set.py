# select the qa pair in the souce
# subject to num of answers >= 3


def filter_qid(PATH_IN, PATH_OUT) :
	
	with open(PATH_IN + 'qid_ex.txt', 'r') as f:
		qid_list = [line.strip() for line in f]

	f_in = open(PATH_IN + 'question.json', 'r')
	f_out = open(PATH_OUT + 'question_filtered.json', 'w')

	for line in f_in:
		info = line.split('"')
		qid = info[-2]
		if qid in qid_list:
			print qid
			f_out.write(line)

	f_in.close()
	f_out.close()
