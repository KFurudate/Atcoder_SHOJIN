Sa = input()
Sb = input()
Sc = input()

tmp = Sa[0]
Sa = Sa[1:]
while True:
    if tmp == "a":
        if not Sa:
            print("A")
            exit()

        tmp = Sa[0]
        Sa = Sa[1:]

    if tmp == "b":
        if not Sb:
            print("B")
            exit()

        tmp = Sb[0]
        Sb = Sb[1:]

    if tmp == "c":
        if not Sc:
            print("C")
            exit()
        tmp = Sc[0]
        Sc = Sc[1:]