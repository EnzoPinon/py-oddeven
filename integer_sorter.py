#let us sort out the integers

def process():
    initial_write_1 = open("even.txt", 'w')
    initial_write_2 = open("odd.txt", 'w')

    initial_write_1.write("All numbers here are even.\n")
    initial_write_2.write("All numbers here are odd.\n")

    initial_write_2.close()
    initial_write_1.close()

process()