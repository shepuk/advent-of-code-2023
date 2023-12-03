with open('input.txt', 'r') as f:
    lines = f.readlines()
    # remove newlines
    lines = [line.rstrip() for line in lines]

numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
lookup = {
    'one': "1",
    'two': "2",
    'three': "3",
    'four': "4",
    'five': "5",
    'six': "6",
    'seven': "7",
    'eight': "8",
    'nine': "9",
}

total = 0

for line in lines:
    flag = False
    flag2 = False
    first_digit = ''
    last_digit = ''
    print(line)
    for char in line:
        print(first_digit)
        if char.isdigit():
            first_digit = char
            break
        first_digit += char
        for num in numbers:
            if num in first_digit:
                first_digit = lookup[num]
                flag2 = True
                break
        if flag2:
            break
    for char in line[::-1]:
        print(last_digit[::-1])
        if char.isdigit():
            last_digit = char
            break
        last_digit += char
        for num in numbers:
            if num in last_digit[::-1]:
                last_digit = lookup[num]
                flag = True
                break
        if flag:
            break
        
            
    print(first_digit, last_digit)
    total += int(first_digit + last_digit)

print(total)



# most of this was done my reese!



