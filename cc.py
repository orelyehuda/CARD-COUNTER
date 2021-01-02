
#value += 1 for {2,3,4,5,6}
#value -= 1 for {10,J,Q,K,A}

def get_num_decks():
    ndecks = int(input("Enter number of decks:"))
    if(ndecks >= 1 and ndecks <= 10):
        return ndecks
    else: return get_num_decks()
    

def count_cards(num_decks):
    running_count = 0

    true_count = 0

print(get_num_decks())
