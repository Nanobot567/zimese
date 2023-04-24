#! /bin/python3
from sys import argv

text = ""

e2z = {
    "a":"aah", # a
    "b":"mm", # ɱ
    "c":"t", # t
    "d":"p", # p
    "e":"uh", # ə
    "f":"r", # ɾ
    "g":"d", # d
    "h":"h", # h
    "i":"ee", # i
    "j":"j", # ʝ
    "k":"th", # θ
    "l":"f", # f
    "m":"l", # l
    "n":"n", # n
    "o":"eh", # e
    "p":"k", # k
    "q":"x", # x
    "r":"rr", # r
    "s":"sh", # ɬ
    "t":"b", # b
    "u":"oh", # ɒ
    "v":"ph", # ɸ
    "w":"w", # w
    "x":"z", # z
    "y":"aeh", # ɛ
    "z":"ss", # s
    "th":"zsh", # ʒ
    " ":" "
}

e2IPA = {
    "a":"a",
    "b":"ɱ",
    "c":"t",
    "d":"p",
    "e":"ə",
    "f":"ɾ",
    "g":"d",
    "h":"h",
    "i":"i",
    "j":"ʝ",
    "k":"θ",
    "l":"f",
    "m":"l",
    "n":"n",
    "o":"e",
    "p":"k",
    "q":"x",
    "r":"r",
    "s":"ɬ",
    "t":"b",
    "u":"ɒ",
    "v":"ɸ",
    "w":"w",
    "x":"z",
    "y":"ɛ",
    "z":"s",
    "th":"ʒ",
    " ":" "
}

def translate(text):
    outputString = ""
    for i in range(len(text)):
        if i > 0 and i < len(text) - 1 and text[i] == "'" and text[i-1] == text[i+1]:
            continue
        else:
            outputString += text[i]
    text = outputString

    ft = ""
    i = 0
    while i < len(text):
        try:
            ft += list(e2IPA.keys())[list(e2IPA.values()).index(text[i])]
        except ValueError:
            ft += text[i]
        i += 1
    return ft

try:
    for z in argv[1]:
        text = " ".join(argv[2:]).lower()

        if z == "z":
            t = e2z
        elif z == "i":
            t = e2IPA
        elif z == "d":
            print(translate(text))
            quit()
        else:
            print("Unknown mode: "+z)
            continue

        ft = ""

        i = 0

        while i < len(text):
            if text[i:i+2] == "th":
                ft += t["th"]
                i += 2
            else:
                try:
                    if ft.endswith(t[text[i]]):
                        ft += "'"
                    ft += t[text[i]]
                except KeyError:
                    ft += text[i]
                i += 1
        
        print(ft)

except IndexError:
    print("zimese translator v1.0. usage: zimese.py mode text")
    print("\nmode can be one or more of the following:")
    print("\tz - output zimese as syllables (hello becomes huhf'feh)")
    print("\ti - output zimese as international phonetic alphabet letters (hello becomes həf'fe)")
    print("\td - output english from IPA letters")
except Exception as e:
    print(str(e))
