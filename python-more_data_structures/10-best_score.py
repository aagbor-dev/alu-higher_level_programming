#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    best_key = None
    best = None
    for key in a_dictionary:
        if best is None or a_dictionary[key] > best:
            best = a_dictionary[key]
            best_key = key
    return best_key
