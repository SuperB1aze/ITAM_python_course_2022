def key_difference(dict1, dict2):
    presence_check = False
    dict3 = {}
    for key, value in dict1.items():
        for key1, value1 in dict2.items():
            if key == key1:
                if value == value1:
                    dict3[key] = "equal"
                    presence_check = True
                    break
                else:
                    dict3[key] = "changed"
                    presence_check = True
                    break
        if presence_check:
            presence_check = False
        else:
            dict3[key] = "deleted"
    
    added_letters = []
    for key, value in dict2.items():
        for key1, value1 in dict3.items():
            if key == key1:
                presence_check = True
                break
        if presence_check:
            presence_check = False
        else:
            added_letters.append(key)
    for i in range(len(added_letters)):
        dict3[added_letters[i]] = "added"

    print(dict3)


dict1 = {"a":"b", "b":"a", "d":"a"}
dict2 = {"a":"b", "b":"a", "c": "a"}

key_difference(dict1, dict2)