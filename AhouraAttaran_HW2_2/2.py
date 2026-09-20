def maping(value):
    if value < 40: return "Young"
    elif value < 65: return "Middle-aged"
    else : return "Old"
def age(value, *args):
    filtered = filter(lambda x: x > value, args)
    out = map(maping, filtered)
    return(out)


print(list(age(5,6,50,71,9,4,38,82,61)))