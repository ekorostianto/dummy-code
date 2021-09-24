from IPython import get_ipython
get_ipython().magic('reset -sf')

from glob import iglob
from os.path import join
import harp

product_path = "E:\\KP_2020\\Progress\\sentinel5p\\raw\\februari_2020\\"
input_files_OFFL = sorted(list(iglob(join(product_path, '**', '*OFFL*NO2*.nc'), recursive=True)))
export_path="E:\\KP_2020\\Progress\\sentinel5p\\hasil\\no2_februari_2020"
for i in input_files_OFFL:
    produk = harp.import_product(i, operations="tropospheric_NO2_column_number_density_validity>75; bin_spatial(101,-8,0.01,101,112,0.01); derive(latitude {latitude});derive(longitude {longitude}); exclude(latitude_bounds,longitude_bounds,latitude_bounds_weight,longitude_bounds_weight,count,weight)")
    export_folder = "{export_path}/{name}".format(export_path=export_path, name=i.split('\\')[-1].replace('L2', 'L3'))
    harp.export_product(produk, export_folder, file_format="netcdf")