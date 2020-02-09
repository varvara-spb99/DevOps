"""
Написать скрипт, который будет вытаскивать gps данные
из фотографии (jpg файл) и передавать их на вход программе
из hw16.txt
"""
from PIL import Image
from hw16_2v import navig

def convert(value):
    d = float(value[0][0]) / float(value[0][1])
    m = float(value[1][0]) / float(value[1][1])
    s = float(value[2][0]) / float(value[2][1])
    return d + (m / 60.0) + (s / 3600.0)

if __name__ == '__main__':
    image = Image.open('zenit.jpg')
    exif_data = image._getexif()

    if exif_data != None and 34853 in exif_data:
        exif_data = exif_data[34853]
        lat = convert(exif_data[2])
        long = convert(exif_data[4])

        out = open('coord.txt', 'w')
        out.write("{0};{1}".format(lat, long))
        out.close()

        navig()
    else:
        print("This image doesn't have any geotags")