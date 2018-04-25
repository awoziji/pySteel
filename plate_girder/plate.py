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
c_load_n=2 #NUmber of Concentrated Loads
c_load = 150 #Concentrated Load at 6m from either ends
c_load_dist = 6 #Distance of loads from either of the ends
span= 20 #Span of the Girder


class plate_girder:
	init() #Initialize Colorama
	
	w_udl = udl*span#UDL Load on Girder
	F_w_udl = w_udl*FOS	#Factored w_udl
	print("Superimposed Uniformaly Distributed Load on the Girder Span is", w_udl)
	print("Factored Superimposed Uniformaly Distributed Load on the Girder Span is", F_w_udl)
	w_c= c_load #Superimposed Concentrated Load
	F_w_c= FOS*w_c #Superimposed Concentrated Load
	print("Concentrated Load on the Span", w_c)
	print("Factored Concentrated Load on the Span", F_w_c)
	w_self = (w_udl+w_c*c_load_n)/300
	F_w_self = FOS*w_self
	print("Self Load on the Girder Span is", w_self)
	print("Factored Self Load on the Girder Span is", F_w_self)
	w_total_udl = (w_self+udl)*FOS
	print("Total UDL Load on the Girder Span is w_total_udl=", w_total_udl)
	w_total = w_total_udl*span + c_load_n*c_load*FOS
	print("Total Load on the Girder w_total=", w_total)

	#Calculation of Reactions
	#Let two reactions be at the supports. Reaction at the one end be Ra and the other end be Rb
	#Moment on one side(Lets say its B) have the moment as 0. So the reaction will play like
	Ra = (w_total_udl*0.5*(span**2)+F_w_c*(span-c_load_dist)+F_w_c*(c_load_dist))/span
	print("The Reaction at Reaction point a be Ra=", Ra)
	Rb = w_total - Ra
	print("The Reaction at Reaction point a be Rb=", Rb)

	#Bending Moments
	BM_cnc = Ra*c_load_dist - w_total_udl*(c_load_dist**2)/2
	print("Bending moment at the concentrated load points BM_cnc=",BM_cnc)
	BM_ctr = Ra*(span/2) - F_w_c*((span/2)-c_load_dist) - w_total_udl*0.5*(span/2)**2
	print("Bending moment at the center of the span BM_ctr=",BM_ctr)
