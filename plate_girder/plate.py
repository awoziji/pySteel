#
##Gantry Girder Designer
##Author-Yajnavalkya Bandyopadhyay
##B.Tech Project Part 2
##Supervisor - Mr. Somnath Majumder
##email-yajnab@gmail.com
#

print("Plate Girder Designer")
print("Author- Yajnavalkya Bandyopadhyay")
print("email- yajnab@gmail.com")

import numpy as np
from colorama import init, Fore, Style, Back
from PIL import Image, ImageFont, ImageDraw

#Constants
FOS = 1.5 #Factor of Safety
udl = 30 #UDL Superimposed Load in KN
c_load = 150 #Concentrated Load at 6m from either ends
c_load_dist = 6 #Distance of loads from either of the ends
span= 20 #Span of the Girder
