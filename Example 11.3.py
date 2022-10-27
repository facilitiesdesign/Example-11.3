# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 10:22:03 2022

@author: grace_elizabeth
"""

from gurobipy import *

try:
    
    #Create lists
    f = [
        [0, 5, 4, 8],
        [12, 0, 6, 2],
        [8, 6, 0, 2],
        [3, 2, 2, 0]
        ]
    d = [
        [0, 1, 1, 2],
        [1, 0, 2, 1],
        [1, 2, 0, 1],
        [2, 1, 1, 0]
        ]
    
    #indices
    n = len(f)
    
    #Create model
    m = Model("Example 11.3")
    
    #Declare decision variables
    x = m.addVars(n, n, vtype = GRB.BINARY, name = "Assignment")
    
    #Set objective fuction
    m.setObjective(quicksum(f[i][k] * d[j][l] * x[i,j] * x[k,l] for i in range(n) for j in range(n) for k in range(n) for l in range(n)), GRB.MINIMIZE)
    
    #Write constraints
    for i in range(n):
        m.addConstr(quicksum(x[i,j] for j in range(n)) == 1, name = "Constraint 11.17")
    
    for j in range(n):
        m.addConstr(quicksum(x[i,j] for i in range(n)) == 1, name = "Constraint 11.18")
    
    # m.addConstr(x[0,2] == 0, name = "other 'optimal'?")
    # m.addConstr(x[0,0] == 0, name = "other 'optimal'?")
    # m.addConstr(x[0,3] == 0, name = "other 'optimal'?")
    # m.addConstr(x[1,0] == 0, name = "other 'optimal'?")
    

    #Call Gurobi Optimizer
    m.optimize()
    if m.status == GRB.OPTIMAL:
       for v in m.getVars():
           if v.x > 0:
               print('%s = %g' % (v.varName, v.x)) 
       print('Obj = %f' % m.objVal)
    elif m.status == GRB.INFEASIBLE:
       print('LP is infeasible.')
    elif m.status == GRB.UNBOUNDED:
       print('LP is unbounded.')
except GurobiError:
    print('Error reported')