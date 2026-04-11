import arcpy

fc = r"C:\Mac\Home\Documents\ArcGIS Pro 3.5\Chapter1\Kern_Co_Richgrove_Template\Kern_Co_Richgrove_Template.gdb\Crops_58_Arvin"

fields = ["Code", "Crop_category", "Crop_type", "Irrigation_Status", "Land_cover", "Notes"]

mapping = {
    "NV": [None, None, None, "Native vegetation", None],
    "NV/iD7": [None, None, None, "Native vegetation", "mixed use, plums"],
    "NB" : [None, None, None, "Barren and Wasteland", None],
    "iP1S": ["P", "Alfalfa and alfalfa mix", "i", None, "seed crop"],
    "iP1": ["P", "Alfalfa and alfalfa mix", "i", None, None],
    "iPF": ["P", "Fallow", "i", None, None],
    "iF1": ["F", "Cotton", "i", None, None],
    "iF2": ["F", "Safflower", "i", None, None],
    "iF11": ["F", "Misc. field", "i", None, None],
    "iT9": ["T", "Melons, squash, and cucumbers", "i", None, None],
    "iT10": ["T", "Onions and garlic", "i", None, None],
    "U13": ["U", None, None, "Sewage treatment plant", None],
    "iF1-50/NV-50": ["F", "Cotton", "i", "Native vegetation", "mixed use"],
    "iF1-50/Unknown-50": ["F", "Cotton", "i", None, "intercrop"],
    "iT9/iD5": ["T", "Potatoes", "i", None, "intercrop"],
    "iTF": ["T", "Fallow", "i", None, None],
    "iF6": ["F", "Corn", "i", None, None],
    "iF9": ["F", "Castor beans", "i", None, None],
    "iFF": ["F", "Fallow", "i", None, None],
    "nG1": ["G", "Barley", "n", None, None],
    "iG1": ["G", "Barley", "i", None, None],
    "iG2": ["G", "Wheat", "i", None, None],
    "iT5": ["T", "Unknown", "i", None, None],
    "iT3": ["T", "Beans (green)", "i", None, None],
    "UI1": [None, None, None, "Urban industrial", "Manufacturing, assembling, and general processing"],
    "UI3": ["U", None, None, "Urban industrial", "Storage and Distribution"],
    "UI2": ["U", None, None, "Urban industrial", "Extractive industries"],
    "iF1-50/iG1-50": ["F", "Cotton", "i", None, "intercrop"],
    "I1": ["I", "Idle", None, None, "Land cropped in past years but not tilled"],
    "I2": ["I", "New Land", "i", None, "prepped for crop production"],
    "IP15": ["P", "Unknown", None, None, "possible irrigated alfalfa seed crop"],
    "iT5b": ["T", "Unknown", "i", None, "b not noted"],
    "iT8": ["T", "Lettuce", "i", None, None],
    "iT11": ["T", "Peas", "i", None, None],
    "iT12W": ["T", "Potatoes", "i", None, "W not noted"],
    "iT12": ["T", "Potatoes", "i", None, None],
    "iT13": ["T", "Sweet potatoes", "i", None, None],
    "iF8": ["F", "Sudan", "i", None, None],
    "iF5": ["F", "Sugar beets", "i", None, None],
    "iV": ["V", "Grapes", "i", None, "unknown subclass"],
    "iS1": ["S", None, "i", "Farmstead", None],
    "S1": ["S", None, None, "Farmstead", None],
    "iF1/iD4Y": ["F", "Cotton", "i", None, "intercrop"],
    "iD4Y": ["D", "Deciduous fruits and nuts", "i", None, "young non-bearing"],
    "iD5Y": ["D", "Peaches and nectarines", "i", None, "young non-bearing"],
    "iD7": ["D", "Plums", "i", None, None],
    "iP2S": ["P", "Clover", "i", None, "seed crop"],
    "UC5": ["U", None, None, "Urban Institutions", "hospitals, prisons"],
    "iP3": ["P", "Mixed pasture", "i", None, None],
    "iV/iT9": ["V", "Grapes", "i", None, "intercrop"],
    "S2": ["S", None, None, "Feed lots", None],
    "iS2": ["S", None, "i", "Feed lots", None],
    "iS6": ["S", None, "i", "Semiagricultural", "unknown subclass"]
}


cursor = arcpy.da.UpdateCursor(fc, fields)

for row in cursor:
    code = row[0]

    if code:
        #some codes have variable spaces
        code = code.replace(" ", "")  

    if code in mapping:
        values = mapping[code]
        #position 1 in each row holds the crop code 
        row[1] = values[0]
        row[2] = values[1]
        row[3] = values[2]
        row[4] = values[3]
        row[5] = values[4]

        cursor.updateRow(row)

del cursor


