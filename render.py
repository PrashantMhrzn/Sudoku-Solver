from boards import random_valid_board 

board = random_valid_board()

def solve(board):
    #Check if we reached the last spot and didn't find any empty space

    find = find_empty(board)
    # If we dont find any empty space
    if not find:
        return True
    else:
        # Setting the row and col to the current position
        row, col = find

    # Use recursive function to keep trying values until solution
    for i in range(1,10):
        # Check if the value is valid
        if valid(board, i, (row, col)):
            # Assign the value in to the postion
            board[row][col] = i

            # Keep checking the next empty spaces by recursion
            if solve(board):
                return True
            
            board[row][col] = 0
    
    return False
 
# We are going to check if the number that we insert is already in either the
# row, column or the square
def valid(board, number, position):

    # Check row
    # Loop through every column in the row
    for i in range(len(board[0])):
        # Check if the number that we have inserted is already in the row or if
        # the number is the one that we just inserted
        if board[position[0]][i] == number and position[1] != i:
            return False 

    # Check column
    # Loop through every row in the column
    for i in range(len(board)):
        # Check if the number that we have insterted is already in the column or
        # if the number is the one that we just inserted
        if board[i][position[1]] == number and position[0] != i:
            return False

    # Check box
    # Determine the posotion of the box using integer division
    box_x = position[1] // 3 
    box_y = position[0] // 3 

    # Loop through the items in the box 
    box_x = position[1] // 3 
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if board[i][j] == number and (i,j) != position:
                return False

    # If all the checks are valid
    return True
        

# Print the board in a format where it is seperated into 3 by 3
def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("-----------------------")
    
        for j in range(len(board[0])):
            if j % 3 == 0 and j!= 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            
            else:
                print(str(board[i][j]) + " ", end="")


# Find the empty value so that we can run our backtraking algo
def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j) # row, col

    # Means there are no black spaces left
    return None

print("Unsolved board: ")
print_board(board)

print(" ______________________ ")

solve(board)

print("Solved board: ")
print_board(board)