import arcpy

fc = r"C:\Mac\Home\Documents\ArcGIS Pro 3.5\Chapter1\Kern_Co_Richgrove_Template\Kern_Co_Richgrove_Template.gdb\Crop_Parcel_1970Acres_complete"

fields = ["code", "Crop_categ", "Crop_type", "Irrigation", "Land_cover", "Notes"]

with arcpy.da.UpdateCursor(fc, fields) as cursor:
    for row in cursor:
        updated = False

        for i in range(len(fields)):
            val = row[i]

            if val is not None and str(val).strip() == "":
                row[i] = None #sets to Null
                updated = True
        if updated:
            cursor.updateRow(row)

field = ['Notes']
where = "code LIKE '%,%'"

table = arcpy.da.UpdateCursor(fc, field, 
                              where_clause = where)

for row in table:
        row[0] = "intercrop"
        table.updateRow(row)

del table


