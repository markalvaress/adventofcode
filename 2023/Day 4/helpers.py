def num_matching(card):
    """
    card: A string of the form "a b c | d e f" where a-f are integers
    """
    winning_numbers_str, my_numbers_str = card.split("|")

    winning_numbers = re.findall("\d+", winning_numbers_str)
    my_numbers = re.findall("\d+", my_numbers_str)

    num_matching_nums = 0
    for number in my_numbers:
        if number in winning_numbers:
            num_matching_nums += 1
    
    return(num_matching_nums)
