def all_numbers_from_tower(tower):
    """
    tower: list of digits, where tower[-1] is the top block (taken first)
    returns: a set of all possible digit strings
    """
    results = set()

    def backtrack(index, current):
        # If all blocks used → save result
        if index == len(tower):
            results.add("".join(current))
            return
        
        digit = str(tower[index])
        
        # Place digit to the left
        backtrack(index + 1, [digit] + current)
        
        # Place digit to the right
        backtrack(index + 1, current + [digit])

    # Start with empty sequence; process from the top (reverse tower)
    backtrack(0, [])
    return results

