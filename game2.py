from adventurelib import *


#Imports
#Define Rooms
spawn_area("""
	you are in a over grown field surounded by lush forests on all sides. there is a small log cabbin to the east aswell as a track to the north and south. there is a shimmer to the east.
	""")

log_cabbin("""
	there is a small cooking space in the south east corner of the house and a large bed covered in animal hide in the south west corner of the room. you see a door leading out to the west and a door leading to the east.
	""")

behind_cabbin("""
	there is a axe stabbed inside of a log and a pile of wood sitting aroud the outside of the house 
	""")

tall_trees1("""
	you are faced with tall trees streched across the path. the past leads north and east. 
	""")

tall_trees2("""
	you are faced with tall trees streched across the path. the past leads north and west. 
	""")

tall_trees3("""
	you are faced with tall trees streched across the path. the past leads east and west. 
	""")

tall_trees4("""
	you are faced with tall trees streched across the path. the past leads east and west. 
	""")

tall_trees5("""
	you are faced with tall trees streched across the path. the past leads east and west. 
	""")

village("""
	you have found the village. there is a villager here. there are exits to the west.
	""")

ladder("""
	there is a tall ladder that leads to a high part of the tree. 
	""")

dungeon_enterance("""
	you hear a large roar comming from the dungeon. Enter if you dare. exits are to the west and east.
	""")

Dungeon("""

	""")
#Define Connections

current_room = spawn_area
spawn_area.south = tall_trees4
spawn_area.west = log_cabbin
spawn_area.north = tall_trees3
spawn_area.east = ladder
log_cabbin.west = behind_cabbin
tall_trees3.west = dungeon_enterance
tall_trees3.east = tall_trees1
dungeon_enterance.west = Dungeon
tall_trees4.east = tall_trees2
tall_trees4.west = tall_trees5
tall_trees5.west = village
#Define Items
#Define Bags
#Add Items to Bags
#Define any variables
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
		t = current_room.item.take(item)
		inventory.add(t)
		print(f'you pick up the {item}')
    else:
    	print(f'you dont see a {item}')



#Main Function











def main():
	start()




if __name__ == '__main__':
	main()