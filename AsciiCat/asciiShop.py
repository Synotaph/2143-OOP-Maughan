"""
Program: 
--------
    AsciiCat - Homework 3

Description:
------------
    This program grabs a picture of a cat from the internet, converts it
    to an ascii image, and then inverts the colors

Name: Zachary Maughan
Date: 3 March 2016
"""
import os
import time
import urllib3, uuid
from PIL import Image
import sys


url = 'http://thecatapi.com/api/images/get'

"""
    @Description:
        This meathod retrieves the cat picture from the internet. 
    @Params:
        directory - Where the picture will be stored
        filename - The name that the picture will be stored under.
        format - The filetype the picture will be stored as. 
    @Returns:
        (savefile) - The picture that was retrieved.
    """


def getCat(directory=None, filename=None, format='png'):
    basename = '%s.%s' % (filename if filename else str(uuid.uuid4()), format)
    savefile =  os.path.sep.join([directory.rstrip(os.path.sep), basename]) if directory else basename
    downloadlink = url + '?type=%s' % format
    http = urllib3.PoolManager()
    r = http.request('GET', downloadlink)
    fp = open(savefile, 'wb')
    fp.write(r.data)
    fp.close()
    return savefile

"""
@Class: RandomCat 
@Usage: 
    getImage() - Will pull a random cat picture from the internet.

@Description:
    This class handles retrieving the picture.
@Params:
    none

@Methods:
    getImage - Pulls a random cat picture from the internet.
"""


class RandomCat(object):

    def __init__(self):

        self.name = ''          # name of image
        self.path = '.'         # path on local file system
        self.format = 'png'
        self.width = 0          # width of image
        self.height = 0         # height of image        
        self.img = None         # Pillow var to hold image


    """
    @Description: 
    - Uses random cat to go get an amazing image from the internet
    - Prompts the user to name the image
    - Saves the image to some location
    @Returns: 
    """
    def getImage(self):
        self.name = input('What do you want to name this image? ')
        os.system('cls')
        getCat(directory=self.path, filename=self.name, format=self.format)
        self.img = Image.open(self.name+'.'+self.format)
        
        self.width, self.heigth = self.img.size

"""
@Class: AsciiImage 
@Usage: 
    AsciiImage(50)      #creates a preset ready for the cat image.
    AsciiImage()        #will accept the image and leave the size unchanged.

@Description:
    This class handles the manipulation of the image by converting it to ascii,
    inverting the brightness, flipping the image vertically or horizontally, and
    printing the image. 
@Params:
    new_Width   - (int) the width of the image or Not_Set.

@Methods:
    convertToAscii - This method will convert the image first into greyscale, and then into ascii.

    flip - This method will flip an image horizontally, or vertically.
        Usage - flip(vertical) = will flip the image vertically
                flip(horizontal) = will flip the image horizontally
    
    listToMatrix - Converts to 2D list of lists to help with manipulating the ascii image.

    printImage - This method will print the ascii picture in a coherent way.
"""


class AsciiImage(RandomCat):

    def __init__(self,new_width="not_set"):
        super(AsciiImage, self).__init__()

        self.newWidth = new_width
        self.newHeight = 0
            
        self.asciiChars = [ '#', 'A', '@', '%', 'S', '+', '<', '*', ':', ',', '.']
        self.imageAsAscii = []
        self.matrix = None
        
        
    """
    @Name: convertToAscii
    @Description:
        This method will convert the image first into greyscale, and then into ascii.
    @Params: none
    @Returns:
    """
    def convertToAscii(self):
    
        if self.newWidth == "not_set":
            self.newWidth = self.width
            
        self.newHeight = int((self.heigth * self.newWidth) / self.width)
            
        if self.newWidth == None:
            self.newWidth = self.width
            self.newHeight = self.height
            
        self.newImage = self.img.resize((self.newWidth, self.newHeight))
        self.newImage = self.newImage.convert("L") # convert to grayscale
        all_pixels = list(self.newImage.getdata())
        self.matrix = listToMatrix(all_pixels,self.newWidth)
        

        for pixel_value in all_pixels:
            index = pixel_value // 25 # 0 - 10
            self.imageAsAscii.append(self.asciiChars[index])

    """
    @Name: flip
    @Description:
        This method will flip an image horizontally, or vertically. 
    @Params: direction (string) - [horizontal,vertical] The direction to flip the cat.
    @Returns: (string) - Flipped ascii image.
    """
    def flip(self, way = 'none'):
        temp = []
        all_pixels = list(self.newImage.getdata())
        if way == 'vertical':
            while len(temp) <= len(self.imageAsAscii):
                for a in range(self.newHeight - 1, 0, -1):
                    for b in range(0, self.newWidth):
                        temp.append(self.imageAsAscii[(a * self.newWidth) + b])
        elif way == 'horizontal':
            while len(temp) <= len(self.imageAsAscii):
                for a in range(0, self.newHeight):
                    for b in range(self.newWidth, 0, -1):
                        temp.append(self.imageAsAscii[(a * self.newWidth - 1) + b])
        self.imageAsAscii = []
        self.imageAsAscii = temp


    """
    @Name: invert
    @Description:
        This method will invert the ascii characters from dark to light, and vice-versa.
    @Params: None
    @Returns: (string) - Inverted ascii image.
    """
    def invert(self):
        self.imageAsAscii = []
        all_pixels = list(self.newImage.getdata())
        for pixel_value in all_pixels:
            index = 10 - pixel_value // 25 # 0 - 10
            self.imageAsAscii.append(self.asciiChars[index])

    """
    Converts to 2D list of lists to help with manipulating the ascii image.
    """
    def listToMatrix(l, n):
        return [l[i:i+n] for i in range(0, len(l), n)]
        """
    @Name: printImage
    @Description:
        This method will print the ascii picture in a coherent way. 
    @Params: none
    @Returns: prints image to screen
    """
    def printImage(self):
        self.imageAsAscii = ''.join(ch for ch in self.imageAsAscii)
        for c in range(0, len(self.imageAsAscii), self.newWidth):
            print (self.imageAsAscii[c:c+self.newWidth])

if __name__=='__main__':
    awesomeCat = AsciiImage(75)
    awesomeCat.getImage()
    
    awesomeCat.convertToAscii()
    awesomeCat.printImage()
    awesomeCat.invert()
    awesomeCat.printImage()
