# Safe Multi-Agent Mujoco

We introduce a safe Multi-Agent Reinforcement Learning Benchmark, **Safe Multi-Agent MuJoCo (Safe MAMujoco)**, a safety-aware modification of [MAMuJoCo](https://github.com/schroederdewitt/multiagent_mujoco).  Safe MAMuJoCo agents learn to not only skilfully manipulate a robot, but also to avoid dangerous obstacles and positions, Figure 1 shows example views of the environment. (This repository is under actively development. We appreciate any constructive comments and suggestions)



In particular, the background environment, agents, physics simulator, and the reward function are preserved. However, as oppose to its predecessor, Safe MAMuJoCo environments come with obstacles, like walls or bombs. Furthermore, with the increasing risk of an agent stumbling upon an obstacle, the environment emits cost.

<!--
<div align=center>
 <img src="https://github.com/chauncygu/Safe-Multi-Agent-Mujoco/blob/main/figures/Ant2x4_new_green_yellow.jpg" width="165"/> <img src="https://github.com/chauncygu/Safe-Multi-Agent-Mujoco/blob/main/figures/New_Ant4x2.jpg" width="175"/> <img src="https://github.com/chauncygu/Safe-Multi-Agent-Mujoco/blob/main/figures/couple_halfcheetah_p1p_color.jpg" width="213"/>
    <img src="https://github.com/chauncygu/Safe-Multi-Agent-Mujoco/blob/main/figures/New_HalfCheetah2x3.jpg" width="202"/>  
</div>
<div align=center>
<center style="color:#000000;text-decoration:underline">Figure.1 Example views of robots in Safe MAMuJoCo. Body parts of different colours are controlled by differentagents. Agents jointly learn to manipulate the robot, while avoiding crashing into unsafe areas. </center>
 </div>
-->
 
 
 <div align=center>
 <img src="https://github.com/chauncygu/Safe-Multi-Agent-Mujoco/blob/main/figures/all-mujoco.png" width="850"/> 
 </div>
<div align=center>
<center style="color:#000000;text-decoration:underline">Figure.1 Example views of robots in Safe MAMuJoCo. Body parts of different colours are controlled by differentagents. Agents jointly learn to manipulate the robot, while avoiding crashing into unsafe areas. </center>
 </div>
 

## Demos

<!--<div align=center>
<img src="https://github.com/chauncygu/Multi-Agent-Constrained-Policy-Optimisation/blob/main/figures/202111071600-unsafe-end%2000_00_00-00_00_30.gif" width="700"/>    
</div>
    
<div align=center>
<center style="color:#000000;text-decoration:underline">
    A demo denotes <b>unsafe</b> performance using <a href="https://arxiv.org/abs/2109.11251">HAPPO</a> on Ant2x4 task.</center>
</div>

&nbsp;
<div align=center>
<img src="https://github.com/chauncygu/Multi-Agent-Constrained-Policy-Optimisation/blob/main/figures/202111140948-safe-end1%2000_00_00-00_00_30.gif" width="700"/>    
</div>
    
<div align=center>
<center style="color:#000000;text-decoration:underline">
    A demo denotes <b>safe</b> performance using <a href="http://arxiv.org/abs/2110.02793">MAPPO-Lagrangian</a> on Ant2x4 task.</center>
</div>-->

**Ant Task**: the width of the corridor set by two walls is 10 m. The environment emits the cost of 1 for an agent, if the distance between the robot and the wall is less than 1.8 m, or when the robot topples over.

|![](https://github.com/chauncygu/Multi-Agent-Constrained-Policy-Optimisation/blob/main/figures/202111071600-unsafe-end%2000_00_00-00_00_30.gif)|![](https://github.com/chauncygu/Multi-Agent-Constrained-Policy-Optimisation/blob/main/figures/202111140948-safe-end1%2000_00_00-00_00_30.gif)|
| :---: | :---: | 
|  A demo denotes <b>unsafe</b> performance using <a href="https://arxiv.org/abs/2109.11251">HAPPO</a> on Ant-2x4 task.</center> | A demo denotes <b>safe</b> performance using <a href="http://arxiv.org/abs/2110.02793">MAPPO-Lagrangian</a> on Ant-2x4 task.</center> | 


**HalfCheetah Task**: In the task, the agents move inside a corridor (which constraints their movement, but does not induce costs). Together with them, there are bombs moving inside the corridor. If an agent finds itself too close to the bomb, the distance between an agent and the bomb is less than 9m, a cost of 1 will be emitted, at the same time, the bomb will turn blood red.

|![](https://github.com/chauncygu/Multi-Agent-Constrained-Policy-Optimisation/blob/main/figures/202111140948-halfcheetah-unsafe-end%2000_00_00-00_00_30.gif)|![](https://github.com/chauncygu/Multi-Agent-Constrained-Policy-Optimisation/blob/main/figures/202111140948-halfcheetah-safe-end%2000_00_00-00_00_30.gif)|
| :---: | :---: | 
|  A demo denotes <b>unsafe</b> performance using <a href="https://arxiv.org/abs/2109.11251">HAPPO</a> on HalfCheetah-2x3 task.</center> | A demo denotes <b>safe</b> performance using <a href="http://arxiv.org/abs/2110.02793">MAPPO-Lagrangian</a> on HalfCheetah-2x3 task.</center> | 


**ManyAgent Ant Task One**: In the ManyAgent Ant task, the width of the corridor set by two walls is 9m. The environment emits the cost of 1 for an agent, if the distance between the robot and the wall is less than 1.8 m, or when the robot topples over. 

|![](https://github.com/chauncygu/Multi-Agent-Constrained-Policy-Optimisation/blob/main/figures/sadppo-manyagent-ant--unsafe-end-have-word%2000_00_00-00_00_30.gif)|![](https://github.com/chauncygu/Multi-Agent-Constrained-Policy-Optimisation/blob/main/figures/safe-mappo-manyagent-ant--safe-end-have-word-01%2000_00_00-00_00_30.gif)|
| :---: | :---: | 
|  A demo denotes <b>unsafe</b> performance using <a href="https://arxiv.org/abs/2109.11251">HAPPO</a> on ManyAgent Ant-2x3 task.</center> | A demo denotes <b>safe</b> performance using <a href="http://arxiv.org/abs/2110.02793">MAPPO-Lagrangian</a> on ManyAgent Ant-2x3 task.</center> | 


**ManyAgent Ant Task Two**: In the ManyAgent Ant task, the width of the corridor is 12 m; its walls fold at the angle of 30 degrees. The environment emits the cost of 1 for an agent, if the distance between the robot and the wall is less than 1.8 m, or when the robot topples over.

|![](https://github.com/chauncygu/Multi-Agent-Constrained-Policy-Optimisation/blob/main/figures/two-wall-sadppo-unsafe-end-have-word-manyagent-ant%2000_00_00-00_00_30.gif)|![](https://github.com/chauncygu/Multi-Agent-Constrained-Policy-Optimisation/blob/main/figures/two-wall-safe-mappo--manyagent-ant-safe-end-have-word-manyagent-ant%2000_00_00-00_00_30.gif)|![](https://github.com/chauncygu/Multi-Agent-Constrained-Policy-Optimisation/blob/main/figures/two-wall-macpo-manyagent-ant--safe-end-have-word%2000_00_00-00_00_30.gif)|
| :---: | :---: | :---: | 
|  A demo denotes <b>unsafe</b> performance using <a href="https://arxiv.org/abs/2109.11251">HAPPO</a> on ManyAgent Ant-2x3 task.</center> | A demo denotes <b>unsafe</b> performance using <a href="http://arxiv.org/abs/2110.02793">MAPPO-Lagrangian</a> on ManyAgent Ant-2x3 task.</center> | A demo denotes <b>safe</b> performance using <a href="http://arxiv.org/abs/2110.02793">MACPO</a> on ManyAgent Ant-2x3 task.</center> | 


## Installation

- Install mujoco accoring to [mujoco-py](https://github.com/openai/mujoco-py) and [MuJoCo website](https://www.roboti.us/license.html).
- clone safety multi-agent mujoco to the env path.
&nbsp;

``` Bash
LD_LIBRARY_PATH=${HOME}/.mujoco/mujoco200/bin;
LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libGLEW.so
pip install -r requirements.txt
```

## Test
Run test.py

``` Bash
python test.py
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
                
    env_args = {"scenario": "manyagent_ant",
                "agent_conf": "2x4",
                "agent_obsk": 1,
                "episode_limit": 1000}
                
                
    env_args = {"scenario": "manyagent_ant",
                "agent_conf": "8x1",
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
@article{gu2023safe,
  title={Safe Multi-Agent Reinforcement Learning for Multi-Robot Control},
  author={Gu, Shangding and Kuba, Jakub Grudzien and Chen, Yuanpei and Du, Yali and Yang, Long and Knoll, Alois and Yang, Yaodong},
  journal={Artificial Intelligence},
  pages={103905},
  year={2023},
  publisher={Elsevier}
}

```

# Acknowledgments

We thank the list of contributors from the following open source repositories: [MAMujoco](https://github.com/schroederdewitt/multiagent_mujoco), [safety-gym](https://github.com/openai/safety-gym), [CMBPO](https://github.com/anyboby/Constrained-Model-Based-Policy-Optimization).





