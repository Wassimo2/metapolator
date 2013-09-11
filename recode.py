from lxml import etree
import os
import sys

ufo = sys.argv[1]

mflist = ['0021', '0022', '0023', '0024', '0025', '0026', '0027', '0028', '0029', '002A', '002B', '002C', '002D', '002E', '002F', '0030', '0031', '0032', '0033', '0034', '0035', '0036', '0037', '0038', '0039', '003A', '003B', '003C', '003D', '003E', '003F', '0040', '0041', '0042', '0043', '0044', '0045', '0046', '0047', '0048', '0049', '004A', '004B', '004C', '004D', '004E', '004F', '0050', '0051', '0052', '0053', '0054', '0055', '0056', '0057', '0058', '0059', '005A', '005B', '005C', '005D', '005E', '005F', '0060', '0061', '0062', '0063', '0064', '0065', '0066', '0067', '0068', '0069', '006A', '006B', '006C', '006D', '006E', '006F', '0070', '0071', '0072', '0073', '0074', '0075', '0076', '0077', '0078', '0079', '007A', '007B', '007C', '007D', '007E']

os.chdir(ufo)
for files in os.listdir("."):
  if files.endswith(".glif"):
    glif = etree.parse(files)
    glyph = glif.getroot() 
    g = glyph.get('name') 
    uni = glif.find('unicode')
    u = uni.get('hex')
    name = glyph.attrib
    
    for i, j in enumerate(mflist) :
      if j == u :
        print i
        newname = str(i+1)
        glyph.set('name', newname)
        glif.write(newname + '.glif')


