import os,sys


sys.path.append(os.getcwd())
import yaml


def base_analyse(filename,data_key):
    file="."+os.sep+"data"+os.sep+filename
    with open(file,"r") as f:
        data=yaml.load(f,Loader=yaml.FullLoader)
        arrs=[]
        for i in data[data_key].values():
            # print(i)
            arrs.append(i)
        return arrs

if __name__ == '__main__':
    data=base_analyse("new_msg.yaml","test_new_msg")
    print(data)