my_dict = {
    'dict1': {"key1": "value1"},
    'dict2': {"key2": "value2"}
}


# print(my_dict['dict1']['key1'])

for keys in my_dict:
    inner_dict = my_dict[keys]
    for key in inner_dict:
        print(inner_dict[key])
 

