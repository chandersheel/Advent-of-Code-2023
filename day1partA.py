# day1
import string
File_object = open(r"C:\\Users\\User\\Desktop\\advent of code 2023\\day1.txt","r")
data = File_object.read()



################Part-A##########################
lower = list(string.ascii_lowercase)  
upper = list(string.ascii_uppercase)  
alphabets = lower+upper
calibration_values = []
for line in data.splitlines():
    line_list = []
    for x in line: 
        if x not in alphabets:
            x = int(x)      
            line_list.append(int(x))             
    value = int("{}{}".format(line_list[0],line_list[-1]))
    calibration_values.append(value)
print(sum(calibration_values))


################Part-B##########################

num_dict = {"zero":0, "one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}  
calibration_values = []
for line in data.splitlines():

    line_list = []
    for x in line: 
        if x not in alphabets:
            x = int(x)      
            line_list.append(int(x))             
    value = int("{}{}".format(line_list[0],line_list[-1]))
    calibration_values.append(value)
print(calibration_values)
print(sum(calibration_values))