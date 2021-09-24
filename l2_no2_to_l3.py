from IPython import get_ipython
get_ipython().magic('reset -sf')

from glob import iglob
from os.path import join
# import harp
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
print (BASE_DIR)

#product_path = "E:\\KP_2020\\Progress\\sentinel5p\\OFFL_L2__AER_AIasd"
#input_files_OFFL = sorted(list(iglob(join(product_path, '**', '*OFFL*AER_AI*.nc'), recursive=True)))
#export_path="E:\\KP_2020\\Progress\\sentinel5p\\hasil\\AER_AI"
#for i in input_files_OFFL:
#    produk = harp.import_product(i, operations="absorbing_aerosol_index_validity>50; bin_spatial(101,-8,0.01,101,112,0.01); derive(latitude {latitude});derive(longitude {longitude}); exclude(latitude_bounds,longitude_bounds,latitude_bounds_weight,longitude_bounds_weight,count,weight)")
#    export_folder = "{export_path}/{name}".format(export_path=export_path, name=i.split('\\')[-1].replace('L2', 'L3'))
#    harp.export_product(produk, export_folder, file_format="netcdf")