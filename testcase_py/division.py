def div(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "any number cannot divided by zero"
