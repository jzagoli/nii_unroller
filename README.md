# NII unroller
You can use this simple script to "unroll" a NII dataset: the folder structure will be cloned, 
and all of the nii files will be replaced with a series of corresponding png images.
The script is written with a precise folder structure in mind, but you can modify the main or main_parallelized files easily to accomodate your needs.
## Usage
- Change the input and output paths as needed in main or main_parallelized
- Launch main.py or main_parallelized.py (the second one uses the multiprocessing library to speed up things)
