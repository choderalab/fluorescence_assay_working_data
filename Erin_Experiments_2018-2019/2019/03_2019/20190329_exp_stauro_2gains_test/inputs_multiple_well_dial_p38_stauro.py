import json
import numpy as np
from glob import glob


ligand_conc = [2.000e-05, 1.320e-05, 8.660e-06, 5.700e-06, 3.750e-06, 2.470e-06, 1.620e-06,
1.0700e-06, 7.02e-07, 4.62e-07, 3.04e-07, 2.00e-07]

xml_files = ['../infinite_results/p38_Sta_ab_gain75_20190329_105335.xml']

inputs = {
    'xml_files'     :  xml_files,
    'file_set'      :  {'p38': xml_files},
    'protein_wells'  :  {'p38': ['A1']},
    'ligand_order'  :  ['Staurosporine'],
    'buffer_wells'   :  {'p38': ['B1']},
    'section'       :  'ex296_scan_top_gain75',
    'wavelength'    :  '380',
    'Lstated'       :  np.array(ligand_conc, np.float64), # ligand concentration
    'Pstated'       :  0.5e-6 * np.ones([12],np.float64), # protein concentration, M
    'assay_volume'  :  100e-6, # assay volume, L
    'well_area'     :  0.3969, # well area, cm^2 for 4ti-0203 [http://4ti.co.uk/files/3113/4217/2464/4ti-0201.pdf]
    }

inputs['Lstated'] = inputs['Lstated'].tolist()
inputs['Pstated'] = inputs['Pstated'].tolist()

with open('inputs.json', 'w') as fp:
    json.dump(inputs, fp)
