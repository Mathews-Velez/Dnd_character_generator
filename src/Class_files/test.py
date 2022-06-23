
pack1=("red","blue","green")
pack2=("car","boat","plane")


packDictionary= { "pack1":pack1, "pack2":pack2 }

def getPack(pack):
    return packDictionary[pack]

print(getPack("pack1"))
