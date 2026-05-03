x = 10 
def outer_function():
    x = 20 
    def inner_function():
        nonlocal x 
        x = 30 
        print("Inner function x:", x) 
    inner_function() 
    print("Outer function x:", x)
outer_function()