import sys, io

def display_inventory():
    print ("Inventory:")
    val=list(inv.values())
    j = 0
    for i in inv:
        print ("{0} {1}".format(val[j],i))
        j+=1
    print ("Total number of items: {0}".format(sum(val)))

def add_to_inventory(inventory, added_items):
    for i in added_items:
        if inventory.get(i):
            inventory[i]+=1
        else:
            inventory[i]=1
    return inventory#new inventory

def print_table(order):
    key_max=len(max(inv, key=len))+6+len("count") #gold has the max value
    key_sort=[]
    if order=="count,desc":
        key_sort=sorted(inv, key=inv.get,reverse=True) #for reversed get start for the ending
    if order=="count,asc":
        key_sort=sorted(inv, key=inv.get,reverse=False) #for reversed get start for the ending
    if order=="":
        key_sort=inv
    print ("{0:^{1}}".format("Inventory:",key_max))
    print ("{0:>{1}}{2:>{3}}".format("count",7,"item name",key_max-7))
    print ("{0:->{1}}".format("",key_max))
    for i in key_sort:
        print ("{0:>{1}}{2:>{3}}".format(inv[i],7,i,key_max-7))
    print ("{0:>{1}}{2}".format("Total number of items: ", key_max-len(str(sum(inv.values()))),sum(inv.values())))

def file_name():
    if len(sys.argv)>1:
        if sys.argv[1] in ("-h", "--help"):
            print ("usage: {0} and csv file with inventories")
            return ""
        else:
            return sys.argv[1].lower()
    else:
        return ""

def import_inventory(filename):
    item_list=[]
    mult=0
    if len(filename)>1:
        for k,i in enumerate(open(filename),start=-1):
            if k>-1:
                i=i.replace("\n","")
                item_list.append(i.split(","))
        for i in range(len(item_list)):
            if inv.get(item_list[i][0]):
                inv[item_list[i][0]]+=int(item_list[i][1])
            else:
                inv[item_list[i][0]]=int(item_list[i][1])
    print (inv)


inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

filename=str(file_name())
print (filename)
display_inventory()
inv=add_to_inventory(inv,dragon_loot)
display_inventory()
print_table("count,desc")
import_inventory(filename)
