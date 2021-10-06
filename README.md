# Safety Multi-Agent Mujoco

We introduce **Safe Multi-Agent MuJoCo (Safe MAMujoco)**, a safety-aware modification of [MAMuJoCo](https://github.com/schroederdewitt/multiagent_mujoco).  Safe MAMuJoCo agents learn to not only skilfully manipulate a robot, but also to avoid dangerous obstacles and positions, Figure 1 shows example views of the environment. 



In particular, the background environment, agents, physics simulator, and the reward function are preserved. However, as oppose to its predecessor, Safe MAMuJoCo environments come with obstacles, like walls or bombs. Furthermore, with the increasing risk of an agent stumbling upon an obstacle, the environment emits cost.

<div align=center>
 <img src="https://github.com/chauncygu/Safe-Multi-Agent-Mujoco/blob/main/figures/Ant2x4_new_green_yellow.jpg" width="165"/> <img src="https://github.com/chauncygu/Safe-Multi-Agent-Mujoco/blob/main/figures/New_Ant4x2.jpg" width="175"/> <img src="https://github.com/chauncygu/Safe-Multi-Agent-Mujoco/blob/main/figures/couple_halfcheetah_p1p_color.jpg" width="213"/>
    <img src="https://github.com/chauncygu/Safe-Multi-Agent-Mujoco/blob/main/figures/New_HalfCheetah2x3.jpg" width="202"/>  
</div>
<div align=center>
<center style="color:#000000;text-decoration:underline">Figure.1 Example views of robots in Safe MAMuJoCo. Body parts of different colours are controlled by differentagents. Agents jointly learn to manipulate the robot, while avoiding crashing into unsafe areas. </center>
 </div>



## Installation
&nbsp;

- Install mujoco accoring to [mujoco-py](https://github.com/openai/mujoco-py) and [MuJoCo website](https://www.roboti.us/license.html).
- clone safety multi-agent mujoco to the env path.
&nbsp;

``` Bash
LD_LIBRARY_PATH=${HOME}/.mujoco/mujoco200/bin;
LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libGLEW.so
```


# Acknowledgments

Some sections of the repository is based on [MAMujoco](https://github.com/schroederdewitt/multiagent_mujoco), [safety-gym](https://github.com/openai/safety-gym), [CMBPO](https://github.com/anyboby/Constrained-Model-Based-Policy-Optimization).





