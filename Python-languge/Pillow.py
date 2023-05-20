import numpy as np
from PIL import Image
import io
wd=512
ht=512
def runlength_ecd(image):

    result = ""
    last = image[0]
    size = len(image)
    i = 1
    count = 1

    while i < size:

        if image[i] == last:
            count = count + 1

        else:
            result = result + str(count) + ","
            last = image[i]
            count = 1

        i = i + 1


    if image[0] == '0':

        result = result + str(count) 
        return result
    else:
        result = str(0) + "," + result + str(count)
        return result
def image_dcd(num_list):
    result = ""
    size = len(num_list)
    i = 0

    while i < size:
        if int(num_list[0]) != '0':
            if i % 2 == 0:
                count = int(num_list[i])
                result += '0' * count
                i += 1
            else:
                count = int(num_list[i])
                result += '1' * count
                i += 1
        else:
            if i % 2 == 0:
                count = int(num_list[i])
                result += '1' * count
                i += 1
            else:
                count = int(num_list[i])
                result += '0' * count
                i += 1
    
    pixel_array = np.array(list(result.replace("255","1")), dtype=np.uint8)


    # 배열을 이미지로 변환
    image = Image.fromarray(pixel_array,mode="1")

    return image   
def list_out(list):
    out_list = [str(a) for b in list for a in b]
    return ''.join(out_list)
def image_ecd(image):
    bw_image = image.convert("1")
    width, height = bw_image.size
    pixels = list(bw_image.getdata())
    pixel_array = [pixels[i:i+width] for i in range(0, len(pixels), width)]

    return pixel_array


image_file = 'C:/Users/young/OneDrive/바탕 화면/코드공간/Python-languge/lenna.png'
original_image = Image.open(image_file)
x = np.array(original_image.convert("1"))
result = image_ecd(original_image)
bokgu_image=image_dcd(runlength_ecd(list_out(result)).replace(",","").replace("255","1"))
bokgu_image = bokgu_image.resize((wd, ht))
bokgu_image = Image.fromarray(x)                                                                                                                  #이 줄이 없으면 그냥 검은화면으로 복구되서 넣었습니다.
bokgu_image.show()