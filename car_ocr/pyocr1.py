from distutils.command.build import build
from operator import le
from PIL import Image
import sys
import pyocr
import pyocr.builders

tools=pyocr.get_available_tools()
print(tools)
if len(tools)==0:
    print("No OCR tool found")
    sys.exit(1)
tool=tools[0]

txt=tool.image_to_string(
    Image.open('test.jpg'),
    builder=pyocr.builders.TextBuilder()
)
print("result=",txt)