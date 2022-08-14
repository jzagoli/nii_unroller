import nrrd
import numpy as np
from pathlib import Path
from PIL import Image


def nrrd_to_png(nrrd_path: Path, imgs_out_path: Path):
    # read nrrd file
    data, _ = nrrd.read(str(nrrd_path))
    # rotate the image by 90 degrees so it is horizontal
    data = np.rot90(data, axes=(0, 1))
    # reading all the images in the nrrd, we want to iterate on the z (2) dimension
    for i in range(0, data.shape[2]):
        img = data[:, :, i]
        # saving the image
        name = Path(nrrd_path.stem + "_S" + str(i) + ".png")
        # image normalization
        img = (img / np.max(img)) * 255
        img = Image.fromarray(img.astype(np.uint8))
        img.save(Path.joinpath(imgs_out_path, name), optimize=True)


# ============================== FOR TESTING PURPOSES ONLY =====================================#
# if __name__ == '__main__':
#     nrrd_to_png(Path(r"C:\Users\user\ "
#                      r"Dataset\cancer_imaging_archive\us\paziente10\Dato1\Prostate_1.3.6.1.4.1.14519.5.2.1"
#                      r".223540088060091256676039744747833703676.nrrd"),
#                 Path(r"C:\Users\user\Desktop\tmp"),
#                 True)
