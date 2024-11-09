

x = 100
def outer():
    x = 5
    def inner():
        global x
        x += 10
        return x
    return inner()
    
print(outer()) # 6