report = []
f = open("input.txt", "r")
lines = f.readlines()
## one line function adding each occurence of `lines` to the list `calories`
value = [entry.strip() for entry in lines]
#value = [entry.strip() for entry in lines]
#print(value)

for levelSplit in value:
    check = levelSplit.split()
    report.append(check)
    #print(check)
print(report)
print(check)
#for nums in report:

#for i in range(len(report)):
#     report[i] = int(report[i])
     
for i, level in enumerate(report[:-1]):
    if level == report[i+1]:
        print("foo")
