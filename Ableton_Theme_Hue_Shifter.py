import re
from hued.conversions import hex_to_hsv, hsv_to_hex
import shutil

hue_shift = 130
input = 'themes/Angst Robot.ask'

output_hex_colors = []

with open(input, 'r') as file:
    text = file.read()
    input_hex_colors = re.findall(r'#([0-9a-fA-F]{6}|[0-9a-fA-F]{3})\b', text)
    #print(input_hex_colors)

for input_hex_color in input_hex_colors:
    hsv_color = list(hex_to_hsv(input_hex_color))
    if hue_shift + hsv_color[0] >= 360:
        overflow_degree = hue_shift + hsv_color[0] - 360
        hsv_color[0] = overflow_degree
    else:
        hsv_color[0] = hue_shift + hsv_color[0]

    output_hex_colors.append(hsv_to_hex(hsv_color).replace("#",""))
    
#print(output_hex_colors)
dest = input[:-4]+' Shifted '+str(hue_shift)+' Degrees.ask'
output_theme = shutil.copyfile(input,dest)

def replace(filePath, text, subs, flags=0):
    with open(filePath, "r+") as file:
        file_contents = file.read()
        text_pattern = re.compile(re.escape(text), flags)
        file_contents = text_pattern.sub(subs, file_contents)
        file.seek(0)
        file.truncate()
        file.write(file_contents)

loop_length = (len(input_hex_colors))
i = 0
while i < loop_length:
    replace(output_theme, input_hex_colors[i], output_hex_colors[i])
    i += 1
    
print('"'+dest + '" Generated!')