'''In this method we didnt want to close it .
   File will automatically close after read it.'''
with open("input_csvfile.csv","r") as infile ,open("output_csvfile.csv","w") as outfile :
    for line in infile:
        print(line.strip())
        outfile.write(line)
        