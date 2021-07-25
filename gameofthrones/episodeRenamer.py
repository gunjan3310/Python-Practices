import csv
import os
import filterstring
episodeNames = []

def episodeList():
    with open('/home/gunjan/Documents/Python-Practices/gameofthrones/episodes.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:

                line_count += 1
            else:
                episodeNames.append(row[2])
                line_count += 1

filePathsToChange = []
got = "path/to/got"
#mine is

got = "/home/gunjan/Downloads/Game of Thrones - all seasons-480p"
def main():
    for root,directories,files in os.walk(got):
        episodeList()
        for dir in directories:
            folder = os.path.join(got,dir)

            for r,d,f in os.walk(folder):
                episodeCounter = 1
                for episode in f:
                    episodetitle = episodeNames[episodeCounter-1]
                    try:
                        mkvFile = filterstring.filterMKV(episode)
                        print(f"{folder}/{episode} will change to -> ")
                        PREVIOUSPATH = f"{folder}/{episode}"
                        print(f"\r{folder}/{episodetitle} - E{episodeCounter}")
                        EPISODERENAMEDPATH = f"\r{folder}/{episodetitle} - E{episodeCounter}.mkv"

                        #not working
                        #os.rename(PREVIOUSPATH,EPISODERENAMEDPATH)

                        episodeCounter += 1
                    except:
                        continue
                        print("")
                    #renamed file string




main()


