import os
import xml.etree.ElementTree as ET
import argparse

def convert_voc_to_yolo(input_dir, output_dir, person_class_id=0):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    annotations_dir = os.path.join(input_dir, "annotations")
    images_dir = os.path.join(input_dir, "images")

    for xml_file in os.listdir(annotations_dir):
        if xml_file.endswith(".xml"):
            tree = ET.parse(os.path.join(annotations_dir, xml_file))
            root = tree.getroot()

            image_file = root.find('filename').text
            img_width = int(root.find('size/width').text)
            img_height = int(root.find('size/height').text)

            yolo_annotations = []

            for obj in root.findall('object'):
                class_name = obj.find('name').text

                # Only process 'person' class
                if class_name != "person":
                    continue

                bbox = obj.find('bndbox')
                xmin = int(bbox.find('xmin').text)
                ymin = int(bbox.find('ymin').text)
                xmax = int(bbox.find('xmax').text)
                ymax = int(bbox.find('ymax').text)

                x_center = (xmin + xmax) / 2.0 / img_width
                y_center = (ymin + ymax) / 2.0 / img_height
                bbox_width = (xmax - xmin) / float(img_width)
                bbox_height = (ymax - ymin) / float(img_height)

                yolo_annotations.append(f"{person_class_id} {x_center:.6f} {y_center:.6f} {bbox_width:.6f} {bbox_height:.6f}")

            # Save the YOLO formatted annotations
            if yolo_annotations:
                output_file = os.path.join(output_dir, xml_file.replace('.xml', '.txt'))
                with open(output_file, "w") as f:
                    f.write("\n".join(yolo_annotations))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert PascalVOC annotations to YOLO format for person detection")
    parser.add_argument("input_directory", type=str, help="Path to input directory containing PascalVOC annotations and images")
    parser.add_argument("output_directory", type=str, help="Path to output directory for YOLO format annotations")

    args = parser.parse_args()
    
    convert_voc_to_yolo(args.input_directory, args.output_directory)
