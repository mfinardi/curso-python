def main():

    with open('numbers.txt', 'r') as file:
         numbers = file.read().split(",")
    for number in numbers:
         print(number.strip())

if __name__ == "__main__":
    main()