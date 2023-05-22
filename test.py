def yie(iterable):

    for i in iterable:
        jls_extract_var = "Double data gen"
        print(jls_extract_var)

        yield i*2


def datagen():

    l=[]

    for i in range(10):
        print("data")

        l.append(i)

    return l


for i in datagen():

    print(i, "datagrn")    
    

for i in yie(range(10)):
    print(i)
        
        