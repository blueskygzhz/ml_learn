#!/usr/bin/env python3

def l1_norm(vec):
    if not vec:
        raise ValueError("vec empty")
    
    l1_norm_val = sum([abs(item) for item in vec])
    norm_vec = [item / l1_norm_val for item in vec]
    return norm_vec

def l2_norm(vec):
    if not vec:
        raise ValueError("vec empty")


    sum_of_squares = sum([item * item for item in vec])
    l2_norm_val = sum_of_squares ** 0.5
    norm_vec = [item / l2_norm_val for item in vec]

    return norm_vec

if __name__ == "__main__":
    test_vec = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    
    for item in test_vec:
        print("l1_norm:", l1_norm(item))
        print("l2_norm:", l2_norm(item))
