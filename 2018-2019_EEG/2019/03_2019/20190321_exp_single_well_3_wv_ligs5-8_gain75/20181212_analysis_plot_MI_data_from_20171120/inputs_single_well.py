import json
import numpy as np
from glob import glob

xml_files = ['infinite_results/EEG_single_well_conc_0_20181107_110725.xml',
            'infinite_results/EEG_single_well_conc_1_20181107_112420.xml',
            'infinite_results/EEG_single_well_conc_2_20181107_113940.xml',
            'infinite_results/EEG_single_well_conc_3_20181107_115458.xml',
            'infinite_results/EEG_single_well_conc_4_20181107_121019.xml',
            'infinite_results/EEG_single_well_conc_5_20181107_122542.xml',
            'infinite_results/EEG_single_well_conc_6_20181107_124104.xml',
            'infinite_results/EEG_single_well_conc_7_20181107_125627.xml',
            'infinite_results/EEG_single_well_conc_8_20181107_131149.xml',
            'infinite_results/EEG_single_well_conc_9_20181107_132712.xml',
            'infinite_results/EEG_single_well_conc_10_20181107_134234.xml',
            'infinite_results/EEG_single_well_conc_11_20181107_135800.xml',
            'infinite_results/EEG_single_well_conc_12_20181107_141326.xml',
            'infinite_results/EEG_single_well_conc_13_20181107_142852.xml',
            'infinite_results/EEG_single_well_conc_14_20181107_144418.xml',
            'infinite_results/EEG_single_well_conc_15_20181107_145942.xml',
            'infinite_results/EEG_single_well_conc_16_20181107_151507.xml']

ligand_conc = [  0.00000000e+00,   8.00000000e-09,   1.34778097e-08,
         2.27064194e-08,   3.82541000e-08,   6.44476851e-08,
         1.08576705e-07,   1.82922021e-07,   3.08173524e-07,
         5.19188015e-07,   8.74689659e-07,   1.47361260e-06, 2.48263378e-06,
         4.18255821e-06, 7.04646547e-06, 1.118713651e-05, 2.0e-05]

inputs = {
    'single_well'   :  True,
    'xml_files'     :  xml_files,
    'file_set'      :  {'Src GK': xml_files},
    'protein_wells'  :  {'Src GK': ['B10', 'B11', 'B12']},
    'ligand_order'  :  ['Bosutinib', 'Bosutinib', 'Bosutinib'],
    'buffer_wells'   :  {'Src GK': ['A2', 'A3', 'A4']},
    'section'       :  'ex280_scan_top_gain100',
    'wavelength'    :  '480',
    'Lstated'       :  np.array(ligand_conc, np.float64), # ligand concentration
    'Pstated'       :  1.0e-6 * np.ones([17],np.float64), # protein concentration, M
    'assay_volume'  :  100e-6, # assay volume, L
    'well_area'     :  0.3969, # well area, cm^2 for 4ti-0203 [http://4ti.co.uk/files/3113/4217/2464/4ti-0201.pdf]
    }

inputs['Lstated'] = inputs['Lstated'].tolist()
inputs['Pstated'] = inputs['Pstated'].tolist()

with open('inputs.json', 'w') as fp:
    json.dump(inputs, fp)
