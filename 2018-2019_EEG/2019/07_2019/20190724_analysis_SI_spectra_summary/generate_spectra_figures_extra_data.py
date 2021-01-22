# adapted from Sonya's script for Figure 1 in the paper
# EEG, July 2019

from assaytools import platereader
from glob import glob
from lxml import etree
import pandas as pd
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import numpy as np

import seaborn as sns
sns.set(style='white')
sns.set_context('talk')

#This function allows us to import a section from an xml formated data file and convert it to a pandas dataframe
def xml2df_section(file,section):

    root = etree.parse(file)

    data = []

    reads = root.xpath("/*/Section[%s]/*/Well"%section)
    Sections = root.xpath("/*/Section")
    #print Sections[(section-1)].attrib['Name']
    section_name = Sections[(section-1)].attrib['Name']

    wellIDs = [read.attrib['Pos'] for read in reads]

    data = [(s.text, float(s.attrib['WL']), r.attrib['Pos'])
        for r in reads
        for s in r]

    dataframe = pd.DataFrame(data, columns=['fluorescence','wavelength (nm)','Well'])

    ### dataframe_rep replaces 'OVER' (when fluorescence signal maxes out) with '3289277', an arbitrarily high number

    #dataframe_rep = dataframe.replace({'OVER':'1.2e5'})

    dataframe_rep = dataframe.replace({'OVER':'NAN'})

    dataframe_rep[['fluorescence']] = dataframe_rep[['fluorescence']].astype('float')

    dataframe_pivot = pd.pivot_table(dataframe_rep, index = 'wavelength (nm)', columns = ['Well'])

    #Rearrange columns so they're in the right order
    cols =  dataframe_pivot['fluorescence'].columns.tolist()
    cols = [cols[0]] + cols[4:12] + cols[1:4] + [cols[12]] + cols[16:24] + cols[13:16]
    dataframe_reindex =  dataframe_pivot.reindex_axis(cols,level='Well',axis=1)

    return [dataframe_reindex,section_name]

#This function allows us to plot spectra choosing ylim and
def plot_spectra_grid_advanced_inset(file,protein,ligands,ligand,section,ylim,lines,Lstated):
    grid = len(protein) + len(ligand)

    # file = file_set[protein]
    file = file

    # make a dataframe
    [df,section_name] = xml2df_section(file,section)

    # pick a title
    title = "%s - %s: %s" %(protein, ligand, section_name)
    print(title)

    # define ylim and lines

    ylim = ylim
    lines = lines

    # plot the spectra
    fig = plt.figure(figsize=(7,6));
    ax = df['fluorescence'].iloc[:,12].plot(ylim=(-10,ylim),legend=False, linewidth=4,color='m',logy=True);
    ax.axvline(x=lines[0],color='black',linestyle='--');
    ax.axvline(x=lines[1],color='blue',linestyle='--');
    for i in range(11):
        df['fluorescence'].iloc[:,i].plot(linewidth=3,c=cm.hsv(i*15), ax = ax,logy=True);
        df['fluorescence'].iloc[:,11+i].plot(legend=False, linewidth=4,c=cm.gray(i*15+50),logy=True,ax = ax, fontsize =20);
    sns.despine()
    plt.yticks([])
    plt.xticks(fontsize=26)
    plt.xlim(310,600)
    plt.xlabel('wavelength (nm)', fontsize=30)
    plt.ylabel('log(Intensity)', fontsize=30)
#    plt.text(550,0.9*ylim,"lines=%s"%lines,color='0.7')
#    plt.title(title)
    plt.tight_layout();

    ## Plot intensity from `lines` wavelengths

    complex_280_340 = df['fluorescence'].loc[lines[0]][:12]
    ligand_280_340 = df['fluorescence'].loc[lines[0]][12:]

    complex_280_480 = df['fluorescence'].loc[lines[1]][:12]
    ligand_280_480 = df['fluorescence'].loc[lines[1]][12:]

    difference_280_480 = complex_280_480.values - ligand_280_480.values
    difference_280_340 = complex_280_340.values - ligand_280_340.values

    difference_280_480_normalized = difference_280_480/np.nanmax(difference_280_480)
    difference_280_340_normalized = difference_280_340/np.nanmax(difference_280_340)

    a = plt.axes([0.7, 0.7, .25, .25])
    plt.semilogx(Lstated,difference_280_480_normalized,color="blue",marker='o',linestyle='None',label='%s nm'%lines[1]);
    plt.semilogx(Lstated,difference_280_340_normalized,color="black",marker='o',linestyle='None',label='%s nm'%lines[0]);
    plt.yticks([])
    x_inset_labels = [0,-8,-7,-6,-5]
    plt.xticks([1e-9,1e-8,1e-7,1e-6,1e-5], x_inset_labels,fontsize=16)
    plt.xlabel('$log_{10}([L])$', fontsize=18);
    plt.ylabel('RFU', fontsize=18);
    plt.legend(loc=0,bbox_to_anchor=(-0.6 , 1.1), fontsize=20);
    a.spines['top'].set_visible(False)
    a.spines['right'].set_visible(False)
    a.spines['left'].set_visible(False)
    a.spines['left'].set_smart_bounds(True)

