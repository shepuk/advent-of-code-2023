import re

with open('testinput.txt', 'r') as text:
    lines = text.readlines()
    # remove newlines
    lines = [line.rstrip() for line in lines]

for index, line in enumerate(lines):
   #print(line)
    print(re.findall('[0-9]+', line))
    print(re.findall('[^a-zA-Z\.]', line))

    #todo
    # find number position in line
    # check line above and below using index
    # remember to also check left and right of number
    # if adjacent tiles are NOT a period and NOT a number, then add the number