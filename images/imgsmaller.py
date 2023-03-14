from PIL import Image

# open the image
image = Image.open("mainview.jpg")

# resize the image to 50% of its original size
width, height = image.size
new_size = (width // 2, height // 2)
resized_image = image.resize(new_size)

# save the resized image to a file
resized_image.save("mainview_half.jpg")
