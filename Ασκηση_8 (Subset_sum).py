import random

def triplet_sum(array,req_sum):
    triplets = []

    if len(array) < 3:
        return None
  
    for mid in range(1, len(array)):
        low = 0
        high = len(array) - 1

        while low < mid and high > mid:


            if array[low] + array[mid] + array[high] == req_sum:
                triplets.append([array[low], array[mid], array[high]])
                break

  
            elif array[low] + array[mid] + array[high] > req_sum:
                high = high - 1
                continue



            else:
                low = low + 1
                continue

    if len(triplets) > 0:
        return triplets
    else:
        return None

if __name__ == "__main__":

    my_list=[]

for i in range (30):

    my_list.append(random.randrange(-30,31,1))
 
print (my_list)


triplets = triplet_sum(my_list,0)

if triplets is None:
        print("Δεν βρεθηκαν 3αδες με αθροισμα 0:", req_sum)
else:
        print("3αδες με αθροισμα 0:", triplets)


  
    
    
   
   
        
    


