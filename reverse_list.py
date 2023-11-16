# Author: Kristin Towns
# GitHub username: kristinlashun
# Date: November 15th, 2023
# Description: This program contains a function reverse_list that reverses the order of elements in a list in place.

def reverse_list(lst):
    start_index = 0
    end_index = len(lst) - 1

    while start_index < end_index:
        lst[start_index], lst[end_index] = lst[end_index], lst[start_index]

        start_index += 1
        end_index -= 1


