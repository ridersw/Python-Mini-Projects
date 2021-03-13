def printBoard(board):
	#print("Call printBoard")
	for swi in range(len(board)):
		if swi % 3 == 0 and swi != 0:
			print("--------------------------")
		for swj in range(len(board[0])):
			if swj % 3 == 0 and swj != 0:
				print(" | ", end = " ")
		
			if swj < len(board[0])-1:
				print(board[swi][swj], end=" ")
			else:
				print(board[swi][swj])

	
def findEmpty(board):
	#print("Call findEmpty")
	for swi in range(len(board)):
		for swj in range(len(board[0])):
			if board[swi][swj] == 0:
				return (swi, swj)
				
	return None
				
def isValid(board, num, pos):
	#print("Call isValid")
	#check row
	for swi in range(len(board[0])):
		if board[pos[0]][swi] == num and pos[1] != swi:
			return False	
	
	#check column
	for swi in range(len(board)):
		if board[swi][pos[1]] == num and pos[0] != swi:
			return False
	
	#check block
	boxX = pos[1] // 3
	boxY = pos[0] // 3
	
	for swi in range(boxY * 3, boxY*3 + 3):
		for swj in range(boxX* 3, boxX*3 + 3):
			if board[swi][swj] == num and (swi,swj) != pos:
				return False
				
	return True

def solveSudoku(board):
	#print("Call solveSudoku")
	find = findEmpty(board)

	if not find:
		return True
	else:
		row, col = find
		
		
	for swi in range(1,10):
		if isValid(board, swi, (row,col)):
			board[row][col] = swi
			#print("Update board")
			
			if solveSudoku(board):
				return True
				
			board[row][col] = 0
			
	return False

if __name__ == "__main__":
	board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]
	
	printBoard(board)
	solveSudoku(board)
	print("-----------------------------------------------------------")
	printBoard(board)