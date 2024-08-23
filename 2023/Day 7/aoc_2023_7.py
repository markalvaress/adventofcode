import functools

hands_file = open("2023/Day 7/input.txt", "r")
hands = hands_file.read()
hands_file.close()

hands = [hand.split(" ") for hand in hands.splitlines()]

def get_hand_type(hand):
    """There are 7 types of hands, so we return a number from
    1-7, where 7 is strongest (5 of a kind)"""
    n_distinct_cards = n_distinct_chars(hand)
    list_of_occurences = [num_occurences(hand, hand[i]) for i in range(5)]

    if n_distinct_cards == 1:
        return 7 # five of a kind
    elif n_distinct_cards == 2:
        if list_of_occurences[0] in [1,4]:
            return 6 # four of a kind
        else:
            return 5 # full house
    elif n_distinct_cards == 3:
        if any([num_occured == 3 for num_occured in list_of_occurences]):
            return 4 # three of a kind
        else:
            return 3 # two pair 
    elif n_distinct_cards == 4:
        return 2 # one pair
    else:
        return 1 # high card

def n_distinct_chars(string):
    n_distinct = 1
    for i in range(1, 5):
        if all(string[i] != prev_letter for prev_letter in string[0:i]):
            n_distinct += 1

    return n_distinct
    
def num_occurences(string, char):
    return sum([string[i] == char for i in range(len(string))])

def hand_is_better(hand1, hand2):
    """Tells you if hand1 is better than hand2. Returns 1 for hand1 > hand2 and 
    -1 for hand1 < hand2"""
    # We do this so we can accept as input just a hand (i.e. hand1 = 'A2345')
    # and hand-bet pairs (i.e. hand1 = ['A2345', 16])
    if isinstance(hand1, list):
        hand1 = hand1[0]
    if isinstance(hand2, list):
        hand2 = hand2[0]

    hand1_type = get_hand_type(hand1)
    hand2_type = get_hand_type(hand2)

    if hand1_type > hand2_type:
        return 1
    elif hand1_type < hand2_type:
        return -1
    else:
        for i in range(5):
            if get_card_value(hand1[i]) > get_card_value(hand2[i]):
                return 1
            elif get_card_value(hand1[i]) < get_card_value(hand2[i]):
                return -1
            
        print("By jingo these are the same hands!")
        return 0

def get_card_value(card):
    # i don't have python 3.10 so can't use match case :(  
    if card == 'A':
        return 14
    elif card == 'K':
        return 13
    elif card == 'Q':
        return 12
    elif card == 'J':
        return 11
    elif card == 'T':
        return 10
    else:
        return int(card)


sorted_hands = sorted(hands, key = functools.cmp_to_key(hand_is_better))
total_winnings = sum([(i + 1) * int(sorted_hands[i][1]) for i in range(len(sorted_hands))])
