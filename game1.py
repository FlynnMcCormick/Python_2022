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

spaceship = room("""
	the bridge if the spaceship is shiney and white, with thousands of small, red, blinking lights.
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
hallway.east  == bridge
hallway.north = cargo
cargo.east = docking
halway.west = airlock
hallway.south = messhall
bridge.south = escape pods

@when ("go DIRECTION")
def travel(direction):
	global current_room
	if direction in current_room.exits():
	current_room = current_room.exit(direction)
	print(f"you go {direction}.")
	print(current_room)








def main():
	start()




if __name__ == '__main__':
	main()