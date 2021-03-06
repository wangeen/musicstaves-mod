#----------------------------------------------------------------------
# This file was generated by /Library/Python/2.3/wxPython/tools/img2py.py
#
try:
   from wx import ImageFromStream, BitmapFromImage
   wxImageFromStream = ImageFromStream
   wxBitmapFromImage = BitmapFromImage
except:
   from wxPython.wx import wxImageFromStream, wxBitmapFromImage
import cStringIO, zlib


def getData():
    return zlib.decompress(
'x\xda\x01\xf3\x02\x0c\xfd\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00 \
\x00\x00\x00 \x08\x06\x00\x00\x00szz\xf4\x00\x00\x00\x04sBIT\x08\x08\x08\x08\
|\x08d\x88\x00\x00\x02\xaaIDATx\x9c\xb5W-\xb3\xe4 \x10\xecwub$\x12\x89D"\x91\
\x91\xc8\xfd\t+\xf7\xa7EFFF"\x91H$\x129\xeeN\\A%\xbb\xf9`\xdf\xbek\xb7\x9b)\
\xe8\xccL\xcft\xbe\x98\xf9\x0f\x0e\x90R\x82\x94\x12Dt\x14\xb2A\xce\x19B\x88\
\xeex\x00\xf8}\xf6p\x9eg03\x86a\x801\xe6\xf2\xb0eY\x90R\x82\xb5\x16\xd6\xda.\
"_g\x19\x98\xe7\x19Zkx\xef\xc1\xcc0\xc6\x9c\x12\xa9\xf11F\xe4\x9c\xa1\x94\
\xc20\x0c\xa7\x04N3\x00\x00J)(\xa5\x90sF\xce\xf94\xb6\x94\x82eY\xe0\x9c\x83\
\x10\x02!\x040\xf3i&.\tTH)!\xa5<\x8d\xa9\xf5\x9f\xe7\x19B\x88\xae2\xfc\xea%\
\xd0\x0bk-\xee\xf7;\xb4\xd6\x98\xe7\x19\xa5\x94\xd3\xf8\xae\x0c\xe4\x9c\xc1\
\xccPJu\x13\xd1ZCk}\x19\xd7\x95\x81\x10\x02\xbc\xf7]\x173sW\\\xc5a\x06B\x08\
\x08!@J\t\xe7\xdc\xe5A)\xa5\xd6t\xb7\xdb\xed}\x02\xa5\x14\x94R@DH)\xb5\x190M\
\x13\x80\x7fM\xb8\xf7vD\x84R\n\xa6iB)\x05\xde{\x10\x11\x8c1/\xf15\x96\x88Z9\
\x1b\x81\xb5\xccRJM>\xcc\x8c\x18\xe3i3\xad\xc933RJ\xbb\xddOD\x881\x82\x99\
\xf1x<\xb6\x04\x9e\x9bf\x9a&x\xefa\xad\xedJ\xa9\x10\x02\xf3<C)\x85\xfb\xfd~(\
?fF\x08\xa1\xfd>\xec\x81\xdb\xed\xd6\xdd\xc9\x000\x0c\x03\xa4\x94PJ\xed^\xee\
\xbd\x87\x10\xe2\xe5\xffS\x19\xf6^\xde\x13\x7fT\xc2\x1f\x1fDGp\xce\xc1Z\xfb\
\xf2\x7f\xcb@] \xff\x0b\xb5,\xcf\r\xda\x08\xec\xd5\xe7\x7f\x90\xa8\n{!p\xb4l\
\xae\xb6\xd9\xbbH)m2}iH\x88\x08D\xb4[\xbfw0\x8e\xe3\xee\x0b\x1e6\xa1\xf7\x1e\
1FXk\x9b\xd3\xf9\x04Z\xeb\xddevH \x84\xd0R\xff<<\xbe\x03c\xcc.\x81C\x15\xd4\
\xd1Z\xb7`\xce\x19\xcb\xb2|D\xa26\xe1\xae\n\xaa\xfb\xad\x0f\xeb\xcc\xae\xac\
\xa5\x94\xd0Z\xbf\xbdn\xd7\x97\x13\xd1\x8b\xb5\xdb\xc8p-Ekm\x1b\x9f\xd5^]Y\
\xb23T5\t!6\xfdt\xa8\x82\xbaNC\x08p\xceu]\x9esF\x8c\x11B\x88\x17\xf7\\U\xf0,\
\xe9S\x19\xbe#\xbd:\xeb\x89\x08\xe38\x82\x886\xbb\xa1:\xe5gg\xd5\x080\xf3\
\xb7\xeb[!\x84\x80R\xaa\x95r}fu\xcc\xcfK\xe9\xc7wA\x1d\xb5!\x84ff+*\x81u\xaf\
m\xbe\x8c>\xc9\xc0zf\x8c\xe3\x88R\n\x1e\x8fGsI{\xb1\xc0S\x0f|2\xf3k\xf6\xa4\
\x940\xc6 \xc6\xd8\xce\xfb\x91/\xa3+T\x17\xed\x9c\x033w9i\xe0\xe2\xe3\xf4]\
\xac\xb3\xd0\x8b\xbf\xdc9\x90.\x9de\xb0\xe5\x00\x00\x00\x00IEND\xaeB`\x82\
\x01TTz' )

def getBitmap():
    return wxBitmapFromImage(getImage())

def getImage():
    stream = cStringIO.StringIO(getData())
    return wxImageFromStream(stream)

