import requests
import csv



with open('kenzlinks2.csv', newline='') as f:
    reader = csv.reader(f)
    row_count = sum(1 for row in reader)

    print (row_count)

with open('kenzlinks2.csv', newline='') as f:
    reader = csv.reader(f)
    existsN=0
    nonexist=0
    i = 1
    for row in reader:
        try:
            x = row[2]
            q = requests.get("http://www.youtube.com/oembed?url={}".format(x))
            if q.text != "Not Found":
                print(row[0],row[1],"Exists")
                existsN +=1
            else:
                print(row[0],row[1],"Not Found")
                nonexist+=1
            if (q.text =="Not Found") and ("Available" in row[3]):
                print("*"*9)
                print(row[0],row[3],q.text,"Contradiction Detected, check link")
                print("*"*9)
            print("\r",i/row_count * 100)
            i+=1
        except:
            pass
print("Exists",existsN)
print("NonExist",nonexist)


