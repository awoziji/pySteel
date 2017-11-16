#
##Gantry Girder Designer
##Author-Yajnavalkya Bandyopadhyay
##B.Tech Project Part 1
##Supervisor - Mr. Somnath Majumder
##email-yajnab@gmail.com
#

print("Gantry Girder Designer")
print("Author- Yajnavalkya Bandyopadhyay")
print("email- yajnab@gmail.com")

import numpy as np
from colorama import init, Fore, Style

#Constants
FOS = 1.5 #Factor of Safety
W_Crane = 200#Weight of the Crane
W_Crab = 40#Weight of the Crab
Lc = 15#Length of
L1 = 1.2#Length of Crane
L = 7.5#Length of Gantry warehouse
c = 3.5#W of Crane
e= 0.45#Depth of Rail and half the depth of the girder
w_d = 1.9#Dead Load (Factored)
E = 2*10**5 #Modulus of Elasticity
fy = 250 #Value of fy


class gantry:
	init()
	#Load Calculation
	print("Load Calculation")
	#Vertical Load
	Wt = W_Crane/4 #Maximum Static Wheel Load due to the weight of the crane
	W1 = (W_Crane+W_Crab)*(Lc-L1)/(2*Lc) #Maximum Static wheel Load due to Crane Load
	W_Vert_Total = (Wt + W1) * 1.25 #Total Load, 1.25 is multiplied for impact
	WC = FOS * W_Vert_Total #Factored Load
	print("Total Vertical Load is", WC);
	
	#Horizontal Load
	W_Horizontal = FOS * 0.1 * (W_Crane + W_Crab)/4 # 10% of Crane and Crab load Combined
	print("Total Horizontal Load is", W_Horizontal)
	
	#Longitudinal Braking Load
	W_Braking = 0.05 * W_Crane * FOS #5% of the Wheel Load of a Crane, it is also known as surge load
	print("Horizontal Braking Load is", W_Braking)
	
	
	#Moment Calculation
	print("Moments")
	#Vertical Maximum Bending Moment
	M1 = WC*L/4
	M2 = 2*WC*(L/2-c/4)**2/L
	M_v = M2 if (M2>M1) else M1 #No Self Load Considered
	print("Vertical Bending without considering Self Load", M_v)
	w = FOS*w_d
	M_v_sf = w*L**2/8 #Due to Self Load
	print("Vertical Bending due to dead Load", M_v_sf)
	#Horizontal Bending Moment
	M_y = 2*W_Horizontal*(L/2-c/4)**2/L
	print("Moment due to Bending in horizontal axis(Surge Load)", M_y)
	#Moment due to Drag
	M_drag = W_Braking*e/L*(L/2-c/4)
	print("Moment due to Drag", M_drag)

	M = M_v + M_v_sf + M_drag #Total Moment
	print("Total Bending Moment is", M)
	#Shear Force
	print("Shear Force")

	SF_L = WC*(2-(c/L)) #Shear Force due to wheel load
	SF_DL = w*L/2 #Shear Force due to Dead Load
	SF_Horizontal = W_Horizontal*(2-c/L) #Horizontal Shear Force
	SF_Braking =  W_Braking*e/L #Shear Force due to Drag Force
	SF = SF_L + SF_DL + SF_Braking #Total Shear Force

	print("Total Shear Force is", SF)

	#Design Calculation 
	print("Design Calculation")

	Ll = (round((L*1000/12)/50.0)*50.0) #Rounding off to nearest multiple of 50
	print("We choose the depth to", Ll);
	Lw = (round((L*1000/30)/50.0)*50.0)
	print("We choose the Width to", Lw); #Rounding off to nearest multiple of 25

	I = ((15.6*W_Crane*1000)*(L-c)*(2*L**2+2*L*c-c**2)/(L*E))*10**6 #Converting to mm**4 unit system
	print("The Required Momenet of Inertia is", I);

	Zp = 1.4*M*10**6/fy #Plastic Index
	print("The Required Plastic Index is", Zp);

	ISMB = np.genfromtxt('ISMB.csv' , dtype=None, delimiter=',', names=True)
	ISMC = np.genfromtxt('ISMC.csv' , dtype=None, delimiter=',', names=True)

	I_sec, = np.where(ISMB['Designation']>=Ll)
	C_sec, = np.where(ISMC['Designation']>=Lw)
	i=0;j=0
	while i<len(I_sec):
		fail=0
		while j<len(C_sec):

			fail=0
			I_sec_sel=ISMB['Designation'][I_sec[i]]#Selected first iteration
			C_sec_sel=ISMC['Designation'][C_sec[j]]#Selected first iteration

			print("The selected I section  and C Section are specifically ISMB",I_sec_sel,"and ISMC",C_sec_sel)

			#Elastic Properties of the Joint Section
			A = ISMB['A'][I_sec[i]] + ISMC['A'][C_sec[j]] #Area
			print("The Summative Area is", A)
			y_bar = ((ISMB['A'][I_sec[i]]*100*ISMB['h'][I_sec[i]]/2) + ISMC['A'][C_sec[j]]*100*(ISMB['h'][I_sec[i]]+ISMC['tw'][C_sec[j]]-ISMC['Cyy'][C_sec[j]]))/(A*100)
			print("The y bar of the joint section is", y_bar)
			h1 = y_bar - ISMB['h'][I_sec[i]]/2
			print("h1 is =", h1)
			h2 = (ISMB['h'][I_sec[i]]+ISMC['tw'][C_sec[j]])-y_bar-ISMC['Cyy'][C_sec[j]]
			print("h2 is =", h2)
			Iz = ISMB['Ixx'][I_sec[i]]*10**4 +  ISMB['A'][I_sec[i]]*(10**2)*h1**2 + ISMC['Iyy'][C_sec[j]] + ISMC['A'][C_sec[j]]*(10**2)*h2**2
			print("Moment of Intertia along x axis is", Iz)
			Zzb = Iz/y_bar
			Zzt = Iz/(ISMB['h'][I_sec[i]]-y_bar)
			print("Plastic Sections are Zzb=",Zzb,"and Zzt=",Zzt)
			Iy = (ISMB['Iyy'][I_sec[i]] + ISMC['Ixx'][C_sec[j]])*10**4
			print("Moment of Intertia along y axis is", Iy)
			Itf=ISMB['tf'][I_sec[i]]*ISMB['b'][I_sec[i]]**3/12
			print("Itf for the tension flange is", Itf)
			Icf=Itf+ (ISMC['Ixx'][C_sec[j]])*10**4
			print("Icf for the compression flange is", Icf)
			Zty=Icf/(ISMC['h'][C_sec[j]]/2)
			print("Zy for top flange is", Zty)

			#Plastic Properties
			dp = ISMC['A'][C_sec[j]]*100/(2*ISMB['tw'][I_sec[i]])
			print("The Plastic Neutral axis is", dp)

			SAy1= ISMB['tf'][I_sec[i]]*ISMB['b'][I_sec[i]]*(ISMB['h'][I_sec[i]]/2+dp-ISMB['tf'][I_sec[i]]/2)+((ISMB['h'][I_sec[i]]/2+dp-ISMB['tf'][I_sec[i]])**2)*ISMB['tw'][I_sec[i]]/2
			print("Above Equal Axis SAy1 is=",SAy1)

			SAy2 = ISMC['A'][C_sec[j]]*100*(ISMB['h'][I_sec[i]]/2+ISMC['tw'][C_sec[j]]-dp-(ISMC['Cyy'][C_sec[j]]*10))+ISMB['b'][I_sec[i]]*ISMB['tf'][I_sec[i]]*(ISMB['h'][I_sec[i]]/2-dp-(ISMB['tf'][I_sec[i]]/2))+(((ISMB['h'][I_sec[i]]/2-dp-ISMB['tf'][I_sec[i]])**2)*ISMB['tw'][I_sec[i]]/2)
			print("Below Equal Axis SAy2 is=",SAy2)

			Zpz = SAy1 + SAy2
			print("Total Zpz=", Zpz)

			Zpy= ISMB['tf'][I_sec[i]]*(ISMB['b'][I_sec[i]]**2)/4 + ((ISMC['h'][C_sec[j]]-2*ISMC['tf'][C_sec[j]])**2)*ISMC['tw'][C_sec[j]]/4 + 2*ISMC['b'][C_sec[j]]*ISMC['tf'][C_sec[j]]*(ISMC['h'][C_sec[j]]-ISMC['tf'][C_sec[j]])/2
			print("Zpy for Top Flange only is", Zpy)

			#Checks
			b_t_I = ((ISMB['b'][I_sec[i]]-ISMB['tw'][I_sec[i]])/2)/ISMB['tf'][I_sec[i]]
			b_t_C = ((ISMC['b'][C_sec[j]]-ISMC['tw'][C_sec[j]])/2)/ISMC['tf'][C_sec[j]]
			d_t_I = ((ISMB['h'][I_sec[i]]-2*ISMB['tf'][I_sec[i]])/ISMB['tw'][I_sec[i]])
			if(b_t_I<9.4):
				print(Fore.GREEN+"b/t ratio of I beam",b_t_I,"< 9.4 is safe"+Style.RESET_ALL)
			else:
				print(Fore.RED+"b/t ratio of I beam",b_t_I,"> 9.4 is unsafe"+Style.RESET_ALL)
				fail=1
			if(b_t_C<9.4):
				print(Fore.GREEN+"b/t ratio of Channel",b_t_C,"< 9.4 is safe"+Style.RESET_ALL)
			else:
				print(Fore.RED+"b/t ratio of Channel",b_t_C,"> 9.4 is unsafe"+Style.RESET_ALL)
				fail=1
			if(d_t_I<84):
				print(Fore.GREEN+"d/t ratio of the web",d_t_I,"< 84 is safe"+Style.RESET_ALL)
			else:
				print(Fore.RED+"d/t ratio of the web",d_t_I,"> 84 is unsafe"+Style.RESET_ALL)
				fail=1

			#Moment Capacity Check
			Mdz1=1.2*Zzb*fy/1.1
			Mdz2=fy*Zpz/1.1
			Mdz = Mdz2 if (Mdz2<Mdz1) else Mdz1
			print("Mdz is ", Mdz)
			Mdy1=fy*Zpy/1.1
			Mdy2=1.2*Zty*fy/1.1
			Mdy = Mdy2 if (Mdy2<Mdy1) else Mdy1
			print("Mdy is ", Mdy)

			#Check
			Mchk=(M/(Mdz*10**(-6)))+(M_y/(Mdy*10**(-6)))
			if(Mchk<1):
				print(Fore.GREEN+"M/Mdz+My/Mdy=",Mchk,"< 1 is safe"+Style.RESET_ALL)
			else:
				print(Fore.RED+"M/Mdz+My/Mdy=",Mchk,"> 1 is unsafe"+Style.RESET_ALL)
				fail=1

			#Shear Check
			print("Check for Shear")
			print("Total Vertical Load Vz=", SF)
			Shear_cap= ISMB['h'][I_sec[i]]*ISMB['tw'][I_sec[i]]*fy/((3**(0.5))*1.1)*10**(-3)
			Shear_cap_6=0.6*Shear_cap
			if(Shear_cap>SF and Shear_cap_6>SF):
				print(Fore.GREEN+"Maximum Shear is",Shear_cap," and 0.6 of the maximum shear is ",Shear_cap_6,"are both greater than the vertical laod",SF,"hence the strcuture is safe"+Style.RESET_ALL)
			else:
				print(Fore.GREEN+"Maximum Shear is",Shear_cap," and 0.6 of the maximum shear is ",Shear_cap_6,"are not greater than the vertical laod",SF,"hence the strcuture is unsafe"+Style.RESET_ALL)
				fail=1

			if(fail==0):
				break;
			fail=0
			j+=1
		i+=1
