# def tri_recursion(k):
#   if(k > 0):
#     result = k + tri_recursion(k - 1)
#     print(result)
#   else:
#     result = 0
#   return result
#
# print("\n\nRecursion Example Results")
# tri_recursion(6)



def Alaa1(nu):

    if(nu > 0):
        r=nu + Alaa1(nu - 1)
        print(r)
    else:
        r=0
        return r

Alaa1(4)

