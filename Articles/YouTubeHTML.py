#!/usr/bin/env python3
import sys
import os
import requests
from bs4 import BeautifulSoup

class YouTubeHTML():
    def __init__(self, url):
        self.url = url
        self.r = requests.get(url)
        self.soup = BeautifulSoup(self.r.content, 'html.parser')
        # self.play_button = self.driver.find_element_by_css_selector(button_selector)
        self.title = self.getTitle()
        self.username = self.getUsername()
        self.id = self.getVideoId(url)
        self.imagePathForWrite = self.getImagePathForWrite()
        self.downloadThumbnail()

    def getImagePathForWrite(self):
        filename = self.getPathForImage(self.title + ".jpg")
        if os.path.exists(filename):
            newFilename = filename
            i = 2
            while os.path.exists(newFilename):
                newFilename = self.getPathForImage(self.title + "_{num}.jpg".format(num=i))
                i += 1
            filename = newFilename
        return filename

    def getUsername(self):
        return self.soup.find(class_="yt-user-info").text[1:-1]

    def getTitle(self):
        return self.soup.title.string.split(" - YouTube")[0]
        # return self.soup.title.string.encode('ascii', 'ignore').split(" - YouTube")[0]

    def getVideoId(self, url):
        return url.split("watch?v=")[-1]

    def getThumbNailUrl(self):
        return "http://img.youtube.com/vi/{id}/maxresdefault.jpg".format(id=self.id)

    def getPathForImage(self, filename):
        return os.path.join(os.path.dirname(os.getcwd()), "images/", filename)

    def downloadThumbnail(self):
        thumbnailUrl = self.getThumbNailUrl()
        requestsImage = requests.get(thumbnailUrl)
        filename = self.imagePathForWrite
        with open(filename, "wb") as f:
            f.write(requestsImage.content)


class READMEWriter():
    def __init__(self, html):
        self.html = html
        self.title = self.getTitle()
        self.image = self.getImage()

    def getTitle(self):
        text = "{title} by {username}".format(title=self.html.title, username=self.html.username)
        return "\n### [{title}]({link})\n".format(title=text, link=self.html.url)



    def getImage(self):
        imagePath = "/images/" + html.imagePathForWrite.split("/images/")[-1]
        # imagePath = "/images/{name}.jpg".format(name=self.html.title)
        return "![{name}]({path})\n".format(name=self.html.title, path=imagePath)

    def write(self):
        with open("README.md", mode='a') as f:
            f.write(self.title)
            f.write(self.image)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("Please give me an Youtube url")
    else:
        url = sys.argv[1]
        print("Get url from command line\n%s"%url)

        try:
            html = YouTubeHTML(url)
            writer = READMEWriter(html)
            writer.write()

        except KeyboardInterrupt:
            print("Ctrl-C clicked!\nBye!")

        finally:
            print("Writing done!")


# http://img.youtube.com/vi/gmvwZRwn-j0/0.jpg
# https://www.youtube.com/watch?v=gmvwZRwn-j0/0.jpg
