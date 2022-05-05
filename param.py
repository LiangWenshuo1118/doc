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
        Argument("model_devi_numb_candi_f", Int, optional =True, doc = doc_model_devi_numb_candi_f)
    ]

def model_devi_numb_candi_v_args ():
    doc_model_devi_numb_candi_v = 'See model_devi_adapt_trust_lo.'
    
    return [
        Argument("model_devi_numb_candi_v", Int, optional =True, doc = doc_model_devi_numb_candi_v)
    ]

def model_devi_perc_candi_f_args ():
    doc_model_devi_perc_candi_f = 'See model_devi_adapt_trust_lo.'
    
    return [
        Argument("model_devi_perc_candi_f", Float, optional =True, doc = doc_model_devi_perc_candi_f)

def model_devi_perc_candi_v_args ():
    doc_model_devi_perc_candi_v = 'See model_devi_adapt_trust_lo.'
    
    return [
        Argument("model_devi_perc_candi_v", Float, optional =True, doc = doc_model_devi_perc_candi_v)
    ]

def model_devi_f_avg_relative_args ():
    doc_model_devi_f_avg_relative = 'Normalized the force model deviations by the RMS force magnitude along the trajectory. This key should not be used with use_relative.'
    
    return [
        Argument("model_devi_f_avg_relative", Boolean, optional =True, doc = doc_model_devi_f_avg_relative)
    ]
	    
def model_devi_f_avg_relative_args ():
    doc_model_devi_f_avg_relative = 'Normalized the force model deviations by the RMS force magnitude along the trajectory. This key should not be used with use_relative.'
    
    return [
        Argument("model_devi_f_avg_relative", Boolean, optional =True, doc = doc_model_devi_f_avg_relative)
    ]

def model_devi_clean_traj_args ():
    doc_model_devi_clean_traj = 'If type of model_devi_clean_traj is boolean type then it denote whether to clean traj folders in MD since they are too large. If it is Int type, then the most recent n iterations of traj folders will be retained, others will be removed.'
    
    return [
        Argument("model_devi_clean_traj", Boolean or Int, optional =False, doc = doc_model_devi_clean_traj)
    ]

def model_devi_nopbc_args ():
    doc_model_devi_nopbc = 'Assume open boundary condition in MD simulations.'
    
    return [
        Argument("model_devi_nopbc", Boolean, optional =False, doc = doc_model_devi_nopbc)
    ]	    
	
def model_devi_activation_func_args ():
    doc_model_devi_activation_func = 'Set activation functions for models, length of the List should be the same as numb_models, and two elements in the list of string respectively assign activation functions to the embedding and fitting nets within each model. Backward compatibility: the orginal "List of String" format is still supported, where embedding and fitting nets of one model use the same activation function, and the length of the List should be the same as numb_models.'
    
    return [
        Argument("model_devi_activation_func", List of list of string, optional =True, doc = doc_model_devi_activation_func)
    ]		    

def model_devi_jobs_args():
    doc_sys_idx = 'Systems to be selected as the initial structure of MD and be explored. The index corresponds exactly to the sys_configs.'
    doc_temps = 'Temperature (K) in MD.'
    doc_press = 'Pressure (Bar) in MD.'
    doc_trj_freq = 'Frequecy of trajectory saved in MD.'
    doc_nsteps = 'Running steps of MD.'	
    doc_ensembles = 'Determining which ensemble used in MD, options include “npt” and “nvt”.'
    doc_neidelay = 'delay building until this many steps since last build.'	
    doc_taut = 'Coupling time of thermostat (ps).'
    doc_taup = 'Coupling time of barostat (ps).'

    args = [
        Argument("sys_idx", List of integer, optional = False, doc = doc_sys_idx),
        Argument("temps", List of integer, optional = False, default = 'set', doc = doc_temps),
        Argument("press", List of integer, optional = False, default = "prob_sys_size", doc = doc_press),
        Argument("trj_freq", Integer, optional = False, doc = doc_trj_freq),
        Argument("nsteps", Integer, optional = False, default = 'auto', doc = doc_nsteps),
        Argument("ensembles", String, optional = False, doc = doc_ensembles),
        Argument("neidelay", Integer, optional = True, doc = doc_neidelay),
        Argument("taut", Float, optional = True, default = 'log', doc = doc_taut),
        Argument("taup", Float, optional = True, default = 'log', doc = doc_taup),	    
    ]

    doc_model_devi_jobs = 'Settings for exploration in 01.model_devi. Each dict in the list corresponds to one iteration. The index of model_devi_jobs exactly accord with index of iterations'
    return Argument("model_devi_jobs", List of dict, args, [], doc = doc_model_devi_jobs)    
 
# Labeling
# VASP
def fp_style_VASP_args ():
    doc_fp_pp_path = 'Directory of psuedo-potential file to be used for 02.fp exists.'
    doc_fp_pp_files = 'Psuedo-potential file to be used for 02.fp. Note that the order of elements should correspond to the order in type_map.'
    doc_fp_incar = 'Input file for VASP. INCAR must specify KSPACING and KGAMMA.'
    doc_fp_aniso_kspacing = 'Set anisotropic kspacing. Usually useful for 1-D or 2-D materials. Only support VASP. If it is setting the KSPACING key in INCAR will be ignored.'
    doc_fp_pp_path = 'If cvasp is true, DP-GEN will use Custodian to help control VASP calculation.'
    
    return [
        Argument("fp_pp_path", String, optional =False, doc = doc_fp_pp_path),
        Argument("fp_pp_files", List of string, optional =False, doc = doc_fp_pp_files),
        Argument("fp_incar", String, optional =False, doc = doc_fp_incarc),
        Argument("fp_aniso_kspacing", List of integer, optional =False, doc = doc_fp_aniso_kspacing),
        Argument("cvasp", Boolean, optional =False, doc = doc_cvasp)
    ]		    

# Gaussian
def fp_params_Gaussian_args ():
    doc_keywords = 'Keywords for Gaussian input.'
    doc_multiplicity = 'Spin multiplicity for Gaussian input. If set to auto, the spin multiplicity will be detected automatically. If set to frag, the "fragment=N" method will be used.'
    doc_nproc = 'The number of processors for Gaussian input.'
	    
    return [
        Argument("doc_keywords", String or list, optional =False, doc = doc_keywords),
        Argument("multiplicity", Integer or String, optional =False, doc = doc_multiplicity),
        Argument("nproc", Integer, optional =False, doc = doc_nproc)
    ]	    
	    
def fp_style_Gaussian_args ():
    doc_use_clusters = 'If set to true, clusters will be taken instead of the whole system. This option does not work with DeePMD-kit 0.x.'
    doc_cluster_cutoff = 'The cutoff radius of clusters if use_clusters is set to true.'
    doc_fp_params_Gaussian = 'Parameters for Gaussian calculation.'
    
    return [
        Argument("use_clusters", Boolean, optional =False, doc = doc_use_clusters),
        Argument("cluster_cutoff", Float, optional =False, doc = doc_cluster_cutoff),
        Argument("fp_params", Dict, [], [fp_params_args_Gaussian ()],  optional =False, doc = doc_fp_params_Gaussian)
    ]	    
	    
# siesta
def fp_params_siesta_args ():
    doc_ecut = 'Define the plane wave cutoff for grid.'
    doc_ediff = 'Tolerance of Density Matrix.'
    doc_kspacing = 'Sample factor in Brillouin zones.'
    doc_mixingweight = 'Proportion a of output Density Matrix to be used for the input Density Matrix of next SCF cycle (linear mixing).'
    doc_NumberPulay = 'Controls the Pulay convergence accelerator.'

    return [
        Argument("ecut", Integer, optional =False, doc = doc_ecut),
        Argument("ediff", Float, optional =False, doc = doc_ediff),
        Argument("kspacing", Float, optional =False, doc = doc_kspacing),
        Argument("mixingweight", Float, optional =False, doc = doc_mixingweight),	    
        Argument("NumberPulay", Integer, optional =False, doc = doc_NumberPulay)
    ]	    
	    
def fp_style_siesta_args ():
    doc_use_clusters = 'If set to true, clusters will be taken instead of the whole system. This option does not work with DeePMD-kit 0.x.'
    doc_cluster_cutoff = 'The cutoff radius of clusters if use_clusters is set to true.'
    doc_fp_params_siesta = 'Parameters for siesta calculation.'
    
    return [
        Argument("use_clusters", Boolean, optional =False, doc = doc_use_clusters),
        Argument("cluster_cutoff", Float, optional =False, doc = doc_cluster_cutoff),
        Argument("fp_params", Dict, [], [fp_params_args_siesta ()], optional =False, doc = doc_fp_params_siesta)
    ]	

# cp2k
def fp_style_cp2k_args ():
    doc_user_fp_params = 'Parameters for cp2k calculation. find detail in manual.cp2k.org. only the kind section must be set before use. we assume that you have basic knowledge for cp2k input.'
    doc_external_input_path = 'Conflict with key:user_fp_params, use the template input provided by user, some rules should be followed, read the following text in detail.'
    
    return [
        Argument("user_fp_params", Dict, optional =False, doc = doc_user_fp_params),
        Argument("external_input_path", String, optional =False, doc = doc_external_input_path)
    ]	
			    


def model_devi_nopbc_args ():
    doc_model_devi_nopbc = 'Assume open boundary condition in MD simulations.'
    
    return [
        Argument("model_devi_nopbc", Boolean, optional =False, doc = model_devi_nopbc)
    ]	    


fp_style	string	"vasp"	Software for First Principles. Options include “vasp”, “pwscf”, “siesta” and “gaussian” up to now.
fp_task_max	Integer	20	Maximum of structures to be calculated in 02.fp of each iteration.
fp_task_min	Integer	5	Minimum of structures to calculate in 02.fp of each iteration.
fp_accurate_threshold	Float	0.9999	If the accurate ratio is larger than this number, no fp calculation will be performed, i.e. fp_task_max = 0.
fp_accurate_soft_threshold	Float	0.9999	If the accurate ratio is between this number and fp_accurate_threshold, the fp_task_max linearly decays to zero.
fp_cluster_vacuum	Float	None	If the vacuum size is smaller than this value, this cluster will not be choosen for labeling
 
	
