from adventurelib import *


#Imports
#Define Rooms
spawn_area("""
	you are in a over grown field surounded by lush forests on all sides. there is a small log cabbin to the east aswell as a track to the north and south. there is a shimmer to the east.
	""")

log_cabbin("""
	there is a small cooking space in the south east corner of the house and a large bed covered in animal hide in the south west corner of the room. you see a door leading out to the west and a door leading to the east.
	""")


tall_trees1("""
	you are faced with tall trees streched across the path. the past leads west. 
	""")

tall_trees2("""
	you are faced with tall trees streched across the path. the past leads east and west. 
	""")

tall_trees3("""
	you are faced with tall trees streched across the path. the past leads north and south.
	""")

tall_trees4("""
	you are faced with tall trees streched across the path. the past leads north and south. 
	""")

tall_trees5("""
	you are faced with tall trees streched across the path. the past leads east and west. 
	""")

tall_trees6("""
	you are faced with tall trees streched across the path. the past leads east and west. 
	""")

elder_hut("""
	you enter the hutt and are greeted by an eldely woman. she challenges you to find three herbs if you do and return to me i will reward you with a sword. 
	""")

Dungeon("""
	you creep through the huge brick walls. the doors slam shut behind you. you see a cyclops. he looks at you through his large eye. you hve 2 options fight or die. 
	""")
#Define Connections


spawn_area.south = tall_trees4
spawn_area.west = log_cabbin
spawn_area.north = tall_trees3
spawn_area.east = ladder
tall_trees2.east = dungeon
tall_trees2.west = tall_trees1
tall_trees3.north = tall_trees2
tall_trees4.south = tall_trees5
tall_trees5.west = tall_trees6

#Define Items
key = Item("key")
key.discription = "the key is rusty and jagered "

herb = Item('herb')
herb.description = "these herbs are the ones the elder wanted"

sword = Item('sword')
sword.description ="thee who weleds this blade shall free this forrest of any monster in a single slach"


#Define Bags


#Add Items to Bags


#Define any variables
current_room = spawn_area

inventory = bag()

herb_count = 0
#Binds 

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

@when('get item')
@when('take item')
@when('pick up item')
def pickup(item):
	if item in current_room.items:
		if item==herb:
			herb_count = herb_count+1
		t = current_room.item.take(item)
		inventory.add(t)
		print(f'you pick up the {item}')
    else:
    	print(f'you dont see a {item}')


@when('inventory')
@when('show inventory')
@when('what is in my pockets')
def Player_inventory():
	print('you are carrying')
	for item in inventory:
		print(item)

@when('look at item')
def look_at(item):
	if item in inventory:
		t = inventory.find(item)
		print(t.description)
	else:
		print(f'you arent carrying an {item}')




#Main Function











def main():
	start()




if __name__ == '__main__':
	main()