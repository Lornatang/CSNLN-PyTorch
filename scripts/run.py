import os

# Prepare dataset
os.system("python ./prepare_dataset.py --images_dir ../data/DIV2K/original/train --output_dir ../data/DIV2K/CSNLN/train --image_size 224 --step 112 --num_workers 10")
os.system("python ./prepare_dataset.py --images_dir ../data/DIV2K/original/valid --output_dir ../data/DIV2K/CSNLN/valid --image_size 224 --step 224 --num_workers 10")
