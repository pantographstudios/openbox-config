size = 16

circle_radius = 7

pixels = [0 for i in range(0, size**2)]

output = f"#define close_width {size}"
output += f"\n#define close_height {size}"
output += "\nstatic unsigned char close_bits[] = {"

def pixel_in_circle(i, j, radius, centre):
    i_centre = i + 0.5
    j_centre = j + 0.5

    distance_to_centre = ((i_centre - centre)**2+(j_centre - centre)**2)**0.5

    return distance_to_centre <= radius

for i in range(0, size):
    s = ""
    byte = ""
    for j in range(0, size):
        if pixel_in_circle(i, j, circle_radius, size/2):
            pixels[i*size + j] = 1
            byte += "1"
        else:
            byte += "0"
        
        if len(byte) == 8:
            output += '0x' + (hex(int(byte[::-1], 2)))[2:].zfill(2) + ', '
            byte = ""

if len(byte) > 0:
    output += '0x' + (hex(int(byte.zfill(8)[::-1], 2)))[2:].zfill(2) + ', '
    byte = ""

output = output[:-2]
output += "};"

with open('close.xbm', mode = 'w') as file:
    file.write(output)