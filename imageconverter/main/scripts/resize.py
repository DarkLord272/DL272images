from PIL import Image


def resize_image(input_path, output_path, left, top, right, bottom, wnsize, hnsize):
    im = Image.open(input_path)
    im1 = im.crop((int(left), int(top), int(right), int(bottom)))
    newsize = (int(wnsize), int(hnsize))
    im1 = im1.resize(newsize)

    im1.save(output_path, format='jpeg')
