from adventurelib import *
Room.items = Bag()

#Imports   #this is whee any imports are gonna be like music ect


#Define Rooms    #this is where all toe room descriptions are 
spawn_area = Room("""
	you are in a over grown field surounded by lush forests on all sides. there is a small log cabbin to the east aswell as a track to the north and south. there is a shimmer to the east.
	""")

log_cabbin = Room("""
	there is a small cooking space in the south east corner of the house and a large bed covered in animal hide in the south west corner of the room. you see a door leading out to the west and a door leading to the east.
	""")


tall_trees1 = Room("""
	you are faced with tall trees streched across the path. the past leads west. 
	""")

tall_trees2 = Room("""
	you are faced with tall trees streched across the path. the past leads east and west. 
	""")

tall_trees3 = Room("""
	you are faced with tall trees streched across the path. the past leads north and south.
	""")

tall_trees4 = Room("""
	you are faced with tall trees streched across the path. the past leads north and south. 
	""")

tall_trees5 = Room("""
	you are faced with tall trees streched across the path. the past leads east and west. 
	""")

tall_trees6 = Room("""
	you are faced with tall trees streched across the path. the past leads east and west. 
	""")

elder_hut = Room("""
	you enter the hutt and are greeted by an eldely woman. she challenges you to find three herbs if you do and return to me i will reward you with a sword. 
	""")

Dungeon = Room("""
	you creep through the huge brick walls. the doors slam shut behind you. you see a cyclops. he looks at you through his large eye. you hve 2 options fight or die. 
	""")
#Define Connections     #this is where the rooms connect to eachother so you can travel between them
spawn_area.south = tall_trees4
spawn_area.west = log_cabbin
spawn_area.north = tall_trees3
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

#Define any variables    #this is wheree all the variables are kept
current_room = spawn_area

inventory = Bag()

herb_count = 0

dungeon_lock=True

#Binds    #this is where the binds for the game are stored like the function to look or move
@when ("DIRECTION")
@when ("go DIRECTION")
def travel(direction):
	global current_room
	if direction in current_room.exits():
		current_room = current_room.exit(direction)
		print(f"you go {direction}.")
		print(current_room)
		print(current_room.exits())


@when('look')
def look():
	print(current_room)
	print(f'there are exits to the {current_room.exits()}.')
	if len(current_room.items) > 0:
		print('you also see:')
		for item in current_room.item:
			print(item)

@when('get ITEM')
@when('take ITEM')
@when('pick up ITEM')
def pickup(item):
	#global dungeon_lock
	if item in current_room.items:
		t = current_room.items.take(item)
		inventory.add(t)
		print(f'you pick up the {item}')
		if item=='herb':
			herb_count+= 1
	else:
		print(f'you dont see a {item}')


@when('inventory')
@when('show inventory')
@when('what is in my pockets')
def Player_inventory():
	print('you are carrying')
	for item in inventory:
		print(item)

@when('look at ITEM')
def look_at(item):
	if item in inventory:
		t = inventory.find(item)
		print(t.description)
	else:
		print(f'you arent carrying an {item}')

@when("use ITEM")
def use(item):
	if inventory.find(item)== key and current_room == Dungeon:
		dungeon_lock == false
		print("You use the key and enter the dungeon")
		print("To the south is the escape pod. Can you use the secret code?")
	if inventory.find(item)== sword and current_room == Dungeon:
		print("the beast is slain ")
		print("you have won the game")
	else:
		print("You can't use that here")



#Main Function



#def main():
print(current_room)
start()




#if __name__ == '__main__':
	#main()