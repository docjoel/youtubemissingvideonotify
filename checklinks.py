import requests
import csv

# opens the video

def checkLink():
    link = input("name of file?")
    # Open primary CSV and load in video list
    # sets a variable to get totoal videos
    with open(link, newline='') as f:
        reader = csv.reader(f)
        row_count = sum(1 for row in reader)
        print(row_count)
    with open(link, newline='') as f:
        reader = csv.reader(f)
        existsN=0
        nonexist=0
        i = 1
        for row in reader:
            try:
                x = row[2]
                q = requests.get("http://www.youtube.com/oembed?url={}".format(x)) #get the links status
                if q.text != "Not Found":
                    print(row[0],row[1],"Exists")
                    existsN +=1
                else:
                    print(row[0],row[1],"Not Found")
                    nonexist+=1

                #Check if there is a contradiction
                if (q.text ==" Not Found") and (" Available" in row[3]):
                    print("*"*9)
                    print(row[0],row[3],q.text,"Contradiction Detected, check link")
                    print("*"*9)
                print("\r",i/row_count * 100)
                i+=1
            except:
                pass
    print("Exists",existsN)
    print("NonExist",nonexist-1)

checkLink()



