#let us sort out the integers

def process():
    initial_write_1 = open("even.txt", 'w')
    initial_write_2 = open("odd.txt", 'w')

    initial_write_1.write("All numbers here are even.\n")
    initial_write_2.write("All numbers here are odd.\n")

    initial_write_2.close()
    initial_write_1.close()
    with open("integers.txt", 'r') as integers, open("odd.txt", 'a') as odd, open("even.txt", 'a') as even:
        #make a loop
        for line in integers:
            #convert to integer
            number = int(line)
            #divide with modulo 2
            check = number % 2
            #see if it returns a 0
            if check == 0:
                even.write(line)
            if check != 0:
                odd.write(line)
process()