Lstated = [20.0e-6,9.15e-6,4.18e-6,1.91e-6,0.875e-6,0.4e-6,0.183e-6,0.0837e-6,0.0383e-6,0.0175e-6,0.008e-6,0.0035e-6]

ylim = 500000
lines = [340,480]

file = "infinite_results/p38/2016-03-07/p38_Bos_20160307_160155.xml"
ligands = ['Bosutinib']
plot_spectra_grid_advanced_inset(file,'p38',ligands,'Bosutinib',1,ylim,lines,Lstated)
plt.savefig('p38-Bosutinib-log-inset.png',dpi=500)
plt.savefig('p38-Bosutinib-log-inset.pdf')

file = "infinite_results/p38/2016-03-07/p38_BosI_20160307_163847.xml"
ligands = ['Bosutinib Isomer']
plot_spectra_grid_advanced_inset(file,'p38',ligands,'Bosutinib Isomer',1,ylim,lines,Lstated)
plt.savefig('p38-Bosutinib Isomer-log-inset.png',dpi=500)
plt.savefig('p38-Bosutinib Isomer-log-inset.pdf')

file = "infinite_results/p38/2016-03-07/p38_Erl_20160307_171539.xml"
ligands = ['Erlotinib']
plot_spectra_grid_advanced_inset(file,'p38',ligands,'Erlotinib',1,ylim,lines,Lstated)
plt.savefig('p38-Erlotinib-log-inset.png',dpi=500)
plt.savefig('p38-Erlotinib-log-inset.pdf')

file = "infinite_results/p38/2016-03-07/p38_Gef_20160307_175343.xml"
ligands = ['Gefitinib']
plot_spectra_grid_advanced_inset(file,'p38',ligands,'Gefitinib',1,ylim,lines,Lstated)
plt.savefig('p38-Gefitinib-log-inset.png',dpi=500)
plt.savefig('p38-Gefitinib-log-inset.pdf')

file = "infinite_results/p38/2016-03-30/p38_DQA_20160330_171906.xml"
ligands = ['DQA']
plot_spectra_grid_advanced_inset(file,'p38',ligands,'DQA',1,ylim,lines,Lstated)
plt.savefig('p38-DQA-log-inset.png',dpi=500)
plt.savefig('p38-DQA-log-inset.pdf')

file = "infinite_results/p38/2016-03-30/p38_Das_20160330_164208.xml"
ligands = ['Dasatinib']
plot_spectra_grid_advanced_inset(file,'p38',ligands,'Dasatinib',1,ylim,lines,Lstated)
plt.savefig('p38-Dasatinib-log-inset.png',dpi=500)
plt.savefig('p38-Dasatinib-log-inset.pdf')

file = "infinite_results/p38/2016-03-30/p38_Ima_20160330_152613.xml"
ligands = ['Imatinib']
plot_spectra_grid_advanced_inset(file,'p38',ligands,'Imatinib',1,ylim,lines,Lstated)
plt.savefig('p38-Imatinib-log-inset.png',dpi=500)
plt.savefig('p38-Imatinib-log-inset.pdf')

file = "infinite_results/p38/2016-03-30/p38_Pon_20160330_160326.xml"
ligands = ['Ponatinib']
plot_spectra_grid_advanced_inset(file,'p38',ligands,'Ponatinib',1,ylim,lines,Lstated)
plt.savefig('p38-Ponatinib-log-inset.png',dpi=500)
plt.savefig('p38-Ponatinib-log-inset.pdf')

file = "infinite_results/p38/2016-12-20/p38_Sta_ab_20161220_112406.xml"
ligands = ['Staurosporine']
plot_spectra_grid_advanced_inset(file,'p38',ligands,'Staurosporine',1,ylim,lines,Lstated)
plt.savefig('p38-Staurosporine-log-inset.png',dpi=500)
plt.savefig('p38-Staurosporine-log-inset.pdf')

file = "infinite_results/p38/2017-01-19/p38_Axi_20170119_144258.xml"
ligands = ['Axitinib']
plot_spectra_grid_advanced_inset(file,'p38',ligands,'Axitinib',1,ylim,lines,Lstated)
plt.savefig('p38-Axitinib-log-inset.png',dpi=500)
plt.savefig('p38-Axitinib-log-inset.pdf')

file = "infinite_results/p38/2017-01-19/p38_Lap_20170119_152110.xml"
ligands = ['Lapatinib']
plot_spectra_grid_advanced_inset(file,'p38',ligands,'Lapatinib',1,ylim,lines,Lstated)
plt.savefig('p38-Lapatinib-log-inset.png',dpi=500)
plt.savefig('p38-Lapatinib-log-inset.pdf')

