Wcollection = ["saree", "kurti" , "dupatta", "lehanga" ]

def collection(name):
    if name in Wcollection:
        print(name, "is available to purchase")
    else:
        print("this item is not available")
def allcollection():
    print("all collections")
    for x in Wcollection:
        print(x)