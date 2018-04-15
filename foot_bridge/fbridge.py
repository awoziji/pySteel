import numpy as np
import pandas as pd

from colorama import init, Fore, Style
from PIL import Image, ImageFont, ImageDraw

#Constants
span = 4 #Span
lload = 4000 #Live Load
thk_plank = 0.065 #Plank thickness
w_plank=8000#Load of Plank in N/(m^2)

class fbridge:
	#Constant Calculations
	sw_plank = thk_plank*w_plank#Self Load of Plank
	total_load = sw_plank+lload
	max_bm = (total_load*span**2)/8 #Maximum Bending moment w*l^2/8
	max_sf = (total_load*span)/2 #Maximum shear force wl/2
	avg_ss = max_sf/(thk*1000) #Average Shear Stress
	avg_ss = 1.5*avg_ss #Maximum Shear Stress

	mi_plank = (1000*thk**3)/12
