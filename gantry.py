#
##Gantry Girder Designer
##Author-Yajnavalkya Bandyopadhyay
##email-yajnab@gmail.com
#

print("Gantry Girder Designer")
print("Author- Yajnavalkya Bandyopadhyay")
print("email- yajnab@gmail.com")

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
	#Shear Force
	print("Shear Force")
	#Design Calculation 
	print("Design Calculation")
