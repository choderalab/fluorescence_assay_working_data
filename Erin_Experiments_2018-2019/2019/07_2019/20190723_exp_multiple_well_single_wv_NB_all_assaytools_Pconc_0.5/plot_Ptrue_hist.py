
import numpy as np
from assaytools import parser
import string
from glob import glob

import matplotlib.pyplot as plt
import matplotlib
import matplotlib.patches as mpatches
import seaborn as sns
sns.set(style='white')
sns.set_context('talk')

def get_parameter(data_file, parameter='F_PL'):

    # Let's plot Ptrue histograms for these.

    import pickle

    p38_Bos_file = args.file1
    p38_Bsi_file = 'p38-Bosutinib Isomer-CD_mcmc-2019-07-23 13/46.pickle'
    p38_Erl_file = 'p38-Erlotinib-EF_mcmc-2019-07-23 15/58.pickle'
    p38_Gef_file = 'p38-Gefitinib-GH_mcmc-2019-07-23 18/10.pickle'

    with open(r'%s'%p38_Bos_file,'rb') as my_file:
        p38_Bos_data = pickle.load(my_file)
    with open(r'%s'%p38_Bsi_file,'rb') as my_file:
        p38_Bsi_data = pickle.load(my_file)
    with open(r'%s'%p38_Erl_file,'rb') as my_file:
        p38_Erl_data = pickle.load(my_file)
    with open(r'%s'%p38_Gef_file,'rb') as my_file:
        p38_Gef_data = pickle.load(my_file)

    cols = sns.color_palette('YlGnBu_r', 5)

    binBoundaries = np.linspace(-35,-9,50)

    kd_binBoundaries = np.exp(np.arange(-30,-9,0.5))

    #Lets make this plot using M for concentrations

    fig, ax = plt.subplots(figsize=(8,4))

    plt.hist(p38_Bos_data['Ptrue'][0],facecolor=cols[0],bins=binBoundaries,edgecolor='white',normed=1,alpha=0.9,label='p38:Bosutinib')
    plt.hist(p38_Bsi_data['Ptrue'][0],facecolor=cols[1],bins=binBoundaries,edgecolor='white',normed=1,alpha=0.9,label='p38:Bosutinib Isomer')
    plt.hist(p38_Erl_data['Ptrue'][0],facecolor=cols[2],bins=binBoundaries,edgecolor='white',normed=1,alpha=0.9,label='p38:Erlotinib')
    plt.hist(p38_Gef_data['Ptrue'][0],facecolor=cols[3],bins=binBoundaries,edgecolor='white',normed=1,alpha=0.9,label='p38:Gefitinib')

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    plt.title('p38 affinities',fontsize=20)
    plt.yticks([])
    plt.ylim((0,0.9))
    plt.ylabel('$P\_true$',fontsize=16)
    plt.xticks(fontsize=16)
    plt.xlim((-25,-8.5))
    plt.xlabel('$P\_true$ ($M$)',fontsize=16)
    plt.legend(loc=2,fontsize=14,frameon=True,framealpha=0.9)

    plt.tight_layout()

    plt.savefig('p38_Ptrue_hist.png', dpi=500)
    plt.savefig('p38_Ptrue_hist.pdf')

def entry_point():

    import argparse

    parser = argparse.ArgumentParser(description="""Get distribution of Ptrue from quickmodel run.""")
    parser.add_argument("--file1", help="The pickle file output by quickmodel for your experiment.",default=None)
    args = parser.parse_args()

    get_Ptrue(data_file=args.file1,parameter=args.parameter)

if __name__ == '__main__':
    entry_point()
