import csv
import requests
with open("kenzlinks.txt","r") as infile:
    text = infile.read()
    text = text.split("\n")
    suplerlist = [item.split(": ") for item in text]
    print(suplerlist)
    csv = open("newKenz.csv","w")
    columnTitleRow = "name, serires, link\n"
    csv.write(columnTitleRow)
    for pair in suplerlist:
        for name in pair:
            csv.write(name + ",")
        csv.write("\n")


