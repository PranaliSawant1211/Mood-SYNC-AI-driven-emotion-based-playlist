# import os
# import glob
# import pandas as pd
# import xml.etree.ElementTree as ET


# def xml_to_csv():
#     xml_list = []
#     for xml_file in glob.glob('/*.xml'):
#         print(xml_file)
#         tree = ET.parse(xml_file)
#         root = tree.getroot()
#         for member in root.findall('object'):
#             value = (root.find('filename').text,
#                      int(root.find('size')[0].text),
#                      int(root.find('size')[1].text),
#                      )
#                      #             member[0].text,
#                      # int(member[4][0].text),
#                      # int(member[4][1].text),
#                      # int(member[4][2].text),
#                      # int(member[4][3].text)
#             # member[0].text
#             xml_list.append(value)
#     column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
#     xml_df = pd.DataFrame(xml_list, columns=column_name)
#     #print(xml_list[0])

#     return xml_df


# def main():
#     for folder in ['train','test']:
#         image_path = os.path.join(os.getcwd(), ('images/' + folder))
#         xml_df = xml_to_csv()
#         xml_df.to_csv(('images/' + folder + '_labels.csv'), index=None)
#         print('Successfully converted xml to csv.')

# main()




# import os
# import glob
# import pandas as pd
# import xml.etree.ElementTree as ET


# def xml_to_csv(path):
#     xml_list = []
#     for xml_file in glob.glob(path + '/*.xml'):
#         print(xml_file)
#         tree = ET.parse(xml_file)
#         root = tree.getroot()
#         for member in root.findall('object'):
#             value = (root.find('filename').text,
#                      int(root.find('size')[0].text),
#                      int(root.find('size')[1].text),
#                      member[0].text,
#                      int(member[4][0].text),
#                      int(member[4][1].text),
#                      int(member[4][2].text),
#                      int(member[4][3].text)
#                      )
#             xml_list.append(value)
#     column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
#     xml_df = pd.DataFrame(xml_list, columns=column_name)
#     return xml_df


# def main():
#     for folder in ['train','test']:
#         image_path = os.path.join(os.getcwd(), ('images/' + folder))
#         xml_df = xml_to_csv(image_path)
#         xml_df.to_csv(('images/' + folder + '_labels.csv'), index=None)
#         print('Successfully converted xml to csv.')


# main()



import os
import glob
import pandas as pd
import cv2
# import xml.etree.ElementTree as ET


def xml_to_csv():
    xml_list = []
    for picture in glob.glob('dataset/sajida/*.jpg'):
        print(picture)
        image = cv2.imread(picture)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        x = faces[0][0]
        y = faces[0][1]
        w = faces[0][2]
        h = faces[0][3]
        # cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 1)
        roi_gray = gray[y:y + h, x:x + w]
        roi_gray = cv2.resize(roi_gray, (48, 48))
        lin_img = roi_gray.flatten()
        pixel_list = lin_img.tolist()
        pixel_str_list = map(str, pixel_list)
        img_str = ' '.join(pixel_str_list)
        # roi_gray = cv2.resize(roi_gray, (48, 48))
        value = ('4',
                 img_str,
                 'Training')
        xml_list.append(value)
    column_name = ['emotion', 'pixels', 'Usage']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df


def main():
    xml_df = xml_to_csv()
    xml_df.to_csv(('labels.csv'), index=None)
    print('Successfully converted xml to csv.')


main()