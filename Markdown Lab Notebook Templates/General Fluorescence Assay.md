# Experiment Title

**Date:** YYYY-MM-DD
**Performed By:** Name

**Aim:** 1-2 sentences of goal of experiment

---

## Prepare Ligand Stock Plate

### EVO Set Up Information

**EVO Script:** `EAG_CreateCompoundPlate_20200831.esc`

**Worktable Vial Holder**

* Source Vials exposed to air for 2 min 40 seconds. After running both scripts sequentially, the compound plate was sealed with our PlateLoc (SGS13PLC14802)

| Source Vial | Location in Holder | UUID |
| :---------: | :----------------: | :--: |
|             |         A1         |      |
|             |         B1         |      |
|             |         C1         |      |

**Destination Plate Lay Out**

(Insert photo here of a 96 well plate with labeled wells)

## Prepare Protein Stock

1. Removed Kinase Binding Assay Buffer, pH 8.0 (Revo#BLANK; made YYYY-MM-DD)
   * Insert photo of Revo Buffer Details Here
2. Removed (#) aliquot of [PROTEIN] from the -80˚C and thawed on ice (Protein was made from Macrolab project#)
   * Measured concentration of protein on the Denovix using the proper [NAME] settings. Did 2 reads of 2 µL each, blanking first with buffer.

| Protein                                                   | Reading 1 (mg/mL) | Reading 2 (mg/mL) | Average (mg/mL) |
| --------------------------------------------------------- | ----------------- | ----------------- | --------------- |
| **Abl D382N**<br />MW: 33273.1 Da, ε: 62340 M-1cm-1       |                   |                   |                 |
| **Abl D382N/T334I**<br />MW: 33285.2 Da, ε: 62340 M-1cm-1 |                   |                   |                 |
| **Src WT**<br/>MW: 32479.4 Da, ε: 52370 M-1cm-1           |                   |                   |                 |
| **Src T338I** <br/>MW: 32507.5 Da, ε: 52370 M-1cm-1       |                   |                   |                 |
| **p38** <br/>MW: 41293.2 Da, ε: 49850 M-1cm-1             |                   |                   |                 |

3. Used the [edited_protein_volume_calculation.py](https://github.com/choderalab/wetlab-protocols/blob/master/Frequent_calculations_during_experiment_preparation/WIP_python_scripts/edited_protein_volume_calculation.py) script (in "Common Wet Lab Scripts" on GitHub) to calculate the amounts of protein and buffer needed to make **10 mL of 0.5 µM protein stock solution.**
   * Used a P10 and a P200 pipette to make the below solution in # - 15 mL conical tube. The solution were then set to equilibrate to room temperature.

| Protein | Amount Protein Needed (µL) | Amount Buffer Needed (mL) |
| ------- | -------------------------- | ------------------------- |
|         |                            |                           |

## Experiment 

### Set Up Notes

* **Plate Type:**
* **Plate Lay out:** (Insert photo here of a 96 well plate with labeled wells)
* **Automation Used:** Our equipment (Note if we used a loaner instrument)
* **Prior to conducting the experiment, the Infinite was power cycled.**

### Methods/Scripts Used

| Automation | Script Title |
| ---------- | ------------ |
| Momentum   |              |
| EVO        |              |
| D300e      |              |
| Infinite   |              |

***Note:** Output files are located here: *link to Google Drive/GitHub*

## Results

**Raw Data:** (link to raw data)

**Output Files:**

* List all output file Names

**Results:**

* Insert photos of graph outputs from result scripts
* Comments on findings
* Next Steps
