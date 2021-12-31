if __name__ == "__main__":
    print("Welcome to the calculator program.")
    global current_value
    current_value = 0
    print("Current value: " + str(current_value))

def display_current_value():
    global current_value
    print("Current Value:", current_value)
if __name__ == "__main__":
    current_value = 0
    display_current_value()

def add(to_add):
    global current_value
    global prev_value
    current_value = current_value + to_add
    return(current_value)
if __name__ == "__main__":
    add(1)

def add2(value, to_add):
    value += to_add
    return value

def mult(to_mult):
    global current_value
    set_prev_value
    current_value *= to_mult

def div(to_div):
    global current_value
    if to_div == 0:
        print("Invalid Operation")
        return
    set_prev_value()
    current_value /= to_div

def memory(to_mem):
    global saved
    saved = to_mem
def recall():
    global saved
    global current_value
    set_prev_value()
    current_value = saved
def set_prev_value():
    global current_value
    global prev_value
    prev_value = current_value
def undo():
    global current_value
    global prev_value
    temp = prev_value
    set_prev_value()
    current_value = temp

if __name__ == "__main__":
    current_value = 0
    display_current_value()
    add(1)
    print(current_value)
    print((add2)(current_value,2))
    mult(2/3)
    print(current_value)
    div(0)
    print(current_value)
    div(.3)
    print(current_value)
if __name__ == "__main__":
     memory(current_value)
     add(5)
     recall()
     display_current_value()
     mult(0)
     add(4)
     undo()
