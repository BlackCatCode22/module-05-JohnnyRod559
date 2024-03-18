fname = input('Enter File: ')
if len(fname) < 1 : fname = 'C:\\Users\\Johnny\\PycharmProjects\\pythonProject11\\module-05-JohnnyRod559\\clown.txt'
elif len(fname) > 1 : fname = 'C:\\Users\\Johnny\\PycharmProjects\\pythonProject11\\module-05-JohnnyRod559\\intro.txt'
handle = open(fname)

di = dict()
for line in handle:
    line = line.rstrip()
   # print(line)
    words = line.split()
    #print(words)
    for word in words:
#if not the key is not there th count is zero

# idiom: retrieve/create/update counter
        di[word] = di.get(word,0) + 1


#print(di)

#now we want to find the most common word
largest = -1
the_word = None
for k,v in di.items() :

    if v > largest :
        largest = v
        the_word = k #capture/remember the word that is largest

print(the_word, largest)