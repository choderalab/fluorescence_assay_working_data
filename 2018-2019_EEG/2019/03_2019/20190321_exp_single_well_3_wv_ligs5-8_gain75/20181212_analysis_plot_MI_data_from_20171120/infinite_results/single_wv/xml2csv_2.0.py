# A somewhat ugly, utilitarian script takes xml data file output from the Tecan Infinite m1000 Pro
# plate reader and allows for the quick visual inspection of raw data.
#
# Usage: python xml2png.py *.xml

# import math, xml, and dataframe libraries
import numpy as np
from lxml import etree
import pandas as pd
import string

# import libraries for making figures
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import seaborn

#import assaytools helper
from assaytools import platereader

# import libraries for interacting with arguments
import sys
import os
import argparse

# Define argparse stuff

parser = argparse.ArgumentParser(description="""Convert data from xml files to csv file:
> python xml2csv_2.0.py --type spectra *.xml""")
parser.add_argument("files", nargs='*', help="xml file(s) to analyze")
parser.add_argument("--type", help="type of data file (spectra, singlet_96, singlet_384, scan)", choices=['spectra', 'singlet_96', 'singlet_384','scan'],default='singlet_96')
args = parser.parse_args()
print(args.files)
print("*** --type: analyzing %s file(s) ***" % args.type)

### Define extract function that extracts parameters
#
# def extract(taglist, parameters): #["Mode", "Wavelength Start", "Wavelength End", "Wavelength Step Size"]
#     result = []
#     for p in taglist:
#         print("Attempting to extract tag '%s'..." % p)
#         try:
#             param = parameters.xpath("*[@Name='" + p + "']")[0]
#             result.append( p + '=' + param.attrib['Value'])
#         except:
#             ### tag not found
#             result.append(None)
#
#     return result

#############################################
 ###               singlet_96            ###
#############################################

# Define get_wells_from_section function that extracts the data from each Section.
# It is written sort of strangely to ensure data is connected to the correct well.

# def get_wells_from_section(path):
#     reads = path.xpath("*/Well")
#     wellIDs = [read.attrib['Pos'] for read in reads]
#
#     def convert_value(text):
#         try:
#             return float(text)
#         except ValueError as e:
#             # OVER
#             return 0.0
#
#     data = [(convert_value(s.text), r.attrib['Pos'])
#          for r in reads
#          for s in r]
#
#     nrows = 8
#     ncols = 12
#     global well_order
#     well_order = list()
#     for row_index in range(nrows):
#         for col_index in range(ncols):
#             row = '%c' % (ord('A')+row_index)
#             col = '%d' % (col_index+1)
#             well = row + col
#             well_order.append(well)
#
#
#     datalist = {
#       well : value
#       for (value, well) in data
#     }
#
#     data_ordered = [datalist[well] for well in well_order]
#
#     return data_ordered

