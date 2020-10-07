from PIL import Image, ImageDraw, ImageFont
import textwrap
#Importing the modules
#Piil -> Pillow module for getting the image and adding font and saving it


def generate_meme(image_path, top_text, bottom_text='', font_path='\\font\\impact.ttf', font_size=9):
	""""Loading image , adding font , wraping text and saving the image """

	# load image
	im = Image.open(image_path)#getting the image object
	
	draw = ImageDraw.Draw(im)#Drawing Object
	image_width, image_height = im.size #im.size returns the tuple(width , height)
	
	# load font
	font = ImageFont.truetype(font=font_path, size=int(image_height*font_size)//100)#getting the font as .ttf
	
	# convert text to uppercase
	top_text = top_text.upper()
	bottom_text = bottom_text.upper()

	# text wrapping
	char_width, char_height = font.getsize('A')
	chars_per_line = image_width // char_width
	top_lines = textwrap.wrap(top_text, width=chars_per_line)
	bottom_lines = textwrap.wrap(bottom_text, width=chars_per_line)

	# draw top lines
	y = 10
	for line in top_lines:
	    line_width, line_height = font.getsize(line)
	    x = (image_width - line_width)/2
	    draw.text((x,y), line, fill='white', font=font)
	    y += line_height

	# draw bottom lines
	y = image_height - char_height * len(bottom_lines) - 15
	for line in bottom_lines:
	    line_width, line_height = font.getsize(line)
	    x = (image_width - line_width)/2
	    draw.text((x,y), line, fill='white', font=font)
	    y += line_height

	# save meme
	im.save('meme-' + im.filename.split('/')[-1])
	print("Imaged Saved Successfully")


if __name__ == '__main__':
	top_text = "I dont always make memes"
	bottom_text = "But when I do, I use Python"
	generate_meme('img.jpg', top_text=top_text, bottom_text=bottom_text)
