import bpy

# Set the path to your OSM file
osm_file = "map.osm"

# Set the path to output the OBJ file
obj_file = "output.obj"

# Import the OSM file
bpy.ops.import_scene.osm(filepath=osm_file)

# Set up any additional configuration or modifications

# Export the scene as OBJ
bpy.ops.export_scene.obj(filepath=obj_file)

# Quit Blender
bpy.ops.wm.quit_blender()
