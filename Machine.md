## Set up machine
### new dpdispatcher update note
dpdispatcher Update Note: 
dpdispatcher has updated and the api of `machine.json` is changed.
dpgen will use new dpdispatcher if the key `api_version` in dpgen's `machine.json`'s value is equal or large than `1.0`.

And dpgen will use old dpdispatcher if the key `api_version` is not specified in `machine.json` or the `api_version` is smaller than `1.0`.
This gurantees that the old `machine.json`s still work.

And for now dpdispatcher is maintained on a seperate repo. 
The repo link: https://github.com/deepmodeling/dpdispatcher

The api of new dpdispatcher is close to old one except for a few changes. 

The new `machine.json` examples can be seen [here](https://docs.deepmodeling.org/projects/dpdispatcher/en/latest/getting-started.html)

And Here are the explanations of the keys in [machine](https://docs.deepmodeling.org/projects/dpdispatcher/en/latest/machine.html)
[resources](https://docs.deepmodeling.org/projects/dpdispatcher/en/latest/resources.html).


Here is a example `machine.json` for dpgen's new dpdispatcher.
Please check the [documents](https://deepmd.readthedocs.io/projects/dpdispatcher/en/latest/) for more information about new dpdispatcher. 

an example of new dpgen's machine.json
```json
{
  "api_version": "1.0",
  "train": [
    {
      "command": "dp",
      "machine": {
        "batch_type": "PBS",
        "context_type": "SSHContext",
        "local_root": "./",
        "remote_root": "/home/user1234/work_path_dpdispatcher_test",
        "remote_profile": {
            "hostname": "39.xxx.xx.xx",
            "username": "user1234"
        }
      },
      "resources": {
        "number_node": 1,
        "cpu_per_node": 4,
        "gpu_per_node": 1,
        "queue_name": "T4_4_15",
        "group_size": 1,
        "custom_flags":["#SBATCH --mem=32G"],
        "strategy": {"if_cuda_multi_devices": true},
        "para_deg": 3,
        "source_list": ["/home/user1234/deepmd.1.2.4.env"]
      }
    }
  ],
  "model_devi":[
    {
      "command": "lmp",
      "machine":{
        "batch_type": "PBS",
        "context_type": "SSHContext",
        "local_root": "./",
        "remote_root": "/home/user1234/work_path_dpdispatcher_test",
        "remote_profile": {
          "hostname": "39.xxx.xx.xx",
          "username": "user1234"
        }
      },
      "resources": {
        "number_node": 1,
        "cpu_per_node": 4,
        "gpu_per_node": 1,
        "queue_name": "T4_4_15",
        "group_size": 5,
        "source_list": ["/home/user1234/deepmd.1.2.4.env"]
      }
    }
  ],
  "fp":[
    {
      "command": "vasp_std",
      "machine":{
        "batch_type": "PBS",
        "context_type": "SSHContext",
        "local_root": "./",
        "remote_root": "/home/user1234/work_path_dpdispatcher_test",
        "remote_profile": {
          "hostname": "39.xxx.xx.xx",
          "username": "user1234"
        }
      },
      "resources": {
        "number_node": 1,
        "cpu_per_node": 32,
        "gpu_per_node": 0,
        "queue_name": "G_32_128",
        "group_size": 1,
        "source_list": ["~/vasp.env"]
      }
    }
  ]
}
```
note1: the key "local_root" in dpgen's machine.json is always `./`

### old dpdispatcher

When switching into a new machine, you may modifying the `MACHINE`, according to the actual circumstance. Once you have finished, the `MACHINE` can be re-used for any DP-GEN tasks without any extra efforts.

An example for `MACHINE` is:
```json
{
  "train": [
    {
      "machine": {
        "batch": "slurm",
        "hostname": "localhost",
        "port": 22,
        "username": "Angus",
        "work_path": "....../work"
      },
      "resources": {
        "numb_node": 1,
        "numb_gpu": 1,
        "task_per_node": 4,
        "partition": "AdminGPU",
        "exclude_list": [],
        "source_list": [
          "....../train_tf112_float.env"
        ],
        "module_list": [],
        "time_limit": "23:0:0",
        "qos": "data"
      },
      "command": "USERPATH/dp"
    }
  ],
  "model_devi": [
    {
      "machine": {
        "batch": "slurm",
        "hostname": "localhost",
        "port": 22,
        "username": "Angus",
        "work_path": "....../work"
      },
      "resources": {
        "numb_node": 1,
        "numb_gpu": 1,
        "task_per_node": 2,
        "partition": "AdminGPU",
        "exclude_list": [],
        "source_list": [
          "......./lmp_tf112_float.env"
        ],
        "module_list": [],
        "time_limit": "23:0:0",
        "qos": "data"
      },
      "command": "lmp_serial",
      "group_size": 1
    }
  ],
  "fp": [
    {
      "machine": {
        "batch": "slurm",
        "hostname": "localhost",
        "port": 22,
        "username": "Angus",
        "work_path": "....../work"
      },
      "resources": {
        "task_per_node": 4,
        "numb_gpu": 1,
        "exclude_list": [],
        "with_mpi": false,
        "source_list": [],
        "module_list": [
          "mpich/3.2.1-intel-2017.1",
          "vasp/5.4.4-intel-2017.1",
          "cuda/10.1"
        ],
        "time_limit": "120:0:0",
        "partition": "AdminGPU",
        "_comment": "that's All"
      },
      "command": "vasp_gpu",
      "group_size": 1
    }
  ]
}
```
Following table illustrates which key is needed for three types of machine: `train`,`model_devi`  and `fp`. Each of them is a list of dicts. Each dict can be considered as an independent environmnet for calculation.

 Key   | `train`          | `model_devi`                                                    | `fp`                                                     |
| :---------------- | :--------------------- | :-------------------------------------- | :-------------------------------------------------------------|
| machine | NEED  | NEED | NEED
| resources | NEED | NEED | NEED
| command | NEED  |NEED |  NEED  
| group_size | NEED | NEED | NEED |

The following table gives explicit descriptions on keys in param.json.


 Key   | Type       | Example                                                  | Discription                                                     |
| :---------------- | :--------------------- | :-------------------------------------- | :-------------------------------------------------------------|
| machine | Dict | | Settings of the machine for TASK.
| resources | Dict | | Resources needed for calculation.
| # Followings are keys in resources
| numb_node | Integer | 1 | Node count required for the job
| task_per_node | Integer | 4 | Number of CPU cores required
| numb_gpu | Integer | Integer | 4 | Number of GPUs required
| manual_cuda_devices | Interger | 1 | Used with key "manual_cuda_multiplicity" specify the gpu number
| manual_cuda_multiplicity |Interger | 5 | Used in 01.model_devi,used with key "manual_cuda_devices" specify the MD program number running on one GPU  at the same time,dpgen will  automatically allocate MD jobs on different GPU. This can improve GPU usage for GPU like V100.
| node_cpu | Integer | 4 | Only for LSF. The number of CPU cores on each node that should be allocated to the job.
| new_lsf_gpu | Boolean | false | **Only for LSF.** Control whether new syntax of GPU to be enabled. If enabled, DP-GEN will generate line like `#BSUB -gpu num=1:mode=shared:j_exclusive=yes` in job submission script. Only support LSF>=10.1.0.3, and `LSB_GPU_NEW_SYNTAX=Y` should be set. Default: `false`.
| exclusive | Boolean | false | **Only for LSF, and only take effect when `new_lsf_gpu` enabled.** Control whether enable `j_exclusive` during running. Default: `false`.
| source_list | List of string | "....../vasp.env" | Environment needed for certain job. For example, if "env" is in the list, 'source env' will be written in the script.
| module_list | List of string | [ "Intel/2018", "Anaconda3"] | For example, If "Intel/2018" is in the list, "module load Intel/2018" will be written in the script.
| partition | String  | "AdminGPU" | Partition / queue in which to run the job. |
| time_limit | String (time format) | 23:00:00 | Maximal time permitted for the job |
mem_limit | Interger | 16 | Maximal memory permitted to apply for the job.
| with_mpi | Boolean | true | Deciding whether to use mpi for calculation. If it's true and machine type is Slurm, "srun" will be prefixed to `command` in the script.
| qos | "string"| "bigdata" | Deciding priority, dependent on particular settings of your HPC.
| allow_failure | Boolean | false | Allow the command to return a non-zero exit code.
| # End of resources
| command | String | "lmp_serial" | Executable path of software, such as `lmp_serial`, `lmp_mpi` and `vasp_gpu`, `vasp_std`, etc.
| group_size | Integer | 5 | DP-GEN will put these jobs together in one submitting script.
| user_forward_files | List of str | ["/path_to/vdw_kernel.bindat"] | These files will be uploaded in each calculation task. You should make sure provide the path exists. 
| user_backward_files | List of str | ["HILLS"] | Besides DP-GEN's normal output, these files will be downloaded after each calculation. You should make sure these files can be generated.
