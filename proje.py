# veri-bilimi-patikasi/python-temel
# Bitirme Projesi

flattened = []
def flatten(list_object):
    for each in list_object:
        if type(each) != str:
            try:
                flatten(each)
            except:
                flattened.append(each)
        else:
            flattened.append(each)
    return flattened

test_case = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
print(flatten(test_case))

reversed_list = []
def reverse(list_object):
    list_object.sort(reverse=True)
    try:
        for each in list_object:
            reversed_list.append(sorted(each, reverse=True))
    except:
        reversed_list.append(list_object)
    return reversed_list

test_case2 = [[1, 2], [3, 4], [5, 6, 7]]
print(reverse(test_case2))
