from collections import Counter

myList = [1,2,3,5,4,6,6,8,8,6,4,7,8,7,7,9,7,8,7,4,5,4,1,4,2,5,6,2,2,1,5,1,3]

newCounter = Counter (myList)
print(newCounter)
print("")

name = "Prince Alfred Gyan"
print(Counter(name))
print("")

punchLine = "When the boss is around who can you boss around, i'm a rare breed no wonder i'm in a rare form"
wordSplit = punchLine.split()
print(Counter(wordSplit))
newWordsplit = Counter(wordSplit)

print (newWordsplit.most_common(3))
print(newWordsplit.values())