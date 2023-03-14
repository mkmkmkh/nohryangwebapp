from PIL import Image

# open the image
image = Image.open("mega.jpg")
width, height = image.size
new_size = (int(width * 0.8), int(height * 0.8))
resized_image = image.resize(new_size)
resized_image.save("mega.jpg")

image = Image.open("smart.jpg")
resized_image = image.resize(new_size)
resized_image.save("smart.jpg")

image = Image.open("real.jpg")
resized_image = image.resize(new_size)
resized_image.save("real.jpg")

image = Image.open("real_1.jpg")
resized_image = image.resize(new_size)
resized_image.save("real_1.jpg")
