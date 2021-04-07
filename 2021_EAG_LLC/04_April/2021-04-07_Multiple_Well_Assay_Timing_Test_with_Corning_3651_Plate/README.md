# Multiple Well Assay Timing Test with Corning 3651 Plate

Date: Apr 7, 2021
Entry Type: Experiment
Tags: Erica Goldberger, Liza Casella

**Aim:** To visually show that protein is binding to the plate. We will measure the same complexes: Abl WT & Src WT against Bos & Erl ligands using DMSO backfill.

- EXP previously completed 2020/09/02 but the data was in `.xlsx` format and couldnot be analyzied
- Important to note that the EXP has been **extended to 4 hrs.** (The length of time it takes to perform a singlewell assay)
- Overview

---

## **Prepared 0.5µM Protein Stock Solution**

1. Used Kinase Binding Assay Buffer, pH 8.0 (Revo #10142; made 2021-04-06)

   - *Buffer Details*

     ![Multiple%20Well%20Assay%20Timing%20Test%20with%20Corning%203651%20%20941917e506734178a6f183d4ce41c9f5/Untitled.png](/Users/goldbee2/Documents/Local GitHub Repositories/Fluorscence_Assay/fluorescence_assay/2021_EAG_LLC/04_April/2021-04-07_Multiple_Well_Assay_Timing_Test_with_Corning_3651_Plate/Untitled.png)

2. Removed (1)100 µL aliquot of Abl D382N from the -80˚C (**Macrolab project 1369b, storage buffer: 20 mM Tris-HCl, pH 8, 150 mM NaCl, 5% glycerol, 1 mM DTT; 03/26/2019**) and (1) 100 µL aliquot of Src WT from the -80˚C (**Macrolab project 1369b, storage buffer: 20 mM Tris-HCl, pH 8, 150 mM NaCl, 5% glycerol, 1 mM DTT; 03/28/2019**) and thawed on ice. 

   - After the proteins were thawed, they were spun down in the tabletop centrifuge for 10 minutes at 4°C at 5000 rcf.
     - There were No pellets/unfolded protein

3. Measured the concentrations of p38 aliquot on the Denovix. Did 2 reads of 2 µL each and averaged:

   * ![](/Users/goldbee2/Documents/Local GitHub Repositories/Fluorscence_Assay/fluorescence_assay/2021_EAG_LLC/04_April/2021-04-07_Multiple_Well_Assay_Timing_Test_with_Corning_3651_Plate/Fluorescence Timing Test-Denovix (1).png)

4. Used the [`edited_protein_volume_calculation.py`](https://github.com/choderalab/wetlab-protocols/blob/master/Frequent_calculations_during_experiment_preparation/WIP_python_scripts/edited_protein_volume_calculation.py) script (in “Common Wet Lab Scripts” on Github) to calculate the amounts of protein and buffer needed to make 10 mL of 0.5 µM protein 

![Multiple%20Well%20Assay%20Timing%20Test%20with%20Corning%203651%20%20941917e506734178a6f183d4ce41c9f5/Fluorescence_Timing_Test-Protein_Stock.png](/Users/goldbee2/Documents/Local GitHub Repositories/Fluorscence_Assay/fluorescence_assay/2021_EAG_LLC/04_April/2021-04-07_Multiple_Well_Assay_Timing_Test_with_Corning_3651_Plate/Fluorescence_Timing_Test-Protein_Stock.png)

## **Ran Experiment with Corning 3651 NBS Plate**

Since the D300e is not entirely integrated into the EVO, I cannot “set it and forget it” and run a Momentum script. The procedure will be performed “by hand.” (Otherwise I would have used the Momentum Script: `EEG_timing_test_single_wv_20190411` & `E_EEG_timing_test_single_wv_20190411`)

**NOTES**

- **Plate Type:** Corning 2651 NBS Plate

- **Plate Layout:**

  ![](/Users/goldbee2/Documents/Local GitHub Repositories/Fluorscence_Assay/fluorescence_assay/2021_EAG_LLC/04_April/2021-04-07_Multiple_Well_Assay_Timing_Test_with_Corning_3651_Plate/-q5hk0dXk-jXoDmncsyT6efIGGRlx3sU6G_eme0hIhmCh2nv9fzQNKdzWS4vOJtgQB2u4OjL8Jx5XgHAnv0nHquG3XIiaCrrYxOcy3ytk27QUFCvZjiJd79xcLwUsO7IpeZk01VT.png)

- **Automation Equipment Used:** Our Infinite, Our EVO, our D300e, our centrifuge

- Prior to the beginning experiment, I powercycled the Infinite.

**METHOD**

1. Run EVO script to dispense Protein into plate and Inhibitor/DMSO onto HP T8+ Dispensehead Cassette

   - **Aspirated from column 12 of Compound Plate (12A, 12B, 12C)**

   - **Ran TWO Scripts (Split original `EEG_timing_test_single_wv_full_plate_20190411.esc` script into 2 since EVOware was having an attitude)**

     - **Script 1:** `EaG_timing_test_single_wv_full_plate_edited_no_D300_1.esc`  ➡️ BEFORE D300e
       - Pipette Protein Plate
       - Pipette/set up T8+ D300e cassette
     - **Script 2:** `EaG_timing_test_single_wv_full_plate_edited_no_D300_part2.esc` ➡️ AFTER D300e
       - Move Plate too Inheco
       - Shake for 2 minutes

   - Worktable Layout:

     ![Multiple%20Well%20Assay%20Timing%20Test%20with%20Corning%203651%20%20941917e506734178a6f183d4ce41c9f5/Untitled%201.png](/Users/goldbee2/Documents/Local GitHub Repositories/Fluorscence_Assay/fluorescence_assay/2021_EAG_LLC/04_April/2021-04-07_Multiple_Well_Assay_Timing_Test_with_Corning_3651_Plate/Untitled 1.png)

2. Run D300e script to pipette serial dilution of Inhibitor/DMSO onto Plate 

   - **Script:** `EEG_timing_test_single_wv_full_plate_2019-04-11_wells_3to_5 2019-07-23 1300.DATA.xml`

     - Aspirated from 6-8 on Chip

     - ***Ligand Titration Series (Ligand concentration in each well)***

       ![Multiple%20Well%20Assay%20Timing%20Test%20with%20Corning%203651%20%20941917e506734178a6f183d4ce41c9f5/Denovix_Chart-D300e_Well_info.png](/Users/goldbee2/Documents/Local GitHub Repositories/Fluorscence_Assay/fluorescence_assay/2021_EAG_LLC/04_April/2021-04-07_Multiple_Well_Assay_Timing_Test_with_Corning_3651_Plate/Denovix_Chart-D300e_Well_info.png)

3. Spin Plate with HiG4 Centrifuge for 30 seconds; 500 G

4. Place Plate into Infinite and Run Script

   - **Script:** `EAG_FLU_timing_test_single_wv_20200902.mdfx`
     - General Description of Script Process: Entire Process is a total of 4 hours of readings
       - Repeat readings 10 times :arrow_right: WAIT 30 minutes timer :arrow_right: Repeat Readings 10 times :arrow_right:  WAIT 30 minutes timer :arrow_right: Repeat Readings 10 times :arrow_right: WAIT 30 minutes timer :arrow_right: Repeat Readings 10 times

## Results

- Google Drive Link: [https://drive.google.com/drive/u/0/folders/1KnVgOEJahUhmaQYb5Q5B-pni25tfs1RN](https://drive.google.com/drive/u/0/folders/1KnVgOEJahUhmaQYb5Q5B-pni25tfs1RN)
- `.xml` File: [2021-04-07_time_test_single_wv_plate_1.xml](Multiple%20Well%20Assay%20Timing%20Test%20with%20Corning%203651%20%20941917e506734178a6f183d4ce41c9f5/2021-04-07_time_test_single_wv_plate_1.xml)

