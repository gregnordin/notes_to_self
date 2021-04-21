from pathlib import Path
import sys

def insert_dir_into_path(cwd, num_levels_up):
    """Starting from cwd, go num_levels_up and insert that directory into PATH.
    Intended to work with Jupyter notebooks to import packages located up the 
    directory tree.
    
    Arguments
    ---------
    cwd: Path object
        Current working directory, i.e., directory in which Jupyter notebook is located.
    num_levels_up: int
        How many directories up from cwd to go
        
    Example usage
    -------------
    from pathlib import Path

    # Go one directory up and insert it into PATH
    from add_parent_dir_to_path import insert_dir_into_path
    cwd = !pwd
    insert_dir_into_path(Path(cwd[0]), 1)

    import <some_package>
    """
    assert isinstance(cwd, Path)
    assert isinstance(num_levels_up, int)
    assert num_levels_up >= 0
    
    module_path = str(cwd.parents[num_levels_up - 1])
    if module_path not in sys.path:
        sys.path.insert(1, module_path)
