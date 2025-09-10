print("Welcome to the manga recommender!")
print("pls insert your preference to find your manga")

Genre = input(" What is prefered genre? (shonen, slice of life, mecha):")
Duration = input(" what duration should the manga be? (short, medium, long):")
Time = input("Which year? (2000s, 2010s):")

if Genre == 'shonen' and Duration == 'short' and Time == '2000':
	print("The manga recommend for this is 'Black Cat' ")
elif Genre == 'shonen' and Duration == 'short' and Time == '2010':
	print("The manga recommend for this is 'Enigma' ")
elif Genre == 'shonen' and Duration == 'medium' and Time == '2000':
	print("The manga recommend for this is 'Flame of Recca' ")
elif Genre == 'shonen' and Duration == 'medium' and Time == '2010':
	print("The manga recommend for this is 'Nurarihyon no Mago' ")
elif Genre == 'shonen' and Duration == 'long' and Time == '2000':
	print("The manga recommend for this is 'Bleach' ")
elif Genre == 'shonen' and Duration == 'long' and Time == '2010':
	print("The manga recommend for this is 'Beelzebub' ")


if Genre == 'slice of life' and Duration == 'short' and Time == '2000':
	print("The manga recommended for this is 'Azumanga Daioh' ")
elif Genre == 'slice of life' and Duration == 'short' and Time == '2010':
	print("The manga recommended for this is 'Anohana' ")
elif Genre == 'slice of life' and Duration == 'medium' and Time == '2000':
	print("The manga recommended for this is 'Love Hina' ")
elif Genre == 'slice of life' and Duration == 'medium' and Time == '2010':
	print("The manga recommended for this is 'K-On!' ")
elif Genre == 'slice of life' and Duration == 'long' and Time == '2000':
	print("The manga recommended for this is 'Nichijou' ")
elif Genre == 'slice of life' and Duration == 'long' and Time == '2010':
	print("The manga recommended for this is 'Seitokai Yakuindomo' ")


if Genre == 'mecha' and Duration == 'short' and Time == '2000':
	print("The manga recommended for this is 'Eureka Seven' ")
elif Genre == 'mecha' and Duration == 'short' and Time == '2010':
	print("The manga recommended for this is 'Saijaku Muhai no Bahamut' ")
elif Genre == 'mecha' and Duration == 'medium' and Time == '2000':
	print("The manga recommended for this is 'Mobile Suit Gundam 00' ")
elif Genre == 'mecha' and Duration == 'medium' and Time == '2010':
	print("The manga recommended for this is 'Broken Blade' ")
elif Genre == 'mecha' and Duration == 'long' and Time == '2000':
	print("The manga recommended for this is 'Full Metal Panic Series' ")
elif Genre == 'mecha' and Duration == 'long' and Time == '2010':
	print("The manga recommended for this is 'Mobile Suit Gundam SEED Series' ")


else:
	print("Invalid input. I can only provide this at the moment (shonen, slice of life, mecha)")