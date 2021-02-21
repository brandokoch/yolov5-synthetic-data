
import cv2
import matplotlib.pyplot as plt

image='rgb_2'
anno_file='data/detections_yolo/txt/rgb_2.txt'
image_file='data/synth_data/rgb/rgb_2.png'

IMG_WIDTH=933
IMG_HEIGHT=700

image=cv2.imread(image_file,cv2.COLOR_BGR2RGB)

bbs=[]
with open(anno_file,'r') as f:
    for line in f.readlines():
        line=line.strip()
        img_id,x,y,w,h=line.split(' ')
        print('written',img_id,x,y,w,h)
        bbs.append([x,y,w,h])


for bb in bbs:

    print(x,y)
    x=int((float(bb[0]))*IMG_WIDTH)
    y=int((float(bb[1]))*IMG_HEIGHT)
    cv2.circle(image, (x,y), radius=1, color=(255, 0, 0), thickness=10)

    #turn from yolo format x_center, y_center, w , h(0-1) 
    # to opecv format x_left,y_up, w ,h(0-int pixel_count)
    x=int((float(bb[0])-float(bb[2])/2)*IMG_WIDTH) #uppper left
    y=int((float(bb[1])-float(bb[3])/2)*IMG_HEIGHT) #upper left

    w=int(float(bb[2])*IMG_WIDTH)
    h=int(float(bb[3])*IMG_HEIGHT)

    print('transformed',x,y,w,h)
    color = (255, 0, 0)
    cv2.rectangle(image, (x, y), ((x + w), (y + h)), color, 2)

plt.imshow(image)
plt.show()