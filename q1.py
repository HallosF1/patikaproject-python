input = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

def flatten(l, a):
    for i in l:
        if isinstance(i, list):
            flatten(i, a)
        else:
            a.append(i)
    return a

print(flatten(input, []))
