import harp
product ="E:KP_2020/Progress/OMNO2/raw/OMI-Aura_L2-OMNO2_2020m0101t0435-o82248_v003-2020m0610t191056.hdf"
test=harp.import_product(product, operations="tropospheric_NO2_column_number_density_validity>75; bin_spatial(101,-8,0.01,101,112,0.01); derive(latitude {latitude});derive(longitude {longitude}); exclude(latitude_bounds,longitude_bounds,latitude_bounds_weight,longitude_bounds_weight,count,weight)")
harp.export_product(test, "S5P_OFFL_L3__NO2____20200422T060756_20200422T074926_13079_01_010302_20200423T223719.nc", file_format='netcdf')
