Feature			List	||Set		||Dictionary		||Tuple    ||
========================||==========||==================||=========||
Ordered			Yes		||No		||No				||Yes      ||
Mutable			Yes		||Yes		||Yes				||No       ||
Duplicates		Yes		||No		||Yes  				||Yes      ||
Indexing		Yes		||No		||Yes (by key)		||Yes      ||
===================================================================||
List =>	 When order matters and duplicates are needed	
Set  =>  When uniqueness is important and order doesn't matter	
Dict =>  When you need key-value mapping	
Tuple=>  When you need an immutable ordered collection


===========================================
Using set() to remove duplicates
===========================================
my_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = list(set(my_list))

my_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = []
for item in my_list:
    if item not in unique_list:
        unique_list.append(item)

import pandas as pd

my_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = pd.Series(my_list).drop_duplicates().tolist()

===========================================
Using set() to remove duplicates
===========================================
from collections import Counter
my_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
element_count = Counter(my_list)
element_count_dict = dict(element_count)

# Sample list
my_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
element_count = {}
for element in my_list:
    if element in element_count:
        element_count[element] += 1
    else:
        element_count[element] = 1
print(element_count)

import pandas as pd
my_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
element_count = pd.Series(my_list).value_counts()