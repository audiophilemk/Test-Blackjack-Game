import random

print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("______ _            _    _            _")
print("| ___ \ |          | |  (_)          | |")
print("| |_/ / | __ _  ___| | ___  __ _  ___| | __")
print("| ___ \ |/ _` |/ __| |/ / |/ _` |/ __| |/ /")
print("| |_/ / | (_| | (__|   <| | (_| | (__|   <")
print("\____/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\ ")
print("                        / |")
print("                       |__/")
print("\nBy Tray and Alex")
print("\n\n\n\n\n\n\n\n\n\n")

array_spades = ["", "", " _____\n|2 .  |\n| /.\ |\n|(_._)|\n|  |  |\n|____2|",
                " _____\n|3 .  |\n| /.\ |\n|(_._)|\n|  |  |\n|____3|",
                " _____\n|4 .  |\n| /.\ |\n|(_._)|\n|  |  |\n|____4|",
                " _____\n|5 .  |\n| /.\ |\n|(_._)|\n|  |  |\n|____5|",
                " _____\n|6 .  |\n| /.\ |\n|(_._)|\n|  |  |\n|____6|",
               	" _____\n|7 .  |\n| /.\ |\n|(_._)|\n|  |  |\n|____7|",
                " _____\n|8 .  |\n| /.\ |\n|(_._)|\n|  |  |\n|____8|",
                " _____\n|9 .  |\n| /.\ |\n|(_._)|\n|  |  |\n|____9|",
                " _____\n|10.  |\n| /.\ |\n|(_._)|\n|  |  |\n|___10|",
		" _____\n|A .  |\n| /.\ |\n|(_._)|\n|  |  |\n|____A|",
               	" _____\n|J .  |\n| /.\ |\n|(_._)|\n|  |  |\n|____J|",
                " _____\n|Q .  |\n| /.\ |\n|(_._)|\n|  |  |\n|____Q|",
               	" _____\n|K .  |\n| /.\ |\n|(_._)|\n|  |  |\n|____K|",
                ]

array_hearts = ["", "", " _____\n|2_ _ |\n|( v )|\n| \ / |\n|  .  |\n|____2|",
                " _____\n|3_ _ |\n|( v )|\n| \ / |\n|  .  |\n|____3|",
                " _____\n|4_ _ |\n|( v )|\n| \ / |\n|  .  |\n|____4|",
                " _____\n|5_ _ |\n|( v )|\n| \ / |\n|  .  |\n|____5|",
                " _____\n|6_ _ |\n|( v )|\n| \ / |\n|  .  |\n|____6|",
                " _____\n|7_ _ |\n|( v )|\n| \ / |\n|  .  |\n|____7|",
                " _____\n|8_ _ |\n|( v )|\n| \ / |\n|  .  |\n|____8|",
                " _____\n|9_ _ |\n|( v )|\n| \ / |\n|  .  |\n|____9|",
                " _____\n|10 _ |\n|( v )|\n| \ / |\n|  .  |\n|___10|",
		" _____\n|A_ _ |\n|( v )|\n| \ / |\n|  .  |\n|____A|",
                " _____\n|J_ _ |\n|( v )|\n| \ / |\n|  .  |\n|____J|",
                " _____\n|Q_ _ |\n|( v )|\n| \ / |\n|  .  |\n|____Q|",
                " _____\n|K_ _ |\n|( v )|\n| \ / |\n|  .  |\n|____K|",
                ]

array_clubs = ["", "", " _____\n|2 _  |\n| ( ) |\n|(_'_)|\n|  |  |\n|____2|",
               " _____\n|3 _  |\n| ( ) |\n|(_'_)|\n|  |  |\n|____3|",
               " _____\n|4 _  |\n| ( ) |\n|(_'_)|\n|  |  |\n|____4|",
               " _____\n|5 _  |\n| ( ) |\n|(_'_)|\n|  |  |\n|____5|",
               " _____\n|6 _  |\n| ( ) |\n|(_'_)|\n|  |  |\n|____6|",
               " _____\n|7 _  |\n| ( ) |\n|(_'_)|\n|  |  |\n|____7|",
               " _____\n|8 _  |\n| ( ) |\n|(_'_)|\n|  |  |\n|____8|",
               " _____\n|9 _  |\n| ( ) |\n|(_'_)|\n|  |  |\n|____9|",
               " _____\n|10_  |\n| ( ) |\n|(_'_)|\n|  |  |\n|___10|",
	       " _____\n|A _  |\n| ( ) |\n|(_'_)|\n|  |  |\n|____A|",
               " _____\n|J _  |\n| ( ) |\n|(_'_)|\n|  |  |\n|____J|",
               " _____\n|Q _  |\n| ( ) |\n|(_'_)|\n|  |  |\n|____Q|",
               " _____\n|K _  |\n| ( ) |\n|(_'_)|\n|  |  |\n|____K|",
               ]

