# My goal is to put the logo in its size or in random size in random position in the image
# and generate the yolo-friendly structure two new directories frist one is the document with logo on it and
# the second one is directory of text files with names exactly the same names of syntitized images , 
# each text file contains yolo-friendly structure

import os
from PIL import Image
import random


def make_index(logos):
    index2logo = {i:logo for i,logo in enumerate(logos)}
    logo2index = {logo:i for i,logo in enumerate(logos)}
    
    return index2logo, logo2index

def create_syntitized_img(image , logo, output_dir):
    #Open the two images
    background = Image.open(image)
    foreground = Image.open(logo)
    
    #Get the width and height of the foreground image
    foreground_width, foreground_height = foreground.size

    #Generate a random x and y position within the bounds of the background image
    max_width, max_height = background.size
    x = random.randint(0, max_width - foreground_width) 
    y = random.randint(0, max_height - foreground_height)
    
    #Resize the foreground image to a random size between 50% and 200% of its original size
    scale = random.uniform(0.25, 0.5)  
    foreground = foreground.resize((int(foreground_width * scale), int(foreground_height * scale)), Image.ANTIALIAS)

    foreground_width, foreground_height = foreground.size

    #Paste the resized foreground image onto the background image at the random position
    background.paste(foreground, (x, y))

    background.save(output_dir)

    ceneter_x = (x + foreground_width/2) / max_width
    ceneter_y = (y + foreground_height/2) / max_height

    foreground_width /= max_width
    foreground_height /= max_height

    return (ceneter_x, ceneter_y , foreground_width, foreground_height)


def save_syntitized_images(output_dir = 'train'):
    base_dir = '/media/mohamedalgebali/HDD/Courses/Projects/Object_detection/'

    images = os.listdir(os.path.join(base_dir, 'imgs')) #path to images
    logos = os.listdir(os.path.join(base_dir, 'logos')) #path to logos
    
    _, logo2index = make_index(logos)
    
    i = 0 #pointer to docs
    j = 0 #pointer to logos
    while i < len(images):

        if j == len(logos):
            j = 0

        img_path = os.path.join(base_dir, 'imgs', images[i])
        logo_path = os.path.join(base_dir, 'logos', logos[j])
        
        if not os.path.exists(f'./images/{output_dir}'):
            os.makedirs(f'./images/{output_dir}')
        
        if not os.path.exists(f'./labels/{output_dir}'):
            os.makedirs(f'./labels/{output_dir}')
        
        if not os.path.exists(f'./images/{output_dir}/{images[i]}'):

            #save syntitized image
            data = create_syntitized_img(img_path, logo_path, f'./images/{output_dir}/{images[i]}')

            #save annotations
            with open(f'./labels/{output_dir}/{images[i][:-3]}txt', 'w') as f:
                label = logo2index[logos[j]]
                ceneter_x, ceneter_y , foreground_width, foreground_height = data

                f.write('{} {} {} {} {}'.format(label, ceneter_x, ceneter_y , foreground_width, foreground_height))
            
            i += 1
            j += 1

        else:
            i += 1
            j += 1

save_syntitized_images(output_dir = 'train')
save_syntitized_images(output_dir = 'val')
save_syntitized_images(output_dir = 'test')

