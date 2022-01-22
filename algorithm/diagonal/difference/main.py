#!/usr/bin/python3

def solution(input):
    dleft = []
    dright = []
    cursor_left = 0
    cursor_right = len(input)-1
    is_valid = True

    for el in input: 
        is_valid = all(-100 <= i <= 100 for i in el)
        if not is_valid:
            break
        dleft.append(el[cursor_left])
        dright.append(el[cursor_right])
        cursor_left += 1
        cursor_right -= 1

    print("cursor left", dleft)
    print("cursor right", dright)
    result = abs(sum(dleft) - sum(dright)) if is_valid else None

    print(result)


if "__main__" == __name__:
    input = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
    solution(input)
