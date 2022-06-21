import os, re
from datetime import datetime
os.system("cls")

print("GTFO DataBlock Edit Helper\n")

def run_regex(data):
    os.system("cls")
    note = """
Most Useful For GTFO:

r'\s+"<something>": [0-9]+.[0-9]+' this is useful because GTFO has most of its values stored as float with decimal points,
it will look for entires that begin with a space of tab and then replace

"<something>": [0-9]+.[0-9]+ this is practically the same as the above but this one will replace values that aren't separated

"<something>": [0-9][0-9][0-9]+ this can find up to three digit numbers, useful for the small rest of variables like IDs

r'\s' looks for spaces in front
+ means more than 1  | also groups numbers so that they don't appear as single digits
* means 0 or more
? means 0 or 1
^ means starts with  | ^run
$ means ends with    | gun$

r'\\n$' is useful when a line doesn't end with ' , ' but instead a new line

Full Guide = https://www.w3schools.com/python/python_regex.asp
"""
    print(note)
    pattern = input("Pattern: ")
    pattern = eval(pattern)
    replace = input("Replacement: ")
    amount = len(re.findall(pattern, data))
    data = re.sub(pattern, replace, data)
    
    return data, pattern, amount

name = input("Name of the file: ")
path = os.path.dirname(__file__) + f"\{name}"
regex = False

while True:
    try:
        file = open(path)
        data = file.read()
        file.close()
        break
    except FileNotFoundError:
        print("File not found")
        name = input("Name of the file: ")
        path = os.path.dirname(__file__) + f"\{name}"

mode = input("Type 1 to enable simple REGEX mode | Type 2 to enable all occurrences mode (no REGEX numbers, only specific ones): ")

while True:
    if mode == "1":
        regex = True
        break
    elif mode == "2":
        to_find = input("What are you searching for: ")
        to_rep = input("What should it be replaced with: ")
        found = data.count(to_find)
        data = data.replace(to_find, to_rep)
        break
    else:
        print("Invalid mode ID")
        mode = input("Type 1 to enable REGEX mode | Type 2 to enable all occurrences mode: ")

if regex == True:
    data, pattern, amount = run_regex(data)

new_name = input("\nShould the output file have a specific name or should it be generic? (leave blank for generic)")

now = datetime.now()
now = now.strftime("%B_%d_%Y-%Hh%Mm%Ss")
name = os.path.splitext(name)
if len(new_name) == 0:
    new_name = f"{now}{name[1]}"

path_save = os.path.dirname(__file__) + f"\{now}"
os.mkdir(path_save)

path_save_file = path_save + f"\{new_name}"
save = open(path_save_file, "x")
save.write(data)
save.close()

if regex == False:
    print(f"\nData [{to_find}] was found {found} times throughout the file.\nOutput saved in {path_save} folder")
else:
    print(f"\nPattern [{pattern}] was matched {amount} times throughout the file.\nOutput saved in {path_save} folder")