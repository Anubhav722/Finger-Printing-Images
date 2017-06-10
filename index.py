from PIL import Image
import imagehash
import argparse
import shelve
import glob

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()

ap.add_argument("-d", "--dataset", required=True, help="path to input dataset of images")
ap.add_argument("-s", "--shelve", required =True, help="output shelve database")

args = vars(ap.parse_args())

import ipdb; ipdb.set_trace()
# open the shelve database

db = shelve.open(args["shelve"], writeback=True)

for imagePath in glob.glob(args["dataset"] + "/*.jpg"):
    image = Image.open(imagePath)
    h = str(imagehash.dhash(image))
    
    # extract the filename from the path and update the database
    # using the hash as the key and the filename append to the
    # list of values

    filename = imagePath[imagePath.rfind("/") + 1:]
    db[h] = db.get(h, []) + [filename]

db.close()
