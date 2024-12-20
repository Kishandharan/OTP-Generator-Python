from random import randint

def generateOTPs(fname, otpfilelen, otplen):
	file = open(fname, "w")
	otps = []
	strotps = ""
	otp = 0

	if not ((otpfilelen <= 1) and (otplen <= 1)):
		for i in range(0, otpfilelen):
		    while True:
		        otp = randint(int(str(1)+("0"*(otplen-1))), int(str("9")*otplen))
		        if otp in otps:
		            continue
		        else:
		            otps.append(otp)
		            break
		    strotps += str(otp)+"\n"
		file.write(strotps)
		file.close()   
	else:
	    print('''
We are sorry,
But the number of OTPs and the number of digits
in each OTP must be higher than 1.
	    	''') 

generateOTPs(
	input("Output File Name: "),
	int(input("How many OTPs: ")),
	int(input("How many digits in each OTP: "))
)