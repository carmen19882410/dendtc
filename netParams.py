from netpyne import specs, sim

try:
	from __main__ import cfg  # import SimConfig object with params from parent module
except:
	from cfg import cfg  # if no simConfig in parent module, import directly from tut8_cfg module

# Network parameters
netParams = specs.NetParams()  # object of class NetParams to store the network parameters


################################################################################################
## Population parameters
################################################################################################


#netParams.popParams['S'] = {'cellType': 'PYR', 'numCells': 20, 'cellModel': 'HH'}
#netParams.popParams['M'] = {'cellType': 'PYR', 'numCells': 20, 'cellModel': 'HH'}

#netParams.popParams['CN'] = {'cellType': 'CN', 'numCells': 1, 'cellModel': 'HH'}
#netParams.defaultThreshold = -10.0
netParams.popParams['TC'] = {'cellType': 'TC_cell', 'numCells': 1, 'cellModel': 'HH'}

#netParams.popParams['CA_229hoc'] = {'cellType': 'DET', 'numCells': 1, 'cellModel': 'blank'}



################################################################################################
## Cell property rules
################################################################################################

#cellRule = netParams.importCellParams(label = 'CN', conds = {'pop': 'CN'} , fileName = 'import_swc3.py', cellName = 'MakeCell', importSynMechs=True)
cellRule = netParams.importCellParams(label = 'TC_cell', conds = {'pop': 'TC'} , fileName = 'import_swc3.py', cellName = 'MakeCell', importSynMechs=True)
#cellRule = netParams.importCellParams(label = 'CA_229hoc', conds = {'pop': 'CA_229hoc'} , fileName = 'cells/CA_229.hoc', cellName = '', importSynMechs=False)


#cellRule = {'conds': {'cellType': 'PYR'},  'secs': {}} 	# cell rule dict, make an new matrix called secs, in which the data will be spit
#cellRule['secs']['soma'] = {'geom': {}, 'mechs': {}}  														# soma params dict
#cellRule['secs']['soma']['geom'] = {'diam': 18.8, 'L': 18.8, 'Ra': 123.0}  			# big dictionary with all the values we want to add into the model						# soma geometry
#cellRule['secs']['soma']['mechs']['hh'] = {'gnabar': 0.12, 'gkbar': 0.036, 'gl': 0.003, 'el': -70}  		# soma hh mechanism
#netParams.cellParams['PYRrule'] = cellRule  
												# add dict to list of cell params



################################################################################################
# Stimulation parameters
################################################################################################
    

#netParams.stimSourceParams['CB_syn'] = {'type': 'AlphaSynapse', 'onset': 'uniform(300,600)', 'tau': 5, 'gmax': 'post_ynorm', 'e': 0}
#netParams.stimTargetParams['CB_syn->TC'] = {'source': 'CB_syn', 'sec':'soma', 'loc': 0.5, 'conds': {'pop':'TC'}}

netParams.stimSourceParams['pulse_TC'] = {'type': 'IClamp', 'del':200, 'dur':200, 'amp':0.02} #ms  nA
netParams.stimTargetParams['pulse->TC'] = {'source': 'pulse_TC', 'conds': {'cellType': 'TC_cell'}, 'sec':'soma_0', 'loc':0.5}

#netParams.stimSourceParams['pulse_CN_IClamp'] = {'type': 'IClamp', 'del':50, 'dur':10, 'amp':2} #ms  nA
#netParams.stimTargetParams['pulse->CN'] = {'source': 'pulse_CN_IClamp', 'conds': {'cellType': 'CN'}, 'sec':'soma_0', 'loc':0.5}

#netParams.stimSourceParams['pulse_CN'] = {'type': 'NetStim', 'rate': 150, 'noise': 10}
#netParams.stimTargetParams['pulse->CN'] = {'source': 'pulse_CN', 'conds': {'cellType': 'CN'}, 'sec':'soma_0', 'loc':0.5}
#netParams.stimTargetParams['pulse_CN->CN'] = {'source': 'pulse_CN', 'conds': {'cellType': 'CN'}, 'weight': 0.001, 'delay': 100, 'synMech': 'exc'}
#netParams.stimSourceParams['Input_4'] = {'type': 'NetStim', 'interval': 'uniform(20,100)', 'number': 1000, 'start': 600, 'noise': 0.1}




################################################################################################
## Synaptic mechanism parameters, most of them get imported from somewhere else
################################################################################################

#netParams.synMechParams['exc'] = {'mod': 'Exp2Syn', 'tau1': 0.1, 'tau2': cfg.synMechTau2, 'e': 0}  # excitatory synaptic mechanism
#netParams.synMechParams['inh'] = {'mod': 'Exp2Syn', 'tau1': 0.6, 'tau2': 8.5, 'e': -75}  # GABA synaptic mechanism



################################################################################################
## Cell connectivity rules
################################################################################################

#netParams.connParams['CN->TC'] = { 	#  S -> M label
	#'preConds': {'pop': 'CN'}, 	# conditions of presyn cells
	#'postConds': {'pop': 'TC'}, # conditions of postsyn cells
	#'probability': 1, 			# probability of connection
	#'weight': cfg.connWeight, 		# synaptic weight
	#'delay': 0,						# transmission delay (ms)
	#'synMech': 'exc',                   #synaptic mechanism
    #'loc': [0.4, 0.7],                   #location of synapses that make a connection
    #'synsPerConn': 10}                  #number of synapses

    



