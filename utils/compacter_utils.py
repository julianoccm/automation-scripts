import os
import zipfile
from tqdm import tqdm

def zip_directory(filename, target_dir):   
    total_files = sum(len(files) for _, _, files in os.walk(target_dir))
    
    zipobj = zipfile.ZipFile(filename + '.zip', 'w', zipfile.ZIP_DEFLATED)
    rootlen = len(target_dir) + 1

    with tqdm(total=total_files, desc="Processing files ") as pbar:
        for base, dirs, files in os.walk(target_dir):
            for file in files:
                fn = os.path.join(base, file)
                zipobj.write(fn, fn[rootlen:])
                # Update progress bar
                pbar.update(1)