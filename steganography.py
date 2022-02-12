from PIL import Image
import PIL 
import sys

def hide_file(cover_file_path, secret_file_path, output_file_path):
    cover_file_image = Image.open(cover_file_path).convert('L') # convert to greyscale
    secret_file = open(secret_file_path, 'rb').read() # a list of bytes
    output_file = PIL.Image.new(mode="L", size=(cover_file_image.width, cover_file_image.height))

    for x in range(cover_file_image.width):
        for y in range(cover_file_image.height):
            pass


def retrieve_secret(file_with_secret_path, output_file_path):
    pass


if __name__ == '__main__':
    if len(sys.argv) != 5 or len(sys.argv) != 4:
        print("usage: steganography embed cover_file secret_file output_file_path")
        print("       steganography extract file_with_secret output_file_path")
        exit()

    if sys.argv[1] == 'embed':
        cover_file_path = sys.argv[2]
        secret_file_path = sys.argv[3]
        output_file_path = sys.argv[4]
        output_file = hide_file(cover_file_path, secret_file_path, output_file_path)
        output_file.show()
    elif sys.argv[1] == 'extract':
        file_with_secret = sys.argv[2]
        output_file = sys.argv[3]
        retrieve_secret(file_with_secret, output_file)