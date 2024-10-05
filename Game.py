import json

Playing = True
PlayingGame = True
def main():
    global Playing
    global PlayingGame
    while PlayingGame:
        menu_Choice = getMenuChoice()
        if menu_Choice == 0:
            Playing = False
            PlayingGame = False
        elif menu_Choice == 1:
            getDefaultGame()
        elif menu_Choice == 2:
            loadGame()
        elif menu_Choice == 3:
            saveGame()
        elif menu_Choice == 4:
            editNode()
        elif menu_Choice == 5:
            playGame()

    

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
    global PlayingGame
    playernode = "start"
    while PlayingGame:
        playernode = playNode(playernode)
        if playernode == "quit":
            PlayingGame = False
            getMenuChoice()
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
    if editing_nodes in game_data.keys():
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
        if update_desc == "":
            node_details[0] = Desc
        else:
            node_details[0] = update_desc
        if update_MenuA == "":
            node_details[1] = MenuA
        else:
            node_details[1] = update_MenuA
        if update_NodeA == "":
            node_details[2] = NodeA
        else:
            node_details[2] = update_NodeA
        if update_MenuB == "":
            node_details[3] = MenuB
        else:
            node_details[3] = update_MenuB
        if update_NodeB == "":
            node_details[4] = NodeB
        else:
            node_details[4] = update_NodeB
        print(game_data)
        return game_data
    else:
        update_desc = input(f"Description (): ")
        update_MenuA = input(f"Menu A (): ")
        update_NodeA = input(f"Node A (): ")
        update_MenuB = input(f"MenuB (): ")
        update_NodeB = input(f"NodeB (): ")
        game_data[editing_nodes] = update_desc, update_MenuA, update_NodeA, update_MenuB, update_NodeB 
        print(game_data)
        return game_data
    
def saveGame():
    outFile = open("savedGame.json", "w")
    json.dump(editNode(), outFile, indent=2)
    outFile.close
    print("Saved game to a json")
def loadGame():
    with open('savedGame.json') as f:
        modified_data = json.load(f)
        cur_game = modified_data
        return cur_game
main()
