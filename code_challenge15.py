anime_list = []
print("Welcome To The Anime Collector")
print("To Stop The Program Type 'Terminate'")

while True:
	
	anime = input("Enter Collected Anime: ")
	
	if anime.lower() == 'terminate':
		print("You have saved your anime titles.")
		break
	
	else:
		print(f"'{anime}' is added to your collection.")
		anime_list.append(anime)
		continue
	
print("Your collection anime collection consist of:")
for x in anime_list:
	print(f"- {x}")