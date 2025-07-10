# Read data
all_lists=[]
with open('input_2.txt', 'r') as file:
    for line_number, line in enumerate(file, 1):      
            num_list = [int(num) for num in line.split()]
            all_lists.append(num_list)



def is_safe(input_list):
    " fucntion to check if a given list is mononotone and satisfies conditions" 
    #Compute inter element distance in the list
    dist=[abs(input_list[j] - input_list[j+1]) for j in range(len(input_list)-1)]
    #Check monotonicity of a given list
    mono= all(x < y for x, y in zip(input_list, input_list[1:])) or all(x > y for x, y in zip(input_list, input_list[1:])) 
   
    #verify problem disance assumptions
    if mono and all(1 <= x <= 3 for x in dist):   
        return True


def is_safe_relaxed(input_list):
    "Function to check relaxed monotonicity and conditions for a given list" 

    if is_safe(input_list): 
        return True
    for i in range(len(input_list)):
        # WE relax the monotonicity assumption simply by creating a checking the ensemble of the sublists for a given list. 
        temp_list = input_list[:i] + input_list[i+1:]  
        if is_safe(temp_list): 
            return True

    return False



safety_count=0 
safey_count_relaxed = 0
for report in all_lists:
    if is_safe(report): 
        safety_count+=1
    if is_safe_relaxed(report):
        safey_count_relaxed += 1

print("Safety count with lists strictly monotonic", safety_count)
print("Safety count relaxed (Monotonoicity assumption)", safey_count_relaxed)
