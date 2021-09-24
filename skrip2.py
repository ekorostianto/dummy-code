import harp
product = 'D:/Data/Mei 2020/L3/CO/*.nc'
average = harp.import_product(product,post_operations="bin();squash(time,(latitude,longitude))")
export_folder = "D:/Data/Mei 2020/L3/CO/average"harp.export_product(test, export_folder, file_format='netcdf')