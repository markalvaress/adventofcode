import functools
import re

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

def hand_is_better(hand1, hand2, is_j_low = False, card_combos1 = None, card_combos2 = None, card_combos3 = None):
    """Tells you if hand1 is better than hand2. Returns 1 for hand1 > hand2 and 
    -1 for hand1 < hand2"""
    # We do this so we can accept as input just a hand (i.e. hand1 = 'A2345')
    # and hand-bet pairs (i.e. hand1 = ['A2345', 16])
    if isinstance(hand1, list):
        hand1 = hand1[0]
    if isinstance(hand2, list):
        hand2 = hand2[0]

    if is_j_low:
        hand1_type = get_hand_type_jokers(hand1, card_combos1, card_combos2, card_combos3)
        hand2_type = get_hand_type_jokers(hand2, card_combos1, card_combos2, card_combos3)
    else:
        hand1_type = get_hand_type(hand1)
        hand2_type = get_hand_type(hand2)

    if hand1_type > hand2_type:
        return 1
    elif hand1_type < hand2_type:
        return -1
    else:
        for i in range(5):
            if get_card_value(hand1[i], is_j_low = is_j_low) > get_card_value(hand2[i], is_j_low = is_j_low):
                return 1
            elif get_card_value(hand1[i], is_j_low = is_j_low) < get_card_value(hand2[i], is_j_low = is_j_low):
                return -1
            
        print("By jingo these are the same hands!")
        return 0

def get_card_value(card, is_j_low = False):
    # i don't have python 3.10 so can't use match case :(  
    if card == 'A':
        return 14
    elif card == 'K':
        return 13
    elif card == 'Q':
        return 12
    elif card == 'J':
        # we don't actually need to reorder everything else, 
        # we just need to make J the lowest
        if is_j_low:
            return 1
        else:
            return 11
    elif card == 'T':
        return 10
    else:
        return int(card)


sorted_hands = sorted(hands, key = functools.cmp_to_key(hand_is_better))
total_winnings = sum([(i + 1) * int(sorted_hands[i][1]) for i in range(len(sorted_hands))])

# pt 2 -------------------

# not very efficient but will get the job done
def get_hand_type_jokers(hand, card_combos1, card_combos2, card_combos3):
    """card_combos3 is the array of all possible combinations of 3 cards, etc."""
    num_jacks = sum([card == "J" for card in hand])
    other_cards = re.sub("J", "", hand) # i.e. not jokers

    if num_jacks in [4,5]:
        return 7 # if there were 4 jokers we'd change them all to the value of the other card to get a 5 of a kind
    elif num_jacks == 3:
        all_possible_hands = [other_cards + joker_combo for joker_combo in card_combos3]
    elif num_jacks == 2:
        all_possible_hands = [other_cards + joker_combo for joker_combo in card_combos2]
    elif num_jacks == 1:
        all_possible_hands = [other_cards + joker_combo for joker_combo in card_combos1]
    else:
        return get_hand_type(hand)

    all_handtypes = [get_hand_type(possible_hand) for possible_hand in all_possible_hands]
    return max(all_handtypes)

# This will include duplicates since the strength of the hand doesn't depend on order, so we'll have
# A2A, 2AA, AA2, etc. 
def get_card_combos(n: int):
    possible_cards = ['J','2','3','4','5','6','7','8','9','T','Q','K','A']
    if n == 1:
        return possible_cards
    else:
        result = []
        for card in possible_cards:
            result.extend([card + subsequent_card for subsequent_card in get_card_combos(n - 1)])
        
        return result
    

card_combos1 = get_card_combos(1)
card_combos2 = get_card_combos(2)
card_combos3 = get_card_combos(3)

sorted_hands_joker = sorted(hands, 
                            key = functools.cmp_to_key(lambda h1, h2: hand_is_better(h1, h2, is_j_low = True, 
                                                                                     card_combos1 = card_combos1, 
                                                                                     card_combos2 = card_combos2, 
                                                                                     card_combos3 = card_combos3)))
total_winnings_joker = sum([(i + 1) * int(sorted_hands_joker[i][1]) for i in range(len(sorted_hands_joker))])


