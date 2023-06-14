def is_sorted(my_list):
    count = 1
    if len(my_list) < 2:  #If the list has less than 2 values, it´s sorted
        return True
    else:
        for i in range(len(my_list) - 1):
            if my_list[i + 1] >= my_list[i]:
                count += 1
    if len(my_list) == count: #Iterating each value in the list, comparing current value to the next in the list
        return True
    return False


#Code for testing is_sorted
"""
print(is_sorted([1, 4, 23, 101, 2912]))
#True
print(is_sorted([]))
#True
print(is_sorted([-1]))
#True
print(is_sorted([2, 4, 1]))
#False
"""



def insert_in_sorted(x,my_list):
    insert_sorted = my_list.copy()

    if is_sorted(my_list):

        if not my_list:                 #If the list is empty, the value is inserted
            insert_sorted.append(x)
            return insert_sorted

        else:

            if x <= my_list[0]:               #If "x" is the smallest value, add it to the start of the list
                insert_sorted.insert(0, x)
                return insert_sorted

            for i in range(len(my_list)-1):
                if my_list[i+1] >= x and x >= my_list[i]:      #Compares "x" with the value before and after in the list
                    insert_sorted.insert(i+1, x)
                    return insert_sorted

            if x > my_list[-1]:               #If "x" is the largest value, add it to the end
                insert_sorted.append(x)
                return insert_sorted
    else:
        raise ValueError("Input must be sorted")

#Testing insert_in_sorted
"""
print(insert_in_sorted(2,[]))
#[2]
print(insert_in_sorted(5,[0,1,3,4]))
#[0, 1, 3, 4, 5]
print(insert_in_sorted(2,[0,1,2,3,4]))
#[0, 1, 2, 2, 3, 4]
print(insert_in_sorted(2,[3,1]))
#Traceback (most recent call last):
 # ...
#ValueError: Input list must be sorted
print(insert_in_sorted(2,[2,2]))
#[2, 2, 2]
"""


def insertion_sort(my_list):
    out = []

    if not my_list:     #If the list is empty
        return my_list

    else: #Takes each element in my_list and inserts in to function insert_in_sorted and sees where the value should be
        for i in my_list:
            out = insert_in_sorted(i, out)
        return out

#Testing insertion_sort
"""
print(insertion_sort([]))
#[]
print(insertion_sort([12,4,3,-1]))
#[-1, 3, 4, 12]
print(insertion_sort([5,4,-3,4,2]))
#[-3,2,4,4,5]
"""

def count_word(f): #Opens file, iterates through lines of text, takes away '\n', then splits the words in to a list
    words = []
    with open(f, "r") as h:
        for i in h:
            i = i.strip("\n")
            words += i.split(" ")
        return len(words)

#Testing count_word
"""
print(count_word("infile.txt"))
"""

def annotate(f):
    row = 0 #counts rows
    count = 0 #counts words
    with open(f, "r") as h:
        with open("annotated.txt", "w") as f: #Opens both files and iterates through the first file.
            for i in h:
                count += len(i.split(" "))
                i = i.strip("\n") #Removes spaces and \n to count the words
                i = str(i) + " " + str(row) + " " + str(count)
                f.write(i + "\n") #Alot of restructuring to get the numbers of rows and words in the right location
                row += 1

#Testing annotate
"""
annotate("infile.txt")
"""

def save_rows(h):
    rows_dictionary = {}

    for keys, a in enumerate(h): #Iterating through each line in the text, assigning a number to a row by enumerating
        a = a.strip("\n")
        rows_dictionary[keys] = a

    print("At any time, write 'exit' to exit.")

    while True: #While loop

        row = input("Please write a row, e.g '5': ")
        if row.upper() == "EXIT":
            print("Program ended")
            break

        column = input("Please write a column, e.g '5': ") #If "exit" is written, the program ends
        if column.upper() == "EXIT":
            print("Program ended")
            break

        try:    #Tries to get the letter from the assigned row and column
            row_wanted = rows_dictionary.get(int(row))
            column_wanted = row_wanted[int(column)]
            print(f"Provided row: {row}")
            print(f"Provided column: {column}")
            if column_wanted == " ":
                print("Letter gotten: Space")
            else:
                print(f"Letter gotten: {column_wanted}")
        except:     #If it fails, prints out of bounds
            print("Out of bounds.")


    h.close()   #closes the open document

def main(): #Asks for a text file, e.g "bananas.txt"
    open_file = open(input("Please write the name of the file you want to open: "), "r")
    return save_rows(open_file)

#Testing the program/snippet
"""
main()
"""
