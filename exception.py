#check the fuctionality of cart
# it will failed the case as product cart is not matching
itemsincart = 0
#if itemsincart != 2:
    #raise Exception("prouduct cart count not matching")
#assert (itemsincart == 2)
# we should get assert error
try:
    with open('tests.text') as reader:
        reader.read()
#except:
   # print("somehow I reach this block beacause there is failure in block")
except Exception as e :
    print(e)
finally:
    print("cleaning up records") # to delete cookies
