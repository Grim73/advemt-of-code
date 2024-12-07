colOne = []
colTwo = []
diffList = []
similarity = []

f = open("input.txt", "r")
lines = f.readlines()
## one line function adding each occurence of `lines` to the list `calories`
value = [entry.strip() for entry in lines]

#print(value)

for spaces in value:
    colSplit = spaces.split()
    colOne.append(colSplit.pop(0))
    colTwo.append(colSplit.pop())
    print(spaces.split())

for i in range(len(colOne)):

     colOne[i] = int(colOne[i])
     colTwo[i] = int(colTwo[i])

colOne.sort()
colTwo.sort()

for compare in colOne:
    compare2 = colTwo[colOne.index(compare)]
    print(compare2)
    if compare > compare2:
        diff = compare - compare2
        diffList.append(diff)

    else:
        diff = compare2 - compare
        diffList.append(diff)
print(sum(diffList))

for simCheck in colOne:
    # check each occurance of colOne against colTwo, add each to count
    # then multiply simCheck * sum(count
    # finally, add simResult to similarity[]
    

    simResult = simCheck * colTwo.count(simCheck) 
    similarity.append(simResult)
print(sum(similarity))
