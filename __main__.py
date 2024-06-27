def InputInteger():

    def InputAgain():
        print("\nPlease enter a integer!")
        return InputInteger()

    value = input("\n=> ")

    try:
        value = int(value)
    except ValueError:
        return InputAgain()

    if value == None:
        return InputAgain()
       
    return value

def Sort(values : list):
    valueCount = len(values)
    for i in range(valueCount - 1):
        for j in range(valueCount - 1):
                if values[j] > values[j+1]:
                    print("Values", values[i], values[i+1], "replacing!")
                    values[j], values[j+1] = values[j+1], values[j]
                    
                    print("New values:", values)
                    print("\n")

    return values

def Main():

    print("\nHow much values will you enter?")

    valueCount = InputInteger()
    values = []

    for i in range(valueCount):
        print("\nPlease enter " + str(i + 1) + ". value :")
        values.append(InputInteger())
    
    print("\n")
    print("Your old :", values)
    print("\n")
    newValues = Sort(values)
    print("Sorted values:", newValues)

    input("\nPress enter to exit!")

if __name__ == "__main__":
    
    Main()