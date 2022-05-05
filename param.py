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

def model_devi_adapt_trust_lo_args ():
    doc_model_devi_adapt_trust_lo = 'Adaptively determines the lower trust levels of force and virial. This option should be used together with model_devi_numb_candi_f, model_devi_numb_candi_v and optionally with model_devi_perc_candi_f and model_devi_perc_candi_v. dpgen will make two sets:\n\n\
- 1. From the frames with force model deviation lower than model_devi_f_trust_hi, select max(model_devi_numb_candi_f, model_devi_perc_candi_f*n_frames) frames with largest force model deviation. \n\n\
- 2. From the frames with virial model deviation lower than model_devi_v_trust_hi, select max(model_devi_numb_candi_v, model_devi_perc_candi_v*n_frames) frames with largest virial model deviation. \n\n\
The union of the two sets is made as candidate dataset.'
    
    return [
        Argument("model_devi_adapt_trust_lo", Boolean, optional =True, doc = doc_model_devi_adapt_trust_lo)
    ]

def model_devi_numb_candi_f_args ():
    doc_model_devi_numb_candi_f = 'See model_devi_adapt_trust_lo.'
    
    return [
        Argument("model_devi_numb_candi_f", Int, optional =True, doc = model_devi_numb_candi_f)
    ]

def model_devi_numb_candi_v_args ():
    doc_model_devi_numb_candi_v = 'See model_devi_adapt_trust_lo.'
    
    return [
        Argument("model_devi_numb_candi_v", Int, optional =True, doc = model_devi_numb_candi_v)
    ]

