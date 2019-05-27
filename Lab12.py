import re
count = 0
regex = r'^([1-8][0-9]|90)\..*(GET|POST).*(200).*'
with open('access.log.txt', "r") as file:
    data = file.readlines()
    for a in data:
        if(re.match(regex, a)):
            x = re.search(regex, a)
            print(x.group())
            count = count+1
    print(count)