.. _`type_map`:

type_map:
    | type: List of string
    | argument path:
    | example：["H", "C"]
    
    Atom types.
    
.. _`mass_map`:

mass_map:
    | type: mass_map
    | argument path: 
    | example：[1, 12]
    
    Standard atom weights.   

.. _`use_ele_temp`:

use_ele_temp:
    | type: int
    | argument path: 
    | example：0
    
    Currently only support fp_style vasp. 0(default): no electron temperature. 1: eletron temperature as frame parameter. 2: electron temperature as atom parameter.  

.. _`init_data_prefix`:

init_data_prefix:
    | type: String, optional
    | argument path: 
    | example："/sharedext4/.../data/"
    
    Prefix of initial data directories.

.. _`init_data_sys`:

init_data_sys:
    | type: List of string
    | argument path: 
    | example：["CH4.POSCAR.01x01x01/.../deepmd"]
    
    Directories of initial data. You may use either absolute or relative path here.
    
.. _`sys_format`:

sys_format:
    | type: String
    | argument path: 
    | example："vasp/poscar"
    
    Format of initial data. It will be `vasp/poscar` if not set.
    
.. _`init_multi_systems`:

init_multi_systems:
    | type: Boolean, optional
    | argument path: 
    | example：false
    
    If set to `true`, `init_data_sys` directories should contain sub-directories of various systems. DP-GEN will regard all of these sub-directories as inital data systems.    

.. _`init_batch_size`:

init_batch_size:
    | type: String of integer, optional
    | argument path: 
    | example：[8]  
    
    Each number is the batch_size of corresponding system  for training in `init_data_sys`. One recommended rule for setting the `sys_batch_size` and `init_batch_size` is that `batch_size` mutiply number of atoms ot the stucture should be larger than 32. If set to `auto`, batch size will be 32 divided by number of atoms.   
 
.. _`sys_configs_prefix`:

sys_configs_prefix:
    | type: String, optional
    | argument path: 
    | example："/sharedext4/.../data/"  
    
    Prefix of `sys_configs`
    
.. _`numb_models`:

numb_models:
    | type: Integer
    | argument path: 
    | example：4 (recommend)  
    
    Number of models to be trained in `00.train`.  
 
.. _`training_iter0_model_path`:

training_iter0_model_path:
    | type: list of string, optional
    | argument path: 
    | example：["/path/to/model0_ckpt/", ...]  
    
    The model used to init the first iter training. Number of element should be equal to `numb_models`. 
    
.. _`training_init_model`:

training_iter0_model_path:
    | type: Boolean, optional
    | argument path: 
    | example：False  
    
    Iteration > 0, the model parameters will be initilized from the model trained at the previous iteration. Iteration == 0, the model parameters will be initialized from `training_iter0_model_path`. 
    
.. _`default_training_param`:

