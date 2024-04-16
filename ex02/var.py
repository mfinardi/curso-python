def my_var ():
    var1 = 42
    print(str(var1) + " has a type " + str(type(var1)))

    var2 = "42"
    print(str(var2) + " has a type " + str(type(var2)))

    var3 = "quarante-deux"
    print(str(var3) + " has a type " + str(type(var3)))      
    
    var4 = 42.0
    print(str(var4) + " has a type " + str(type(var4)))    

    var5 = True
    print(str(var5) + " has a type " + str(type(var5))) 

    var6 = [42]
    print(str(var6) + " has a type " + str(type(var6)))  

    var7 = {42:42}
    print(str(var7) + " has a type " + str(type(var7)))

    var8 = (42,)
    print(str(var8) + " has a type " + str(type(var8)))

    var9 = set()
    print(str(var9) + " has a type " + str(type(var9)))


if __name__ == '__main__':
    my_var()