'''method 1-convert to dictionary'''
import csv
with open("input_csvfile.csv","r") as file:
    line=csv.DictReader(file)
    for row in line:
        print(row["age"])

'''method 2-convert to array'''
with open("input_csvfile.csv","r") as file:
    lines=file.readlines()
    for line in lines[1:]:
        columns=line.strip().split(",")
        print("columns :",columns[2])
