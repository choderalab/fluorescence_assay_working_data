import json
import numpy as np
from glob import glob

xml_files = ['../infinite_results/p38_Abl_WT_GK_Src_WT_GK_conc_0_20190410_133519.xml',
             '../infinite_results/p38_Abl_WT_GK_Src_WT_GK_conc_1_20190410_134751.xml',
             '../infinite_results/p38_Abl_WT_GK_Src_WT_GK_conc_2_20190410_135902.xml',
             '../infinite_results/p38_Abl_WT_GK_Src_WT_GK_conc_3_20190410_141013.xml',
             '../infinite_results/p38_Abl_WT_GK_Src_WT_GK_conc_4_20190410_142122.xml',
             '../infinite_results/p38_Abl_WT_GK_Src_WT_GK_conc_5_20190410_143235.xml',
             '../infinite_results/p38_Abl_WT_GK_Src_WT_GK_conc_6_20190410_144346.xml',
             '../infinite_results/p38_Abl_WT_GK_Src_WT_GK_conc_7_20190410_145456.xml',
             '../infinite_results/p38_Abl_WT_GK_Src_WT_GK_conc_8_20190410_150611.xml',
             '../infinite_results/p38_Abl_WT_GK_Src_WT_GK_conc_9_20190410_151725.xml',
             '../infinite_results/p38_Abl_WT_GK_Src_WT_GK_conc_10_20190410_152839.xml',
             '../infinite_results/p38_Abl_WT_GK_Src_WT_GK_conc_11_20190410_153954.xml',
             '../infinite_results/p38_Abl_WT_GK_Src_WT_GK_conc_12_20190410_155108.xml',
             '../infinite_results/p38_Abl_WT_GK_Src_WT_GK_conc_13_20190410_160222.xml',
             '../infinite_results/p38_Abl_WT_GK_Src_WT_GK_conc_14_20190410_161343.xml',
             '../infinite_results/p38_Abl_WT_GK_Src_WT_GK_conc_15_20190410_162500.xml',
             '../infinite_results/p38_Abl_WT_GK_Src_WT_GK_conc_16_20190410_163618.xml']

ligand_conc = [  0.00000000e+00,   8.00000000e-09,   1.34778097e-08,
         2.27064194e-08,   3.82541000e-08,   6.44476851e-08,
         1.08576705e-07,   1.82922021e-07,   3.08173524e-07,
         5.19188015e-07,   8.74689659e-07,   1.47361260e-06, 2.48263378e-06,
         4.18255821e-06, 7.04646547e-06, 1.118713651e-05, 2.0e-05]

inputs = {
    'single_well'   :  True,
    'xml_files'     :  xml_files,
    'file_set'      :  {'p38': xml_files},
    'protein_wells'  :  {'p38': ['G12']},
    'ligand_order'  :  ['Staurosporine'],
    'buffer_wells'   :  {'p38': ['G2']},
    'section'       :  'ex296_em396_top_gain65_bw10',
    'wavelength'    :  '396',
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
