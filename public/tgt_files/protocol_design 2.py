import numpy as np
import pandas as pd
from random import shuffle

def circ_shift(arr, shift):
    # from stack overflow https://stackoverflow.com/questions/2150108/efficient-way-to-rotate-a-list-in-python
    return(arr[shift:] + arr[:shift])
    
def generate_category_orders(csv_filepath, num_difficulty_levels, num_blocks):
    
    """
        Create protocols for testing
    
        save 4 protocol csvs with 4 different trial orders and correspodning travel duraitons 
    """
    
    orig_list = range(1, num_categories + 1)
    
    chunk_size = num_categories/num_difficulty_levels
    chunk = [shuffle(orig_list[i:i+chunk_size]) for i in range(0, len(orig_list), chunk_size)]
    
    cat_listASf = []
    cat_listBSf = []
    cat_listALf = []
    cat_listBLf = []
    
    block1 = []
    block2 = []
    for k in len(chunk):
        chunk_k = chunk[k]
        block1.append(random.shuffle(chunk[1:len(chunk_k)/2]))
        block2.append(random.shuffle(chunk[len(chunk_k)/2: ]))
        
    
    block1 = random.shuffle(block1)
    block1_circ = circ_shift(block1, 1)
    block2 = random.shuffle(block2)
    block2_circ = circ_shift(block2, 1)
    
    A = []
    B = []
    for blk in range(block1):
        A.append(blk[0])
        B.append(blk[1])  
    
    