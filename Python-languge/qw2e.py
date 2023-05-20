from PIL import Image
def convert_grayscale(image):
    width, height = image.size
    new_image = Image.new("RGB", (width, height), "white")

    # 그레이스케일로 변환한다
    for i in range(width):
        for j in range(height):
            pixel = image.getpixel((i,j))

            # 픽셀의 R,G,B 값을 얻는다. (0에서 255사이의 값)
            red = pixel[0]
            green = pixel[1]
            blue = pixel[2]

            # 공식을 이용하여 그레이스케일 값으로 바꾼다
            gray = (red * 0.299) + (green * 0.587) + (blue * 0.114)

        # 새로운 이미지에 저장한다.
            new_image.putpixel((i,j), (int(gray), int(gray), int(gray)))
    return new_image
    
original = Image.open('C:/Users/young/OneDrive/바탕 화면/코드공간/Python-languge/lenna.png')
output = convert_grayscale(original)
output.show()