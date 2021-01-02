
#value += 1 for {2,3,4,5,6}
#value -= 1 for {10,J,Q,K,A}

def get_num_decks():
    ndecks = int(input("Enter number of decks:"))
    if(ndecks >= 1 and ndecks <= 10):
        return ndecks
    else: return get_num_decks()
    

def count_cards(num_decks):
    running_count = 0

    #the true count is the running count / number of decks
    true_count = 0 
    
    not_done = True

    while not_done:
        inp = input("(high: h, low: l):  ")

        if(inp == "h"):
            running_count -= 1
        elif(inp == "l"):
            running_count += 1
        else:
            not_done = False

        true_count = running_count/num_decks
        print("Running count : " + str(running_count))
        print("True count : " + str(true_count))


count_cards(get_num_decks())
