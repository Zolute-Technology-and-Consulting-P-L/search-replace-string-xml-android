import csv
replace_rule = 'file.csv'
stringfile = 'strings.xml'


    

with open(replace_rule, mode ='r')as file:
    # reading the CSV file
    csvFile = csv.reader(file)
    reading_file = open(stringfile, "r")
    content = reading_file.read()
    new_file_content = content
    # displaying the contents of the CSV file
    for lines in csvFile:
        new_file_content = new_file_content.replace(lines[0], lines[1])
   # print(new_file_content)
    reading_file.close()
    writing_file = open("replaced-"+stringfile, "w")
    writing_file.write(new_file_content)
    writing_file.close()


