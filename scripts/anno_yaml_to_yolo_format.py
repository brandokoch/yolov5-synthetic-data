import os
import json
import pprint

anno_files_pth='data/synth_data/txt/'
formated_anno_output_pth='data/detections_yolo/txt/'
os.makedirs(formated_anno_output_pth, exist_ok=True)

IMG_WIDTH=933
IMG_HEIGHT=700

for file_name in os.listdir(anno_files_pth):

    # Check if file contains object detections
    if(file_name[:8]=='captures'):
        file_pth=anno_files_pth+file_name
        print(file_pth)

        # Open json src file
        with open(file_pth) as f:
            data=json.load(f)
            
            # Iterate through images
            for image in data['captures']:
                img_name=image['filename'].split('/')[-1]
                print(img_name)

                # Open file to store annotations for image
                with open(formated_anno_output_pth+img_name.split('.')[0]+'.txt','w') as f:

                    # with open()
                    for annotation in image['annotations'][0]['values']:
                        label_id=annotation['label_id'] -1 #Must start from 0
                        label_name=annotation['label_name']

                        #unity format
                        width=annotation['width']
                        height=annotation['height']
                        x=annotation['x']
                        y=annotation['y']

                        #yolo format
                        x_center=x+(width/2) 
                        y_center=y+(height/2)
                        x_center_norm=x_center/IMG_WIDTH
                        y_center_norm=y_center/IMG_HEIGHT
                        width_norm=width/IMG_WIDTH
                        height_norm=height/IMG_HEIGHT


                        f.write(f"{label_id} {x_center_norm:.6f} {y_center_norm:.6f} {width_norm:.6f} {height_norm:.6f}\n")
