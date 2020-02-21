class Node:
    def __init__(self, value, parent):
        self.parent = parent
        self.value = value


# Location should be 2-element list representing cartesian coordinates of the location
# Grid 2D list of 1's and 0's (aka imported)
# Return list of location points list of [row,col]'s
def getneighbors(loc, grid):
    maxheight = len(grid[0])  # Length of one column
    maxlength = len(grid)  # Length of one row
    neighbor_list = []

    if loc[1] > 0 and grid[loc[0]][loc[1] - 1] != 1:  # test downward movement
        neighbor_list.append([loc[0], loc[1] - 1])
    if loc[1] < (maxheight - 1) and grid[loc[0]][loc[1] + 1] != 1:  # test upward movement
        neighbor_list.append([loc[0], loc[1] + 1])
    if loc[0] > 0 and grid[loc[0] - 1][loc[1]] != 1:  # test leftward movement
        neighbor_list.append([loc[0] - 1, loc[1]])
    if loc[0] < (maxlength - 1) and grid[loc[0] + 1][loc[1]] != 1:  # test rightward movement
        neighbor_list.append([loc[0] + 1, loc[1]])

    return neighbor_list

# Purpose is to get all valid neighbors of the node object passed in and
# add those neighbors to the open list
# Closed and Open list should be a list of Nodes not a list of cordinates
def expandnode(node, grid, closedL, openL):
    # get the list of current children
    listOfChildren = getNeighbors(node.value, grid)
    # iterate through each child
    for x in range(len(listOfChildren)):
        testVar = True
        # if it's in either list, keep looking
        for y in openL:
          if listOfChildren[x] == y.value: # compare coordinate values
            testVar = False
        for y in closedL:
          if listOfChildren[x] == y.value:
            testVar = False
        if(not testVar):
          continue
        # if it's in neither, append it to the open list to be explored
        newNode = Node(listOfChildren[x], node)
        openL.append(newNode)
    return