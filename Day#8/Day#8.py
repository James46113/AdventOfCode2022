trees = [[tree for tree in row if tree != "\n"] for row in open("Day#8input.txt", "r").readlines()]
visible = 0
best_score = 0

def check_visible(row: int, column:int) -> None:
    global visible, best_score
    height = trees[row][column]

    # Checking North
    visible_N = True
    trees_visible_N = row
    temp_trees_north = trees[:row]
    temp_trees_north.reverse()
    for ind, trees_row in enumerate(temp_trees_north):
        if trees_row[column] >= height:
            trees_visible_N = row - (row - ind -1)
            visible_N = False
            break

    # Checking East
    visible_E = True
    trees_visible_E = len(trees[row]) - column - 1
    for ind, tree in enumerate(trees[row][column+1:]):
        if tree >= height:
            trees_visible_E = (column+1+ind) - column
            visible_E = False
            break
    
    # Checking South
    visible_S = True
    trees_visible_S = len(trees) - row -1
    for row_ind, trees_row in enumerate(trees[row+1:]):
        if trees_row[column] >= height:
            trees_visible_S = (row+1+row_ind) - row
            visible_S = False
            break
    
    # Checking West
    visible_W = True
    trees_visible_W = column
    temp_trees_west = trees[row][:column]
    temp_trees_west.reverse()
    for ind, tree in enumerate(temp_trees_west):
        if tree >= height:
            trees_visible_W = column - (column - ind -1)
            visible_W = False
            break

    if visible_N or visible_E or visible_S or visible_W:
        visible += 1

    scenic_score = trees_visible_N * trees_visible_E * trees_visible_S * trees_visible_W
    if scenic_score > best_score:
        best_score = scenic_score


for row_ind, row in enumerate(trees):
    for column_ind in range(len(row)):
        check_visible(row=row_ind, column=column_ind)

print("ANSWER TO PART 1:", visible)

print("ANSWER TO PART 2:", best_score)