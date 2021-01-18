def main():
    def getdate():
        import datetime
        return datetime.datetime.now()
    inp1 = input("Enter 1 if you want to lock and 2 if you want to retrieve\n")
    if inp1 == "1":
        while(1):
            inp2 = input("press 1 for Harry 2 for Rohan and 3 for Hammad\n")
            if inp2 == "1":
                while(1):
                    inp3 = input("press 1 for exercise, 2 for diet\n")
                    if inp3 == "1":
                        with open("harryex.txt", "a") as f:
                            print("Add your entry\n")
                            date = str(getdate())
                            f.write("[")
                            f.write(date)
                            f.write("]")
                            f.write("   ")
                            f.write( input())
                            f.write("\n")
                            break
                    elif inp3 == "2":
                        with open("harryfo.txt", "a") as f:
                            print("Add your entry\n")
                            date = str(getdate())
                            f.write("[")
                            f.write(date)
                            f.write("]")
                            f.write("   ")
                            f.write( input())
                            f.write("\n")
                            break
                    else:
                        print("Invalid input try again\n")
                        continue
                break
            elif inp2 == "2":
                while (1):
                    inp3 = input("press 1 for exercise, 2 for diet\n")
                    if inp3 == "1":
                        with open("rohanex.txt", "a") as f:
                            print("Add your entry\n")
                            date = str(getdate())
                            f.write("[")
                            f.write(date)
                            f.write("]")
                            f.write("   ")
                            f.write(input())
                            f.write("\n")
                            break
                    elif inp3 == "2":
                        with open("rohanfo.txt", "a") as f:
                            print("Add your entry\n")
                            date = str(getdate())
                            f.write("[")
                            f.write(date)
                            f.write("]")
                            f.write("   ")
                            f.write(input())
                            f.write("\n")
                            break
                    else:
                        print("Invalid input try again\n")
                        continue
                break

            elif inp2 == "3":
                while (1):
                    inp3 = input("press 1 for exercise, 2 for diet\n")
                    if inp3 == "1":
                        with open("hamadex.txt", "a") as f:
                            print("Add your entry\n")
                            date = str(getdate())
                            f.write("[")
                            f.write(date)
                            f.write("]")
                            f.write("   ")
                            f.write(input())
                            f.write("\n")
                            break
                    elif inp3 == "2":
                        with open("hamadfo.txt", "a") as f:
                            print("Add your entry\n")
                            date = str(getdate())
                            f.write("[")
                            f.write(date)
                            f.write("]")
                            f.write("   ")
                            f.write(input())
                            f.write("\n")
                            break
                    else:
                        print("Invalid input try again\n")
                        continue
                break

            else:
                print("Invalid input try again\n")
                continue

    elif inp1 =="2":
        while (1):
            inp2 = input("press 1 for Harry 2 for Rohan and 3 for Hammad\n")
            if inp2 == "1":
                while (1):
                    inp3 = input("press 1 for exercise, 2 for diet\n")
                    if inp3 == "1":
                        with open("harryex.txt") as f:
                            content = f.read()
                            print(content)
                        break
                    elif inp3 == "2":
                        with open("harryfo.txt") as f:
                            content = f.read()
                            print(content)
                        break
                    else:
                        print("Invalid Entry try again")
                        continue
            elif inp2 == "2":
                while (1):
                    inp3 = input("press 1 for exercise, 2 for diet\n")
                    if inp3 == "1":
                        with open("rohanex.txt") as f:
                            content = f.read()
                            print(content)
                        break
                    elif inp3 == "2":
                        with open("rohanfo.txt") as f:
                            content = f.read()
                            print(content)
                        break
                    else:
                        print("Invalid Entry try again")
                        continue
            elif inp2 == "3":
                while (1):
                    inp3 = input("press 1 for exercise, 2 for diet\n")
                    if inp3 == "1":
                        with open("hamadex.txt") as f:
                            content = f.read()
                            print(content)
                        break
                    elif inp3 == "2":
                        with open("hamadfo.txt") as f:
                            content = f.read()
                            print(content)
                        break
                    else:
                        print("Invalid Entry try again")
                        continue
            else:
                print("Wrong input try again")
                continue
            break
    else:
        print("wrong iput try again\n")
        main()
    try1 = input("Do you want run code again?\n(Enter y for yes and n for no)\n")
    if try1 == "y":
         main()
    else:
        exit()
main()

