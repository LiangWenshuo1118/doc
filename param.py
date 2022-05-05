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

#Training
  
