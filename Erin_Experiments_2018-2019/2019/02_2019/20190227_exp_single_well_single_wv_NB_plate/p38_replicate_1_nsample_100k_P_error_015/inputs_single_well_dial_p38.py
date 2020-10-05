import json
import numpy as np
from glob import glob

xml_files = ['../infinite_results/p38_Abl_GK_WT_Src_conc_0_20190227_111938.xml',
            '../infinite_results/p38_Abl_GK_WT_Src_conc_1_20190227_113051.xml',
            '../infinite_results/p38_Abl_GK_WT_Src_conc_2_20190227_114049.xml',
            '../infinite_results/p38_Abl_GK_WT_Src_conc_3_20190227_115045.xml',
            '../infinite_results/p38_Abl_GK_WT_Src_conc_4_20190227_120042.xml',
            '../infinite_results/p38_Abl_GK_WT_Src_conc_5_20190227_121038.xml',
            '../infinite_results/p38_Abl_GK_WT_Src_conc_6_20190227_122034.xml',
            '../infinite_results/p38_Abl_GK_WT_Src_conc_7_20190227_123026.xml',
            '../infinite_results/p38_Abl_GK_WT_Src_conc_8_20190227_124021.xml',
            '../infinite_results/p38_Abl_GK_WT_Src_conc_9_20190227_125019.xml',
            '../infinite_results/p38_Abl_GK_WT_Src_conc_10_20190227_130011.xml',
            '../infinite_results/p38_Abl_GK_WT_Src_conc_11_20190227_131004.xml',
            '../infinite_results/p38_Abl_GK_WT_Src_conc_12_20190227_131956.xml',
            '../infinite_results/p38_Abl_GK_WT_Src_conc_13_20190227_132952.xml',
            '../infinite_results/p38_Abl_GK_WT_Src_conc_14_20190227_133951.xml',
            '../infinite_results/p38_Abl_GK_WT_Src_conc_15_20190227_134945.xml',
            '../infinite_results/p38_Abl_GK_WT_Src_conc_16_20190227_135943.xml']

ligand_conc = [  0.00000000e+00,   8.00000000e-09,   1.34778097e-08,
         2.27064194e-08,   3.82541000e-08,   6.44476851e-08,
         1.08576705e-07,   1.82922021e-07,   3.08173524e-07,
         5.19188015e-07,   8.74689659e-07,   1.47361260e-06, 2.48263378e-06,
         4.18255821e-06, 7.04646547e-06, 1.118713651e-05, 2.0e-05]

inputs = {
    'single_well'   :  True,
    'xml_files'     :  xml_files,
    'file_set'      :  {'p38': xml_files},
    'protein_wells'  :  {'p38': ['A2', 'C2', 'E2', 'G2']},
    'ligand_order'  :  ['Bosutinib', 'Bosutinib Isomer', 'Erlotinib', 'Gefitinib'],
    'buffer_wells'   :  {'p38': ['B2', 'D2', 'F2', 'H2']},
    'section'       :  'ex280_em480_top_gain100',
    'wavelength'    :  '480',
    'Lstated'       :  np.array(ligand_conc, np.float64), # ligand concentration
    'Pstated'       :  0.5e-6 * np.ones([17],np.float64), # protein concentration, M
    'P_error'       :  0.15, # coefficient of protein concentration uncertainity (0.15 for 15% error)
    'assay_volume'  :  100e-6, # assay volume, L
    'well_area'     :  0.3969, # well area, cm^2 for 4ti-0203 [http://4ti.co.uk/files/3113/4217/2464/4ti-0201.pdf]
    }

inputs['Lstated'] = inputs['Lstated'].tolist()
inputs['Pstated'] = inputs['Pstated'].tolist()

with open('inputs.json', 'w') as fp:
    json.dump(inputs, fp)
