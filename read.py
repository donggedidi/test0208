import yaml
with open("./data.yaml","r") as f:
    a=yaml.load(f,Loader=yaml.FullLoader)
    print(a)