def main():
    people = int(input("How many people are coming to the cookout?"))
    foodForPeople = int(input("How many hot dogs will each person get?"))
    hotDogs = 0
    hotDogBuns = 0

    while True:
        hotDogs += 10
        if hotDogs >= people:
            break

    while True:
        hotDogBuns += 8
        if hotDogBuns >= people:
            break


    hotDogPackages = hotDogs / 10
    hotDogBunPackages = hotDogBuns / 8
    remainderDogs = hotDogs - people
    remainderBuns = hotDogBuns - people

    print(f"The minimum number of hot dog packages required is {hotDogPackages}.")
    print(f"The minimum number of bun packages required is {hotDogBunPackages}.")
    print(f"The remainder of hot dogs left over is {remainderDogs}.")
    print(f"The remainder of hot dog buns left over is {remainderBuns}.")


main()
