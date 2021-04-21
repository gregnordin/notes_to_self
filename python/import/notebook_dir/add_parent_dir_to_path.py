from pathlib import Path
import sys

def insert_dir_into_path(cwd, num_levels_up):
    """Starting from cwd, go num_levels_up and insert that directory into PATH.
    """
    assert isinstance(cwd, Path)
    
    module_path = str(cwd.parents[num_levels_up - 1])
    if module_path not in sys.path:
        sys.path.insert(1, module_path)
