from PIL import Image
import os

print('*** Image Compressor ***')

images_path = input('Введите абсолютный путь к директории с изображениями: ')

if not os.path.isdir(images_path):
    print('Указанного пути не существует.')
    quit()

images_names = os.listdir(images_path)
images_count = len(images_names)

print('Выбранный путь: ' + images_path)

thumbnail_width = input(
    'Введите максимальную ширину к которой нужно привести все изображения (0 если сохранить оригинальные размеры): ')

if not thumbnail_width.isdigit():
    print('Ширина должна быть числом')
    quit()

thumbnail_height = input(
    'Введите максимальную высоту к которой нужно привести все изображения (0 если сохранить оригинальные размеры): ')

if not thumbnail_height.isdigit():
    print('Высота должна быть числом')
    quit()

save_quality = input('Введите качество (от 0 до 100): ')

if not save_quality.isdigit():
    print('Качество должно быть числом')
    quit()

print('Начинаю работать...')

i = 1
for image_name in images_names:
    if not os.path.isdir(images_path + '/image_compressor/'):
        os.mkdir(images_path + '/image_compressor/')

    try:
        if thumbnail_height == str(0) or thumbnail_width == str(0):
            image = Image.open(images_path + '/' + image_name)
            image.save(images_path + '/image_compressor/' + image_name, quality=int(save_quality), optimize=True)

            print(str(i) + '/' + str(images_count))
            i = i + 1
            continue

        image = Image.open(images_path + '/' + image_name)
        image.thumbnail(size=(int(thumbnail_width), int(thumbnail_height)))
        image.convert('RGB')
        image.save(images_path + '/image_compressor/' + image_name)

        print(str(i) + '/' + str(images_count))
        i = i + 1
    except:
        print('Файл ' + image_name + ' не является изображением или введены недопустимые параметры')

print('Обработка завершена. Обработанные изображения находятся в директории image_compressor в папке с фотографиями')
