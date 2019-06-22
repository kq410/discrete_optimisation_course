#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple
Item = namedtuple("Item", ['index', 'value', 'weight'])

def solve_it(input_data):
    """
    This function takes in the set of input_data for the knapsack
    problem and solves it. It returns the solution as output_data.
    """

    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    items = []

    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i-1, int(parts[0]), int(parts[1])))



    # a trivial greedy algorithm for filling the knapsack
    # it takes items in-order until the knapsack is full
    value = 0
    weight = 0
    taken = [0]*len(items)
    the_table = \
    dynamic_programming_knapsack(capacity, items, table = None, item_number = 0)

    solution_list = trace_back(the_table, items)

    # for item in items:
    #     if weight + item.weight <= capacity:
    #         taken[item.index] = 1
    #         value += item.value
    #         weight += item.weight

    # prepare the solution in the specified output format
    output_data = str(the_table[-1][-1]) + ' ' + str(1) + '\n'
    output_data += ' '.join(map(str, solution_list))
    return output_data

def dynamic_programming_knapsack(capacity, item, table = None, item_number = 0):
    """
    This function takes in the capacity of the knapsack, and
    the item list to build up the dynamic table
    """
    # if all itmes have been checked, DP is finished

    if item_number == len(item):
        return None
    # if there is no table, initialise the table
    if table == None:
        table = [[0] for rows in range(capacity + 1)]

    for row_idx in range(len(table)):
        # if the item's weight is less than the capacity at each row
        # then compare the value of the previous col of the same row
        # against the value of the previous col with row = row - weight
        if item[item_number].weight > row_idx:
            value_to_put = table[row_idx][item_number]

        else:
            value_to_put = max(table[row_idx][item_number],
                table[row_idx - item[item_number].weight][item_number] \
                + item[item_number].value)


        table[row_idx].append(value_to_put)

    item_number += 1
    next_table = table
    dynamic_programming_knapsack(capacity, item, next_table, item_number)


    return next_table


def trace_back(table, items):
    """
    This function takes in the solution table and
    returns the list of decisions for each item
    """
    # column length of the table
    col_length = len(table[0])
    back_ward_col = -1
    back_ward_row = -1
    solution_list = []

    while back_ward_col + col_length > 0:
    # start with the last entry
        last_entry = table[back_ward_row][back_ward_col]
        # check if the last item is taken or not
        if table[back_ward_row][back_ward_col] == \
        table[back_ward_row][back_ward_col - 1]:

            solution_list.insert(0, 0)

        else:
            solution_list.insert(0, 1)
            back_ward_row += -items[back_ward_col].weight
        back_ward_col += -1

    return solution_list




if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)')
