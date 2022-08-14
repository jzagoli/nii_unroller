from nii_to_png import nii_to_png as unroll_nii
from pathlib import Path
import os
import multiprocessing
from multiprocessing import Pool

dataset_src = Path("C:/Users/ML/Desktop/ProstatexJacopoNII")
dataset_dst = Path("C:/Users/ML/Desktop/unrolled_ProstatexJacopoNII")


def gen_single(nii):
    niidir = nii.parent
    out = Path(str(niidir).replace(str(dataset_src), str(dataset_dst)))
    if not out.exists():
        os.makedirs(out)
    unroll_nii(nii, out)


if __name__ == '__main__':
    assert dataset_src.exists()
    niifiles = []
    for dirpath, _, files in os.walk(dataset_src):
        for f in files:
            if f.endswith(".nii") and (f.startswith("Prostate") or f.startswith("MRI")):
                niifiles.append(Path(dirpath) / f)
    with Pool(multiprocessing.cpu_count()) as pool:
        print("Processing...")
        pool.map(gen_single, niifiles)
        print("Done.")
