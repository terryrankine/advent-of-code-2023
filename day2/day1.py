import dataread
import re

limits = {
    'red':12,
    'blue':14,
    'green':13
}

passing = []

def processGame(id, game):
    red, blue, green = 0,0,0
    if 'red' in game:
        red = int(re.search('(\d+) red', game).group(1))
    if 'blue' in game:
        blue = int(re.search('(\d+) blue', game).group(1))
    if 'green' in game:
        green = int(re.search('(\d+) green', game).group(1))
    return (red, blue, green)


def test1():
    failing = []
    total = []
    for line in dataread.test.splitlines():
        id, pics = line.split(':')
        pics = pics.split(';')
        for draw in pics:
            red, blue, green = processGame(id, draw)
            if red <= limits['red'] and blue <= limits['blue'] and green <= limits['green']:
                pass
            else:
                failing.append( int(id.split()[1]))
                break
        total.append (int(id.split()[1]))
    print (sum(total) - sum(failing))

def part1():
    failing = []
    total = []
    for line in dataread.data:
        id, pics = line.strip().split(':')
        pics = pics.split(';')
        for draw in pics:
            red, blue, green = processGame(id, draw)
            if red <= limits['red'] and blue <= limits['blue'] and green <= limits['green']:
                pass
            else:
                failing.append( int(id.split()[1]))
                break
        total.append (int(id.split()[1]))
    print (sum(total) - sum(failing))



def test2():
    runningtotal = 0
    redmax, bluemax, greenmax = 0,0,0

    for line in dataread.test.splitlines():
        id, pics = line.strip().split(':')
        pics = pics.split(';')
        for draw in pics:
            red, blue, green = processGame(id, draw)
            redmax = max(red,redmax)
            bluemax = max(bluemax,blue)
            greenmax = max (greenmax,green)
        runningtotal += redmax*bluemax*greenmax
        redmax, bluemax, greenmax = 0,0,0
    print(runningtotal)

def part2():
    runningtotal = 0
    redmax, bluemax, greenmax = 0,0,0

    for line in dataread.data:
        id, pics = line.strip().split(':')
        pics = pics.split(';')
        for draw in pics:
            red, blue, green = processGame(id, draw)
            redmax = max(red,redmax)
            bluemax = max(bluemax,blue)
            greenmax = max (greenmax,green)
        runningtotal += redmax*bluemax*greenmax
        redmax, bluemax, greenmax = 0,0,0

    print(runningtotal)


test1()
part1()
test2()
part2()
