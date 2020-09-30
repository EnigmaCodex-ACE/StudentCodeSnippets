import os
songlist = open("newmore.txt","r",encoding="utf-8")
songarr = songlist.readlines()
tot = len(songarr)
for x in range(tot):
    os.system('spotdl --song ' + '"'+songarr[x]+'"' + r"-f A:\Coding Stuff\misc\songs\newsongs")
    print("\n\n===================================================\n\n Songs Left to download {}/{} \n\n===================================================\n\n".format(tot-x,tot))

