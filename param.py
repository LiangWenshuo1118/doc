from context import dargs
from dargs import dargs, Argument, 

# basics
def type_map_args ():
    doc_type_map = 'Atom types.'
    
    return [
        Argument("type_map", List of string, optional = False, doc = doc_type_map)
    ]
  
def mass_map_args ():
    doc_mass_map = 'Standard atom weights.'
    
    return [
        Argument("mass_map", List of float, optional = False, doc = doc_mass_map)
    ]

def use_ele_temp_args ():
    doc_use_ele_temp = 'Currently only support fp_style vasp. \n\n\
- 0: no electron temperature. \n\n\
- 1: eletron temperature as frame parameter. \n\n\
- 2: electron temperature as atom parameter.'
    
    return [
        Argument("use_ele_temp", int, optional = False, default = 0, doc = doc_use_ele_temp)
    ]
  
from context import dargs
from dargs import dargs, Argument, 

def type_map_args ():
    doc_type_map = 'Atom types.'
    
    return [
        Argument("type_map", List of string, optional = False, doc = doc_type_map)
    ]
  
def mass_map_args ():
    doc_mass_map = 'Standard atom weights.'
    
    return [
        Argument("mass_map", List of float, optional = False, doc = doc_mass_map)
    ]

# Data
def init_data_prefix_args ():
    doc_init_data_prefix = 'Prefix of initial data directories.'
    
    return [
        Argument("init_data_prefix", String, optional = True, doc = doc_init_data_prefix)
    ]

def init_data_sys_args ():
    doc_init_data_sys = 'Directories of initial data. You may use either absolute or relative path here.'
    
    return [
        Argument("init_data_prefix", List of string, optional = False, doc = doc_init_data_sys)
    ]

def sys_format_args ():
    doc_sys_format = 'Format of initial data. It will be vasp/poscar if not set.'
    
    return [
        Argument("sys_format", String, optional = False, doc = doc_sys_format)
    ]

def init_multi_systems_args ():
    doc_init_multi_systems = 'If set to true, init_data_sys directories should contain sub-directories of various systems. DP-GEN will regard all of these sub-directories as inital data systems.'
    
    return [
        Argument("init_multi_systems", Boolean, optional = True, doc = doc_init_multi_systems)
    ]

def init_batch_size_args ():
    doc_init_batch_size = 'Each number is the batch_size of corresponding system for training in init_data_sys. One recommended rule for setting the sys_batch_size and init_batch_size is that batch_size mutiply number of atoms ot the stucture should be larger than 32. If set to auto, batch size will be 32 divided by number of atoms.'
    
    return [
        Argument("init_batch_size", String of integer, optional = True, doc = doc_init_batch_size)
    ]

def sys_configs_prefix_args ():
    doc_sys_configs_prefix = 'Prefix of sys_configs.'
    
    return [
        Argument("sys_configs_prefix", String, optional = True, doc = doc_sys_configs_prefix)
    ]

def sys_configs_args ():
    doc_sys_configs = 'Containing directories of structures to be explored in iterations.Wildcard characters are supported here.'
    
    return [
        Argument("sys_configs", String, optional = False, doc = doc_sys_configs)
    ]

def sys_batch_size_args ():
    doc_sys_batch_size = 'Each number is the batch_size for training of corresponding system in sys_configs. If set to auto, batch size will be 32 divided by number of atoms.'
    
    return [
        Argument("sys_batch_size", List of integer, optional = True, doc = doc_sys_batch_size)
    ]

# Training
def numb_models_args ():
    doc_numb_models = 'Number of models to be trained in 00.train. 4 is recommend.'
    
    return [
        Argument("numb_models", Integer, optional =False, doc = doc_numb_models)
    ]

def training_iter0_model_path_args ():
    doc_training_iter0_model_path = 'The model used to init the first iter training. Number of element should be equal to numb_models.'
    
    return [
        Argument("training_iter0_model_path", list of string, optional =True, doc = doc_training_iter0_model_path)
    ]
  

def training_init_model_args ():
    doc_training_init_model = 'Iteration > 0, the model parameters will be initilized from the model trained at the previous iteration. Iteration == 0, the model parameters will be initialized from training_iter0_model_path.'
    
    return [
        Argument("training_init_model", bool, optional =True, doc = doc_training_init_model)
    ]

def default_training_param_args ():
    doc_default_training_param = 'Training parameters for deepmd-kit in 00.train. You can find instructions from here: (https://github.com/deepmodeling/deepmd-kit).'
    
    return [
        Argument("default_training_param", Dict, optional =False, doc = doc_default_training_param)
    ]

def dp_compress_args ():
    doc_dp_compress = 'Use dp compress to compress the model.'
    
    return [
        Argument("dp_compress", bool, optional =True, default = false, doc = doc_dp_compress)
    ]

# Exploration
def model_devi_dt_args ():
    doc_model_devi_dt = 'Timestep for MD. 0.002 is recommend.'
    
    return [
        Argument("model_devi_dt", Float, optional =False, doc = doc_model_devi_dt)
    ]
		
def model_devi_skip_args ():
    doc_model_devi_skip = 'Number of structures skipped for fp in each MD.'
    
    return [
        Argument("model_devi_skip", Integer, optional =False, doc = doc_model_devi_skip)
    ]	

def model_devi_f_trust_lo_args ():
    doc_model_devi_f_trust_lo = 'Lower bound of forces for the selection. If List, should be set for each index in sys_configs, respectively.'
    
    return [
        Argument("model_devi_f_trust_lo", Float or List of float, optional =False, doc = doc_model_devi_f_trust_lo)
    ]

def model_devi_f_trust_hi_args ():
    doc_model_devi_f_trust_hi = 'Upper bound of forces for the selection. If List, should be set for each index in sys_configs, respectively.'
    
    return [
        Argument("model_devi_f_trust_hi", Float or List of float, optional =False, doc = doc_model_devi_f_trust_hi)
    ]

def model_devi_v_trust_lo_args ():
    doc_model_devi_v_trust_lo = 'Lower bound of virial for the selection. If List, should be set for each index in sys_configs, respectively. Should be used with DeePMD-kit v2.x.'
    
    return [
        Argument("model_devi_v_trust_lo", Float or List of float, optional =False, doc = doc_model_devi_v_trust_lo)
    ]

def model_devi_v_trust_hi_args ():
    doc_model_devi_v_trust_hi = 'Upper bound of virial for the selection. If List, should be set for each index in sys_configs, respectively. Should be used with DeePMD-kit v2.x.'
    
    return [
        Argument("model_devi_v_trust_hi", Float or List of float, optional =False, doc = doc_model_devi_v_trust_hi)
    ]

model_devi_adapt_trust_lo	Boolean	False	
Adaptively determines the lower trust levels of force and virial. This option should be used together with model_devi_numb_candi_f, model_devi_numb_candi_v and optionally with model_devi_perc_candi_f and model_devi_perc_candi_v. dpgen will make two sets: 1. From the frames with force model deviation lower than model_devi_f_trust_hi, select max(model_devi_numb_candi_f, model_devi_perc_candi_f*n_frames) frames with largest force model deviation. 2. From the frames with virial model deviation lower than model_devi_v_trust_hi, select max(model_devi_numb_candi_v, model_devi_perc_candi_v*n_frames) frames with largest virial model deviation. The union of the two sets is made as candidate dataset
