# Hurricane Analysis

## Setting: 
As a concerned environmentalist, Write several functions that organize and analyze data concerning category 5 hurricanes in the Atlantic region.

## Objective: 
Project emphasized **writing functions using a number of parameters, conditionals, lists, dictionaries, string manipulation, and return statements.**

## Dataset:
The dataset utilized is information concerning 34 category 5 Atlantic hurricanes stored in 7 different lists. The lists is located in `Hurricane_Analysis_Test_Functions.ipynb`.

**List Descriptions**  
**names:** Names of the Hurricanes  
**months:** Months in which the Hurricanes occurred  
**years:** Years in which the Hurricanes occurred  
**max_sustained_winds:** Maximum sustained winds (mph) of Hurricanes.   
**areas_affected:** List of Areas affected by each Hurricane.  
**damages:** Total Cost (USD($)) of damages per Hurricane  
**deaths:** Total Number of Deaths per Hurricane.  

## Jupyter Libraries:
- Hurricane_Analysis.py  
  
  Hurricane_Analysis.py holds all the functions created to organize and analyze the Hurricane Lists. 
  
  To import all functions in jupyter notebook:  
  - Download Hurricane_Analysis.py and place in the same folder as your notebook.   
  - Copy and paste the below phrase to import module into your notebook.  
                  **from Hurricane_Analysis import \*** 
- DefaultDict from collections
  Collections is a built-in Python module that implements specialized container datatypes providing         alternatives to Python's general purpose built-in containers such as dict, list, set, and tuple. To
  learn more, click on this [link](https://towardsdatascience.com/pythons-collections-module-high-performance-container-data-types-cb4187afb5fc).
  
  DefaultDict is like a dictionary, but the only difference is that it does not raise a KeyError as it       provides a default value for the key that does not exist. To Learn more about DefaultDict, follow this [link](https://www.geeksforgeeks.org/defaultdict-in-python/).
  
  To import DefaultDict into your notebook, copy and paste the below phrase:  
  **from collections import defaultdict**



**This is a CodeAcademy-tasked open-ended project to test your overall comprehension for a specific benchmark in Python fundamentals.**
