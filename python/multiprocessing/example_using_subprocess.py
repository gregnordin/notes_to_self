import os
import subprocess
import time


def listdirs(path):
    return [d for d in os.listdir(path) if os.path.isdir(d)]


def find_python_make_file(path):
    for d in os.listdir(path):
        if d.startswith("make_") and d.endswith(".py"):
            return d


save_dir = os.path.dirname(os.path.abspath(__file__))

# Gather directories for gallery
dirs = sorted(listdirs(save_dir))
print("Directories: ", dirs)

# Get make_gallery....py file from each directory and create commands list
t0 = time.clock()
cmds_list = []
for dir in dirs:
    search_dir = os.path.join(save_dir, dir)
    gallery_make_file = find_python_make_file(search_dir)
    print(f"    {gallery_make_file}")
    cmds_list.append(["python", os.path.join(search_dir, gallery_make_file)])
    # subprocess.run(["python", os.path.join(search_dir, gallery_make_file)])
t1 = time.clock()
t_elapsed = t1 - t0
print(
    f"Time elapsed to gather make_gallery files: {t_elapsed} s"
)  # CPU seconds elapsed (floating point)

# Spawn parallel processes to run commands in commands list
t0 = time.clock()
procs_list = [
    subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    for cmd in cmds_list
]
t1 = time.clock()
t_elapsed = t1 - t0
print(
    f"   Time elapsed to run make_gallery files: {t_elapsed} s"
)  # CPU seconds elapsed (floating point)
