def main():
    #write your code below this line
    amountOfNumbers = 0
    sumOfNumbers = 0

    while True:
      number = int(input("Give a number:"))

      if (number == 0):
        break
      
      if (number != 0):
        amountOfNumbers = amountOfNumbers + 1
        sumOfNumbers = sumOfNumbers + number
    
    print("Number of numbers: " + str(amountOfNumbers))
    print("Sum of numbers: " + str(sumOfNumbers))


if __name__ == '__main__':
    main()
