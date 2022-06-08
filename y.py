from collections import defaultdict
import math
u = "A"
songdictionary = {"A" : ["First Class - Jack Harlow", "edamame - Rich Brian"]}
currentuser = songdictionary[u]
listforeverysong = set()
for song in range(0, len(currentuser)):
    songdifference = math.inf
    highestranking = 0
    lowestranking = 10
    if song - 3 >= 0:
        highestranking = song-3
    if song + 3 <= 10:
        lowestranking = song + 3
    for key in songdictionary:
        if key != u:
            for index in range(highestranking, lowestranking):
                if songdictionary[key][index] == currentuser[song]:
                    for s in range(0, len(songdictionary[key])):
                        if songdictionary[key][s]!=currentuser[s]:
                            listforeverysong.append((songdictionary[key][s]))