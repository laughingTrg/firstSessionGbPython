import sys

if len(sys.argv) > 2:
    start_num = int(sys.argv[1])
    end_num = int(sys.argv[2])
elif len(sys.argv) > 1:
    start_num, end_num = int(sys.argv[1]), None
else:
    start_num, end_num = None, None

with open('bakery.csv', 'r+', encoding='utf-8') as file:
    for num, line in enumerate(file):
        if start_num and end_num:
            if num + 1 >= start_num and num + 1 <= end_num: print(line.strip())
        elif start_num:
            if num + 1 >= start_num: print(line.strip())
        else:
            print(line.strip())




