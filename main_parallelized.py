from nrrd_to_png import nrrd_to_png as unroll_nrrd
from pathlib import Path
import os
import ctypes
import multiprocessing
from multiprocessing import Pool

dataset_src = Path("C:/Users/user/Desktop/dataset/mri")
assert dataset_src.exists()
dataset_dst = Path("C:/Users/user/Desktop/dataset_preprocessed/mri")

count = 0
nrrdfiles = []
for dirpath, subdirs, files in os.walk(dataset_src):
    for x in files:
        if x.endswith(".nrrd"):
            nrrdfiles.append(os.path.join(dirpath, x))


def gen_single(nrrd):
    file = str(nrrd).split("\\")[-1]
    dir = os.path.dirname(nrrd)
    out = Path(str(dataset_dst) + "\\" + str(dir.split("\\")[-2]) + "\\" + str(dir.split("\\")[-1]) + "\\")
    if not os.path.exists(dir):
        os.makedirs(dir)
    if not os.path.exists(out):
        os.makedirs(out)

    if file.startswith("MRI") or file.startswith("Prostate") or file.startswith("Target"):
        # nrrd = Path.joinpath(Path(dataset_src),Path(str(dst_folder).replace("preprocessed_for_training","")), Path(f))
        #print("DEBUG: ", nrrd)
        unroll_nrrd(Path(nrrd), out)#is_mask=(False if file.startswith("MRI") else True))
        # count += 1
        #print("\t{} was converted".format(file))


if __name__ == '__main__':
    with Pool(multiprocessing.cpu_count()) as pool:
        pool.map(gen_single, nrrdfiles)
        print("Done.")
