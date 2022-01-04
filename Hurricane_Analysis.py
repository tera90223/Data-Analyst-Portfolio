# write your update damages function here:
# Description: change string to float for USD cost for damages
# function(list)
# return new list

def updated_damages(list_damages):
    updated_damages = []
    for cost in list_damages:
        if cost[-1] == 'M':
            cost = cost[:-1] 
            cost = float(cost) * 10**6
            updated_damages.append(cost)
        elif cost[-1] == 'B':
            cost = cost[:-1] 
            cost = float(cost) * 10**9
            updated_damages.append(cost)
        else:
            updated_damages.append(cost)
    return updated_damages
        
        

# write your construct hurricane dictionary function here:
# Description: take 7 lists of information concerning different hurricanes and create a dictionary with the key being the name of the hurricane and the value being a dictionary of the hurricane's information
# function( list, list, list, list, list, list, list)
# return a dictionary

def hurricane_information(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
    hurricane_info = {}
    updated_damage_cost = updated_damages(damages)
    
    for n in range(0, len(names)):
        
        hurricane_info[names[n]] = {"Name": names[n], "Month": months[n],
                                "Year": years[n], 
                                "Max Sustained Wind": max_sustained_winds[n], 
                                "Areas Affected": areas_affected[n], 
                                "Damage": updated_damage_cost[n], "Deaths": deaths[n]
                               }
    return hurricane_info






# write your construct hurricane by year dictionary function here:
# Description: Create a new dictionary with a key, which is years. The values is a list of dictionaries containing hurricane information of hurricanes that occurred in that year.
# function(dictionary)
# return a new dictionary

def hurricane_information_by_year(hurricane_information):
   
    hurricane_by_year = {}
    
    for info in hurricane_information.values():
        year = info.get("Year")
       
        if year in hurricane_by_year:
            hurricane_by_year[year].append(info)
        else:
            
            hurricane_by_year[year] = [info]  
            
    return hurricane_by_year

#defaultdic(default_value) is a container present in the module collections.
#The difference between defaultdic and a regular dictionary is that defaultdic
#never raises a KeyError as it provides a dafault value for the key 
#that does not exist
#https://www.geeksforgeeks.org/defaultdict-in-python/

from collections import defaultdict as dd 

def hurricane_information_by_year(hurricane_information):
    hurricane_by_year = dd(list)
    
    for info in hurricane_information.values():
        year = info.get("Year")
        hurricane_by_year[year].append(info)
    return hurricane_by_year




# write your count affected areas function here:
# Description: Counts how often each affected area is listed for the hurricanes in the hurricane dictionary.
# function(hurricane dictionary)
# return dictionary key, affected areas: values, number of times the areas were affected


#dict.setdefault(key, default=None) sets dict[key] = default if key is not already in dict.
#https://www.tutorialspoint.com/python/dictionary_setdefault.htm

def count_affected_areas(hurricane_information):
    counted_areas = {}
    
    for info in hurricane_information.values():
        areas = info.get("Areas Affected")
        for area in areas:
            if area in counted_areas:
                #num = counted_areas.get(area)
                num = counted_areas.setdefault(area)
                num += 1
                counted_areas[area] = num
            else: 
                num = 1
                counted_areas[area] = num
    return counted_areas



# write your find most affected area function here:
# Description: Finds the area affected by the most hurricanes and how often it was hit
# function(affected_area_dictionary)
# return list affected area, how often it was hit

#lambda arguments:expression, lamda functions can accept zero or more arguments,
#but only one expression
#https://www.afternerd.com/blog/python-lambdas/

#https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
#https://stackoverflow.com/questions/16125229/last-key-in-python-dictionary

from collections import OrderedDict

def most_affected_area(count_affected_areas):
    od= OrderedDict(count_affected_areas)
    return list(od.items())[0]
    
#OR

#def most_affected_area(count_affected_areas):
#    sorted_affected_areas = {k:v for k, v in sorted(count_affected_areas.items(), key = lambda item:item[1])}
#    return list(sorted_affected_areas.items())[-1]
    



# write your greatest number of deaths function here:
# Description: Find the hurricane that causes the greatest number of deaths and how many #deaths it caused.
# function(hurricane dictionary)
# return list hurricane, number of deaths

def most_hurricane_deaths(hurricane_information):
    hurricane_deaths = {}
    
    for name, info in hurricane_information.items():
        deaths = info.get("Deaths")
        hurricane_deaths[name] = deaths
    
    sorted_deaths = {key:value for key, value in sorted(hurricane_deaths.items(), key=lambda items:items[1])}
    
    return list(sorted_deaths.items())[-1] 





# write your catgeorize by mortality function here:
# Description: Rate the hurricanes on a mortality scale where the key is the rating
# function(hurricane dictionary)
# return dictionary key, mortality scale: value, hurricane information in the range of the ratings

def mortality_ratings(hurricane_information):
    
    hurricane_mortality_ratings = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
    
    for info in hurricane_information.values():
        death = info.get("Deaths")
        
        if death == 0:
            hurricane_mortality_ratings[0].append(info)
        elif death > 0 and death < 100:
            hurricane_mortality_ratings[1].append(info)
        elif death > 100 and death <= 500:
            hurricane_mortality_ratings[2].append(info)
        elif death > 500 and death <= 1000:
            hurricane_mortality_ratings[3].append(info)
        elif death > 1000 and death <= 10000:
            hurricane_mortality_ratings[4].append(info)
        elif death > 10000:
            hurricane_mortality_ratings[5].append(info)
            
    return hurricane_mortality_ratings





# write your greatest damage function here:
# Description: Find the hurricane that caused the greatest damage and how costly it was. 
# function(hurricane dictionary)
# return list hurricane, hurricane damage cost

def most_damage(hurricane_information):
    damage_dict = {}
    
    for name, info in hurricane_information.items():
        damage = info.get('Damage')
        
        if damage == "Damages not recorded":
            damage = float(0)
            
        damage_dict[name] = damage
        
    sort_damage_dict = {key:value for key,value in sorted(damage_dict.items(),
                        key = lambda items:items[1])}
                        
    return (list(sort_damage_dict.items())[-1])





# write your catgeorize by damage function here:
# Description: Rate the hurricanes on a damage scale where the key is the rating
# function(hurricane dictionary)
# return dictionary key, damage scale: value, hurricane information in the range of the ratings

def damage_ratings(hurricane_information):
    hurricane_damage_ratings = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
    
    for info in hurricane_information.values():
        damage = info.get('Damage')
        
        if damage == 0 or damage == "Damages not recorded":
            hurricane_damage_ratings[0].append(info)
        elif damage > 0 and damage <= 100000000:
            hurricane_damage_ratings[1].append(info)
        elif damage > 100000000 and damage <= 1000000000:
            hurricane_damage_ratings[2].append(info)
        elif damage > 1000000000 and damage <= 10000000000:
            hurricane_damage_ratings[3].append(info)
        elif damage > 10000000000 and damage <= 50000000000:
            hurricane_damage_ratings[4].append(info)
        elif damage > 50000000000:
            hurricane_damage_ratings[5].append(info)
            
    return hurricane_damage_ratings