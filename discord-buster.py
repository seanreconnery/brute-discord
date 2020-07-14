import os, time, shutil, sys, requests, math, random

#################
# USE:  discord-buster.py 100
# file takes 1 arg:  number of tries
#   script will generate random directory names that conform to Discord standards and check if anything exists
#
#   TO DO:
#       - add in ability to SET a SERVER, CHANNEL, or FILE NAME
#       - add in "smart scan" --> if a file IS found, it logs the server directory and tries to find files in there.
#       - proxy support maybe?

init1 = 123456789000000000
init2 = 999999999987654321

init3 = 111111111111111111
init4 = 999999999999999999

vid = 'video0.mov'
pic = 'unknown.png'

known_png = 'https://cdn.discordapp.com/attachments/732696818697109504/732697099090526279/unknown.png'
known_txt = 'https://discordapp.com/channels/572330844056715284/615334603049271322/732673840622075914'

base_url = "https://cdn.discordapp.com/channels/"
file_url = "https://cdn.discordapp.com/attachments/"

num_of_tries = int(sys.argv[1])


t = 0
while t < num_of_tries:

    folder1 = random.randint(init1, init2)
    folder2 = random.randint(init3, init4)
    folder3 = random.randint(init3, init4)

    convo_url = base_url + str(folder1) + "/" + str(folder2) + "/" + str(folder3)
    pic_url = file_url + str(folder1) + "/" + str(folder2) + "/" + pic
    vid_url = file_url + str(folder1) + "/" + str(folder2) + "/" + vid

    print(convo_url)
    print(pic_url)
    print(vid_url)

    x = requests.get(pic_url)
    if x.status_code == 403:
        # nothing found
        print("PICTURES - Nothing found.")
    else:
        # found something!!!!
        print("PICTURES - FOUND SOMETHING?!?!?!")
        print(x)

    x = requests.get(vid_url)
    if x.status_code == 403:
        # nothing found
        print("VIDEOS - Nothing found.")
    else:
        # found something!!!!
        print("VIDEOS - FOUND SOMETHING?!?!?!")
        print(x)

    x = requests.get(convo_url)
    if x.status_code == 403:
        # nothing found
        print("CONVOS - Nothing found.")
    elif x.status_code == 200:
        # might have found something..
        if x.text.find('Log in with QR'):
            # sending you to a login page..
            print("CONVO EXISTS - trying to send you to a login page though..")
        else:
            # found something!!!!
            print("CONVOS - FOUND SOMETHING?!?!?!")
            print(x)

    t += 1


print("   ---   COMPLETE   ---")
