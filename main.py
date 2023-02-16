# python3
# Nikita Plotnikovs 221RDB021
from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    vieta=0 #to return position if stack is empty
    for i, next in enumerate(text):
        if next in "([{":
            vieta+=1
            opening_brackets_stack.append(Bracket(next,i+1))
            pass

        if next in ")]}":
            vieta+=1
            if opening_brackets_stack:
                #print(opening_brackets_stack)
                if are_matching(opening_brackets_stack[len(opening_brackets_stack)-1].char,next):
                    #print(
                    opening_brackets_stack.pop()#)
                    #print(opening_brackets_stack)
                else:
                    return opening_brackets_stack[len(opening_brackets_stack)-1].position +1
                pass
            else: 
                return vieta
    if not opening_brackets_stack:
        return 0
    else:
        return opening_brackets_stack[len(opening_brackets_stack)-1].position
#(((((((()) - it will return the position of the last unclosed braket
#What: Use an input to choose files or input - F or I If input I, wait for another input to input the brackets.
#test one should pass
#code after for loop

def main():
    text = input()
    if 'I' in text:
        text = input()
        mismatch = find_mismatch(text)
        if mismatch==0:
            print("Success")
            #print(mismatch)
        else:
            print(mismatch)

if __name__ == "__main__":
    main()
