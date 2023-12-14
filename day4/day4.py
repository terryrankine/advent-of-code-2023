import dataread
import math
import re


def find_intersect(input):
    runningtotal = 0
    winningcards = []

    for card, line in enumerate(input, start=1):
        # Use regular expression to extract numbers from both sets
        match = re.search(r'(\d+(?:\s+\d+)*)\s+\|\s+(\d+(?:\s+\d+)*)', line)

        if match:
            set1_str, set2_str = match.groups()
                        
            # Convert the string representations of sets into actual sets
            set1 = set(map(int, set1_str.split()))
            set2 = set(map(int, set2_str.split()))

            # Find the intersection (AND) of the sets
            intersection_set = set1 & set2

            # Print the sets and their intersection
            #print("Intersection of Set 1 and Set 2:", intersection_set, math.floor(math.pow(2, len(intersection_set)-1)))
            
            winningcards.append([card, len(intersection_set), math.floor(math.pow(2, len(intersection_set)-1))])
            runningtotal += math.floor(math.pow(2, len(intersection_set)-1))
            
        else:
            print("No sets found in the input string.")
        
    print (runningtotal, winningcards)
    
    finaldict={}
    
    for cardnum,orijwins,k in winningcards:
        print('card', cardnum)
        if cardnum in finaldict.keys():
            finaldict[cardnum] += 1
            cardcount = finaldict[cardnum]
        else:
            finaldict[cardnum] = 1
            cardcount = 1
        
        for totalcards in range(cardcount):
            for card in range(cardnum+1,cardnum+orijwins+1):
                if card in finaldict.keys():
                    finaldict[card] += 1
                else:
                    finaldict[card] = 1

    print (sum(finaldict.values()))



def test1():
    find_intersect(dataread.test)
    
    return 


def part1():
    find_intersect(dataread.data)
    return


def test2():
    #find_gears(dataread.test)
    return

def part2():
    #find_gears(dataread.data)
    return


test1()
part1()
test2()
part2()