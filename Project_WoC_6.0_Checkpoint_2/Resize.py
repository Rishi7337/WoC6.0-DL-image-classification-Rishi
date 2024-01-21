import cv2
import matplotlib.pyplot as plt
import os

def load_images_from_folder(folder):
    images=[]
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))#[...,::-1]
        if img is not None:
            images.append(img)
    return images

def resize_image(images):
    resized_images = []
    for img in images:
        resized_img = cv2.resize(img,(128,128),)
        resized_images.append(resized_img)
    return resized_images

def save_image(folder,img,file):
    file_path = folder+file
    #cv2.imwrite(file_path,img)
    cv2.imwrite(os.path.join(folder,file), img)#[...,::-1]


orig_images = load_images_from_folder('Dog_breeds\Poodles')
print(len(orig_images))
resi_images = resize_image(orig_images)
print(resi_images[2].shape)
plt.imshow(resi_images[43])
plt.show()

dirname='Dog_breeds\Poodles_res'
os.mkdir(dirname)


for i, img in enumerate(resi_images):
    save_image(dirname, img,str(i) + ".jpg")


#for img in resi_images:
#           cv2.imwrite(os.path.join(dirname, 'image.jpg'), img)
#img = cv2.imread(path)
#img = cv2.imread(path)[...,::-1]

#print(img.shape)
