import matplotlib.pyplot as plt
import pandas as pd
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
def strip_punctuation(x):
    s=""
    for i in x:
        if i not in punctuation_chars:
            s=s+i
    return s
def get_pos(x):
    y=strip_punctuation(x)
    count=0
    y=y.lower()
    #print(y)
    my_list=y.split()
    #print(my_list)
    for item in my_list:
        if item in positive_words:
            count=count+1
    return count
def get_neg(x):
    y=strip_punctuation(x)
    count=0
    y=y.lower()
    #print(y)
    my_list=y.split()
    #print(my_list)
    for item in my_list:
        if item in negative_words:
            count=count+1
    return count
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())
negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
obj=open("project_twitter_data.csv","r")
line=obj.readlines()
no_of_lines=len(line)

re_tweet=[]
no_reply=[]
text_row=[]
get_positive=[]
get_negative=[]
get_netscore=[]

for row in line[1:no_of_lines+1]:
    vals=row.strip().split(',')
    re_tweet.append(vals[1])
    no_reply.append(vals[2])
    text_row.append(vals[0])
for a_line in text_row:
    get_positive.append(get_pos(a_line))
    get_negative.append(get_neg(a_line))
    
zip_obj=zip(get_positive,get_negative)
for i,j in zip_obj:
    get_netscore.append(i-j)
obj.close()

file_obj=open("resulting_data.csv","w")
file_obj.write("Number of Retweets,Number of Replies,Positive Score,Negative Score,Net Score")
file_obj.write('\n')
for l in range(no_of_lines-1):
    row_s='{},{},{},{},{}'.format(re_tweet[l],no_reply[l],get_positive[l],get_negative[l],get_netscore[l])
    file_obj.write(row_s)
    file_obj.write('\n')
file_obj.close()
data=pd.read_csv('resulting_data.csv')
get_netscore=data['Net Score']
re_tweet=data['Number of Retweets']
plt.scatter(get_netscore,re_tweet)
plt.xlabel('Net score')
plt.ylabel('Number of retweets')
plt.show()





