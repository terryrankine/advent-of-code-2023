import dataread
import re

subs = {
    'nine':'9',
    'eight':'8',
    'seven':'7',
    'six': '6',
    'five': '5',
    'four': '4',
    'three': '3',
    'two': '2',
    'one': '1',
    'zero':'0',
}

def get_digit(x):
        return x if x.isnumeric() else str(letter_digits.index(x))


def readfirstandlast(line):
    firstnum = re.findall(r'(zero|one|two|three|four|five|six|seven|eight|nine|\d)', line)[0]
    lastnum = re.findall(r'(?=(zero|one|two|three|four|five|six|seven|eight|nine|\d))', line)[-1]

    if firstnum in subs.keys():
        firstnum = subs[firstnum]
    if lastnum in subs.keys():
        lastnum = subs[lastnum]
    print (line, firstnum, lastnum, re.findall(r'(zero|one|two|three|four|five|six|seven|eight|nine|\d)', line))
    return int(firstnum+lastnum)

runningtotal = 0
for line in dataread.test.split():
    runningtotal += readfirstandlast(line)
print (runningtotal)


letter_digits = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
regex = r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))'
total = 0

runningtotal = 0
for line in dataread.data:


    runningtotal += readfirstandlast(line)
    digits = re.findall(regex, line)


    total += int(get_digit(digits[0]) + get_digit(digits[-1]))
    if runningtotal != total:
        break


print (runningtotal, total)
