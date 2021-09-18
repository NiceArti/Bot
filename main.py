from Bot.ImageBot import ImageBot


if __name__ == '__main__':
    b = ImageBot()

    b.set_image_path(234)
    print(b.get_image_path())
