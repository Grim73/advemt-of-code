f = open("input.txt", "r")
lines = f.readlines()
## one line function adding each occurence of `lines` to the list `calories`
value = [entry.strip() for entry in lines]
print(value)

container = []
numbers = [1,2,3,4,5,6,7,8,9,0]
for num in value:
    print(num)
    input()
    for words in  num:
        words.split()
    container.append(num)
    print(container)
print(value)
print(container)
