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
    lastFourYears = ['2014', '2015', '2016','2017']
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

## The code below doesn't work. It's supposed to find the banks
## that have dropped out of the program.
            
    for m in range(0, len(uniqueIDs)):
        if (uniqueIDs[m] in bankYearsMissing):
            if set(lastFourYears).issubset(set(bankYearsMissing[uniqueIDs[m]])):
                banksDropped[uniqueIDs[m]] = uniqueIDInfo[uniqueIDs[m]]
                print(uniqueIDs[m] + ': ' + banksDropped[uniqueIDs[m]])
    
def main():
    dataset = sys.argv[1]
    compute(dataset)

if __name__ == '__main__':
    main()
