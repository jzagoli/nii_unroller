from nrrd_to_png import nrrd_to_png as unroll_nrrd
from pathlib import Path
import os
import ctypes


if __name__ == '__main__':

    # no screensaver
    # ctypes.windll.kernel32.SetThreadExecutionState(0x80000002)

    dataset_src = Path("C:/Users/user/cancer_imaging_archive/us")
    dataset_dst = Path("C:/Users/user/cancer_imaging_archive/preprocessed_for_training/us")
    
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
            # in this new folder we will unroll the prostate and segmentation nrrds
            for file in [f for f in files if f.startswith("US") or f.startswith("Prostate")]:
                nrrd = Path.joinpath(Path(path), Path(file))
                unroll_nrrd(nrrd, dst_folder, is_mask=(False if file.startswith("US") else True))
                count += 1
                print("\t{} was converted".format(file))
                
    # reset screensaver
    # ctypes.windll.kernel32.SetThreadExecutionState(0x80000000)
    
    print("{} nrrds was converted.".format(count))

