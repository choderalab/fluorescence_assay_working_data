import json
import numpy as np
from glob import glob

inputs = {
    'xml_file_path' :  "../../data/spectra/",
    'file_set'      :  {'Src': glob("../../data/spectra/Src/2016-03-09/*.xml"),
                        'p38': glob("../../data/spectra/p38/2016-03-07/*.xml"),
                        'Abl': glob("../../data/spectra/Abl/2016-03-11/*.xml")},
    'ligand_order'  :  [None, None, None, 'Gefitinib'],
    'section'       :  'em280_Copy2',
    'wavelength'    :  '480',
    'Lstated'       :  np.array([1.9986e-05,9.139698767819545e-06,4.179630419617837e-06,1.911366106080368e-06,8.740773763932141e-07,3.9971999999999993e-07,1.8279397535639084e-07,8.359260839235672e-08,3.822732212160734e-08,1.7481547527864277e-08,7.994399999999995e-09, 0.0], np.float64), # ligand concentration
    'Pstated'       :  1.0e-6 * np.ones([12],np.float64), # protein concentration, M
    'assay_volume'  :  100e-6, # assay volume, L
    'well_area'     :  0.3969, # well area, cm^2 for 4ti-0203 [http://4ti.co.uk/files/3113/4217/2464/4ti-0201.pdf]
    }

inputs['Lstated'] = inputs['Lstated'].tolist()
inputs['Pstated'] = inputs['Pstated'].tolist()

with open('inputs.json', 'w') as fp:
    json.dump(inputs, fp)
