
# Loading character matrix
data_list = []
with open('input_4.txt', 'r') as file:
    for line in file:
        char_list = list(line.strip())
        data_list.append(char_list)
rows = len(data_list)
cols = len(data_list[0])
word = "MAS"


def check_mas(start_row, start_col, dr, dc, matrix):
    "This function checks if XMAS exists starting at position in given direction"

    for i in range(len(word)):
        row = start_row + i * dr
        # Handling matrix limit
        if row < 0 or row >= rows or col < 0 or col >= cols:
            return False
            # Verifying chatacters if from the word
        elif matrix[row][col] != word[i]:
            return False
    return True
    

def check_x_mas(center_row, center_col, matrix):
    "This functiion checks if there's an X-MAS pattern centered at given position"
    
    if center_row < 1 or center_row >= rows - 1 or center_col < 1 or center_col >= cols - 1:
        return False
    
    # Check if center is 'A' (middle of MAS)
    if matrix[center_row][center_col] != 'A':
        return False
    
    # Get the four diagonal positions around the center
    top_left = matrix[center_row - 1][center_col - 1]
    top_right = matrix[center_row - 1][center_col + 1]
    bottom_left = matrix[center_row + 1][center_col - 1]
    bottom_right = matrix[center_row + 1][center_col + 1]
    
    # Check diagonal 1
    diag_1 = top_left + 'A' + bottom_right
    diag_1_valid = diag_1 == "MAS" or diag_1 == "SAM"
    
    # Check diagonal 2 
    diag_2 = top_right + 'A' + bottom_left
    diag_2_valid = diag_2 == "MAS" or diag_2 == "SAM"
    
    return diag_1_valid and diag_2_valid


#We define the directions for which we check to a given matrix cell.
directions = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (-1,-1), (1,-1), (-1,1)]

#Verifying the first problem
counter_1=0
for row in range(rows):
    for col in range(cols):
        for dr, dc in directions:
            if check_mas(row, col, dr, dc,data_list):
                counter_1 += 1

#Verifying the second problem
counter_2=0
for row in range(rows):
    for col in range(cols):
        if check_x_mas(row, col,data_list):
            counter_2 += 1

print("XMAS word count",counter_1,"...... X-MAS word count",counter_2)