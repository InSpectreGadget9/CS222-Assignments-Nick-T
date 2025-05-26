def main():
    try:
        students = open("C:/Users/ninja/OneDrive/Documents/GitHub/CS222-Assignments-Nick-T/students.txt", 'r')
        keyslist = []
        lastnameslist = []
        firstnameslist = []
        majorslist = []
        gpalist = []
        studentDictionary = {}
        for line in students:
            if "," in line:
                keypart = line.split(',', 4)[0]
                lastnamespart = line.split(',', 4)[1]
                firstnamespart = line.split(',', 4)[2]
                majorspart = line.split(',', 4)[3]
                gpapart = line.split(',', 4)[4]
                keyslist.append(keypart)
                lastnameslist.append(lastnamespart)
                firstnameslist.append(firstnamespart)
                majorslist.append(majorspart)
                gpapart = gpapart.rstrip()
                gpalist.append(gpapart)
            else:
                keyslist.append(line.strip())
            
        studentDictionary["id"] = keyslist
        studentDictionary["lastname"] = lastnameslist
        studentDictionary["firstname"] = firstnameslist
        studentDictionary["major"] = majorslist
        studentDictionary["gpa"] = gpalist
        while True:
            print("Choose an option:")
            print("1. Search by Last Name")
            print("2. Search by Major")
            print("3. Quit")
            uInput = input("Which will you choose?")
            if uInput == "1":
                uSearch = input("Which name do you want to search for?")
                for i in lastnameslist:
                    if i == uSearch:
                        index = lastnameslist.index(uSearch)
                        print(f"ID: {keyslist[index]}, Name: {firstnameslist[index]} {lastnameslist[index]}, Major: {majorslist[index]}, GPA: {gpalist[index]}")
            elif uInput == "2":
                uSearch = input("Which major do you want to search for?")
                for i in majorslist:
                    if i == uSearch:
                        index = majorslist.index(uSearch)
                        print(f"ID: {keyslist[index]}, Name: {firstnameslist[index]} {lastnameslist[index]}, Major: {majorslist[index]}, GPA: {gpalist[index]}")
            elif uInput == "3":
                break
            else:
                print("That wasn't quite a correct input. Try again.")
        students.close()


    except FileNotFoundError:
        print("File Not Found")


main()