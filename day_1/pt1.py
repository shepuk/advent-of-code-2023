with open('input.txt', 'r') as f:
    lines = f.readlines()

first_digit = ''
last_digit = ''
total = 0

for line in lines:
    for char in line:
        if char.isdigit():
            first_digit = char
            break
    for char in line[::-1]:
        if char.isdigit():
            last_digit = char
            break
    total += int(first_digit + last_digit)

print(total)



