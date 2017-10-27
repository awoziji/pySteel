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
	print("Vertical Load Calculation") #Vertical Load
	W_Crane = #Weight of the Crane
	W_Crab = #Weight of the Crab 	
	Wt = W_Crane/4 #Maximum Static Wheel Load due to the weight of the crane
	W1 = (W_Crane+W_Crab)*(Lc-L1)/(2*Lc) #Maximum Static wheel Load due to Crane Load
	W_Vert_Total = (Wt + W1) * 1.25 #Total Load, 1.25 is multiplied for impact
	WC = FOS * W_Vert_Total #Factored Load
	print("Total Vertical Load is", WC);
	#Moment Calculation
	print("Moments")
	#Shear Force
	print("Shear Force")
	#Design Calculation 
	print("Design Calculation")
