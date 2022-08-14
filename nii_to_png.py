import nibabel as nii
import numpy as np
from pathlib import Path
from PIL import Image


def nii_to_png(nii_path: Path, imgs_out_path: Path):
    # read nii file
    data = nii.load(nii_path).get_fdata()
    # rotate the image by 90 degrees so it is horizontal
    data = np.rot90(data, axes=(0, 1))
    # reading all the images in the nii, we want to iterate on the z (2) dimension
    for i in range(data.shape[2]):
        img = data[..., i]
        # saving the image
        name = Path(nii_path.stem + "_S" + str(i) + ".png")
        # image normalization
        img = (img / np.max(img)) * 255
        img = Image.fromarray(img.astype(np.uint8))
        img.save(imgs_out_path / name, optimize=True)


# ============================== FOR TESTING PURPOSES ONLY =====================================
if __name__ == '__main__':
    nii_to_png(Path("C:/Users/ML/Desktop/ProstatexJacopoNII/ProstateX-0004/MRI_ProstateX-0004.nii"),
               Path("C:/Users/ML/Desktop/unrolled_ProstatexJacopoNII"))
