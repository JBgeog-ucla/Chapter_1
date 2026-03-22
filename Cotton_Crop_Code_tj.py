import arcpy

tj = r"C:\Mac\Home\Documents\ArcGIS Pro 3.5\Chapter1\Kern_Co_Richgrove_Template\Kern_Co_Richgrove_Template.gdb\Crops_58_Tejon_Hills"

fields = ["Code", "Crop_category", "Crop_type", "Irrigation_Status", "Land_cover", "Notes"]
values = ["iF1", "F", "Cotton", "i", "<Null>", "<Null>"]

table = arcpy.da.UpdateCursor(tj, fields)

for row in table:
    for i, val in enumerate(values):
        row[i] = val
    table.updateRow(row)

del table