def process_files_five(xml_files):
    """
    Main entry point.
    """

    reads = list()
    nreads = len(xml_files)
    for read in range(nreads):
        read = platereader.read_icontrol_xml(xml_files[read])
        reads.append(read)


    nrows = 8
    ncols = 2
    index = 0

    label = '280_480_TOP_100'


    data = np.zeros([nrows, ncols, nreads, 65], np.float64)
    for row_index in range(nrows):
        for col_index in range(ncols):
            row = '%c' % (ord('A')+row_index)
            col = '%d' % (col_index+5)
            well = row + col

            # measurements = [list(reads[i][label][well].values()) for i in range(nreads)]
            measurements = [list(reads[i][label].values())[well_order.keys()] for i in range(nreads)]
            # for i in range(nreads):
            #     measurements[i] = [x if x != 'OVER' else 0 for x in measurements[i]]
            # data[row_index,col_index,:] = np.array(measurements)
            print(measurements)
            # print(data[row_index,col_index,:])

    # for file in xml_files:
    #
    #     # Parse XML file.
    #
    #     root = etree.parse(file)
    #
    #     # Remove extension from xml filename.
    #
    #     file_name = os.path.splitext(file)[0]
    #
    #     # Define Sections.
    #
    #     Sections = root.xpath("/*/Section")
    #     much = len(Sections)
    #     print("****The xml file " + file + " has %s data sections:****" % much)
    #     for sect in Sections:
    #         print(sect.attrib['Name'])
    #
    #     data = []
    #
    #     for i, sect in enumerate(Sections):
    #
    #        # Extract Parameters for this section.
    #
    #         path = "/*/Section[@Name='" + sect.attrib['Name'] + "']/Parameters"
    #         parameters = root.xpath(path)[0]
    #
    #         # Parameters are extracted slightly differently depending on Absorbance or Fluorescence read.
    #
    #         if  parameters[0].attrib['Value'] == "Absorbance":
    #             result = extract(["Mode", "Wavelength", "Part of Plate"], parameters)
    #             title = '%s, %s, %s' % tuple(result)
    #
    #         else:
    #             result = extract(["Gain", "Excitation Wavelength", "Emission Wavelength", "Part of Plate", "Mode"], parameters)
    #             title = '%s, %s, %s, \n %s, %s' % tuple(result)
    #
    #         print("****The %sth section has the parameters:****" % i)
    #         print(title)
    #
    #         # Extract Reads for this section.
    #
    #         Sections = root.xpath("/*/Section")
    #
    #         data = get_wells_from_section(sect)
    #
    #         dataframe(i) = pd.DataFrame(data, index=well_order)
    #
    #         large_dataframe = pd.DataFrame()
    #         large_dataframe.append(dataframe(i))
    #         # append data to empty data frame so all data is in one place
    #
    #         # Make csv file, using dataframe as basis
    #         section_name = sect.attrib['Name']
    #         dataframe.to_csv('%s_%s.csv' % (file_name, section_name))
    #
    return

#############################################
 ###               SPECTRA               ###
#############################################

### Define an initial set of dataframes, one per each section

large_dataframe0 = pd.DataFrame()
large_dataframe1 = pd.DataFrame()
large_dataframe2 = pd.DataFrame()
large_dataframe3 = pd.DataFrame()
large_dataframe4 = pd.DataFrame()
large_dataframe5 = pd.DataFrame()

def process_files_spectra(xml_files):
    """
    Main entry point.
    """

    so_many = len(xml_files)
    print("****This script is about to make png files for %s xml files. ****"  % so_many)

    for file in xml_files:

        ### Parse XML file.

        root = etree.parse(file)

        ### Remove extension from xml filename.

        file_name = os.path.splitext(file)[0]

        ### Extract plate type and barcode.

        plate = root.xpath("/*/Header/Parameters/Parameter[@Name='Plate']")[0]
        plate_type = plate.attrib['Value']

        try:
            bar = root.xpath("/*/Plate/BC")[0]
            barcode = bar.text
        except:
            barcode = 'no barcode'

        ### Define Sections.

        Sections = root.xpath("/*/Section")
        much = len(Sections)
        print("****The xml file " + file + " has %s data sections:****" % much)
        for sect in Sections:
            print(sect.attrib['Name'])

        for i, sect in enumerate(Sections):

            ### Extract Parameters for this section.

            path = "/*/Section[@Name='" + sect.attrib['Name'] + "']/Parameters"
            parameters = root.xpath(path)[0]

            ### Parameters are extracted slightly differently depending on Absorbance or Fluorescence read.
            # Attach these to title1, title2, or title3, depending on section which will be the same for all 4 files.

            if  parameters[0].attrib['Value'] == "Absorbance":
                result = extract(["Mode", "Wavelength Start", "Wavelength End", "Wavelength Step Size"], parameters)
                globals()["title"+str(i)] = '%s, %s, %s, %s' % tuple(result)

            else:
                result = extract(["Gain", "Excitation Wavelength", "Emission Wavelength", "Part of Plate", "Mode"], parameters)
                globals()["title"+str(i)] = '%s, %s, %s, \n %s, %s' % tuple(result)

            print("****The %sth section has the parameters:****" % i)
            print(globals()["title"+str(i)])

            ### Extract Reads for this section.

            Sections = root.xpath("/*/Section")

            reads = root.xpath("/*/Section[@Name='" + sect.attrib['Name'] + "']/*/Well")

            wellIDs = [read.attrib['Pos'] for read in reads]

            data = [(s.text, float(s.attrib['WL']), r.attrib['Pos'])
                     for r in reads
                     for s in r]

            dataframe = pd.DataFrame(data, columns=['fluorescence','wavelength (nm)','Well'])

            ### dataframe_rep replaces 'OVER' (when fluorescence signal maxes out) with '3289277', an arbitrarily high number

            dataframe_rep = dataframe.replace({'OVER':'3289277'})

            dataframe_rep[['fluorescence']] = dataframe_rep[['fluorescence']].astype('float')

            # Make csv file, using dataframe as basis
            section_name = sect.attrib['Name']
            dataframe_rep.to_csv('%s_%s.csv' % (file_name, section_name))

    return

