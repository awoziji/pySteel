#
##Gantry Girder Designer
##Author-Yajnavalkya Bandyopadhyay
##email-yajnab@gmail.com
#

print("Gantry Girder Designer")
print("Author- Yajnavalkya Bandyopadhyay")
print("email- yajnab@gmail.com")

import numpy as np

#Constants
FOS = 1.5 #Factor of Safety

class gantry:
	#Load Calculation
	print("Load Calculation")
	#Vertical Load
	W_Crane = #Weight of the Crane
	W_Crab = #Weight of the Crab 	
	Wt = W_Crane/4 #Maximum Static Wheel Load due to the weight of the crane
	W1 = (W_Crane+W_Crab)*(Lc-L1)/(2*Lc) #Maximum Static wheel Load due to Crane Load
	W_Vert_Total = (Wt + W1) * 1.25 #Total Load, 1.25 is multiplied for impact
	WC = FOS * W_Vert_Total #Factored Load
	print("Total Vertical Load is", WC);
	
	#Horizontal Load
	W_Horizontal = FOS * 0.1 * (W_Crane + W_Crab) # 10% of Crane and Crab load Combined
	print("Total Horizontal Load is", W_Horizontal)
	
	#Longitudinal Braking Load
	W_Braking = 0.05 * W_Crane * FOS #%% of the Wheel Load of a Crane
	print("Horizontal Braking Load is", W_Braking)
	
	
	#Moment Calculation
	print("Moments")
	#Vertical Maximum Bending Moment
	M1 = WC*L/4
	M2 = 2*WC*(L/2-c/4)**2/L
	M_v = (M2>M1)?M2:M1 #No Self Load Considered
	print("Vertical Bending without considering Self Load", M_v)
	M_v_sf = w*L**2/8 #Due to Self Load
	print("Vertical Bending due to dead Load", M_v_sf)
	#Horizontal Bending Moment
	M_y = 2*W_Horizontal*(L/2-c/4)**2/L
	print("Moment due to Bending in horizontal axis", M_y)
	#Moment due to Drag
	M_drag = W_Braking*e/L*(L/2-c/4)
	print("Moment due to Drag", M_drag)

	M = M_v + M_v_sf + M_drag #Total Moment
	print("Total Bending Moment is", M)
	#Shear Force
	print("Shear Force")

	SF_L = WC*(2-c/L) #Shear Force due to wheel load
	SF_DL = wL/2 #Shear Force due to Dead Load
	SF_Horizontal = W_Horizontal*(2-c/L) #Horizontal Shear Force
	SF_Braking =  W_Braking*e/L #Shear Force due to Drag Force
	SF = SF_L + SF_DL + SF_Horizontal + SF_Braking #Total Shear Force

	print("Total Shear Force is", SF)

	#Design Calculation 
	print("Design Calculation")
