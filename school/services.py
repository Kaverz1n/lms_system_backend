from PIL import Image


def resize_image(img: Image, size: tuple) -> Image:
    '''
    Фунция изменяет размер на переданный, если размер
    переданого изображения не соответствует ему.
    :param img: объект класса Image
    :param size: кортеж состоящий из желаемой высоты и ширины
    картинки
    :return: объект класса Image
    '''
    try:
        if img.width != size[0] or img.height != size[1]:
            resized_image = img.resize(size)

            return resized_image

        return img
    except IndexError:
        print('Неверное указание размера изображения')
    except TypeError:
        print('Ошибка изменения размера изображения')
