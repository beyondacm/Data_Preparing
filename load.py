from pandas import Series, DataFrame
import pandas as pd
import json
import numpy as np
import string

PATH_IN = './'
PATH_OUT = './'

def str_strip(data) :
    data = data.str.replace('\n','')
    data = data.str.replace('\r','')
    data = data.str.replace(',',' ')
    data = data.str.replace('.','')
    data = data.str.replace('"','')
    data = data.str.lower()   
    return data  
   
f1 = open(PATH_IN + 'answer.json')
f2 = open(PATH_IN + 'q_source.json')
f3 = open(PATH_IN + 'user.json')
f4 = open(PATH_IN + 'qtags.json')

answer = [json.loads(line.strip().strip(',')) for line in f1]
#print answer[0]
#answer_frame 
answer_frame = DataFrame(answer)
answer_frame = answer_frame.drop_duplicates('answer_id')
#print answer_frame #14781 x 5

question = [json.loads(line.strip().strip(',')) for line in f2]
#print question[0]
question_frame = DataFrame(question)
question_frame = question_frame.drop_duplicates('question_id')
#print question_frame  # 898 x 2


user = [json.loads(line.strip().strip(',')) for line in f3]
user_frame = DataFrame(user)
user_frame = user_frame.drop_duplicates('user_id')
#print user_frame    # 3378 x 14


qtag = [json.loads(line.strip().strip(',')) for line in f4]
qtag_frame = DataFrame(qtag)
qtag_frame = qtag_frame.drop_duplicates('question_id')
#print qtag_frame      # 9999 x 2



# Generate the source data
m1 = pd.merge(answer_frame, user_frame, how = 'outer')
m1 = m1.rename(columns = {'related_id':'question_id'})
#print m1.head()    # 14781 x 18


m2 = pd.merge(qtag_frame, question_frame)
#print m2.head()     # 898 x 3 


# Generate 
m = pd.merge(m1, m2, on = 'question_id')
#print m
m = m.sort(['question_id','answer_voted'], ascending=[1,0])
m = m.drop('user_address', axis=1)
m = m.drop('user_name', axis=1)
m = m.reset_index(drop=True)
#print m

# modify the string in dataframe m
m['answer_content'] = str_strip(m['answer_content'])
m['question_content'] = str_strip(m['question_content'])
m['user_edu'] = str_strip(m['user_edu'])
m['user_specialty'] = str_strip(m['user_specialty'])
m['user_interest'] = str_strip(m['user_interest'].astype(str))
m['user_intro'] = str_strip(m['user_intro'])
m['question_tags'] = str_strip(m['question_tags'].astype(str))
m['user_recommends'] = str_strip(m['user_recommends'].astype(str))
print m      # 3195 x 20

#m.to_json(PATH_OUT + 'total01.json')
m.to_csv(PATH_OUT + 'depress.csv', encoding='utf-8', index = False)


f1.close()
f2.close()
f3.close()
f4.close()

