import json

Playing = True

def main():
    global Playing
    while Playing:
        menu_Choice = getMenuChoice()
        if menu_Choice == 0:
            Playing = False
        elif menu_Choice == 1:
            playGame()
        elif menu_Choice == 4:
            editNode()

    

def getMenuChoice(): 
    print("""
         0) exit
         1) load default game
         2) load a game file
         3) save the current game
         4) edit or add a node
         5) play the current game""")
    menu_Choice = int(input("What will you do?"))
    return menu_Choice

def playGame():
    global Playing
    playernode = "start"
    while Playing:
        playernode = playNode(playernode)
        if playernode == "quit":
            Playing = False
        elif playernode == "start":
            getDefaultGame()


def playNode(node):
    dict = getDefaultGame()
    dict_info = dict[node]
    
    Desc = dict_info[0]
    MenuA = dict_info[1]
    NodeA = dict_info[2]
    MenuB = dict_info[3]
    NodeB = dict_info[4]

    print(Desc)
    print(MenuA)
    print(MenuB)

    next_choice = int(input("Your Choice: "))

    if next_choice == 1:
        return NodeA
    if next_choice == 2:
        return NodeB
    else:
        print("select choice 1 or 2")
        return node
def getDefaultGame():
    return {
        "start":["Default start node","1) start over","start", "2) quit","quit"],
    }
def editNode():
    print("Create or edit a node")
    print("Current nodes:")
    
    game_data = getDefaultGame()
    for node in game_data.keys(): # i figured out the key was the thing on the outside of the dict from a handy yt video
        print(node)

    editing_nodes = input("Choose node to edit or enter new node name: ")
    if editing_nodes in game_data:
        node_details = game_data[editing_nodes]
        Desc = node_details[0]
        MenuA = node_details[1]
        NodeA = node_details[2]
        MenuB = node_details[3]
        NodeB = node_details[4]
        update_desc = input(f"Description ( Current: {Desc}) New: ")
        update_MenuA = input(f"Menu A ( Current: {MenuA}) New: ")
        update_NodeA = input(f"Node A ( Current: {NodeA}) New: ")
        update_MenuB = input(f"MenuB ( Current: {MenuB}) New: ")
        update_NodeB = input(f"NodeB ( Current: {NodeB}) New: ")
        node_details[0] = update_desc
        print(node_details)
    else:
        print("No node found")


def editField():
    print()
def saveGame():
    print()
def loadGame():
    print()

main()
