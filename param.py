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

def use_ele_temp_args ():
    doc_use_ele_temp = 'Currently only support fp_style vasp. \n\n\
- 0: no electron temperature. \n\n\
- 1: eletron temperature as frame parameter. \n\n\
- 2: electron temperature as atom parameter.'
    
    return [
        Argument("use_ele_temp", int, optional = False, default = 0, doc = doc_use_ele_temp)
    ]
  