def model_devi_perc_candi_f_args ():
    doc_model_devi_perc_candi_f = 'See model_devi_adapt_trust_lo.'
    
    return [
        Argument("model_devi_perc_candi_f", Float, optional =True, doc = model_devi_perc_candi_f)

def model_devi_perc_candi_v_args ():
    doc_model_devi_perc_candi_v = 'See model_devi_adapt_trust_lo.'
    
    return [
        Argument("model_devi_perc_candi_v", Float, optional =True, doc = model_devi_perc_candi_v)
    ]

def model_devi_f_avg_relative_args ():
    doc_model_devi_f_avg_relative = 'Normalized the force model deviations by the RMS force magnitude along the trajectory. This key should not be used with use_relative.'
    
    return [
        Argument("model_devi_f_avg_relative", Boolean, optional =True, doc = model_devi_f_avg_relative)
    ]
	    
def model_devi_f_avg_relative_args ():
    doc_model_devi_f_avg_relative = 'Normalized the force model deviations by the RMS force magnitude along the trajectory. This key should not be used with use_relative.'
    
    return [
        Argument("model_devi_f_avg_relative", Boolean, optional =True, doc = model_devi_f_avg_relative)
    ]

def model_devi_clean_traj_args ():
    doc_model_devi_clean_traj = 'If type of model_devi_clean_traj is boolean type then it denote whether to clean traj folders in MD since they are too large. If it is Int type, then the most recent n iterations of traj folders will be retained, others will be removed.'
    
    return [
        Argument("model_devi_clean_traj", Boolean or Int, optional =False, doc = model_devi_clean_traj)
    ]

def model_devi_nopbc_args ():
    doc_model_devi_nopbc = 'Assume open boundary condition in MD simulations.'
    
    return [
        Argument("model_devi_nopbc", Boolean, optional =False, doc = model_devi_nopbc)
    ]	    
	
def model_devi_activation_func_args ():
    doc_model_devi_activation_func = 'Set activation functions for models, length of the List should be the same as numb_models, and two elements in the list of string respectively assign activation functions to the embedding and fitting nets within each model. Backward compatibility: the orginal "List of String" format is still supported, where embedding and fitting nets of one model use the same activation function, and the length of the List should be the same as numb_models.'
    
    return [
        Argument("model_devi_activation_func", List of list of string, optional =True, doc = model_devi_activation_func)
    ]		    

	def training_args():
    link_sys = make_link("systems", "training/systems")
    doc_systems = 'The data systems. This key can be provided with a listthat specifies the systems, or be provided with a string by which the prefix of all systems are given and the list of the systems is automatically generated.'
    doc_set_prefix = f'The prefix of the sets in the {link_sys}.'
    doc_stop_batch = 'Number of training batch. Each training uses one batch of data.'
    doc_batch_size = f'This key can be \n\n\
- list: the length of which is the same as the {link_sys}. The batch size of each system is given by the elements of the list.\n\n\
- int: all {link_sys} use the same batch size.\n\n\
- string "auto": automatically determines the batch size so that the batch_size times the number of atoms in the system is no less than 32.\n\n\
- string "auto:N": automatically determines the batch size so that the batch_size times the number of atoms in the system is no less than N.'
    doc_seed = 'The random seed for getting frames from the training data set.'
    doc_disp_file = 'The file for printing learning curve.'
    doc_disp_freq = 'The frequency of printing learning curve.'
    doc_numb_test = 'Number of frames used for the test during training.'
    doc_save_freq = 'The frequency of saving check point.'
    doc_save_ckpt = 'The file name of saving check point.'
    doc_disp_training = 'Displaying verbose information during training.'
    doc_time_training = 'Timing durining training.'
    doc_profiling = 'Profiling during training.'
    doc_profiling_file = 'Output file for profiling.'
    doc_train_auto_prob_style = 'Determine the probability of systems automatically. The method is assigned by this key and can be\n\n\
- "prob_uniform"  : the probability all the systems are equal, namely 1.0/self.get_nsystems()\n\n\
- "prob_sys_size" : the probability of a system is proportional to the number of batches in the system\n\n\
- "prob_sys_size;stt_idx:end_idx:weight;stt_idx:end_idx:weight;..." : the list of systems is devided into blocks. A block is specified by `stt_idx:end_idx:weight`, where `stt_idx` is the starting index of the system, `end_idx` is then ending (not including) index of the system, the probabilities of the systems in this block sums up to `weight`, and the relatively probabilities within this block is proportional to the number of batches in the system.'
    doc_train_sys_probs = "A list of float, should be of the same length as `train_systems`, specifying the probability of each system."
    doc_tensorboard = 'Enable tensorboard'
    doc_tensorboard_log_dir = 'The log directory of tensorboard outputs'

    args = [
        Argument("systems", [list,str], optional = False, doc = doc_systems, alias = ["trn_systems"]),
        Argument("set_prefix", str, optional = True, default = 'set', doc = doc_set_prefix),
        Argument("auto_prob", str, optional = True, default = "prob_sys_size", doc = doc_train_auto_prob_style, alias = ["trn_auto_prob", "auto_prob_style"]),
        Argument("sys_probs", list, optional = True, default = None, doc = doc_train_sys_probs, alias = ["trn_sys_probs"]),
        Argument("batch_size", [list,int,str], optional = True, default = 'auto', doc = doc_batch_size, alias = ["trn_batch_size"]),
        Argument("numb_steps", int, optional = False, doc = doc_stop_batch, alias = ["stop_batch"]),
        Argument("seed", [int,None], optional = True, doc = doc_seed),
        Argument("disp_file", str, optional = True, default = 'lcueve.out', doc = doc_disp_file),
        Argument("disp_freq", int, optional = True, default = 1000, doc = doc_disp_freq),
        Argument("numb_test", [list,int,str], optional = True, default = 1, doc = doc_numb_test),
        Argument("save_freq", int, optional = True, default = 1000, doc = doc_save_freq),
        Argument("save_ckpt", str, optional = True, default = 'model.ckpt', doc = doc_save_ckpt),
        Argument("disp_training", bool, optional = True, default = True, doc = doc_disp_training),
        Argument("time_training", bool, optional = True, default = True, doc = doc_time_training),
        Argument("profiling", bool, optional = True, default = False, doc = doc_profiling),
        Argument("profiling_file", str, optional = True, default = 'timeline.json', doc = doc_profiling_file),
        Argument("tensorboard", bool, optional = True, default = False, doc = doc_tensorboard),
        Argument("tensorboard_log_dir", str, optional = True, default = 'log', doc = doc_tensorboard_log_dir),
    ]

    doc_training = 'The training options'
    return Argument("training", dict, args, [], doc = doc_training)    
 
