with open('input.txt', 'r') as text:
    lines = text.readlines()
    # remove newlines
    lines = [line.rstrip() for line in lines]

max_red = 12
max_green = 13
max_blue = 14

summed_total = 0

for index, line in enumerate(lines):
    add_number = True
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
                add_number = False
            if value == 'green' and int(key) > max_green:
                add_number = False
            if value == 'blue' and int(key) > max_blue:
                add_number = False
    if add_number:
        game_number = line[1]
        summed_total += int(game_number)

print(summed_total)

