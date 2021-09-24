from IPython import get_ipython
get_ipython().magic('reset -sf')

from glob import iglob
from os.path import join
import harp

product_path = "~/kp/l3/no2_januari_april_qa75/januari"
input_files_OFFL = sorted(list(iglob(join(product_path, '**', '*.hdf'), recursive=True)))
export_path="/~/kp/l3/rata2_bulan"
for i in input_files_OFFL:
    produk = harp.import_product(i, post_operations="bin();squash(time,(latitude,longitude))")
    export_folder = "{export_path}/{name}".format(export_path=export_path, name=i.split('\\')[-1])
    harp.export_product(produk, export_folder, file_format="netcdf")