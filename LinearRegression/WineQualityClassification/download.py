import urllib.request
import os
def download(root_dir):
    if not os.path.exists(root_dir):
        os.mkdir(root_dir)
    classification_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/"
    classification_namefiles = ["winequality-red.csv", "winequality-white.csv", "winequality.names"]
    for k in range(len(classification_namefiles)):
        path_dir = os.path.join(root_dir, classification_namefiles[k])
        file_url = classification_url + classification_namefiles[k]
        if not os.path.exists(path_dir):
            urllib.request.urlretrieve(file_url, path_dir)
            print(path_dir + " downloaded!")
        else:
            print(path_dir + " has downloaded!")
if __name__ == '__main__':
    root_dir = "data"
    download(root_dir)