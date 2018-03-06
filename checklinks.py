import requests
import csv

# opens the video

def countRows(filename):
    with open(filename, newline='') as f:
        reader = csv.reader(f)
        row_count = sum(1 for row in reader)
        return row_count


def checkifavalible(youtubelink):
    q = requests.get("http://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={}".format(youtubelink))
    return q.text != "Not Found"


def checkLinks(filename):

    # Open primary CSV and load in video list
    # sets a variable to get totoal videos
    row_count = countRows(filename)
    with open(filename, newline='') as f:
        reader = csv.reader(f)
        existsN=0
        nonexist=0
        i = 1
        for row in reader:
            try:
                youtubeLink = row[0]
                if checkifavalible(youtubelink=youtubeLink):
                    print(row[0],row[1],"Exists")
                    existsN +=1
                else:
                    print(row[0],row[1],"Not Found")
                    nonexist+=1

                #Check if there is a contradiction
                if not checkifavalible() and ("Available" in row[3]):
                    print("*"*9)
                    print(row[0],row[3],checkifavalible(youtubelink=youtubeLink),"Contradiction Detected, check link")
                    print("*"*9)
                print("\r",i/row_count * 100)
                i+=1
            except:
                pass
    print("Exists",existsN)
    print("NonExist",nonexist-1)




