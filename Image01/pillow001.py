import sys
import PIL.Image

def main():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <image_file>")
        sys.exit(-1)

    image_file = sys.argv[1]

    img = PIL.Image.open(image_file)
    size = img.size

    img = img.convert("RGB")

    r,g,b = img.split()

    blank = PIL.Image.new('L', size, 0)
    img_red = PIL.Image.merge("RGB", (r, blank, blank))
    img_red.show(title="Red-only")

    blank = PIL.Image.new('L', size, 0)
    img_green = PIL.Image.merge("RGB", (blank, g, blank))
    img_green.show(title="Green-only")

    blank = PIL.Image.new('L', size, 0)
    img_blue = PIL.Image.merge("RGB", (blank, blank, b))
    img_blue.show(title="Blue-only")


if __name__ == "__main__":
    main()