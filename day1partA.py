# day1
import string
File_object = open(r"C:\\Users\\User\\Desktop\\advent of code 2023\\day1.txt","r")
data = File_object.read()
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
