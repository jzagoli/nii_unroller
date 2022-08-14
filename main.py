from nii_to_png import nii_to_png as unroll_nii
from pathlib import Path
import os
import ctypes


if __name__ == '__main__':

    # no screensaver
    # ctypes.windll.kernel32.SetThreadExecutionState(0x80000002)

    dataset_src = Path("C:/Users/ML/Desktop/ProstatexJacopoNII")
    dataset_dst = Path("C:/Users/ML/Desktop/unrolled_ProstatexJacopoNII")
    
    count = 0
    for path, dirs, files in os.walk(dataset_src):
        # we reached te data folder
        if not dirs:
            # creation of the folder that will contain the images
            dst_folder = Path(path.replace(str(dataset_src), str(dataset_dst)))
            try:
                dst_folder.mkdir(parents=True)
                print(dst_folder)
            except OSError as e:
                raise e
            # in this new folder we will unroll the prostate and segmentation niis
            for file in [f for f in files if f.startswith("MRI") or f.startswith("Prostate")]:
                nii = Path(path) / Path(file)
                unroll_nii(nii, dst_folder)
                count += 1
                print(f"\t{file} was converted")
                
    # reset screensaver
    # ctypes.windll.kernel32.SetThreadExecutionState(0x80000000)
    
    print(f"{count} niis were converted.")

