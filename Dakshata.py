# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 21:28:25 2019

@author: Dakshata PC
"""
from xml.etree import ElementTree as ET

        
def main():
    cod_list = list()
    tree = ET.parse('A.xml')
    root = tree.getroot()
    
    data = root.find('data_rows')
    
    for data_row in data:

        dictionary = process_row(data_row)
        cod_list.append(dictionary)
    
    print_rows(cod_list)
    
    
def process_row(row):
     result = {}
     for item in row:
         
          if(item.tag == 'year'):
              rec_ey = 'YEAR'
              rec_value = item.text
          elif(item.tag == '_113_cause_name'):
              rec_ey = '_113 CAUSENAME'
              rec_value = item.text
          elif(item.tag == 'cause_name'):
              rec_ey = 'CAUSE_NAME'
              rec_value = item.text
          elif(item.tag == 'state'):
              rec_ey = 'STATE'
              rec_value = item.text
          elif(item.tag == 'deaths'):
              rec_ey = 'DEATHS'
              rec_value = item.text
          elif(item.tag == 'aadr'):
              rec_ey = 'AADR'
              rec_value = item.text
              
          result[rec_ey] = rec_value
         
     return result
    
def print_rows(row_list):
    print(row_list)
    
if __name__ == '__main__':
    main()