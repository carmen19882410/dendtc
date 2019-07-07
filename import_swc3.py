
#%%

# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 20:33:29 2019

@author: René, Adna and Carmen
"""
import os
wdir=os.getcwd()

from netpyne.support import morphology
from netpyne import sim
from neuron import h
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import platform
import neuron as nrn
if platform.system() == 'Windows':
    nrn.load_mechanisms(os.path.join(wdir + 'Morph_practice', 'modfiles'))
    import sys
    sys.path.append('C:', 'nrn', 'lib', 'python')
    sys.path.append('D:', 'Okinawa', 'Python')
    sys.path.append(wdir + 'Morph_practice', 'modfiles')

#load cell as mycell
#    def getmorph(self):
myCell= morphology.Cell()
morphology.load(filename=os.path.join(wdir,'SWC', 'MN_morphology.swc'), cell=myCell)

#h.load_file('import3d.hoc')
#myCell = h.Import3d_SWC_read()
#myCell.input('SWC/AA_0266.swc')
#i3d = h.Import3d_GUI(myCell, 0)
#i3d.instantiate(None)


#import neuron as h
#myCell = h.read.swc('SWC/MN_morphology.swc')
#read.ngraph.swc('SWC/MN_morphology.swc', weights = FALSE, directed = TRUE)



#plot loaded cell
fig = plt.figure()
ax = plt.axes(projection='3d')
morphology.shapeplot(h, ax)
           
#get the sections from the cell
secs=list(h.allsec());
secs_all = secs
soma = []
axon = []
dend = []


    #get the sections fro soma, axon and dend
    #def getset(self):
for sec in secs:
    name = sec.name()   
    if name[0:4] == 'soma':
        soma.append(sec)
    if name[0:4] == 'axon':
        axon.append(sec)
    if name[0:4] == 'dend':
        dend.append(sec)


corrD = 1			# no dendritic surface correction

G_pas = 3.79e-5
E_pas = -73			# to fit current-clamp data (was -71 to -73)
E_pas = -76.5			# within 3 mV error




class TC_cell():

    def __init__(self):
            
            self.add_biophys_all()
            self.add_biophys_axon()
            self.add_biophys_soma()
            self.add_biophys_dend()
            #self.getmorph()
            #self.getset()
    
    def add_biophys_all(self):
        for sec in secs_all:
            sec.Ra = 173 #add a axial resistance of 100ohm per square cm
            #sec.cm = 0.8 # Membrane capacitance in micro Farads / cm^2
            sec.insert('pas')
            sec.g_pas = G_pas * corrD
            sec.e_pas = E_pas
            sec.cm = 0.88 * corrD
            #L = L
            
            # insert t-type calcium channel
            sec.insert('itGHK')		# T-current everywhere
            sec.cai = 2.4e-4 
            sec.cao = 2 
            sec.eca = 120 
            sec.shift_itGHK = -1	# screening charge shift + 3 mV error
            #sec.gcabar_itGHK = corrD * 0.0002 ##check why this doesnt work!!!!!!!!!!!!!!!
            sec.qm_itGHK = 2.5   ##check why this doesnt work!!!!!!!!!!!!!!!!!!
            #sec.qh_itGHK = 2.5     ##check why this doesnt work!!!!!!!!!!!!!!

            #insert calcium diffusion
            sec.insert('cad')		# calcium diffusion everywhere
            sec.depth_cad = 0.1 * corrD
            sec.kt_cad = 0		# no pump
            sec.kd_cad = 1e-4
            sec.taur_cad = 5
            sec.cainf_cad = 2.4e-4	
	
	

    #give the cell biphys props
    def add_biophys_soma(self):       
        for sec in soma:
            sec.cm = 0.88
            sec.g_pas = G_pas
            sec.insert('hh2')		# insert fast spikes
            sec.ena = 50
            sec.ek = -100
            sec.vtraub_hh2 = -52
            sec.gnabar_hh2 = 0.1
            sec.gkbar_hh2 = 0.1

            #sec.insert('hh')
            #sec.insert('na')
            #sec.insert('kv')
            
    
    def add_biophys_axon(self):   
        for sec in axon:
            sec.insert('hh2')		# insert fast spikes
            sec.ena = 50
            sec.ek = -100
            sec.vtraub_hh2 = -52
            sec.gnabar_hh2 = 0.1
            sec.gkbar_hh2 = 0.1
            
            #sec.insert('hh')
            #sec.insert('na')
            #sec.insert('kv')
        #axon[0].gnabar_hh2 = 0.5
            
            
    def add_biophys_dend(self):       
        for sec in dend:
            sec.insert('pas')
        
    add_biophys_all(secs_all)     
    add_biophys_soma(soma)
    add_biophys_axon(axon)
    add_biophys_dend(dend)


def MakeCell():
    TC = TC_cell()
    return TC
