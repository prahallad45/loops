#ACCEPT A LIST OF VALUE AND SORT THEM IN BOTH ASC AND DESC ORDER
n=int(input("ENTER HOW MANY NUMBER YOY WANT TO INPUT:"))
if(n<=0):
    print("INVALID  INPUT")
else:
    l=list()
    for i in range(1,n+1):
        val=float(input("ENTER THE VALUE:"))
        l.append(val)
    else:
        print("CONTENT OF L={}",format(l))
        l.sort()
        print("ACCENDING ORDER={}".format(l))
        l.sort(reverse=True)
        print("DECENDING ORDER={}".format(l))
    