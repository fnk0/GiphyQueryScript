__author__ = 'marcus'

import urllib
import json
import os


def add_to_file(file, json_data):
    arr = json_data['data']
    for d in arr:
        gif = str(d["images"]["downsized"]["url"])
        print gif
        file.write(gif + "\n")


def get_all_gifs(filename, search):

    gifs = open(filename, 'w')
    data = json.loads(urllib.urlopen("http://api.giphy.com/v1/gifs/search?q=" + str(search) + "&limit=100&api_key=dc6zaTOxFJmzC").read())
    count = data["pagination"]["total_count"] / 100
    add_to_file(gifs, data)

    for offset in range(0, count):
        o_data = json.loads(urllib.urlopen("http://api.giphy.com/v1/gifs/search?q=" + str(search) + "&limit=100&offset=" + str(offset) + "&api_key=dc6zaTOxFJmzC").read())
        add_to_file(gifs, o_data)

    gifs.close()


# get_all_gifs("cat_gifs.txt", "funny+cats")
# get_all_gifs("dog_gifs.txt", "funny+dogs")
# get_all_gifs("futurama_gifs.txt", "futurama")
# get_all_gifs("funny_gifs.txt", "funny")