#############################################
 ###               SCAN                  ###
#############################################

def process_files_scan(xml_files):

    so_many = len(xml_files)
    print("****This script is about to make png files for %s xml files. ****"  % so_many)

    for file in xml_files:

        # Parse XML file.
        root = etree.parse(file)

        # Remove extension from xml filename.
        file_name = os.path.splitext(file)[0]

        # Extract plate type and barcode.
        plate = root.xpath("/*/Header/Parameters/Parameter[@Name='Plate']")[0]
        plate_type = plate.attrib['Value']

        bar = root.xpath("/*/Plate/BC")[0]
        barcode = bar.text

        # Define Sections.
        Sections = root.xpath("/*/Section")
        much = len(Sections)
        print("****The xml file " + file + " has %s data sections:****" % much)
        for sect in Sections:
            print(sect.attrib['Name'])

        data = []

        for i, sect in enumerate(Sections):

            # Extract Parameters for this section.
            path = "/*/Section[@Name='" + sect.attrib['Name'] + "']/Parameters"
            parameters = root.xpath(path)[0]

            # Parameters are extracted slightly differently depending on Absorbance or Fluorescence read.
            if  parameters[0].attrib['Value'] == "Absorbance":
                result = extract(["Mode", "Wavelength Start", "Wavelength End", "Wavelength Step Size"], parameters)
                title = '%s, %s, %s, %s' % tuple(result)

            else:
                result = extract(["Gain", "Excitation Wavelength", "Emission Wavelength", "Part of Plate", "Mode"], parameters)
                title = '%s, %s, %s, \n %s, %s' % tuple(result)

            print("****The %sth section has the parameters:****" %i)
            print(title)

            # Extract Reads for this section.
            Sections = root.xpath("/*/Section")

            reads = root.xpath("/*/*/*/Well")

            wellIDs = [read.attrib['Pos'] for read in reads]

            data = [(float(s.text), float(s.attrib['WL']), r.attrib['Pos'])
                    for r in reads
                    for s in r]

            dataframe = pd.DataFrame(data, columns=['fluorescence','wavelength (nm)','Well'])

            ### dataframe_rep replaces 'OVER' (when fluorescence signal maxes out) with '3289277', an arbitrarily high number

            dataframe_rep = dataframe.replace({'OVER':'3289277'})

            dataframe_rep[['fluorescence']] = dataframe_rep[['fluorescence']].astype('float')

            dataframe_pivot = pd.pivot_table(dataframe, index = 'wavelength (nm)', columns = ['Well'])

            # Make csv file, using dataframe as basis
            section_name = sect.attrib['Name']
            dataframe_rep.to_csv('%s_%s.csv' % (file_name, section_name))

    return


def entry_point():
    xml_files = args.files
    if args.type == 'singlet_96':
        process_files_five(xml_files)
    if args.type == 'spectra':
        process_files_spectra(xml_files)
    if args.type == 'scan':
        process_files_scan(xml_files)

if __name__ == '__main__':
    xml_files = args.files
    if args.type == 'singlet_96':
        process_files_five(xml_files)
    if args.type == 'spectra':
        process_files_spectra(xml_files)
    if args.type == 'scan':
        process_files_scan(xml_files)
