from adventurelib import *

@when('brush teeth')
@when('brush')
@when('clean teeth')
def brush_teeth():
	print('you brush your teeth')

@when('comb hair')
@when('comb')
def comb_hair():
	print("""
	you brush your long flowing locks with the gold hairbrush that you have selected from in the red basket
	""")

space = Room("""
	you are drifting in space. it feelsvery cold. a slate-blue spaceship sits compleatly siently to your left, its airlock open and ready.
	""")

spaceship = Room("""
	the bridge if the spaceship is shiney and white, with thousands of small, red, blinking lights.
	""")

cargo = Room("""
	the room is filled with buggies and research equipment. 
	""")

quarters = Room("""
	in the quarters there are bunk beds attatched to the walls 
	""")

hallway = Room("""
	ther hall way is a baran area between areas
	""")

mess_hall = Room("""
	in this room there are long tables streched across the room 
	""")

docking = Room("""
	in this room there are several vessels from which others came from
	""")

bridge = Room("""
	in the bridge there is the ships crew and capitain commanding the ship
	""")

escape_pods = Room("""
	in this room there are escape pods ready to be activated 
	""")

current_room = space

@when("enter airlock")
@when("enter spaceship")
@when("enter ship")
def enter_spaceship():
	global current_room

	if current_room is not space:
		say("there is no airlock here")
		return
	else:
		current_room = spaceship
		print("""you heave yourself into the spaceship and slam you hand on the button to close the door.
		""")
	print(current_room)

#variable
current_room = space
spaceship.east = hallway
spaceship.south = quarters
hallway.east  = bridge
hallway.north = cargo
cargo.east = docking
halway.west = airlock
hallway.south = messhall
bridge.south = escape.pods

@when ("go DIRECTION")
def travel(direction):
	global current_room
	if direction in current_room.exits():
		current_room = current_room.exit(direction)
		print(f"you go {direction}.")
		print(current_room)
		print(current_room.exits())

#defining the items
Item.description = "" #this adds a blank discriptio to each item

knife = Item("knife")
knife.discription = "the knife is a jagered blade 6 inches long and been recently sharpened"

red_keycard = Item("a red kecard","keycard")
red_keycard = "a red keycard to open a door or a locker "

headphones = Item("headphones")
headphones.description = "red wireless headphones" 

yellow_keycard = Item("a yellow keycard","yellow keycard")
yellow_keycard = "a yellow keycard to open adoor or locker"

current



def main():
	start()




if __name__ == '__main__':
	main()