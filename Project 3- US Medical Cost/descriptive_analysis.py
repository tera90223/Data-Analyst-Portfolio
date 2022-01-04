# Create Descriptive Statistcal Functions
## - Create functions to use to analyze Medical Insurance Costs Data

#Function returns a list of unique elements in each column
def unique_elements(a_list):
    list_of_unique_categories = []
    for i in a_list:
        if i not in list_of_unique_categories:
            list_of_unique_categories.append(i)
    return list_of_unique_categories
    
#Function returns a dictionary of unique elements and their counts for each column
def count_category(a_list):
    list_of_unique_categories = unique_elements(a_list)
    unique_count= {}
    for i in list_of_unique_categories:
        unique_count[i]=a_list.count(i)
    return  unique_count

#Function that returns the sum 
def my_sum(a_list):
    total = 0
    for i in a_list:
        total += i
    return total

#Function that returns the maximum element of a list
def maximum(a_list):
    high = 0
    for i in a_list:
        if i > high:
            high = i
    return high

#Function that returns the minimum element of a list
def minimum(a_list):
    low = a_list[0]
    for i in a_list:
        if i < low:
            low = i
    return low

#Mean is apart of the Central tendency which tells you about the center of the data.
#The mean is the average of a dataset which means that 50% of the data is on either side of the mean.
def mean(a_list):
    #find the sum of the list
    total = sum(a_list)
    
    #find the length of the list
    length = len(a_list)
    
    #return the sum/number of elements in list
    return total/length    


#Median is apart of the Central tendency which tells you about the centers of
#the data. The median is the middle element of a sorted dataset.
def median(a_list): 
    #sort the list
    a_list.sort()
    
    #Find the length of the list
    list_length = len(a_list)
    
    #if the length/2 has a remainder of 1
    # divide the length by 2 and return the value in the middle. 
    # Use example [1,2,3] to explain
    if list_length%2 == 1:
        middle = list_length // 2
        print (middle)
        return a_list[middle]
    
    #if the length/2 has a remainder of 0
    # divide the length by 2. Add list[length/2] + list[length/2-1] and get average.
    # Use example [1,2,3,4] to explain
    elif list_length%2 == 0:
        average = (a_list[int(list_length/2)] + a_list[int(list_length/2-1)]) / 2
        return average
    
#Mode is apart of the Central Tendency which tells you about the centers of the data.
#The mode returns the element that appears most often in a dataset
def mode(a_list):
    counts_dict = count_category(a_list)
    mode = [k for k,v in counts_dict.items() if v == maximum(list(counts_dict.values()))]
    mode = ", ".join(str(mode))
    return mode

#range is the difference between the max and min values
def my_range(a_list):
    high = maximum(a_list)
    low = minumum(a_list)
    return high-low

#sample variance quatifies the spread of the data. It shows numerically how far 
#the data points are from the mean.
# 𝑠² = Σᵢ(𝑥ᵢ − mean)² / (𝑛 − 1)
def sample_variance(a_list):
    avg = mean(a_list)
    n = len(a_list)
    s_squared = sum((x_i - avg)**2 for x_i in a_list) / (n-1)
    return s_squared


#sample standard deviation is another measure of data spread. It is the positive
#square root of the sample variance.
def sample_standard_deviation(a_list):
    standard_deviation = sample_variance(a_list) ** 0.5
    return standard_deviation


#######################################################################################################################################

#Add commas to numbers for a better display
def format_number(num):
    num = round(num, 2)
    num = "{:,}".format(num)
    return num 

#######################################################################################################################################

#Smoker column currently says yes/no which does not give enough information
#Change Yes to Smoker and No to Non-smoker
def smoker_status(a_list):
    smoker_status = []
    for element in a_list:
        if element == 'yes':
            smoker_status.append('Smoker')
        elif element == 'no':
            smoker_status.append('Non-Smoker')
    return smoker_status

#######################################################################################################################################           
#Create list of charges indices
def sublist_indices(alist, list_range=None,category=None):
    indices = []
    if list_range is not None:
        for i in range(len(alist)):
            if alist[i] in list_range:
                indices.append(i)
    elif category is not None:
        for i in range(len(alist)):
            if alist[i] == category:
                indices.append(i)
    return indices

#Create list of charges
def sublist_charges(charges_list, indices):
    sublist = []
    for i in indices:
        sublist.append(charges_list[i])
    return sublist
