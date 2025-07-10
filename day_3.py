
# Load data
with open('input_3.txt', 'r') as file:
    data_list = file.read().split()


def sum_mul_product(data):
    ' This funcction locates all the mul(X,Y) in the data  and extracts the X,Y'

    result = 0
    for item in data: 
        i = 0
        i_end = len(item)

        while i < i_end:
            if  item[i:i+4] == 'mul(':
                i = i + 4
                flag1 = False
                flag2 = False

                # Find closing parenthesis
                for j in range(i, i_end):
                    if item[j] == ')':
                        flag1 = True
                        parenthesis_idx = j
                        break
            
                if flag1:
                    # Find comma
                    for k in range(i, parenthesis_idx):
                        if item[k] == ',':
                            comma_idx = k
                            flag2 = True
                            break
                
                    if flag1 and flag2:
                        #Extract the characters between the first and the second parenthesis
                        x = item[i:comma_idx]
                        y = item[comma_idx+1:parenthesis_idx]
                        # Only process if enabled and both are valid digits
                        if  x.isdigit() and y.isdigit():
                            result += int(x) * int(y)
                i += 1
            else : 
                i += 1

    return result



def sum_mul_product_constrained(data):
    ' This funcction locates all the mul(X,Y) in the data preceded by do() and extracts the X,Y'
    
    result = 0
     # Flag to capture Do()/Don't()
    enabled = True
    for item in data:
        i = 0
        i_end = len(item)

        while i < i_end:
        # Check for do() instruction
            if item[i:i+4] == 'do()':
                enabled = True
                i += 4
                continue
        
            # Check for don't() instruction
            if item[i:i+7] == "don't()":
                enabled = False
                i += 7
                continue
        
             # Check for mul( instruction
            if item[i:i+4] == 'mul(':
                i = i + 4
                flag1 = False
                flag2 = False
            
            # Find closing parenthesis
                for j in range(i, i_end):
                    if item[j] == ')':
                        flag1 = True
                        parenthesis_idx = j
                        break
            
                if flag1:
                # Find comma
                    for k in range(i, parenthesis_idx):
                        if item[k] == ',':
                            comma_idx = k
                            flag2 = True
                            break
                
                    if flag1 and flag2:
                        x = item[i:comma_idx]
                        y = item[comma_idx+1:parenthesis_idx]
                    # Only process if enabled and both are valid digits
                        if enabled and x.isdigit() and y.isdigit():
                            result += int(x) * int(y)
                i += 1
            else:
                i += 1
    return result



print("Sum of multiplications:", sum_mul_product(data_list))
print("Sum of multiplications when taking into account do()/don't()", sum_mul_product_constrained(data_list))



