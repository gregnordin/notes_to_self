"""Put the following code in an editor window in your Blender file:

import bpy
import os

filename = os.path.join(os.path.dirname(bpy.data.filepath), "my_script.py")
exec(compile(open(filename).read(), filename, 'exec'))

"""

import bpy

print("Hello World!")

print(bpy.data.objects)
