import os
import xml.etree.ElementTree as ET 
from PIL import Image, ImageDraw

# Method to get xml files from current directory and return a list of the files
def getFiles():

    directory = os.getcwd()
    xml_files = list()

    for filename in os.listdir(directory):

        if filename.endswith(".xml"):
            xml_files.append(filename)

    return xml_files

# Method to draw the yellow borders of the leaf components. 
# Needs to be passed a list of x,y points in tuple form and the path to the png
# Uses Pillow to draw the borders on the image
def drawBorders(points,pngPath):

    image = Image.open(pngPath)
    draw = ImageDraw.Draw(image)

    for point in points:
        draw.rectangle(point,fill= None,outline="yellow", width=8)
        out = pngPath[0:len(pngPath)-4] + '_out' + pngPath[len(pngPath)-4:len(pngPath)]

    # Save screenshots with borders added to the output folder
    toDir = os.path.join(os.getcwd(),'output')
    image.save(os.path.join(toDir,out))

        
def main():

    # Getting list of xml files 
    xml_files = getFiles()

    # Creating an output folder to hold the processed
    newpath = os.path.join(os.getcwd(),'output')
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    
    # Looping over every xml file in the current directory
    for file in xml_files:

        tree = ET.parse(file)
        root = tree.getroot()
 
        points = list()
        
        # Loop over all nodes in file
        for node in root.iter('*'):

            # if a node is length 0 then it is a leaf
            if 0 ==  len(node):
                #If a node has attributes then it is a node we want to get the bounds of
                if node.attrib is not None:
                    bounds = node.attrib['bounds']
                    idx = bounds.find(']')
                    xy = str(bounds[1:idx] + ',' + bounds[idx+2:len(bounds)-1])
                    points.append(eval(xy))

        imgPath = file[0:len(file)-3] + 'png'
        drawBorders(points,imgPath)
        

if __name__ == "__main__":
    main()