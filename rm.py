# в случае когда список содержит хэшируемые объекты 
# "Significantly faster than numpy.unique."
# использует хэш-таблицы
# сложность между O(N) и O(NlogN)  

import pandas as pd
def remove_duplicates_pd(l):
    return list(pd.unique(l))


#в случае нехэируемых объектов
#сложность O(N^2)

def remove_duplicates(l):
    final_list = []
    for element in l:
        if element not in final_list:
            final_list.append(element)
    return final_list
