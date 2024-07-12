# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 21:20:00 2024

@author: gbulb
"""

n=10
dict_edges={1:2,2:8,4:10,5:9,6:10,7:9}
class min_edges_needed:
    def dict_to_edges(dict_edges,n):
        num_of_edges=len(dict_edges.items())
        min_edges=n-1
        discrepancy=min_edges-num_of_edges
        return discrepancy
if __name__=="__main__":
   print(min_edges_needed.dict_to_edges(dict_edges,n))
