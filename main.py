import csv
replace_rule = 'file.csv'

def doreplace(str1,replc,filename):
    reading_file = open(filename, "r")
    new_file_content = ""
    for line in reading_file:
        stripped_line = line.strip()
        new_line = stripped_line.replace(str1, replc)
        new_file_content += new_line +"\n"
    reading_file.close()
    writing_file = open("replaced-"+filename, "w")
    writing_file.write(new_file_content)
    writing_file.close()

with open(replace_rule, mode ='r')as file:
   
  # reading the CSV file
  csvFile = csv.reader(file)
 
  # displaying the contents of the CSV file
  for lines in csvFile:
        print(lines[0]+" replaced by "+lines[1])
        doreplace(lines[0],lines[1],'strings.xml')


