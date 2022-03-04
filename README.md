# Safe Multi-Agent Mujoco

We introduce **Safe Multi-Agent MuJoCo (Safe MAMujoco)**, a safety-aware modification of [MAMuJoCo](https://github.com/schroederdewitt/multiagent_mujoco).  Safe MAMuJoCo agents learn to not only skilfully manipulate a robot, but also to avoid dangerous obstacles and positions, Figure 1 shows example views of the environment. (This repository is under actively development. We appreciate any constructive comments and suggestions)



In particular, the background environment, agents, physics simulator, and the reward function are preserved. However, as oppose to its predecessor, Safe MAMuJoCo environments come with obstacles, like walls or bombs. Furthermore, with the increasing risk of an agent stumbling upon an obstacle, the environment emits cost.

<div align=center>
 <img src="https://github.com/chauncygu/Safe-Multi-Agent-Mujoco/blob/main/figures/Ant2x4_new_green_yellow.jpg" width="165"/> <img src="https://github.com/chauncygu/Safe-Multi-Agent-Mujoco/blob/main/figures/New_Ant4x2.jpg" width="175"/> <img src="https://github.com/chauncygu/Safe-Multi-Agent-Mujoco/blob/main/figures/couple_halfcheetah_p1p_color.jpg" width="213"/>
    <img src="https://github.com/chauncygu/Safe-Multi-Agent-Mujoco/blob/main/figures/New_HalfCheetah2x3.jpg" width="202"/>  
</div>
<div align=center>
<center style="color:#000000;text-decoration:underline">Figure.1 Example views of robots in Safe MAMuJoCo. Body parts of different colours are controlled by differentagents. Agents jointly learn to manipulate the robot, while avoiding crashing into unsafe areas. </center>
 </div>



## Installation

- Install mujoco accoring to [mujoco-py](https://github.com/openai/mujoco-py) and [MuJoCo website](https://www.roboti.us/license.html).
- clone safety multi-agent mujoco to the env path.
&nbsp;

``` Bash
LD_LIBRARY_PATH=${HOME}/.mujoco/mujoco200/bin;
LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libGLEW.so
```

## Tasks
``` Bash
    ManyAgent Ant
    env_args = {"scenario": "manyagent_ant",
                  "agent_conf": "3x2",
                  "agent_obsk": 1,
                  "episode_limit": 1000}

    env_args = {"scenario": "manyagent_ant",
                  "agent_conf": "2x3",
                  "agent_obsk": 1,
                  "episode_limit": 1000}
                  
    env_args = {"scenario": "manyagent_ant",
                  "agent_conf": "6x1",
                  "agent_obsk": 1,
                  "episode_limit": 1000}

    env_args = {"scenario": "manyagent_ant",
                "agent_conf": "4x2",
                "agent_obsk": 1,
                "episode_limit": 1000}  
                
    HalfCheetah
    env_args = {"scenario": "HalfCheetah-v2",
                "agent_conf": "2x3",
                "agent_obsk": 1,
                "episode_limit": 1000}
                
    env_args = {"scenario": "HalfCheetah-v2",
                "agent_conf": "3x2",
                "agent_obsk": 1,
                "episode_limit": 1000}
                
    env_args = {"scenario": "HalfCheetah-v2",
                "agent_conf": "6x1",
                "agent_obsk": 1,
                "episode_limit": 1000}
                  
    Ant 
    env_args = {"scenario": "Ant-v2",
                "agent_conf": "2x4",
                "agent_obsk": 1,
                "episode_limit": 1000}

    env_args = {"scenario": "Ant-v2",
                "agent_conf": "8x1",
                "agent_obsk": 1,
                "episode_limit": 1000}

    env_args = {"scenario": "Ant-v2",
                "agent_conf": "2x4d",
                "agent_obsk": 1,
                "episode_limit": 1000}

    env_args = {"scenario": "Ant-v2",
                "agent_conf": "4x2",
                "agent_obsk": 1,
                "episode_limit": 1000}
                
   Coupled_half_cheetah
    env_args = {"scenario": "coupled_half_cheetah",
                "agent_conf": "1p1",
                "agent_obsk": 1,
                "episode_limit": 1000}
    Hopper
    env_args = {"scenario": "Hopper-v2",
                "agent_conf": "3x1",
                "agent_obsk": 1,
                "episode_limit": 1000}
```


## Publication
If you find the repository useful, please cite the [paper](https://arxiv.org/abs/2110.02793):
```
@article{gu2021multi,
  title={Multi-Agent Constrained Policy Optimisation},
  author={Gu, Shangding and Kuba, Jakub Grudzien and Wen, Munning and Chen, Ruiqing and Wang, Ziyan and Tian, Zheng and Wang, Jun and Knoll, Alois and Yang, Yaodong},
  journal={arXiv preprint arXiv:2110.02793},
  year={2021}
}
```

# Acknowledgments

Some sections of the repository are based on [MAMujoco](https://github.com/schroederdewitt/multiagent_mujoco), [safety-gym](https://github.com/openai/safety-gym), [CMBPO](https://github.com/anyboby/Constrained-Model-Based-Policy-Optimization).





