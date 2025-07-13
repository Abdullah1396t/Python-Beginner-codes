# SO finding the bits
mood = ""
key="Abdullah.1396t"
while mood=="":
    def choices(bin1, bin2):
        den1 = int(bin1, 2)
        den2 = int(bin2, 2)
        ans = den1 + den2
        print("\n", bin(ans), "→ FOR OR Answer in binary")
        print(ans, "→ Answer in denary\n")
        ans = den1 & den2
        print("\n", bin(ans), "\n→ FOR AND Answer in binary")
        print(ans, "→ Answer in denary\n")
        ans = den1 ^ den2
        print('\n', bin(ans), "\n→ FOR XOR Answer in binary")
        print(ans, "→ Answer in denary\n")


    def choice2(denary1, denary2):
        ans = denary1 + denary2
        print("\n", bin(ans), "→ FOR OR Answer in binary")
        print(ans, "→ Answer in denary\n")
        ans = denary1 & denary2
        print("\n", bin(ans), "→ FOR AND Answer in binary")
        print(ans, "→ Answer in denary\n")
        ans = denary1 ^ denary2
        print("\n", bin(ans), "→ FOR XOR Answer in binary")
        print(ans, "→ Answer in denary\n")


    from time import sleep

    print("This is teh beta version and can only find the And , Or , Xor gates")
    print("Hi, choose the below options;")
    sleep(2)
    choice = input(
        "option 1; Input= Binary value\noption2; Input= Denary\n option 3: check by program by yourself OR EXIT...\n :.. ")
    if choice == "1":
        x = input("Enter the first binary value:..")
        y = input("Enter the second binary value:..")
        choices(x, y)
        mood = input("Want to continue press [ENTER] or EXIT write [EXIT]")

    elif choice == "2":
        x = int(input("Enter the first Denary value:.."))
        y = int(input("Enter the second Denary value:.."))
        choice2(x, y)
        mood = input("Want to continue press [ENTER] or EXIT write [EXIT]")
    else:
        print("If a pro member ans key or EXIT, to find the code")
        n = input("Enter to varify a pro member\n:..")
        if n == key:
            print("""SO finding the bits key=*********** 
    def choices(bin1, bin2):
        den1 = int(bin1, 2)
        den2 = int(bin2, 2)
        ans = den1 + den2
        print("\n",bin(ans), "→ FOR OR Answer in binary")
        print(ans, "→ Answer in denary\n")
        ans= den1&den2
        print("\n",bin(ans), "\n→ FOR AND Answer in binary")
        print(ans, "→ Answer in denary\n")
        ans = den1^den2
        print('\n', bin(ans), "\n→ FOR XOR Answer in binary")
        print(ans, "→ Answer in denary\n")
    def choice2(bin1,bin2):
        den1 = int(bin1, 2)
        den2 = int(bin2, 2)
        ans = den1 + den2
        print("\n",bin(ans), "→ FOR OR Answer in binary")
        print(ans, "→ Answer in denary\n")
        ans = den1 & den2
        print("\n",bin(ans), "→ FOR AND Answer in binary")
        print(ans, "→ Answer in denary\n")
        ans = den1 ^ den2
        print("\n",bin(ans), "→ FOR XOR Answer in binary")
        print(ans, "→ Answer in denary\n")

    from time import sleep
    print("This is teh beta version and can only find the And , Or , Xor gates")
    print("Hi, choose the below options;")
    sleep(2)
    choice = input("option 1; Input= Binary value\noption2; Input= Denary\n option 3: check by program itself...\n :.. ")
    if choice == "1":
        x=input("Enter the first binary value:..")
        y=input("Enter the second binary value:..")
        choices(x,y)

    elif choice== "2":
        x = input("Enter the first Denary value:..")
        y = input("Enter the second Denary value:..")
        choices(x, y)
    else:
        [INCEPTED AREA CANNOT BE INTERCEPTED]""")
    mood=input("Want to exit...")

else:
    exit()
