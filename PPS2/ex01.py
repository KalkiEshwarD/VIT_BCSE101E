# Create a Python code that takes every object from the list and checks if it has a list object or not.
# If a list object is present in a list, it should be unpacked and the overall count of the list should be conveyed.
# If list object is not present in the existing list, it should say “cannot unpack”.

def list_unpacker(list0):
    """
    INPUT:      list0 [list]
    OUTPUT:     total_objects / cannot unpack [integer / string]

    DESCRIPTION:    This function takes in a list as input upacks all the elements inside list objects in the input list and then outputs all the elements in the input list.
    DEPENDENCIES:   Nil
    """
    total_objects = 0
    list_obj = 0

    for item in list0:
        if type(item) == list:
            for element in item:
                total_objects += 1
            list_obj += 1
        else:
            total_objects += 1

    if list_obj == 0:
        return 'cannot unpack'
    else:
        return total_objects


def main():
    input_stuff = eval(input())
    result = list_unpacker(input_stuff)
    print(result)
    

if __name__ == "__main__":
    main()
