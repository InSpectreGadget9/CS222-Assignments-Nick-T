import os
def main():
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, "students.txt")

        keyslist = []
        lastnameslist = []
        firstnameslist = []
        majorslist = []
        gpalist = []

        with open(file_path, "r") as students:
            for line in students:
                if "," in line:
                    parts = line.strip().split(',', 4)
                    if len(parts) == 5:
                        keypart, lastnamespart, firstnamespart, majorspart, gpapart = parts
                        keyslist.append(keypart)
                        lastnameslist.append(lastnamespart)
                        firstnameslist.append(firstnamespart)
                        majorslist.append(majorspart)
                        gpalist.append(gpapart)
                else:
                    keyslist.append(line.strip())

        

        while True:
            print("\nChoose an option:")
            print("1. Search by Last Name")
            print("2. Search by Major")
            print("3. Quit")
            uInput = input("Which will you choose? ")

            if uInput == "1":
                uSearch = input("Which last name do you want to search for? ")
                found = False
                for index, lastname in enumerate(lastnameslist):
                    if lastname == uSearch:
                        print(f"ID: {keyslist[index]}, Name: {firstnameslist[index]} {lastnameslist[index]}, Major: {majorslist[index]}, GPA: {gpalist[index]}")
                        found = True
                if not found:
                    print("No student found with that last name.")

            elif uInput == "2":
                uSearch = input("Which major do you want to search for? ")
                found = False
                for index, major in enumerate(majorslist):
                    if major == uSearch:
                        print(f"ID: {keyslist[index]}, Name: {firstnameslist[index]} {lastnameslist[index]}, Major: {majorslist[index]}, GPA: {gpalist[index]}")
                        found = True
                if not found:
                    print("No student found with that major.")

            elif uInput == "3":
                break
            else:
                print("That wasn't a valid input. Try again.")

        

main()