default_training_param:
    | type: Dict
    | argument path: 
    | example：
    
    Training parameters for `deepmd-kit` in `00.train`. You can find instructions from here: (https://github.com/deepmodeling/deepmd-kit).
    
.. _`dp_compress`:

dp_compress:
    | type: Boolean, optional
    | argument path: 
    | example：false
    
    Use `dp compress` to compress the model. Default is false.     

.. _`model_devi_dt`:

model_devi_dt:
    | type: Float
    | argument path: 
    | example：0.002 (recommend)
    
    Timestep for MD.
    
.. _`model_devi_skip`:

model_devi_skip:
    | type: Integer
    | argument path: 
    | example：0
    
    Number of structures skipped for fp in each MD.  

.. _`model_devi_f_trust_lo`:

model_devi_f_trust_lo:
    | type: Float or List of float
    | argument path: 
    | example：0.05
    
    Lower bound of forces for the selection. If List, should be set for each index in `sys_configs`, respectively.  
    
.. _`model_devi_f_trust_hi`:

model_devi_f_trust_hi:
    | type: Float or List of float
    | argument path: 
    | example：0.15
    
    Upper bound of forces for the selection. If List, should be set for each index in `sys_configs`, respectively.
    
.. _`model_devi_v_trust_lo`:

model_devi_v_trust_lo:
    | type: Float or List of float
    | argument path: 
    | example：1e10
    
    Lower bound of virial for the selection. If List, should be set for each index in `sys_configs`, respectively. Should be used with DeePMD-kit v2.x.    

.. _`model_devi_v_trust_hi`:

model_devi_v_trust_hi:
    | type: Float or List of float
    | argument path: 
    | example：1e10
    
    Upper bound of virial for the selection. If List, should be set for each index in `sys_configs`, respectively. Should be used with DeePMD-kit v2.x. 

.. _`model_devi_adapt_trust_lo`:

model_devi_adapt_trust_lo:
    | type: Boolean, optional
    | argument path: 
    | example：False
    
    Adaptively determines the lower trust levels of force and virial. This option should be used together with `model_devi_numb_candi_f`,  `model_devi_numb_candi_v` and optionally with `model_devi_perc_candi_f` and `model_devi_perc_candi_v`. `dpgen` will make two sets: 1. From the frames with force model deviation lower than `model_devi_f_trust_hi`, select `max(model_devi_numb_candi_f, model_devi_perc_candi_f*n_frames)` frames with largest force model deviation. 2. From the frames with virial model deviation lower than `model_devi_v_trust_hi`, select `max(model_devi_numb_candi_v, model_devi_perc_candi_v*n_frames)` frames with largest virial model deviation. The union of the two sets is made as candidate dataset.

.. _`model_devi_numb_candi_f`:

model_devi_numb_candi_f:
    | type: Integer, optional
    | argument path: 
    | example：10
    
    See `model_devi_adapt_trust_lo`.


.. _`model_devi_numb_candi_v`:

model_devi_numb_candi_v:
    | type: Integer, optional
    | argument path: 
    | example：0
    
    See `model_devi_adapt_trust_lo`.

.. _`model_devi_perc_candi_f`:

model_devi_perc_candi_f:
    | type: Float, optional
    | argument path: 
    | example：0.0
    
    See `model_devi_adapt_trust_lo`.


.. _`model_devi_perc_candi_v`:

model_devi_perc_candi_v:
    | type: Float, optional
    | argument path: 
    | example：0.0
    
    See `model_devi_adapt_trust_lo`.

.. _`model_devi_f_avg_relative`:

model_devi_f_avg_relative:
    | type: Boolean, optional
    | argument path: 
    | example：False
    
    Normalized the force model deviations by the RMS force magnitude along the trajectory. This key should not be used with `use_relative`.

.. _`model_devi_clean_traj`:

model_devi_clean_traj:
    | type: Boolean or Int
    | argument path: 
    | example：true
    
    If type of model_devi_clean_traj is boolean type then it denote whether to clean traj folders in MD since they are too large. If it is Int type, then the most recent n iterations of traj folders will be retained, others will be removed.
    
.. _`model_devi_nopbc`:

model_devi_nopbc:
    | type: Boolean 
    | argument path: 
    | example：False   
    
    Assume open boundary condition in MD simulations.

.. _`model_devi_activation_func`:

model_devi_activation_func:
    | type: List of list of string, optional
    | argument path: 
    | example：[["tanh","tanh"],["tanh","gelu"],["gelu","tanh"],["gelu","gelu"]]  
    
    Set activation functions for models, length of the List should be the same as `numb_models`, and two elements in the list of string respectively assign activation functions to the embedding and fitting nets within each model. *Backward compatibility*: the orginal "List of String" format is still supported, where embedding and fitting nets of one model use the same activation function, and the length of the List should be the same as `numb_models`.

.. _`model_devi_jobs`:

model_devi_jobs:
    | type: List of dict
    | argument path: 
    | example：["{sys_idx": [0], "temps": [100], "press":[1], "trj_freq":10, "nsteps":1000, "ensembles":"nvt"},...]   
    
    Settings for exploration in `01.model_devi`. Each dict in the list corresponds to one iteration. The index of `model_devi_jobs` exactly accord with index of iterations.
    
    .. _`model_devi_jobs/sys_idx`:
    
    sys_idx:
        | type: List of integer
        | argument path:
        | example：[0]
        
        Systems to be selected as the initial structure of MD and be explored. The index corresponds exactly to the `sys_configs`.

    .. _`model_devi_jobs/temps`:
    
    temps:
        | type: List of integer
        | argument path:
        | example：[50, 300]
        
        Temperature (**K**) in MD.

    .. _`model_devi_jobs/press`:
    
    press:
        | type: List of integer
        | argument path:
        | example： [1,10] 
        
        Pressure (**Bar**) in MD.

    .. _`model_devi_jobs/trj_freq`:
    
    trj_freq:
        | type: Integer
        | argument path:
        | example： 10  
        
        Frequecy of trajectory saved in MD.
        
    .. _`model_devi_jobs/nsteps`:
    
    nsteps:
        | type: Integer
        | argument path:
        | example： 3000   
        
        Running steps of MD.
        
    .. _`model_devi_jobs/nsteps`:
    
    nsteps:
        | type: String
        | argument path:
        | example： "nvt"    
        
        Determining which ensemble used in MD, **options** include “npt” and “nvt”.  

    .. _`model_devi_jobs/neidelay`:
    
    neidelay:
        | type: Integer, optional
        | argument path:
        | example： 10    
        
        Delay building until this many steps since last build.  

    .. _`model_devi_jobs/taut`:
    
    taut:
        | type: Float, optional
        | argument path:
        | example： "0.1"   
        
        Coupling time of thermostat (ps).  

    .. _`model_devi_jobs/taup`:
    
    taup:
        | type: Float, optional
        | argument path:
        | example： "0.5"   
        
        Coupling time of barostat (ps).  
