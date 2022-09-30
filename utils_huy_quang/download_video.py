import os
import gdown

download_dict = {"lp_id": "1WnER0kV_W4TKjlRif795OPL3fod-nGYl"}

for value in download_dict.values():
    gdown.download(id=value, output=os.getcwd())
