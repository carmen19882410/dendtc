from netpyne import specs

# Simulation options
cfg = specs.SimConfig()		# object of class SimConfig to store simulation configuration

cfg.duration = 2000 			# Duration of the simulation, in ms
cfg.dt = 0.025 				# Internal integration timestep to use
cfg.verbose = True  			# Show detailed messages
cfg.recordStim = True
#cfg.recordCells = ['TC']
cfg.recordTraces = {'V_soma':{'sec':'soma_0', 'loc': 0.5, 'var':'v'}}  # Dict with traces to record
cfg.recordStep = 0.1 			# Step size in ms to save data (eg. V traces, LFP, etc)
cfg.filename = 'Carmen_mod_swc'  # Set file output name
cfg.saveJson = True 	
cfg.printPopAvgRates = True
cfg.analysis['plotRaster'] = {'saveFig': True} 			# Plot a raster
cfg.analysis['plotTraces'] = {'include': [0], 'saveFig': True} 			# Plot recorded traces for this list of cells

# Variable parameters (used in netParams)
cfg.synMechTau2 = 5
cfg.connWeight = 1
cfg.hParams.celsius = 34 # change temperature at which sim is made 
cfg.hParams.v_init = -74 # change v init 