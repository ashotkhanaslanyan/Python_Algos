#
# Problem:
#
# In a list of length n+1
# containing numbers from 1 to n
# there is at least one repeating number
# due to the pigeon hole principle.
# Given that there can be only one repeating number
# which can repeat more that one times
# find that number.
#
# Limitations:
#
# Memory should be constant O(1)
# Input list is read only
# Time complexity should be less than O(n^2)
#
# Solution:
#
# Use floyd's turtle and hare algorithm
# to find a cycle in (key, value) pairs of
# turtle's and hare's positions.
# Find the starting index of the cycle,
# which will be the repeating number in the list.
#
# Implementation:
#


def turtle_step(turtle_pos, arr):

    # Turtle goes to the nest node
    turtle = (turtle_pos[1], arr[turtle_pos[1]])

    return turtle


def hare_step(hare_pos, arr):

    # Hare does two turle steps
    hare = turtle_step(turtle_step(hare_pos, arr), arr)

    return hare


def meet(turtle, hare, turtle_pos, hare_pos, arr):

    # Moves hare and turtle to their next positions
    turtle_pos = turtle(turtle_pos, arr)
    hare_pos = hare(hare_pos, arr)

    # If hare and the turtle are on the same positions returns
    # that position, if not recursively calls this function
    return turtle_pos if turtle_pos == hare_pos\
        else meet(turtle, hare, turtle_pos, hare_pos, arr)


def floyd_th(arr):

    # Gives hare and turtle staring positions 
    # at the beginning of the given array
    starting_pos = (0, arr[0])

    # Gets the meeting node of hare and turtle
    meet_pos = meet(turtle_step, hare_step, starting_pos, starting_pos, arr)

    # Two turtle start walking, one from starting node
    # and the other from meeting node.
    # They will meet at the node where cycle starts.
    # That node's index is the repeating number as
    # it has more than one parents.
    cycle_pos = meet(turtle_step, turtle_step, meet_pos, starting_pos, arr)
    repeating_num = cycle_pos[0]

    return repeating_num
    

#
# Tests: 
#


def main():

    print(floyd_th([5, 4, 1, 1, 2, 3]))
    print(floyd_th([5, 3, 4, 1, 2, 1, 6]))
    print(floyd_th([5, 4, 1, 1, 2, 1]))
    print(floyd_th([2, 2, 2]))
    print(floyd_th([1, 1]))
    print(floyd_th([4, 5, 6, 2, 1, 3, 4]))


if(__name__ == '__main__'):

    main()
