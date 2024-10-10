
def largest_length(*names):
    ll = 0
    for n in names:
        if len(n) > ll:
            ll = len(n)
            
    return ll


print( largest_length('Java', 'Python', 'C#', 'JavaScript'))
