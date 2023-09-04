# leaf_highlight.py

leaf_highlight is a program that takes android screenshots and xml metadata dumps from android's UIAutomator Framework and uses them to highlight the leaf-level GUI components that are present in the xml files. The program outputs screenshots with these leaf components highlighted by yellow rectangles.

# How To Run

To run this program you can use the following command:
    
    python leaf_highlight.py
**NOTE that both the Python file and the screenshot/xml file pairs all need to be in the same directory for the program to work.**

The program should create an output folder if it doesn't exist already and populate the folder with the highlighted files
# Libraries

The two libraries needed for the program are ElementTree and Pillow. ElementTree is included in Python installs but Pillow needs to be installed separately. Pillow can be installed through a pip command, for example:

    pip install Pillow

# Explanation of Solution and Design Decisions

To solve this problem I firstly needed to find a way to parse the XML files for all of its components. Using **ElementTree** as an XML parsing tool was the first step. Secondly, I needed to find out how to parse all the way down to the leaf nodes and ignore other components like layouts. I used the `iter()` function starting at the root to iterate through all of the xml nodes. I then figured out that if a node is length 0 then it is a leaf node. Then for every leaf node I captured the bounds (xy coordinate pairs) and put them into a list.

I used the Python library **Pillow** to draw rectangles around the bounds that I put into the list. I made the outline of the rectangles yellow to highlight the components. Lastly, I output the new image files with the highlights into the output folder.

I decided to use **ElementTree** mostly because I didn't have to install any extra libraries to use it because it comes with Python. I used **Pillow** because I felt that it was easy to use and it was able to cleanly draw the rectangles for the highlights.