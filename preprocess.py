import numpy as np
import os
import pydicom as dicom
from skimage.transform import resize
from skimage.color import gray2rgb


def read_dicom(dicom_path):
    dicom_file =  dicom.read_file(dicom_path)
    pixel_data = list()

    for record in dicom_file.DirectoryRecordSequence:
        if record.DirectoryRecordType == "IMAGE":
        # Extract the relative path to the DICOM file
            dir_path = os.path.dirname(dicom_path)
            path = f'{dir_path}/{os.path.join(*record.ReferencedFileID)}'
            dcm = dicom.read_file(path)

            # Now get your image data
            pixel_data.append(dcm.pixel_array)
    return np.array(pixel_data)

def preprocess(dicom_path: str):
    image = read_dicom(f'{dicom_path}/DICOMDIR').astype(float)[0]

    # Rescaling grey scale between 0-255
    image_2d_scaled = (np.maximum(image,0) / image.max()) * 255.0

    # Convert to uint
    image_2d_scaled = np.uint8(image_2d_scaled)

    print(f'image starts in shape {image_2d_scaled.shape}')


    image_2d_scaled = resize(image_2d_scaled, (224, 224))

    image_2d_scaled = gray2rgb(image_2d_scaled)

    print(f'image is shape {image_2d_scaled.shape}')

    image_2d_scaled = np.expand_dims(image_2d_scaled, axis=0)

    return image_2d_scaled