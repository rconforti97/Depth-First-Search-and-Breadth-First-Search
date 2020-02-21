# Returns a 2D list of 1s and 0s
def readGrid(filename):
    # print('In readGrid')
    grid = []
    with open(filename) as f:
        for l in f.readlines():
            grid.append([int(x) for x in l.split()])

    f.close()
    # print 'Exiting readGrid'
    return grid


# Writes a 2D list of 1s and 0s with spaces in between each character
def outputGrid(grid, start, goal, path):
    # print('In outputGrid')
    filenameStr = 'path.txt'

    # Open filename
    f = open(filenameStr, 'w')

    # Mark the start and goal points
    grid[start[0]][start[1]] = 'S'
    grid[goal[0]][goal[1]] = 'G'

    # Mark intermediate points with *
    for i, p in enumerate(path):
        if i > 0 and i < len(path) - 1:
            grid[p[0]][p[1]] = '*'

    # Write the grid to a file
    for r, row in enumerate(grid):
        for c, col in enumerate(row):

            # Don't add a ' ' at the end of a line
            if c < len(row) - 1:
                f.write(str(col) + ' ')
            else:
                f.write(str(col))

        # Don't add a '\n' after the last line
        if r < len(grid) - 1:
            f.write("\n")

    # Close file
    f.close()


# print('Exiting outputGrid')

class Node:
    def __init__(self, value, parent):
        self.parent = parent
        self.value = value


def uninformedSearch(grid, start, goal, option):
    openList = []
    closedList = []
    path = []
    current = Node(start, None)
    openList.append(current)
    #print("Starting the while loop")
    while len(openList) != 0:
        # BFS popping from the front of the list.
        if option == 1:
            #print(current.value)
            current = openList.pop(0)
        # DFS b/c popping with no parameter pops from the back of the list.
        if option == 0:
            #print(current.value)
            current = openList.pop()
        if current.value == goal:
            return setpath(current, path)
        expandnode(current, grid, closedList, openList)
        #print("Adding to closed list")
        closedList.append(current)


# don't call this explicitly. The expandnode calls it within its own method.
def getneighbors(loc, grid):
    maxheight = len(grid[0])  # Length of one column
    maxlength = len(grid)  # Length of one row
    neighbor_list = []

    if loc[1] > 0 and grid[loc[0]][loc[1] - 1] != 1:  # test downward movement
        neighbor_list.append([loc[0], loc[1] - 1])
    if loc[1] < (maxheight - 1) and grid[loc[0]][loc[1] + 1] != 1:  # test upward movement
        neighbor_list.append([loc[0], loc[1] + 1])
    if loc[0] < 0 and grid[loc[0] - 1][loc[1]] != 1:  # test leftward movement
        neighbor_list.append([loc[0] - 1, loc[1]])
    if loc[0] < (maxlength - 1) and grid[loc[0] + 1][loc[1]] != 1:  # test rightward movement
        neighbor_list.append([loc[0] + 1, loc[1]])

    return neighbor_list


# Purpose is to get all valid neighbors of the node object passed in and
# add those neighbors to the open list
# Closed and Open list should be a list of Nodes not a list of coordinates
def expandnode(node, grid, closedL, openL):
    # get the list of current children
    listOfChildren = getneighbors(node.value, grid)
    # iterate through each child
    for x in range(len(listOfChildren)):
        testVar = True
        # if it's in either list, keep looking
        for y in openL:
            if listOfChildren[x] == y.value:  # compare coordinate values
                testVar = False
        for y in closedL:
            if listOfChildren[x] == y.value:
                testVar = False
            if not testVar:
                continue
        # if it's in neither, append it to the open list to be explored
        newNode = Node(listOfChildren[x], node)
        openL.append(newNode)
    return


def setpath(current, path):
    # while the parent of the node is not none. B/c the current node is set to None in the uninformed search so when
    # it hits none it should break the loop.
    while current.parent is not None:
        path.append(current.value)  # add the current value of the node to path. Added value b/c was getting addresses
        current = current.parent  # set the current node to its parent node. Move to the next node and check.
    path.append(current.value)  # adds the start coordinates to the path.
    return path  # without this I get a return value of None from uninformed search.


def main():
    print("Testing BFS:")
    gridFromFile = readGrid("gridfile.txt")
    path = uninformedSearch(gridFromFile, [1, 2], [4, 3], 1)
    print(path)
    outputGrid(gridFromFile, [1, 2], [4, 3], path)

    print("Testing DFS")
    gridFromFile = readGrid("gridfile.txt")
    path = uninformedSearch(gridFromFile, [1, 2], [4, 3], 0)
    print(path)
    outputGrid(gridFromFile, [1, 2], [4, 3], path)


# runs the main
main()