def difference(*args):
    if args == ():
        print(0)
    else:
        lst = list(args)
        x = round(max(lst) - min(lst),2)
        print(x)

difference()