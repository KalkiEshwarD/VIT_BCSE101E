# Create a Python code that takes every object from the list and checks if it has a list object or not.
# If a list object is present in a list, it should be unpacked and the overall count of the list should be conveyed.
# If list object is not present in the existing list, it should say “cannot unpack”.

def list_unpacker(list0):
    total_objects = 0
    list_obj = 0

    for item in list0:
        if type(item) == list:
            for element in item:
                total_objects += 1
            list_obj += 1
        else:
            total_objects += 1
        
    if list_obj > 0:
        return total_objects
    else:
        return 'cannot unpack'


def main():
    input_stuff = eval(input())
    result = list_unpacker(input_stuff)
    print(result)


if __name__ == "__main__":
    main()
