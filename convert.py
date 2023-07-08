import bpy

# Set the path to the OSM file
osm_file = "map.osm"

# Import the OSM file using the OpenStreetMap addon
bpy.ops.import_scene.openstreetmap(filepath=osm_file)

# Set the output file path
output_file = "map.obj"

# Export the scene as OBJ
bpy.ops.export_scene.obj(filepath=output_file, use_selection=False, use_materials=False)
