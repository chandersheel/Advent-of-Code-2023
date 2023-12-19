import string
File_object = open(r"C:\\Users\\User\\Desktop\\advent of code 2023\\day1.txt","r")
data = File_object.read()
def min_max_key(num_index_dict, word_index_dict):
     if bool(num_index_dict) == True and bool(word_index_dict) == True:
        
        min_value = min(min(min(value) for value in num_index_dict.values()),min(min(value) for value in word_index_dict.values()))
        max_value = max(max(max(value) for value in num_index_dict.values()),max(max(value) for value in word_index_dict.values()))
        try:
            min_key = next(key for key, value in num_index_dict.items() if min_value in value)    
        except:
            min_key = next(key for key, value in word_index_dict.items() if min_value in value)   
        try:
            max_key = next(key for key, value in num_index_dict.items() if max_value in value)          
        except:
            max_key = next(key for key, value in word_index_dict.items() if max_value in value)
        print(min_key, max_key)   
        return min_key, max_key
     else:
        return None, None
lower = list(string.ascii_lowercase)  
upper = list(string.ascii_uppercase)  
alphabets = lower+upper
num_word_dict = {"zero":0, "one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}  
calibration_values = []
for line in data.splitlines():
    num_index_dict = {}
    word_index_dict = {}
    for key in num_word_dict.keys():
        if line.find(key) != -1:
            # try: 
                # if key not in word_index_dict.keys(): 
                
                    word_index_dict[num_word_dict[key]] = [index for index, _ in enumerate(line) if line.startswith(key, index)]       
                    print (f'(the index of {key} in {line} is {line.index(key)}')
                #     word_index_dict[num_word_dict[key]].append(line.index(key))
                # else:
                #     word_index_dict[num_word_dict[key]] = [line.index(key)]
            # except:
            #     print (f'(there is no - {key} in {line}')
            #     continue
    print (word_index_dict)

    
    for x in line: 
        if x not in alphabets:
            num_index_dict[int(x)] = [i for i, value in enumerate(line) if value == x]
    print (num_index_dict) 
    if bool(num_index_dict) == True and bool(word_index_dict) == True:
        
        min_value = min(min(min(value) for value in num_index_dict.values()),min(min(value) for value in word_index_dict.values()))
        max_value = max(max(max(value) for value in num_index_dict.values()),max(max(value) for value in word_index_dict.values()))
        try:
            min_key = next(key for key, value in num_index_dict.items() if min_value in value)    
        except:
            min_key = next(key for key, value in word_index_dict.items() if min_value in value)   
        try:
            max_key = next(key for key, value in num_index_dict.items() if max_value in value)          
        except:
            max_key = next(key for key, value in word_index_dict.items() if max_value in value)
        value = int("{}{}".format(int(min_key),int(max_key)))             
        calibration_values.append(value)
    elif bool(num_index_dict) == True and bool(word_index_dict) == False:
        min_value = min(min(value) for value in num_index_dict.values())
        max_value = max(max(value) for value in num_index_dict.values())
        # try:
        min_key = next(key for key, value in num_index_dict.items() if min_value in value)    
        # except:
        #     min_key = next(key for key, value in word_index_dict.items() if min_value in value)   
        # try:
        max_key = next(key for key, value in num_index_dict.items() if max_value in value)          
        # except:
        #     max_key = next(key for key, value in word_index_dict.items() if max_value in value)
        value = int("{}{}".format(int(min_key),int(max_key)))             
        calibration_values.append(value)
    elif bool(num_index_dict) == False and bool(word_index_dict) == True:
        min_value = min(min(value) for value in word_index_dict.values())
        max_value = max(max(value) for value in word_index_dict.values())
        # try:
        min_key = next(key for key, value in word_index_dict.items() if min_value in value)    
        # except:
        #     min_key = next(key for key, value in word_index_dict.items() if min_value in value)   
        # try:
        max_key = next(key for key, value in word_index_dict.items() if max_value in value)          
        # except:
        #     max_key = next(key for key, value in word_index_dict.items() if max_value in value)
        value = int("{}{}".format(int(min_key),int(max_key)))             
        calibration_values.append(value)
    elif bool(num_index_dict) == False and bool(word_index_dict) == False:
        min_value = 0
        max_value = 0
        
        value = int("{}{}".format(int(min_key),int(max_key)))             
        calibration_values.append(value)

print(calibration_values)
print(sum(calibration_values))



     
     
     