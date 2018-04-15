import numpy as np
import pandas as pd

from colorama import init, Fore, Style, Back
from PIL import Image, ImageFont, ImageDraw

#Constants
span = 2.25 #Span
lload = 4000 #Live Load
thk_plank = 0.065 #Plank thickness
w_plank=8000#Load of Plank in N/(m^2)
E = 1*10**4 #Modulus of Elasticity

class fbridge:
	init()
	#Constant Calculations
	sw_plank = thk_plank*w_plank#Self Load of Plank
	print("Self Load of Plank \t",sw_plank,"")
	print("Live Load of Plank \t",lload,"")
	total_load = sw_plank+lload
	print("Total Load \t\t",Fore.WHITE+Back.MAGENTA+"",total_load,"",Style.RESET_ALL)
	max_bm = (total_load*span**2)/8 #Maximum Bending moment w*l^2/8
	print("Maximum Benging Moment \t",Fore.WHITE+Back.GREEN+"",max_bm,"",Style.RESET_ALL)
	max_sf = (total_load*span)/2 #Maximum shear force wl/2
	print("Maximum Shear Force \t",Fore.WHITE+Back.GREEN+"",max_sf,"",Style.RESET_ALL)
	avg_ss = max_sf/(thk_plank*10**6) #Average Shear Stress
	print("Average Shear Stress \t",Fore.WHITE+Back.GREEN+"",avg_ss,"",Style.RESET_ALL)
	avg_ss = 1.5*avg_ss #Maximum Shear Stress
	print("Maximum Shear Stress \t",Fore.WHITE+Back.GREEN+"",avg_ss,"",Style.RESET_ALL)
	I = (1000*(1000*thk_plank)**3)/12
	print("Moment of Inertia \t",Fore.WHITE+Back.CYAN+"",I,"",Style.RESET_ALL)
	max_def  = (5/384)*total_load*((span*1000)**4)/(E*I*1000)
	print("Maximum Deflection \t",Fore.WHITE+Back.BLUE+"",max_def,"",Style.RESET_ALL)
	perm_def = span*1000/325
	print("Permissible Deflection \t",Fore.WHITE+Back.BLUE+"",perm_def,"",Style.RESET_ALL)
