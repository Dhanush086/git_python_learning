#Reverse a String
n="python"
print(n[::-1])
#Count Vowels
m="education"
vowels='aeiou'
count=0
for i in m:
    if i in vowels:
        count+=1
print(count)
#Palindrome Checker
s="madam"
if s==s[::-1]:
    print("is a palindrome")
else:
    print("not a palindrome")
#Count Words
k="Python is very easy"
count=0
for i in k.split():
    count+=1
print(count)
#Character Frequency
t="programming"
n="g"
count=0
for i in t:
    if i in n:
        count+=1
print(count)
#. Remove Duplicate Characters
j="programming"
print("".join(set(j)))
#2nd method
j="programming"
l=[]
for i in j:
    if i not in l:
        l.append("".join(l))
print(l)
#First Non-Repeating Character
g="aabbcde"
for i in g:
    if i[0]==1:
        break
print(i)
#Check Anagrams
m="listen"
k="silent"
if sorted(m)==sorted(k):
    print("anagram")
else:
    print("not a anagram")
#the Longest Word
i="Python programming is interesting"
for j in i.split():
    if j[0]<j[1]:
        continue
print(j)
#Compress a String
p="aaabbccccd"
count=0
for i in p:
    count+=1
    print(i,count,end="")
##
print("i am working on a new feature")

    
    



    


