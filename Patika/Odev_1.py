"""
1- Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı listtlerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir.
Örnek olarak:

input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

output: [1,'a','cat',2,3,'dog',4,5]
"""


def flattenlist(myList):
    flatlist = []

    for item in myList:
        if type(item) is list:
            for element in flattenlist(item):
                flatlist.append(element)
        else:
            flatlist.append(item)
    return flatlist

nestedlist = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
print('Nested List:', nestedlist)
print('Converted Flat List:', flattenlist(nestedlist))