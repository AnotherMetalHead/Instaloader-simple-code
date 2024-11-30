import os
import sys
from time import sleep
from instaloader import *

folderName = "instaSaved"
loader = instaloader.Instaloader(dirname_pattern=folderName)
loader.save_metadata = False
loader.download_comments = False
loader.download_video_thumbnails = False

# Making a directory if doesn't exist
try:
   os.mkdir(folderName)
except FileExistsError:
   # directory already exists
   pass

# Clears all .txt files as unnecessary
def clearFromTxt():
    for item in os.listdir(folderName):
        if item.endswith(".txt"):
            os.remove(os.path.join(folderName, item))



def saveFromInsta():
    shortcode = input("Enter the shortcode: ")

    post = Post.from_shortcode(loader.context, shortcode)

    photosCount = post.mediacount

    def dwnPhoto():
        booled = bool(loader.download_post(post, target=folderName))

        if booled:
            clearFromTxt()
        else:
            print(input(
                """
                This file is in your folder already!
                press "Enter" to exit.
                """))
            sys.exit()



    if photosCount == 1:
        print(f"Downloading file into {folderName} folder\n")
        dwnPhoto()

        print(input(
        """
        The file was successfully saved!
        press "Enter" to exit.
        """))


    if photosCount > 1:
        print("There're more than 1 file in that post.")
        print("Download it anyway? [y/n]: ", end="")
        _ = input().lower()

        if _ == "y":
            print(f"Downloading files in folder «{folderName}»")
            dwnPhoto()

        else:
            print("\nShutting down.", end="")
            for i in range(2):
                sleep(0.8)
                print(".", end="")

            sys.exit()


try:
    saveFromInsta()
except BadResponseException:
    print("Incorrect shortcode :(")
