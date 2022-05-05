from adventurelib import *
Room.items = Bag()
#Imports   #this is whee any imports are gonna be like music ect
import random
#screenapp.oi 

#Define Rooms    #this is where all the room descriptions are 
spawn_area = Room("""
	You're on an overgrown area surrounded on all sides by lush woodlands. A key can be found on the seat next to the door. To the west, there is a tiny log cabbin, and to the east, there is a hut. There are exits available to the
	""")

log_cabbin = Room("""
	In the south east corner of the house, there is a little cooking area, and in the south west corner, there is a huge bed covered in animal skin. There is a way out to the
	""")


tall_trees1 = Room("""
	you are faced with tall trees streched across the path. there is a small patch of herbs here. there are exits to
	""")

tall_trees2 = Room("""
	you are faced with tall trees streched across the path.there is a small patch of herbs here.  there are exits to
	""")

tall_trees3 = Room("""
	you are faced with tall trees streched across the path. there are exits to
	""")

tall_trees4 = Room("""
	you are faced with tall trees streched across the path.  there are exits to
	""")

tall_trees5 = Room("""
	you are faced with tall trees streched across the path.  there are exits to 
	""")

tall_trees6 = Room("""
	you are faced with tall trees streched across the path. there is a small patch of herbs here.  there are exits to
	""")

elder_hut = Room("""
	An elderly woman greets you as you enter the hutt. She challenges you to gather three herbs and bring them back to me, and if you do, I'll give you a sword. There are exits to the
	""")

Dungeon = Room("""
You make your way through the massive brick walls. Behind you, the doors crash shut. You come across a cyclops. Through his huge eye, he looks at you. You have two choices: fight or perish.
	""")
#Define Connections     #this is where the rooms connect to eachother so you can travel between them
spawn_area.south = tall_trees4
spawn_area.west = log_cabbin
spawn_area.north = tall_trees3
spawn_area.east = elder_hut
tall_trees2.east = Dungeon
tall_trees2.west = tall_trees1
tall_trees3.north = tall_trees2
tall_trees4.south = tall_trees5
tall_trees5.west = tall_trees6


#Define Items    #this is where i put all the descriptions for the items 
Item.description = ""
key = Item("key")
key.discription = "the key is rusty and jagered "

herb = Item('herb')
herb.description = "these herbs are the ones the elder wanted"

sword = Item('sword')
sword.description ="thee who weleds this blade shall free this forrest of any monster in a single slach"


#Add Items to Bags     #this is where i put the items into the "bags"
log_cabbin.items.add(key)

tall_trees1.items.add(herb)

tall_trees2.items.add(herb)

tall_trees6.items.add(herb)

elder_hut.items.add(sword)

#Define any variables    #this is wheree all the variables are kept
current_room = spawn_area

inventory = Bag()


herb_count = 0

dungeon_lock = True 


#Binds    #this is where the binds for the game are stored like the function to look or move

#this function allows you to move around the map
@when ("go DIRECTION")
def travel(direction):
	global current_room
	global dungeon_lock
	if current_room == Dungeon and inventory.find('key') == None:
		print("you have died")
		quit()

	if direction in current_room.exits():
		current_room = current_room.exit(direction)
		print(f"you go {direction}.")
		print(current_room)
		print(current_room.exits())


#this function allows you to look around the room you are in 
@when('look')
def look():
	print(current_room)
	print(f'there are exits to the {current_room.exits()}.')
	if len(current_room.items) > 0:
		print('you also see:')
		for item in current_room.item:
			print(item)

#this allows you to pick up items
@when('get ITEM')
@when('take ITEM')
@when('pick up ITEM')
def pickup(item):
	global herb_count
	if item in current_room.items:
		t = current_room.items.take(item)
		inventory.add(t)
		print(f'you pick up the {item}')

	else:
		print(f'you dont see a {item}')

	if  inventory.find('sword'):
		herb_count = 0 

	if item =='herb':
		herb_count += 1
		print(f'you have {herb_count} herb')


#this allows you to see whats in you inventory
@when('inventory')
@when('show inventory')
@when('what is in my pockets')
def Player_inventory():
	global herb_count
	print('you are carrying')
	for item in inventory:
		print(item)
	if inventory.find(item)== 'herb':
		print(f'you have {herb_count} herbs')

#this function allows you to look at the item 
@when('look at ITEM')
def look_at(item):
	if item in inventory:
		t = inventory.find(item)
		print(t.description)
	else:
		print(f'you arent carrying an {item}')


#this is the bind that makes the player use items
@when("use ITEM")
def use(item):
#	if inventory.find(item)== key and current_room == Dungeon:
	#	dungeon_lock == false
	#	print("You use the key and enter the dungeon")
	#	print("To the south is the escape pod. Can you use the secret code?")
	if inventory.find(item)== sword and current_room == Dungeon:
		sword_rand_num = (random.randint(1, 6))
		if sword_rand_num <= 4:
		   print('the beast has defeat you')
		   quit()
		if sword_rand_num >= 3:
		   print('you slay the beast')
	else:
		print("You can't use that here")


#Main Function



def main():
	print(current_room)
	start()




if __name__ == '__main__':
	main()