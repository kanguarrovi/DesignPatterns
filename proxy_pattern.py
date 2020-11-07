# https://www.tutorialspoint.com/design_pattern/proxy_pattern.htm

class Image:

    def display(self):
        pass


class RealImage(Image):

    def __init__(self, file_name):
        self.file_name = file_name
        self.__load_from_disk(file_name)

    def display(self):
        print("Displaying: {}".format(self.file_name))

    def __str__(self):
        return "Displaying: {}".format(self.file_name)

    @staticmethod
    def __load_from_disk(file_name):
        print("Loading: {}".format(file_name))


class ProxyImage(Image):

    def __init__(self, file_name):
        self.real_image = None
        self.file_name = file_name

    def display(self):
        if not self.real_image:
            self.real_image = RealImage(self.file_name)
        self.real_image.display()

    def __str__(self):
        if not self.real_image:
            self.real_image = RealImage(self.file_name)
        return self.real_image.__str__()


if __name__ == "__main__":
    image = ProxyImage("test_10mb.jpg")
    # image will be loaded from disk
    # image.display()
    print(image)
    # image will not be loaded from disk
    # image.display()
    print(image)