array_diamonds = ["", "", " _____\n|2 ^  |\n| / \ |\n| \ / |\n|  .  |\n|____2|",
                  " _____\n|3 ^  |\n| / \ |\n| \ / |\n|  .  |\n|____3|",
                  " _____\n|4 ^  |\n| / \ |\n| \ / |\n|  .  |\n|____4|",
                  " _____\n|5 ^  |\n| / \ |\n| \ / |\n|  .  |\n|____5|",
                  " _____\n|6 ^  |\n| / \ |\n| \ / |\n|  .  |\n|____6|",
                  " _____\n|7 ^  |\n| / \ |\n| \ / |\n|  .  |\n|____7|",
                  " _____\n|8 ^  |\n| / \ |\n| \ / |\n|  .  |\n|____8|",
                  " _____\n|9 ^  |\n| / \ |\n| \ / |\n|  .  |\n|____9|",
                  " _____\n|10^  |\n| / \ |\n| \ / |\n|  .  |\n|___10|",
		  " _____\n|A ^  |\n| / \ |\n| \ / |\n|  .  |\n|____A|",
                  " _____\n|J ^  |\n| / \ |\n| \ / |\n|  .  |\n|____J|",
                  " _____\n|Q ^  |\n| / \ |\n| \ / |\n|  .  |\n|____Q|",
                  " _____\n|K ^  |\n| / \ |\n| \ / |\n|  .  |\n|____K|",
                  ]

player_bread = 1000
card_values = [2,3,4,5,6,7,8,9,10,11,12,13,14]


#Introduction and tutorial
print("")

