# A team has a maximum of 7 members.
# They have to fill a form indicating their name and age in the format of name:age.
# The data collector task is to convert all the team members given data to a list and give it as input to the network admin.
# The Network admin will perform modifications in the given list based on the following conditions. (Dictionary)
# * If anyone shares same age, their names are merged together as a single name and their ages should be cube rooted.
# * If anyone shares the same name, their ages should be merged together and the duplicate names are to be removed.
# * If any of the input is in wrong format (say age:name instead of name:age), that should be verified and modified in the correct format (name: age)

def network_admin_func(list0):
    """
    DESCRIPTION: It takes in the input list with details of all members, alters it as requested, and outputs it throught a list
    DEPENDENCIES: Nil

    @param: --[list]-- list0 Takes in the input list
    @result: --[list]-- final_person_details_list
    """
    for person_dict in list0:
        if type(list(person_dict.values())[0]) == int:
            pass
        else:
            person_age = list(person_dict.keys())[0]
            person_name = list(person_dict.values())[0]
            del person_dict[person_age]
            person_dict[person_name] = person_age

    persons_names_list = []
    person_details_list = []

    for person_dict in list0:
        if list(person_dict.keys())[0] in persons_names_list:
            for person_name_detail_dict in person_details_list:
                if list(person_name_detail_dict.keys())[0] == list(person_dict.keys())[0]:
                    person_name_detail_dict[list(person_dict.keys())[0]] = int(
                        str(list(person_name_detail_dict.values())[0]) + str(list(person_dict.values())[0]))
        else:
            persons_names_list.append(list(person_dict.keys())[0])
            person_details_list.append({list(person_dict.keys())[0]: list(person_dict.values())[0]})

    persons_ages_list = []
    final_person_details_list = []

    for person_dict in person_details_list:
        if list(person_dict.values())[0] in persons_ages_list:
            name2 = list(person_dict.keys())[0]
            age = list(person_dict.values())[0]
            for person_age_detail_dict in final_person_details_list:
                if list(person_age_detail_dict.values())[0] == age:
                    name1 = list(person_age_detail_dict.keys())[0]
                    index = final_person_details_list.index(person_age_detail_dict)
                    final_person_details_list.pop(index)
                    final_person_details_list.insert(index, {f'{name1}' + f'{name2}': int(round(age**(1/3), 0))})
        else:
            final_person_details_list.append(person_dict)
            persons_ages_list.append(list(person_dict.values())[0])

    return final_person_details_list


def data_collector():
    """
    DESCRIPTION: Takes in the input, feeds it to the network admin function, and then prints the result
    DEPENDENCIES: Nil

    @param: --Nil--
    @result: --Nil--
    """
    input_stuff = eval(input())

    result = network_admin_func(input_stuff)
    print(result)


if __name__ == "__main__":
    data_collector()
