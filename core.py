import os, re
from datetime import datetime
os.system("cls")

print("GTFO DataBlock Edit Helper\n")

def run_regex(data):
    os.system("cls")
    note = '''
Most Useful For GTFO:
'\\s+"<something>": [0-9]+.[0-9]+' this is useful because GTFO has most of its values stored as float with decimal points, it will look for entires that begin with a space of tab and then replace
"<something>": [0-9]+.[0-9]+ this is practically the same as the above but this one will replace values that aren't separated
"<something>": [0-9][0-9][0-9]+ this can find up to three digit numbers, useful for the small rest of variables like IDs
+ means more than 1  | also groups numbers so that they don't appear as single digits
* means 0 or more
? means 0 or 1
^ means starts with  | ^run
$ means ends with    | gun$
\s looks for spaces in front
\\n$ is useful when a line doesn't end with ' , ' but instead a new line
\\t is a better way of marking '    ' (TAB)

Full Guide = https://www.w3schools.com/python/python_regex.asp

Remember that if both \" and \' are a part of what you're looking for, you can use triple quotation marks around your pattern, e.g ( """ "Test" = 'Done' """) (Yes, you MUST put those)
'''
    print(note)
    pattern = input("Pattern: ")
    while True:
        try:
            pattern = eval(pattern)
            break
        except (NameError, SyntaxError):
            print("You forgot to add quotation marks around the pattern or input was empty")
            pattern = input("Pattern: ")
    replace = input("Replacement: ")
    amount = len(re.findall(pattern, data))
    data = re.sub(pattern, replace, data)
    
    return data, pattern, replace, amount

def main(name, data):
    try:
        os.mkdir(os.path.dirname(__file__) + "\input")
    except FileExistsError:
        pass

    try:
        os.mkdir(os.path.dirname(__file__) + "\output")
    except FileExistsError:
        pass

    if len(data) == 0:
        name = input("Name of the file: ")
        path = os.path.dirname(__file__) + f"\input\{name}"
        while True:
            try:
                file = open(path)
                data = file.read()
                file.close()
                break
            except FileNotFoundError:
                print("File not found")
                name = input("Name of the file: ")
                path = os.path.dirname(__file__) + f"\input\{name}"

    regex = False
    mode = input("\nType 1 to enable simple REGEX mode | Type 2 to enable all occurrences mode (no REGEX numbers, only specific ones): ")
    
    while True:
        if mode == "1":
            regex = True
            break
        elif mode == "2":
            print('''
Remember that if both \" and \' are a part of what you're looking for, you can use triple quotation marks around what you're searching for, e.g ( """ "Test" = 'Done' """) (Yes, you MUST put those)\n''')
            to_find = input("What are you searching for: ")
            while True:
                try:
                    to_find = eval(to_find)
                    break
                except (NameError, SyntaxError):
                    print("You forgot to add quotation marks around what you're searching for or input was empty")
                    to_find = input("What are you searching for: ")
            to_rep = input("What should it be replaced with: ")
            found = data.count(to_find)
            data = data.replace(to_find, to_rep)
            break
        else:
            print("Invalid mode ID")
            mode = input("Type 1 to enable REGEX mode | Type 2 to enable all occurrences mode: ")

    if regex == True:
        data, pattern, replace, amount = run_regex(data)

    new_name = input("\nShould the output file have a specific name or should it be generic? (leave blank for generic)")

    now = datetime.now()
    now = now.strftime("%B_%d_%Y-%Hh%Mm%Ss")
    if len(name) == 0:
        name = os.path.splitext(name)
        name = name[1]
        if len(new_name) == 0:
            new_name = f"{now}{name}"
    else:
        new_name = f"{now}{name}"

    path_save = os.path.dirname(__file__) + f"\output\{now}"
    os.mkdir(path_save)

    path_save_file = path_save + f"\{new_name}"
    save = open(path_save_file, "x")
    save.write(data)
    save.close()

    if regex == False:
        print(f'\nData " {to_find} " was replaced with " {to_rep} " {found} times.\nOutput saved in {path_save} folder')
    else:
        print(f'\nPattern " {pattern} " was matched and replaced with " {replace} " {amount} times.\nOutput saved in {path_save} folder')

    again = input("\nType 1 to continue editing this file | Type 2 to continue with a new file | Leave blank to exit: ")
    if again == "1":
        main(name, data)
    elif again == "2":
        main("", "")
    else:
        exit()

main("", "")
