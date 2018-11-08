# 遍历指定目录下的所有文件及子目录

import os


def ftree(path):
    l = os.listdir(path)
    tree = []
    for f in l:
        np = os.path.join(path, f)
        if os.path.isdir(np):
            tree.append(ftree(np))
        else:
            tree.append(f)
    return tree


path = '/home/prime/Pictures'
print(ftree(path))