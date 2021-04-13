# REPEAT: Multiple Well Assay Timing Test with Corning 3651 Plate (Full 4 Hours)

Date: Apr 8, 2021
Erica Goldberger, Liza Casella

**Aim:** To visually show that protein is binding to the plate. We will measure the same complexes: Abl WT & Src WT against Bos & Erl ligands using DMSO backfill.

- EXP previously completed 2021/04/07 was apparently not actually 4 hours (see [analysis section](https://www.notion.so/Multiple-Well-Assay-Timing-Test-with-Corning-3651-Plate-560918d7d57947a1aa02c92d97ab6f58) for explanation)

---

# Experiment

## Preparation of Ligand and Protein

### Created Ligand Compound Stock Plate

- Ran EVO Script: `EAG_CreateCompoundPlate_20200831.esc`

    ![Vial Holder](/Users/goldbee2/Documents/Local GitHub Repositories/Fluorscence_Assay/fluorescence_assay/2021_EAG_LLC/04_April/2021-04-08_Multiple_Well_Assay_Timing_Test_with_Corning_3651_Plate/Photos for README/Vial_Holder.jpg)

- **PLATE LAYOUT**

    - ![Compound Stock Plate Layout](/Users/goldbee2/Documents/Local GitHub Repositories/Fluorscence_Assay/fluorescence_assay/2021_EAG_LLC/04_April/2021-04-08_Multiple_Well_Assay_Timing_Test_with_Corning_3651_Plate/compound_stock_plate_2021-04-06-8329942.jpg)
    - Source Vials exposed to air for 1 min 24 seconds. (Total time vial has been exposed to air: 2 min 3 sec)

The compound plate was then sealed with our Agilent PlateLoc (SN#SGS13PLC14802)

### **0.5µM Protein Stock Solution: Using solution made [2021-04-07](https://www.notion.so/Multiple-Well-Assay-Timing-Test-with-Corning-3651-Plate-560918d7d57947a1aa02c92d97ab6f58)**

# **Ran Experiment with Corning 3651 NBS Plate**

Since the D300e is not entirely integrated into the EVO, I cannot “set it and forget it” and run a Momentum script. The procedure will be performed “by hand.” (Otherwise I would have used the Momentum Script: `EEG_timing_test_single_wv_20190411` & `E_EEG_timing_test_single_wv_20190411`)

**NOTES**

- **Plate Type:** Corning 2651 NBS Plate
- **Plate Layout:**

    ![](/Users/goldbee2/Documents/Local GitHub Repositories/Fluorscence_Assay/fluorescence_assay/2021_EAG_LLC/04_April/2021-04-08_Multiple_Well_Assay_Timing_Test_with_Corning_3651_Plate/Photos for README/Plate Layout_EXP.png)

- **Automation Equipment Used:** Our Infinite, Our EVO, our D300e, our centrifuge
- Prior to the beginning experiment, I powercycled the Infinite.

**METHOD**

1. Run EVO script to dispense Protein into plate and Inhibitor/DMSO onto HP T8+ Dispensehead Cassette
    - **Aspirated from column 12 of Compound Plate (12A, 12B, 12C)**
    - **Ran TWO Scripts (Split original `EEG_timing_test_single_wv_full_plate_20190411.esc` script into 2 since EVOware was having an attitude)**
        - Script 1: `EaG_timing_test_single_wv_full_plate_edited_no_D300_1.esc`  ➡️ BEFORE D300e
            - Pipette Protein Plate
            - Pipette/set up T8+ D300e cassette
        - Script 2: `EaG_timing_test_single_wv_full_plate_edited_no_D300_part2.esc` ➡️ AFTER D300e
            - Move Plate too Inheco
            - Shake for 2 minutes
    - Worktable Layout:

        ![](/Users/goldbee2/Documents/Local GitHub Repositories/Fluorscence_Assay/fluorescence_assay/2021_EAG_LLC/04_April/2021-04-08_Multiple_Well_Assay_Timing_Test_with_Corning_3651_Plate/Photos for README/EVO_Worktable.png)

2. Run D300e script to pipette serial dilution of Inhibitor/DMSO onto Plate 
    - Script: `EEG_timing_test_single_wv_full_plate_2019-04-11_wells_3to_5 2019-07-23 1300.DATA.xml`
        - Aspirated from 6-8 on Chip
        - ***Ligand Titration Series (Ligand concentration in each well)***

            ![](/Users/goldbee2/Documents/Local GitHub Repositories/Fluorscence_Assay/fluorescence_assay/2021_EAG_LLC/04_April/2021-04-08_Multiple_Well_Assay_Timing_Test_with_Corning_3651_Plate/Photos for README/D300e_Well_info.png)

3. Spin Plate with HiG4 Centrifuge for 30 seconds; 500 G
4. Place Plate into Infinite and Run Script
    - Script: `EAG_LLC_FLU_timing_test_singlet_20210408.mdfx`
        - Protocol: Kinetic Cycle Duration of 4:00:00 with an interval time 00:15:00 (hh:mm:ss)
            - Meaning for 4 hours, the infiinute should read the entire plate every 15 minutes
                - 8 times with a Fluorescence Intensity Scan (Excitation 280nm, Emission 480 nm)
                - 1 times with an Absorbance (measurement wavelength 280nm)

# Results

Infinite Output File: [2021-04-08 13-08-30_plate_1.xml](REPEAT%20Multiple%20Well%20Assay%20Timing%20Test%20with%20Cornin%207f823f74ec8942cbb7144d1d95f3f4cc/2021-04-08_13-08-30_plate_1.xml)

- Also on Google Drive here:[https://drive.google.com/file/d/1zc99N3GQsxIgS6PSMXsi4rZK5iQj361a/view?usp=sharing](https://drive.google.com/file/d/1zc99N3GQsxIgS6PSMXsi4rZK5iQj361a/view?usp=sharing)

# Analysis

## Notebook

[https://gist.github.com/jchodera/1cac27356da87ec6962c0e6c7aa285ca](https://gist.github.com/jchodera/1cac27356da87ec6962c0e6c7aa285ca)

## Output

**Fluorescence by well:**

* ![]()



**Fluorescence intensity by concentration** 



**Fluorescence intensity by time**

### Comments by JDC in slack [#fluoresceince-assay](https://choderalab.slack.com/archives/C0XSW4M17/p1618172597028700)

- What’s super weird here is that well 12 should have protein but no ligand, but the fluorescence does not seem different from the rest of the wells. Be sure to check the D300 script to make sure the concentrations are what you expect.
- The buffer wells also do not show a fluorescence increase at high ligand concentrations (well 1), suggesting there is just a lot of variation in how much protein was dispensed from well-to-well (or how much protein got down into the well) and no ligand was dispensed.
- These measurements are not very forgiving, so all sorts of things could be wrong:
    - Protein could be bad/unfolded
    - Buffer could be wrong pH/temperature
    - Ligand stocks could be problematic, or have undissolved ligand in them
    - Protein stock solution could be wrong concentration
    - Protein stock solution could be not dispensing correctly or consistently, or wrong temperature
    - Ligand could be dispensing incorrectly
    - Centrifugation was insufficient to get all the dispensed liquid down to the bottom
    - Shaking to mix could be problematic
    - Fluorescence reading is at wrong height to actually excite the well or capture the fluorescence well