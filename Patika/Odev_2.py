"""
2- Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün.
Örnek olarak:

input: [[1, 2], [3, 4], [5, 6, 7]]

output: [[7, 6, 5], [4, 3], [2, 1]]
"""


def reverse(mylist):
    result = []
    for e in mylist[::-1]:
        if isinstance(e, list):
            result.append(reverse(e))
        else:
            result.append(e)
    return result

liste = reverse([[1, 2], [3, 4], [5, 6, 7]])
print(liste)