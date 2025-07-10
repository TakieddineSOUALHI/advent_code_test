list_1 = []
list_2 = []
with open('input_1.txt', 'r') as file:
    for line in file:
        if not line.strip():
            continue    
        parts = line.split()     
        if len(parts) < 2:
            continue  
        list_1.append(int(parts[0]))
        list_2.append(int(parts[1]))




def list_dist_compute(list_1,list_2):
    "This function computes the distance between two lists"

    list_1=sorted(list_1)
    list_2=sorted(list_2)
    output=[]
    for j in range(len(list_1)): 
        # Compute the distance between two lists
        output.append( abs(list_2[j]-list_1[j]))
    return sum(output)


def similarty_compute(list_1,list_2):
    "This function computes the similarity coefficients between two lists"

    output=[]
    for j in range(len(list_1)): 
        counter=0
        for i in range(len(list_1)):
            # Check similarity between two lists 
            if list_1[j]==list_2[i]: 
                counter+=1
        
        output.append(counter*list_1[j])
    return sum(output)



result_1= list_dist_compute(list_1,list_2)
result_2=similarty_compute(list_1,list_2)
print("The distance between two given lists", result_1)
print("The Simularity coefficient between two given lists", result_2)