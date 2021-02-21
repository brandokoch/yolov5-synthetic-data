import os
import shutil 

os.makedirs('data/synth_dataset/images/train')
os.makedirs('data/synth_dataset/images/val')
os.makedirs('data/synth_dataset/labels/train')
os.makedirs('data/synth_dataset/labels/val')

threshold_for_split=800

anno_source='data/detections_yolo/txt/'
img_source='data/synth_data/rgb/'

img_train_dst='data/synth_dataset/images/train/'
img_val_dst='data/synth_dataset/images/val/'
anno_train_dst='data/synth_dataset/labels/train/'
anno_val_dst='data/synth_dataset/labels/val/'

anno_file_names=os.listdir(anno_source)
img_file_names=os.listdir(img_source)

for file_name in anno_file_names:
    anno_id=int(file_name.split('.')[0].split('_')[-1])
    if anno_id<=threshold_for_split:
        src_file=anno_source+file_name
        dst_file=anno_train_dst+file_name
        shutil.copy(src_file,dst_file)
    else:
        src_file=anno_source+file_name
        dst_file=anno_val_dst+file_name
        shutil.copy(src_file,dst_file)


for file_name in img_file_names:
    img_id=int(file_name.split('.')[0].split('_')[-1])
    if img_id<=threshold_for_split:
        src_file=img_source+file_name
        dst_file=img_train_dst+file_name
        shutil.copy(src_file,dst_file)
    else:
        src_file=img_source+file_name
        dst_file=img_val_dst+file_name
        shutil.copy(src_file,dst_file)