#Combines two input dictionaries
#Returns combined dictionary
def merge(dict_1, dict_2):
    #Run through dictionary elements in dict_2
    #If current key is a key in dict_1, combine values under same key into dict_1
    for key, value in dict_2.items():
        #dict_2[key] = value
        if key in dict_1:
            if isinstance(dict_1[key], dict):
                if isinstance(dict_2[key], dict):
                    merge(dict_1[key],dict_2[key])
                else:
                    dict_1[key] = [dict_1[key]].append(dict_2[key])
            elif isinstance(dict_1[key], list):
                dict_1[key].append(dict_2[key])
            else:
                dict_1[key] = [dict_1[key]]
                dict_1[key].append(dict_2[key])
        else:
            dict_1[key] = dict_2[key]
    return dict_1

#Formats dictionary into JSON file
#Returns json data
def format(dictionary):
    characters = list(str(dictionary))
    json = ""
    tabs = ""
    position = 0
    in_string = False
    while position < len(characters):
        char = characters[position]
        if char in "{[":
            tabs += "\t"
            json = json + char + "\n" + tabs
        elif char in ",":
            json = json + char + "\n" + tabs
        elif char in "}]":
            tabs = tabs[:-1]
            json = json + "\n" + tabs + char
        elif char in "'":
            if in_string == False:
                in_string = True
            else:
                in_string = False
            json = json + '"'
        elif char in " ":
            if in_string == True:
                json = json + char
            else:
                pass
        elif char in ":":
            if in_string == False:
                json = json + char + " "
            else:
                pass
        else:
            json = json + char
        position += 1
    return json