file = "infinite_results/p38/2017-01-19/p38_Pal_20170119_160546.xml"
ligands = ['Palbociclib']
plot_spectra_grid_advanced_inset(file,'p38',ligands,'Palbociclib',1,ylim,lines,Lstated)
plt.savefig('p38-Palbociclib-log-inset.png',dpi=500)
plt.savefig('p38-Palbociclib-log-inset.pdf')

file = "infinite_results/p38/2017-01-19/p38_Paz_20170119_164846.xml"
ligands = ['Pazopanib']
plot_spectra_grid_advanced_inset(file,'p38',ligands,'Pazopanib',1,ylim,lines,Lstated)
plt.savefig('p38-Pazopanib-log-inset.png',dpi=500)
plt.savefig('p38-Pazopanib-log-inset.pdf')


file = "infinite_results/Abl/2016-03-11/Abl_D382N_Bos_20160311_132205.xml"
ligands = ['Bosutinib']
plot_spectra_grid_advanced_inset(file,'Abl',ligands,'Bosutinib',1,ylim,lines,Lstated)
plt.savefig('Abl-Bosutinib-log-inset.png',dpi=500)
plt.savefig('Abl-Bosutinib-log-inset.pdf')

file = "infinite_results/Abl/2016-03-11/Abl_D382N_BosI_20160311_135952.xml"
ligands = ['Bosutinib Isomer']
plot_spectra_grid_advanced_inset(file,'Abl',ligands,'Bosutinib Isomer',1,ylim,lines,Lstated)
plt.savefig('Abl-Bosutinib Isomer-log-inset.png',dpi=500)
plt.savefig('Abl-Bosutinib Isomer-log-inset.pdf')

file = "infinite_results/Abl/2016-03-11/Abl_D382N_Erl_20160311_143642.xml"
ligands = ['Erlotinib']
plot_spectra_grid_advanced_inset(file,'Abl',ligands,'Erlotinib',1,ylim,lines,Lstated)
plt.savefig('Abl-Erlotinib-log-inset.png',dpi=500)
plt.savefig('Abl-Erlotinib-log-inset.pdf')

file = "infinite_results/Abl/2016-03-11/Abl_D382N_Gef_20160311_152340.xml"
ligands = ['Gefitinib']
plot_spectra_grid_advanced_inset(file,'Abl',ligands,'Gefitinib',1,ylim,lines,Lstated)
plt.savefig('Abl-Gefitinib-log-inset.png',dpi=500)
plt.savefig('Abl-Gefitinib-log-inset.pdf')

file = "infinite_results/Abl/2016-05-26/Abl_Afa_20160526_161533.xml"
ligands = ['Afatinib']
plot_spectra_grid_advanced_inset(file,'Abl',ligands,'Afatinib',1,ylim,lines,Lstated)
plt.savefig('Abl-Afatinib-log-inset.png',dpi=500)
plt.savefig('Abl-Afatinib-log-inset.pdf')

file = "infinite_results/Abl/2016-05-26/Abl_Ner_20160526_165224.xml"
ligands = ['Neratinib']
plot_spectra_grid_advanced_inset(file,'Abl',ligands,'Neratinib',1,ylim,lines,Lstated)
plt.savefig('Abl-Neratinib-log-inset.png',dpi=500)
plt.savefig('Abl-Neratinib-log-inset.pdf')


file = "infinite_results/Src/2016-03-09/Src_Bos_20160309_143920.xml"
ligands = ['Bosutinib']
plot_spectra_grid_advanced_inset(file,'Src',ligands,'Bosutinib',1,ylim,lines,Lstated)
plt.savefig('Src-Bosutinib-log-inset.png',dpi=500)
plt.savefig('Src-Bosutinib-log-inset.pdf')

file = "infinite_results/Src/2016-03-09/Src_BosI_20160309_151610.xml"
ligands = ['Bosutinib Isomer']
plot_spectra_grid_advanced_inset(file,'Src',ligands,'Bosutinib Isomer',1,ylim,lines,Lstated)
plt.savefig('Src-Bosutinib Isomer-log-inset.png',dpi=500)
plt.savefig('Src-Bosutinib Isomer-log-inset.pdf')

file = "infinite_results/Src/2016-03-09/Src_Erl_20160309_155259.xml"
ligands = ['Erlotinib']
plot_spectra_grid_advanced_inset(file,'Src',ligands,'Erlotinib',1,ylim,lines,Lstated)
plt.savefig('Src-Erlotinib-log-inset.png',dpi=500)
plt.savefig('Src-Erlotinib-log-inset.pdf')

file = "infinite_results/Src/2016-03-09/Src_Gef_20160309_163417.xml"
ligands = ['Gefitinib']
plot_spectra_grid_advanced_inset(file,'Src',ligands,'Gefitinib',1,ylim,lines,Lstated)
plt.savefig('Src-Gefitinib-log-inset.png',dpi=500)
plt.savefig('Src-Gefitinib-log-inset.pdf')
