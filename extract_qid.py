# calculate the number of examples in the training set

def extract_qid(PATH_IN, PATH_OUT) :

    #f_in = open(PATH_IN + 'qapair.txt', 'r')
    #f_out = open(PATH_OUT + 'qid_ex.txt', 'w')    
    
    with open(PATH_IN + 'qapair.txt', 'r') as f_in, \
    open(PATH_OUT + 'qid_more_3', 'w') as f_out1,     \
    open(PATH_OUT + 'qid_less_3', 'w') as f_out2:
        examples = 0
        for line in f_in:

            info = line.split(',')
            qid = info[0]
            num_answer = info[-1]

            if int(num_answer) >= 3:
                # print num_a
                # examples = examples + 1        
                    f_out1.write(qid+'\n')
                # print qid`
                else :
                    f_out2.write(qid+'\n')


                    #f_in.close()
                    #f_out.close()
