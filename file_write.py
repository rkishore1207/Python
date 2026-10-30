temperatures = [10, -20, -289, 100]

def celsius_to_farenheit(celsius):
    if (celsius < -273.15):
        return "Invalid Celsius"
    else:
        farenheit = celsius * 9/5 + 32
        return farenheit

def writer(filePath, temperatures):
    with open(filePath, "w") as myFile:    
        for i in temperatures:
            farenheit = celsius_to_farenheit(i)
            if (isinstance(farenheit, (int, float))):
                myFile.write(str(farenheit) + "\n")

writer("farenheit.txt", temperatures)