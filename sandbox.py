#! python3

theInventory={'rope': 1,
              'torch': 6,
              'gold coin': 42,
              'dagger': 1,
              'arrow': 12
              }
dragonLoot = ['gold coin',
              'dagger',
              'gold coin',
              'gold coin',
              'ruby'
              ]
              
def displayInventory(inventory):
    totalItems = 0
    print('Inventory:')
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        totalItems += v
    print('Total number of items: ' + str(totalItems))
    print('')

def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(item, 0)
        inventory[item] +=1
    return inventory

displayInventory(theInventory)
addToInventory(theInventory, dragonLoot)
displayInventory(theInventory)