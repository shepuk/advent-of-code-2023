with open('input.txt', 'r') as text:
    lines = text.readlines()
    # remove newlines
    lines = [line.rstrip() for line in lines]


summed_total = 0

for index, line in enumerate(lines):
    max_red = 0
    max_green = 0
    max_blue = 0
    line = line.replace(',', '')
    line =line.replace(';', '')
    line = line.replace(':', '')
    line = line.split(' ')
    for i, l in enumerate(line):
        if i % 2 == 0: #even
            key = l #number
        if i % 2 != 0: #odd
            value = l #colour
            if value == 'red' and int(key) > max_red:
                max_red = int(key)
            if value == 'green' and int(key) > max_green:
                max_green = int(key)
            if value == 'blue' and int(key) > max_blue:
                max_blue = int(key)
    max_nos_multiplied = max_red * max_green * max_blue
    summed_total += max_nos_multiplied

print(summed_total)

