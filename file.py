filename = "test.txt"

append_file = open(filename, 'a')

print("Enter a city name: ")
x = 0

while True:
    mycity = input("")
    if mycity == "q": break
    append_file.write(mycity + '\n')
    x += 1
    if x > 3:
        print("Enter q to quit: ")

    

append_file.close()

open_file = open(filename, 'r')

print("Contents of the file: " + open_file.read())

open_file.close()
