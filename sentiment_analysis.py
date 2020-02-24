# Function to remove punctuations from tweet
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@', '\n']
def strip_punctuation(s):
    for item in punctuation_chars:
        if item in s:
            s = s.replace(item,"")
    return s


# lists of positive words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

# Function to find number of positive words in tweet
def get_pos(s):
    l = list(s.split(" "))
    count = 0
    for item in l:
        if strip_punctuation(item).lower() in positive_words:
            count+=1
    return count                   


# lists of negative words to use
negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

# Function to find number of negative words in tweet
def get_neg(s):
    l = list(s.split(" "))
    count = 0
    for item in l:
        if strip_punctuation(item).lower() in negative_words:
            count+=1
    return count  

print("Enter a tweet: ")
tweet = input()
p = get_pos(tweet)
n = get_neg(tweet)
print("Tweet: ",tweet,"\nPositive words: ",p,"\nNegative words: ",n,"\nOverall: ",p-n)



# ==================== To work with a database ===========================

# # List to keep all the words of all the tweets
# final_data = []
# with open("project_twitter_data.txt") as pos_f:
#     for line in pos_f:
#         data = line.split(",")
#         final_data.append(data)
# final_data = final_data[1:]
# #print(final_data)


# # List to store final results
# ans = []
# for item in final_data:
#     tweet = item[0]
#     p = get_pos(tweet)
#     n1 = get_neg(tweet)
#     overall = p-n1
#     ans.append([int(item[1]),int(strip_punctuation(item[2])),p,n1,overall])
# #print(ans)


# # Storing the results in a file "resulting_data.txt"
# with open('resulting_data.txt', 'w') as file:
#     file.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score\n")
#     print("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
#     for item in ans:
#     	print(item)
#     	for i in range(4):
#     		file.write("%d, " % item[i])
#     	file.write("%d\n" % item[-1])

    