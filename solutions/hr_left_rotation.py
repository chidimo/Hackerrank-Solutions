"""Left Rotation"""

def left_rotation():
    r"""https://www.hackerrank.com/challenges/array-left-rotation?

    A left rotation operation on an array of size $n$ shifts each of the
    array's elements $1$ unit to the left. For example, if $2$ left rotations
    are performed on array $[1, 2, 3, 4, 5]$, then the array would become $[3, 4, 5, 1, 2]$.

    Given an array of $n$ integers and a number, $d$, perform $d$ left rotations on the array.
    Then print the updated array as a single line of space-separated integers.

    Input Format

    The first line contains two space-separated integers denoting the respective values of
    $n$ (the number of integers) and $d$ (the number of left rotations you must perform).
    The second line contains $n$ space-separated integers describing the respective
    elements of the array's initial state.

    Constraints

    $
    1 \le n \le 10^5\\
    1 \le d \le n\\
    1 \le a_i \le 10^6
    $
    """
    inputs = input().split()
    # number_of_integers = int(inputs[0])
    number_of_left_rotations = int(inputs[1])
    input_array = input()
    array_list = [x for x in input_array.split()]

    while number_of_left_rotations > 0:
        array_list.append(array_list.pop(0))
        number_of_left_rotations -= 1
    print(' '.join(array_list))
