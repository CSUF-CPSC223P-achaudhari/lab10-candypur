import threading, time, json

f = open('inventory.dat', 'r')
file_contents = json.load(f)
f.close()

inventory = file_contents


def bot_clerk(items):
    cart = []
    lock = threading.Lock()
    list_one = []
    list_two = []
    list_three = []
    count = 0
    
    for i in range(len(items)):
        if count == 0:
            list_one.append(items[i])
            count += 1
        elif count == 1:
            list_two.append(items[i])
            count += 1
        elif count == 2:
            list_three.append(items[i])
            count = 0
    
    robot_one = threading.Thread(target=bot_fetcher, args=(list_one, cart, lock))
    robot_two = threading.Thread(target=bot_fetcher, args=(list_two, cart, lock))
    robot_three = threading.Thread(target=bot_fetcher, args=(list_three, cart, lock))
    
    robot_one.start()
    robot_two.start()
    robot_three.start()
    
    robot_one.join()
    robot_two.join()
    robot_three.join()
    
    return cart
    
def bot_fetcher(items, cart, lock):
    for i in range(len(items)):
        time.sleep(inventory[items[i]][1])
        cart.append([items[i], inventory[items[i]][0]])
    
    