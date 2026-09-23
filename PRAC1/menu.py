MENU = "(H)ello\n(G)oodbye\n(Q)uit"

name = input("input your name: ")
print(MENU)
choice = input("input your choice (H/G/Q) >>> ").upper()

while choice != "Q":
    if choice == "H":
        print(f"HELLO {name}")
    elif choice == "G":
        print(f"GOODBYE {name}")
    else:
        print(f"ERROR choice")
        
    print(MENU)
    choice = input("input your choice (H/G/Q) >>> ").upper()


print("finished")