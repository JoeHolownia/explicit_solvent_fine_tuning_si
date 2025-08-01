"""
Some helper functions for generating figures.
"""
import re

def get_name_from_path(fpath: str):
    """
    Get the name of a file (i.e. dataset / model) from a path string.
    """
    fname = fpath.split('/')[-1]
    if '.xyz' in fname:
        return fname.split('.xyz')[0]
    elif '.model' in fname:
        return fname.split('.model')[0]
    elif '.info' in fname:
        return fname.split('.info')[0]
    elif '.csv' in fname:
        return fname.split('.csv')[0]
    elif '.npz' in fname:
        return fname.split('.npz')[0]
    elif '.h5' in fname:
        return fname.split('.h5')[0]
    else:
        raise ValueError('File extension not handled by path splitter.')
    
def natural_sort_key(s):
    return [int(text) if text.isdigit() else text.lower() for text in re.split(r'(\d+)', s)]