import arcpy

wp = r"C:\Mac\Home\Documents\ArcGIS Pro 3.5\Chapter1\Kern_Co_Richgrove_Template\Kern_Co_Richgrove_Template.gdb\Crops_58_Weed_Patch"

fields = ["Code_txt", "Crop_type_txt"]

for i, f in enumerate(fields):
    print(i, f)

cursor = arcpy.da.UpdateCursor(wp, fields)

for row in cursor:
    if row[0] and str(row[0]).startswith("iT9"):
        row[1] = "Melons, squash, and cucumbers"
    cursor.updateRow(row)

del cursor


