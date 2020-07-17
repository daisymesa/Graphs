from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

'''
Instructions from README:
You may find the commands `player.current_room.id`, `player.current_room.get_exits()` and `player.travel(direction)` useful.

To solve this path, you'll want to construct your own traversal graph. You start in room `0`, which contains exits `['n', 's', 'w', 'e']`. Your starting graph should look something like this:

```
{
  0: {'n': '?', 's': '?', 'w': '?', 'e': '?'}
}
```

Using a dictionary, key is direction, value is the room id.

Try moving south and you will find yourself in room `5` which contains exits `['n', 's', 'e']`. You can now fill in some entries in your graph:

```
{
  0: {'n': '?', 's': 5, 'w': '?', 'e': '?'},
  5: {'n': 0, 's': '?', 'e': '?'}
}
```

You know you are done when you have exactly 500 entries (0-499) in your graph and no `'?'` in the adjacency dictionaries. To do this, you will need to write a traversal algorithm that logs the path into `traversal_path` as it walks.

## Hints

There are a few smaller graphs in the file which you can test your traversal method on before committing to the large graph. You may find these easier to debug.

Start by writing an algorithm that picks a random unexplored direction from the player's current room, travels and logs that direction, then loops. 

This should cause your player to walk a depth-first traversal. When you reach a dead-end (i.e. a room with no unexplored paths), walk back to the nearest room that does contain an unexplored path.

You can find the path to the shortest unexplored room by using a breadth-first search for a room with a `'?'` for an exit. If you use the `bfs` code from the homework, you will need to make a few modifications.

1. Instead of searching for a target vertex, you are searching for an exit with a `'?'` as the value. If an exit has been explored, you can put it in your BFS queue like normal.

2. BFS will return the path as a list of room IDs. You will need to convert this to a list of n/s/e/w directions before you can add it to your traversal path.

If all paths have been explored, you're done!
'''

# Nodes: Rooms
# Edges: Exits

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)


# class Stack():
#     def __init__(self):
#         self.stack = []

#     def push(self, value):
#         self.stack.append(value)

#     def pop(self):
#         if self.size() > 0:
#             return self.stack.pop()
#         else:
#             return None

#     def size(self):
#         return len(self.stack)


def graph_traversal(current_room, visited=None, directions=None):

    # create set to store visited
    if visited is None:
        visited = set()

    # create list to store directions
    if directions is None:
        directions = []

    # if all rooms have been visited, return
    if len(visited) == len(room_graph):
        return directions

    # store opposite directions
    opposite_directions = {
        "n": "s",
        "s": "n",
        "w": "e",
        "e": "w"
    }

    # get all exits for current room, travel to selected room
    for direction in player.current_room.get_exits():
        player.travel(direction)

        # if room in visited, go back in opposite direction
        if player.current_room in visited:
            player.travel(opposite_directions[direction])
        else:
            # add room to visited
            visited.add(player.current_room)
            # append direction to list of directions
            directions.append(direction)

            # repeat recursively with current room
            graph_traversal(player.current_room, visited, directions)

            # return to previous room
            player.travel(opposite_directions[direction])
            # add return to directions traversal
            directions.append(opposite_directions[direction])

    # return directions for traversing the graph
    return directions


# Fill this out with directions to walk
# traversal_path = ['n', 'n']
# traversal_path = ['n', 'n', 's', 's', 's', 's',
#                   'n', 'n', 'w', 'w', 'e', 'e', 'e', 'e']
# traversal_path = []
traversal_path = graph_traversal(player.current_room)
print(traversal_path)


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
