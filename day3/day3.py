import dataread
import math
import re

import re

def find_continuous_numbers_not_near_symbols(rows):
    symbols_positions = set()

    # Find symbols and their positions
    for row_number, row in enumerate(rows):
        for match in re.finditer(r'[^\w\s.]', row):
            symbol_start, symbol_end = match.span()
            symbols_positions.add((row_number, symbol_start, symbol_end, match.group()))

    # Find positions of numbers
    numbers_positions = set()
    for row_number, row in enumerate(rows):
        for match in re.finditer(r'\d+', row):
            number_start, number_end = match.span()
            numbers_positions.add((row_number, number_start, number_end, match.group()))

    result = []

    near = False
    gears = {}
    # Check each number and identify continuous ones not near symbols
    for num_row, num_start, num_end, actual_num in numbers_positions:
        for i in range (num_start, num_end):
            for sym_row, sym_start, sym_end, actual_symbol in symbols_positions:
                if abs(sym_row-num_row) <= 1 and abs (sym_start-i) <= 1:
                    near=True
                       
        if near==True:
            result.append(int(actual_num))
        near=False
    
        
        
                    
    
    return result


def find_gears(rows):
    symbols_positions = set()

    # Find symbols and their positions
    for row_number, row in enumerate(rows):
        for match in re.finditer(r'[^\w\s.]', row):
            symbol_start, symbol_end = match.span()
            symbols_positions.add((row_number, symbol_start, symbol_end, match.group()))

    # Find positions of numbers
    numbers_positions = set()
    for row_number, row in enumerate(rows):
        for match in re.finditer(r'\d+', row):
            number_start, number_end = match.span()
            numbers_positions.add((row_number, number_start, number_end, match.group()))

    result = []

    near = False
    gears = {}
    # Check each number and identify continuous ones not near symbols
    for sym_row, sym_start, sym_end, actual_symbol in symbols_positions:
        if actual_symbol == '*':
            for num_row, num_start, num_end, actual_num in numbers_positions:
                for i in range (num_start, num_end):
                    if abs(sym_row-num_row) <= 1 and abs (sym_start-i) <= 1:
                        near=True
                        if (sym_row, sym_start) in gears.keys():
                            gears[(sym_row, sym_start)].append(int(actual_num))
                        else:
                            gears[(sym_row, sym_start)] = [int(actual_num)]
                        break
                    
        if near==True:
            result.append(int(actual_num))


        near=False
    
    runningtotal = 0
    finalgears = []
    for key,gear in gears.items():
        if len(gear) == 2:
            runningtotal += gear[0]*gear[1]
            finalgears.append(sorted(gear))
    print ('Gears-v2: ', runningtotal)
        
        
                    
    
    return result




def test1():
    print (sum(find_continuous_numbers_not_near_symbols(dataread.test)))
    
    return 


def part1():
    print (sum(find_continuous_numbers_not_near_symbols(dataread.data)))
    return


def test2():
    find_gears(dataread.test)
    return

def part2():
    find_gears(dataread.data)
    return


test1()
part1()
test2()
part2()