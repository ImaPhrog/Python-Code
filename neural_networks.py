class network():
    pass
class node():
    def squash(self,item):
        item = (1/(1+(2.7**-item)))
        return item
n = node()
print(n.squash(-1))