"""notas
objetivo:
    voce consegue fazer anotaçoes rapidas, sendo gravadas em notes.txt

como usar:
    python3 notas.py new "<NOTA>"

    python3 notas.py read "<TAG>"
"""


import os
import sys
__version__ = "0.1.0"
argument = sys.argv[1:]
cmd = ("new", "read")
path = os.curdir
filepath=  os.path.join(path, "notes.txt")
if argument[0] not in cmd:
    print("comando invalido!")
    sys.exit(1)
if argument[0] == cmd[1]:
    tag = None
    tag_cmd = sys.argv[2]
    for line in open(filepath):
        name = line.split("\t")
        if name[1] == tag_cmd:
            print(f"Titulo: {name[0]}\nTag: {name[1]}\n - {name[2]} {'-'*25}")


if argument[0] == cmd[0]:
    name = sys.argv[2].strip()
    text = input("text: ").strip()
    if text == "":
        print("digite um nome!")
    tag = input("tag: ").strip()
    if tag == "":
        print("digite um texto!")

    with open(filepath, "a") as file:
        file.write(f"{name.title()}\t{tag}\t{text}\n")



