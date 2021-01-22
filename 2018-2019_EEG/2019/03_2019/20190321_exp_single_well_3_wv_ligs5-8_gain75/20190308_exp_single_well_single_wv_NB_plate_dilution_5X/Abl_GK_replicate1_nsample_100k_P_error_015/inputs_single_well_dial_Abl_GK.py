import json
import numpy as np
from glob import glob

xml_files = ['../infinite_results/p38_Abl_WT_GK_Src_WT_GK_conc_0_20190308_112925.xml',
             '../infinite_results/p38_Abl_WT_GK_Src_WT_GK_conc_1_20190308_114040.xml',
             '../infinite_results/p38_Abl_WT_GK_Src_WT_GK_conc_2_20190308_115034.xml',
             '../infinite_results/p38_Abl_WT_GK_Src_WT_GK_conc_3_20190308_120028.xml',
             '../infinite_results/p38_Abl_WT_GK_Src_WT_GK_conc_4_20190308_121025.xml',
             '../infinite_results/p38_Abl_WT_GK_Src_WT_GK_conc_5_20190308_122018.xml',
             '../infinite_results/p38_Abl_WT_GK_Src_WT_GK_conc_6_20190308_123014.xml',
             '../infinite_results/p38_Abl_WT_GK_Src_WT_GK_conc_7_20190308_124006.xml',
             '../infinite_results/p38_Abl_WT_GK_Src_WT_GK_conc_8_20190308_125003.xml',
             '../infinite_results/p38_Abl_WT_GK_Src_WT_GK_conc_9_20190308_125956.xml',
             '../infinite_results/p38_Abl_WT_GK_Src_WT_GK_conc_10_20190308_130948.xml',
             '../infinite_results/p38_Abl_WT_GK_Src_WT_GK_conc_11_20190308_131941.xml',
             '../infinite_results/p38_Abl_WT_GK_Src_WT_GK_conc_12_20190308_132933.xml',
             '../infinite_results/p38_Abl_WT_GK_Src_WT_GK_conc_13_20190308_133926.xml',
             '../infinite_results/p38_Abl_WT_GK_Src_WT_GK_conc_14_20190308_134924.xml',
             '../infinite_results/p38_Abl_WT_GK_Src_WT_GK_conc_15_20190308_135924.xml',
             '../infinite_results/p38_Abl_WT_GK_Src_WT_GK_conc_16_20190308_140921.xml']

ligand_conc = [  0.00000000e+00,   8.00000000e-09,   1.34778097e-08,
         2.27064194e-08,   3.82541000e-08,   6.44476851e-08,
         1.08576705e-07,   1.82922021e-07,   3.08173524e-07,
         5.19188015e-07,   8.74689659e-07,   1.47361260e-06, 2.48263378e-06,
         4.18255821e-06, 7.04646547e-06, 1.118713651e-05, 2.0e-05]

inputs = {
    'single_well'   :  True,
    'xml_files'     :  xml_files,
    'file_set'      :  {'Abl_GK': xml_files},
    'protein_wells'  :  {'Abl_GK': ['B4', 'D4', 'F4', 'H4']},
    'ligand_order'  :  ['Bosutinib', 'Bosutinib Isomer', 'Erlotinib', 'Gefitinib'],
    'buffer_wells'   :  {'Abl_GK': ['A2', 'C2', 'E2', 'G2']},
    'section'       :  'ex280_em480_top_gain100',
    'wavelength'    :  '480',
    'Lstated'       :  np.array(ligand_conc, np.float64), # ligand concentration
    'Pstated'       :  0.1e-6 * np.ones([17],np.float64), # protein concentration, M
    'P_error'       :  0.15, # coefficient of protein concentration uncertainity (0.15 for 15% error)
    'assay_volume'  :  100e-6, # assay volume, L
    'well_area'     :  0.3969, # well area, cm^2 for 4ti-0203 [http://4ti.co.uk/files/3113/4217/2464/4ti-0201.pdf]
    }

inputs['Lstated'] = inputs['Lstated'].tolist()
inputs['Pstated'] = inputs['Pstated'].tolist()

with open('inputs.json', 'w') as fp:
    json.dump(inputs, fp)
