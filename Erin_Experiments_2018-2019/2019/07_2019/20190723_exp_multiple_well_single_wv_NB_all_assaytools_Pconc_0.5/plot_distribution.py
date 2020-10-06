# This script allows you to plot the distribution of a parameter,
# for example F_PL, from a previous run of quickmodel.py

# Usage:
#  python plot_distribution.py --input 'Src-Bosutinib-AB_mcmc_1.pickle'
#  or
#  python plot_distribution.py --input 'Src-Bosutinib-AB_mcmc_1.pickle' --parameter 'F_PL'

# Sonya M. Hanson & EEG

import json
import pickle
import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def get_parameter(data_file):
    """
    Quick model for both spectra and single wavelength experiments
    ----------
    input_file : file_name
        File_name of pickle file to get mean from.
    parameter : string, default='F_PL'
        Parameter to get mean of.
    """

    # load data from pickle file
    with open(r'%s'%data_file,'rb') as my_file:
        data = pickle.load(my_file)

    # get t_equil from json file
    base_name = os.path.splitext(data_file)[0]
    json_base = base_name.replace('_mcmc','')
    json_file = json_base + '.json'

    with open(json_file) as f:
        json_data = json.load(f)

    t_equil = json_data['t_equil']

    # find distribution of desired parameter
    my_distribution = data['Ptrue'][0]

    # convert array to list
    my_distribution_list = my_distribution.tolist()
    # create flattened version for later use in kdeplot
    my_distribution_flat = [val for sublist in my_distribution_list for val in sublist]

    distribution_dict = {}
    distribution_dict['data_file'] = data_file
    distribution_dict[parameter] = my_distribution_list

    import datetime
    my_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    my_datetime_filename = datetime.datetime.now().strftime("%Y-%m-%d %H%M")

    # get mean and std from distribution after equilibration
    distribution_equil = my_distribution[t_equil:].mean()
    ddistribution_equil = my_distribution[t_equil:].std()

    ## PLOT HISTOGRAM
    import matplotlib.patches as mpatches
    import matplotlib.lines as mlines

    plt.clf()
    plt.figure(figsize=(8,8))

    interval = np.percentile(a=my_distribution[t_equil:], q=[2.5, 50.0, 97.5])
    [hist,bin_edges] = np.histogram(my_distribution_list[t_equil:],bins=40,density=True)
    binwidth = np.abs(bin_edges[0]-bin_edges[1])

    # Print summary
    print( 'Ptrue (95% credibility interval after equilibration):')
    print( '   %.3g [%.3g,%.3g] M' %(interval[1],interval[0],interval[2]))
    print( 'Ptrue (mean and std after equil):')
    print('   %.3g +- %.3g M' %(distribution_equil,ddistribution_equil) )

    #set colors for 95% interval
    clrs = [(0.7372549019607844, 0.5098039215686274, 0.7411764705882353) for xx in bin_edges]
    idxs = bin_edges.argsort()
    idxs = idxs[::-1]
    gray_before = idxs[bin_edges[idxs] < interval[0]]
    gray_after = idxs[bin_edges[idxs] > interval[2]]
    for idx in gray_before:
        clrs[idx] = (.5,.5,.5)
    for idx in gray_after:
        clrs[idx] = (.5,.5,.5)

    plt.bar(bin_edges[:-1],hist,binwidth,color=clrs, edgecolor = "white");
    sns.kdeplot(my_distribution_flat[t_equil:],bw=.4,color=(0.39215686274509803, 0.7098039215686275, 0.803921568627451),shade=False)
    plt.axvline(x=interval[0],color=(0.5,0.5,0.5),linestyle='--')
    plt.axvline(x=interval[1],color=(0.5,0.5,0.5),linestyle='--')
    plt.axvline(x=interval[2],color=(0.5,0.5,0.5),linestyle='--')
    plt.xlabel('$P\_true$ ($M$)',fontsize=16);
    plt.ylabel('$P(P\_true)$',fontsize=16);
    plt.xlim(0.05e-6,0.6e-6)
    hist_legend = mpatches.Patch(color=(0.7372549019607844, 0.5098039215686274, 0.7411764705882353),
                label = '$P\_true$ =  %.3g [%.3g,%.3g] $M$'
                %(interval[1],interval[0],interval[2]) )
    plt.legend(handles=[hist_legend],fontsize=14,loc=0,frameon=True)


    plt.suptitle("%s: %s" % (my_file, my_datetime))
    plt.tight_layout()

    fig1 = plt.gcf()
    png_base = os.path.splitext(base_name)[0]
    fig1.savefig('P_true_%s.png'%(png_base))

    plt.close('all')

def entry_point():

    import argparse

    parser = argparse.ArgumentParser(description="""Get parameter from quickmodel run. Default parameter is Ptrue.""")
    parser.add_argument("--input", help="The pickle file output by quickmodel for your experiment.",default=None)
    parser.add_argument("--parameter", help="The parameter you want to get the distribution for.",default='Ptrue')
    args = parser.parse_args()

    get_parameter(data_file=args.input,parameter=args.parameter)

if __name__ == '__main__':
    entry_point()
