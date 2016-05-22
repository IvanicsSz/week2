import sys, io

def display_inventory():
    print ("Inventory:")
    val=list(inv.values())
    j,sum_val=0,0
    for i in inv:
        print ("{0} {1}".format(val[j],i))
        sum_val+=val[j]
        j+=1
    print ("Total number of items: {0}".format(sum_val))

def add_to_inventory(inventory, added_items):
    for i in added_items:
        if inventory.get(i):
            inventory[i]+=1
        else:
            inventory[i]=1
    return inventory#new inventory

def print_table(order):
    key_max=max(inv, key=len) #gold has the max value
    key_asc=sorted(inv, key=inv.get) #for reversed get start for the ending
    #for i in key_lenght:
    #    print (len(i))
    print (key_asc)
    print (key_max)

#    Inventory:
#  count    item name
#--------------------
#     45    gold coin
#     12        arrow
#      6        torch
#      2       dagger
#      1         rope
#      1         ruby
#--------------------
#Total number of items: 67   right-justified.
inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

display_inventory()
inv=add_to_inventory(inv,dragon_loot)
display_inventory()
print_table("")
