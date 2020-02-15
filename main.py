# Author: Ting-Chen Wang
# Computational Biology Spring 2020
# Assignment 4
# Due Date: 2/15/2020
# main

import sys

X = []  # declare a list for a set of pairwise distances list
width = 0  # declare the width
result = []  # the result list is used to store the output


def partial_digest(multiset):  # This function performs the PartialDigest Algorithm
    multiset_1 = multiset.copy()  # multiset_1 is used to check for appending duplicates
    global X, width
    width = max(multiset)  # width is set to the maximum value in multiset
    multiset.remove(width)  # remove width from multiset
    X = [0, width]  # X is a set of integers such that DX=L
    place(multiset, X, multiset_1)  # conduct partial digest recursive operations


def place(multiset, x_1, multiset_1):
    if len(multiset) == 0:  # if there is no pairwise distances left
        result.append(list(set(x_1)))  # append the result to a set
        return
    y = max(multiset)  # assign the max pairwise distance to y

    if subset(y, x_1, multiset):  # if the distance between y and points x_1 is in the pairwise distance set l
        x_1.append(y)  # add y to x_1
        remove_elements(y, x_1, multiset)  # remove lengths D(y, x_1) from l
        place(multiset, x_1, multiset_1)  # recursively operate the process
        if y in x_1:  # if a recursive call needs to backtrack
            x_1.remove(y)  # remove y from set x_1
        multiset.extend(distance(y, x_1, multiset))  # add the length of distances removed from the previous instruction
        # back the the pairwise distance set
        for i in multiset:
            if multiset.count(i) > multiset_1.count(i):  # if multiset after appending has more elements than the
                # beginning list
                multiset.remove(i)  # keep only the number of elements defined in the original list
                continue

    if subset(abs(width - y), x_1,
              multiset):  # if the complement distance between y and points x_1 is in the pairwise distance set l
        x_1.append(abs(width - y))  # add the complement point to x_1
        remove_elements(abs(width - y), x_1, multiset)  # remove lengths D(abs(width - y), x_1) from l
        place(multiset, x_1, multiset_1)  # recursively operate the process
        if abs(width - y) in x_1:  # if a recursive call needs to backtrack
            x_1.remove(abs(width - y))  # remove abs(width - y) from set x_1
        multiset.extend(distance(abs(width - y), x_1,
                                 multiset))  # add the length of distances removed from the previous instruction back
        #  to the pairwise distance set
        for i in multiset:
            if multiset.count(i) > multiset_1.count(
                    i):  # if multiset after appending has more elements than the beginning list
                multiset.remove(i)  # keep only the number of elements defined in the original list
                continue
    return


# This function finds the distance between point y and all other points  in the set X
# if the number of a certain element is more than the original list of contents after appending
# remove it from the list
def distance(y, x_1, multiset_1):
    difference = []
    for i in x_1:
        difference.append(abs(y - i))
        if difference.count(abs(y - i)) >= 2 and (difference.count(abs(y - i)) > multiset_1.count(abs(y - i))):
            difference.remove(abs(y - i))
    return difference


# if the distance between point y and
# a point in set x_1 is in the pairwise
# distance set l, remove it from the set l
def remove_elements(y, x_1, multiset):
    for i in x_1:
        if abs(y - i) in multiset:
            multiset.remove(abs(y - i))


# This function checks if a distance between point y
# and a point in set x_1 is in the pairwise distance
# set l
def subset(y, x_1, multiset):
    for i in x_1:
        if abs(y - i) not in multiset:
            return False
    return True


# main()
def main():
    if len(sys.argv) == 2:  # this program takes in 2 command line arguments
        multiset = list(map(int, sys.argv[1].split(',')))  # convert input list of strings to list of integers
        partial_digest(multiset)  # perform the partial digest algorithm
        if len(result) == 0:
            print("no result")
        else:
            res = list(
                set(tuple(sorted(sub)) for sub in result))  # each element in a set is sorted to eliminate duplicates
            for i in range(len(res)):
                print("The result is: ", res[i], ", and the number of integers is: ", len(res[i]))  # display the result
    else:
        exit(
            "Incorrect number of arguments.")  # print error message and exit the program if the number of arguments
        # is not correct


if __name__ == '__main__':
    main()
