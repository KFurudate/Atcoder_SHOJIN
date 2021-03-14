from collections import Counter

n = int(input())
sentence = input()

# remove priod in the sentence
sentence = sentence[:-1]

words = sentence.split(" ")
words = Counter(words)

check_lst = ("TAKAHASHIKUN",
             "Takahashikun",
             "takahashikun")

cnt = 0
for check in check_lst:
    cnt += words[check]
print(cnt)