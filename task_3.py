import pandas
import csv
import sys
from pandas import DataFrame
import numpy as np

def compute(dataset):
    data = pandas.read_csv(dataset, sep="\t", dtype=object)
    sortedData = data.sort_values(['ApprovalDate'])
    years = ['1990', '1991', '1992', '1993', '1994', '1995', '1996',
             '1997', '1998', '1999', '2000', '2001', '2002', '2003',
             '2004', '2005', '2006', '2007', '2008', '2009', '2010',
             '2011', '2012', '2013', '2014', '2015', '2016', '2017',
             '2018']
    lastFourYears = ['2014', '2015', '2016','2017', '2018']
    uniqueIDInfo = {}
    bankInfo = {}
    cbsa = {}
    uniqueIDs = []
    bankYearsMissing = {}
    banksDropped = {}
    
    for i in range(0, len(data)):
        uniqueID = data['BankStreet'][i]
        currentYear = data['ApprovalDate'][i][:4]
        if (uniqueID in bankInfo):
            bankInfo[uniqueID] += (', '+currentYear)
        else:
            uniqueIDInfo[uniqueID] = data['BankName'][i]
            uniqueIDs.append(uniqueID)
            cbsa[uniqueID] = data['CBSA'][i]
            bankInfo[uniqueID] = currentYear
            
    for j in range(0, len(uniqueIDs)):
        for k in range(0, len(years)):
            yearChecked = years[k]
            if (uniqueIDs[j] in bankYearsMissing):
                if ((yearChecked in bankInfo[uniqueIDs[j]]) == False):
                    bankYearsMissing[uniqueIDs[j]] += (', ' + yearChecked)
            else:
                if ((yearChecked in bankInfo[uniqueIDs[j]]) == False):
                    bankYearsMissing[uniqueIDs[j]] = yearChecked
        if (uniqueIDs[j] in bankYearsMissing):           
            print(uniqueIDInfo[uniqueIDs[j]] + ': ' + bankYearsMissing[uniqueIDs[j]])

    for ID in bankYearsMissing.keys():
        if ((bankYearsMissing[ID].find('2014')!=-1) and (bankYearsMissing[ID].find('2015')!=-1)  and (bankYearsMissing[ID].find('2016')!=-1) and (bankYearsMissing[ID].find('2017')!=-1) and (bankYearsMissing[ID].find('2018')!=-1)):
            banksDropped[ID] = uniqueIDInfo[ID]
            print(banksDropped[ID])
    
def main():
    dataset = sys.argv[1]
    compute(dataset)

if __name__ == '__main__':
    main()
