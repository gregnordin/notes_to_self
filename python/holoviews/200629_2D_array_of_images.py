from pathlib import Path
import zipfile
import io

import numpy as np
import holoviews as hv
from holoviews import opts
from holoviews import streams
import panel as pn

from PIL import Image
import cv2

hv.extension('bokeh')


def get_image_from_in_memory_zipfile(image_file_path, zipped_file):
    return cv2.imdecode(np.frombuffer(zipped_file.read(image_file_path), np.uint8), 
                        cv2.IMREAD_GRAYSCALE)

# Global variables
zipped_file = None
image_file_names = []
num_image_rows = 9
max_num_images_to_display = 9


# Simplifying functions
file = lambda s: f"slices/{s}"
image = lambda f: get_image_from_in_memory_zipfile(file(f), zipped_file)


# Set up options for hv.Images objects
ymax, xmax = 1600, 2560
scale_factor = 8
bounds=(0, 0, xmax, ymax)   # Coordinate system: (left, bottom, right, top)
options = {'cmap': 'gray',
           'clim': (0, 255),
           'aspect': 'equal',
           'frame_width': int(xmax/scale_factor),
           'frame_height': int(ymax/scale_factor),
          }


# Create and organize basic elements in layout
file_input = pn.widgets.FileInput()
item_selector = pn.widgets.MultiSelect()
controls = pn.Column(file_input, "")
layout = pn.Row(controls, pn.Column(""))
# print(layout)


# Action when zip file is selected
@pn.depends(file_contents=file_input, watch=True)
def _image_selector(file_contents):
    global zipped_file
    zipped_file = zipfile.ZipFile(io.BytesIO(file_contents))
    global image_file_names
    image_file_names = sorted([
                f.filename.strip('slices/') for f in zipped_file.filelist \
                if f.filename.startswith('slices/') and f.filename.endswith('.png')
            ])
    
    initially_selected_files = image_file_names[:2].copy()
    
    # Set up selector object
    item_selector.options = image_file_names
    item_selector.value = initially_selected_files
    item_selector.size = 25
    item_selector.width = 120
    
    # Place selector object in proper position in layout
    layout[0][1] = item_selector


# Re-make Panel object containing images when different files are selected
@pn.depends(selected_file_names=item_selector, watch=True)
def _images_col(selected_file_names):
    
    n_tot = len(selected_file_names)
    if n_tot > max_num_images_to_display: n_tot = max_num_images_to_display

    n_rows = num_image_rows
    n_cols = int(n_tot / n_rows)
    if (n_tot % num_image_rows) != 0: n_cols += 1 

    # Set up Row and Columns with images
    row = pn.Row()
    for i in range(n_cols):
        col = pn.Column()
        for j in range(n_rows):
            im = i * n_rows + j
            if im == n_tot:
                break
            file_name = selected_file_names[im]
            col.append(
                hv.Image(image(file_name), bounds=bounds).opts(title=file_name, **options)
                # f"{file_name}"
            )
        row.append(col)
    
    # Replace appropriate spot in layout with new pn.Row object containing selected images
    layout[1] = row
    

# layout.show()
layout.servable()
