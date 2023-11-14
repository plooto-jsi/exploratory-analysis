# download data

# define files to download
files = [
    'http://test.server.com/data/dataset1.zip',
    'http://test.server.com/data/dataset2.zip'
]

targets = [
    '../../data/interim/dataset1.zip',
    '../../data/interim/dataset2.zip',
]

raw_targets = [
    '../../data/raw/dataset1',
    '../../data/raw/dataset2',
]

# imports
import requests, zipfile, io, sys

def download_url(url, save_path, chunk_size=256 * 1024):
    """
    Downloading an URL do disk in 256kB chunks.
    """
    print("Starting download", url)
    r = requests.get(url, stream=True)
    with open(save_path, 'wb') as fd:
        for chunk in r.iter_content(chunk_size=chunk_size):
            sys.stdout.write('.')
            sys.stdout.flush()
            fd.write(chunk)
    print(" Finished.\n")


# download files
print("### DOWNLOADING TO INTERIM FOLDER ###")
for i in range(len(targets)):
    download_url(files[i], targets[i])

# unzipping
print("### UNZIPPING TO RAW FOLDER ###")
for i in range(len(targets)):
    with zipfile.ZipFile(targets[i], 'r') as zip_ref:
        print("Starting to unzip into", raw_targets[i])
        zip_ref.extractall(raw_targets[i])