#Main game loop
while player_bread > 0:
	print ("==================================/\n Your current funds: $ %d      /\n================================/\n\n" % player_bread)
	player_hand_amount = 0
	house_hand_amount = 0
	player_aces = 0
	house_aces = 0
	x = 1
	while x == 1:
		betting_amount = 0
		betting_amount = int(input("How much would you like to wager?: "))
		x = 0
		if betting_amount > player_bread:
			print("Insufficient funds.")
			x = 1
		if betting_amount <= 0:
			print("Please enter an amount greater than 0.")
			x = 1
	
	win_loss_multiplier = int(input("Would you like to set your win/loss multiplier to x1, x2, or x3?: "))
	print("\n\n")

	betting_amount = betting_amount * win_loss_multiplier
	
	
	#Player draws two cards
	print("#################")
	print("  YOU DREW....")
	print("#################\n")
	throwaway = random.choice(card_values)
	
	random_number = random.randint(1, 4)
	
	if random_number == 1:
		print(array_spades[throwaway])
	if random_number == 2:
		print(array_hearts[throwaway])
	if random_number == 3:
		print(array_clubs[throwaway])
	if random_number == 4:
		print(array_diamonds[throwaway])
	
	if throwaway == 11:
		player_aces = player_aces + 1
	elif throwaway == 12:
		throwaway = throwaway - 2
	elif throwaway == 13:
		throwaway = throwaway - 3
	elif throwaway == 14:
		throwaway = throwaway - 4
	
	player_hand_amount = player_hand_amount + throwaway
		
	throwaway = random.choice(card_values)
	
	
	random_number = random.randint(1, 4)
	
	if random_number == 1:
		print(array_spades[throwaway])
	if random_number == 2:
		print(array_hearts[throwaway])
	if random_number == 3:
		print(array_clubs[throwaway])
	if random_number == 4:
		print(array_diamonds[throwaway])
	
	if throwaway == 11:
		player_aces = player_aces + 1
	elif throwaway == 12:
		throwaway = throwaway - 2
	elif throwaway == 13:
		throwaway = throwaway - 3
	elif throwaway == 14:
		throwaway = throwaway - 4
	
	player_hand_amount = player_hand_amount + throwaway
	
	print("\nYour hand: " + str(player_hand_amount))

	
	#House draws two cards
	print("\n")
	print("##################")
	print("  HOUSE DREW....")
	print("##################\n")
	throwaway = random.choice(card_values)
	
	random_number = random.randint(1, 4)
	
	if random_number == 1:
		print(array_spades[throwaway])
	if random_number == 2:
		print(array_hearts[throwaway])
	if random_number == 3:
		print(array_clubs[throwaway])
	if random_number == 4:
		print(array_diamonds[throwaway])
	
	if throwaway == 11:
		house_aces = house_aces + 1
	elif throwaway == 12:
		throwaway = throwaway - 2
	elif throwaway == 13:
		throwaway = throwaway - 3
	elif throwaway == 14:
		throwaway = throwaway - 4
	
	house_hand_amount = house_hand_amount + throwaway
		
	throwaway = random.choice(card_values)
	
	random_number = random.randint(1, 4)
	
	if random_number == 1:
		print(array_spades[throwaway])
	if random_number == 2:
		print(array_hearts[throwaway])
	if random_number == 3:
		print(array_clubs[throwaway])
	if random_number == 4:
		print(array_diamonds[throwaway])
	
	if throwaway == 11:
		house_aces = house_aces + 1
	elif throwaway == 12:
		throwaway = throwaway - 2
	elif throwaway == 13:
		throwaway = throwaway - 3
	elif throwaway == 14:
		throwaway = throwaway - 4
	
	house_hand_amount = house_hand_amount + throwaway
	
	print("\nHouse's hand: " + str(house_hand_amount))
	print("\n")
	
	game_in_play = True
	
	if player_hand_amount == 21:
		print("Blackjack! You win $%s\n\n" % betting_amount)
		player_bread = player_bread + betting_amount
		game_in_play = False
	elif house_hand_amount == 21 and player_hand_amount != 21:
		print("House wins. Better luck next time.\n\n")
		player_bread = player_bread - betting_amount
		game_in_play = False

	hit_or_stand = "h"
	
	#Hit or stand loop
	while hit_or_stand != "s" and game_in_play:
		hit_or_stand = input("Would you like to hit(h) or stand(s): ")
		if hit_or_stand == "h":
			throwaway = random.choice(card_values)
	
			random_number = random.randint(1, 4)
	
			if random_number == 1:
				print(array_spades[throwaway])
			if random_number == 2:
				print(array_hearts[throwaway])
			if random_number == 3:
				print(array_clubs[throwaway])
			if random_number == 4:
				print(array_diamonds[throwaway])
	
			if throwaway == 11:
				player_aces = player_aces + 1
			elif throwaway == 12:
				throwaway = throwaway - 2
			elif throwaway == 13:
				throwaway = throwaway - 3
			elif throwaway == 14:
				throwaway = throwaway - 4
	
			player_hand_amount = player_hand_amount + throwaway
		if player_hand_amount > 21 and player_aces > 0:
			player_hand_amount = player_hand_amount - 10
			player_aces = player_aces - 1
		print("\nYour hand: " + str(player_hand_amount))
		if player_hand_amount > 21 and player_aces == 0:
			print("\nYou bust. House wins. Better luck next time.\n\n")
			player_bread = player_bread - betting_amount
			game_in_play = False
		if player_hand_amount == 21:
			print("\nBlackjack! You win $%s\n\n" % betting_amount)
			player_bread = player_bread + betting_amount
			game_in_play = False
	
	#House draw loop
	while game_in_play and  house_hand_amount <= player_hand_amount:
		throwaway = random.choice(card_values)
	
		random_number = random.randint(1, 4)
	
		if random_number == 1:
			print(array_spades[throwaway])
		if random_number == 2:
			print(array_hearts[throwaway])
		if random_number == 3:
			print(array_clubs[throwaway])
		if random_number == 4:
			print(array_diamonds[throwaway])
	
		if throwaway == 11:
			house_aces = house_aces + 1
		elif throwaway == 12:
			throwaway = throwaway - 2
		elif throwaway == 13:
			throwaway = throwaway - 3
		elif throwaway == 14:
			throwaway = throwaway - 4
	
		house_hand_amount = house_hand_amount + throwaway
			
		if house_hand_amount > 21 and house_aces > 0:
			house_hand_amount = house_hand_amount - 10		
			house_aces = house_aces - 1
		print("\nHouse's hand: " + str(house_hand_amount))
		if house_hand_amount > 21 and house_aces == 0:
			print("\nHouse busts! You win $%s\n\n" % betting_amount)	
			player_bread = player_bread + betting_amount					
			game_in_play = False
		if house_hand_amount <= 21 and house_hand_amount > player_hand_amount:
			print("\nHouse wins. Better luck next time.\n\n")
			player_bread = player_bread - betting_amount
			game_in_play = False
	
	
	
	
	
