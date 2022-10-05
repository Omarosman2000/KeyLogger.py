import keyboard

a_list = []
def first_hotkey():
    print("You pressed on a SPACE!")
keyboard.add_hotkey('space', lambda: print('you pressed on a SPACE!'))

def second_hotkey():
    print("ctrl+shift+a")
keyboard.add_hotkey('ctrl+shift+a', lambda : print('triggered', 'hotkey'))

def key_was_pressed(event):
    my_file = open("text.txt", "a")
    #my_file.write("more text")
    keypressed = (event.name)
    print(keypressed)
    a_list.append(event.name)
    if len(a_list) == 10:
        for element in a_list:
            my_file.write(element)
        my_file.write("\n")
        keypressed.clear()
    my_file.close()
keyboard.on_press(key_was_pressed)
keyboard.wait()


