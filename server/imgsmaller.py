from PIL import Image

# open the image
image = Image.open("smart.jpg")

# resize the image to 50% of its original size
width, height = image.size
new_size = (width // 4, height // 4)
resized_image = image.resize(new_size)

# save the resized image to a file
resized_image.save("smart.jpg")
