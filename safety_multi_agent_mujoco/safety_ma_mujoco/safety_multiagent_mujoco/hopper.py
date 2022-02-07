<mujoco model="hopper">
  <compiler angle="degree" coordinate="global" inertiafromgeom="true"/>
  <default>
    <joint armature="1" damping="1" limited="true"/>
    <geom conaffinity="1" condim="1" contype="1" margin="0.001" material="geom" rgba="0.8 0.6 .4 1" solimp=".8 .8 .01" solref=".02 1"/>
    <motor ctrllimited="true" ctrlrange="-.4 .4"/>
  </default>
  <option integrator="RK4" timestep="0.002"/>
  <visual>
    <map znear="0.02"/>
  </visual>
  <worldbody>
    <light cutoff="100" diffuse="1 1 1" dir="-0 0 -1.3" directional="true" exponent="1" pos="0 0 1.3" specular=".1 .1 .1"/>
    <geom conaffinity="1" condim="3" name="floor" pos="40 0 0" rgba="0.2 0.2 0.2 1" size="100 25 .125" type="plane" material="MatPlane"/>
    <geom conaffinity="1" condim="3" name="wall1" type="box" size="24.8 0.1 1.0" pos="0  -4 1.0"  euler='0 0 0'  rgba="1 0.5 0.5 1"/>
    <geom conaffinity="1" condim="3" name="wall2" type="box" size="24.8 0.1 1.0" pos="0   4 1.0"  euler='0 0 0'  rgba="1 0.5 0.5 1"/>
    <geom conaffinity="1" condim="3" name="wall3" type="box" size="24.8 0.1 1.0" pos="50 -4 1.0"  euler='0 0 -0'  rgba="1 0.5 0.5 1"/>
    <geom conaffinity="1" condim="3" name="wall4" type="box" size="24.8 0.1 1.0" pos="50  4 1.0"  euler='0 0 -0'  rgba="1 0.5 0.5 1"/>
    <geom conaffinity="1" condim="3" name="wall5" type="box" size="24.8 0.1 1.0" pos="100 -4 1.0"  euler='0 0 0'  rgba="1 0.5 0.5 1"/>
    <geom conaffinity="1" condim="3" name="wall6" type="box" size="24.8 0.1 1.0" pos="100  4 1.0"  euler='0 0 0'  rgba="1 0.5 0.5 1"/>
    <body name="mocap1" pos="5 0 .5" mocap="true">
        <geom conaffinity="0" condim="3" name="mocap_geom" pos='5 0 .5' type="box" size=".3 0.3 0.3"  rgba="1 0.5 0.5 0"/>
    </body>
    <body name="obj1" pos="5 0 .5">
        <freejoint name="obj1_fj"/>
        <geom conaffinity="1" condim="3" name="obj_geom" pos='5 0 .5' type="box" size=".3 0.3 0.3"  rgba="1 0.5 0.5 1"/>
    </body>
    <body name="torso" pos="0 1 1.25">
      <camera name="track" mode="trackcom" pos="0 -3 1" xyaxes="1 0 0 0 0 1"/>
      <joint armature="0" axis="1 0 0" damping="0" limited="false" name="rootx" pos="0 0 0" stiffness="0" type="slide"/>
      <joint armature="0" axis="0 0 1" damping="0" limited="false" name="rootz" pos="0 0 0" ref="1.25" stiffness="0" type="slide"/>
      <joint armature="0" axis="0 1 0" damping="0" limited="false" name="rooty" pos="0 0 1.25" stiffness="0" type="hinge"/>
      <geom friction="0.9" fromto="0 0 1.45 0 0 1.05" name="torso_geom" size="0.05" type="capsule"/>
      <body name="thigh" pos="0 0 1.05">
        <joint axis="0 -1 0" name="thigh_joint" pos="0 0 1.05" range="-150 0" type="hinge"/>
        <geom friction="0.9" fromto="0 0 1.05 0 0 0.6" name="thigh_geom" size="0.05" type="capsule"/>
        <body name="leg" pos="0 0 0.35">
          <joint axis="0 -1 0" name="leg_joint" pos="0 0 0.6" range="-150 0" type="hinge"/>
          <geom friction="0.9" fromto="0 0 0.6 0 0 0.1" name="leg_geom" size="0.04" type="capsule"/>
          <body name="foot" pos="0.13/2 0 0.1">
            <joint axis="0 -1 0" name="foot_joint" pos="0 0 0.1" range="-45 45" type="hinge"/>
            <geom friction="2.0" fromto="-0.13 0 0.1 0.26 0 0.1" name="foot_geom" size="0.06" type="capsule"/>
          </body>
        </body>
      </body>
    </body>
  </worldbody>
  <equality>
    <weld name="weld1" body1="mocap1" body2="obj1" solref=".02 .5"/>
  </equality>
  <actuator>
    <motor ctrllimited="true" ctrlrange="-1.0 1.0" gear="200.0" joint="thigh_joint"/>
    <motor ctrllimited="true" ctrlrange="-1.0 1.0" gear="200.0" joint="leg_joint"/>
    <motor ctrllimited="true" ctrlrange="-1.0 1.0" gear="200.0" joint="foot_joint"/>
  </actuator>
    <asset>
        <texture type="skybox" builtin="gradient" rgb1=".4 .5 .6" rgb2="0 0 0"
            width="100" height="100"/>
        <texture builtin="flat" height="1278" mark="cross" markrgb="1 1 1" name="texgeom" random="0.01" rgb1="0.8 0.6 0.4" rgb2="0.8 0.6 0.4" type="cube" width="127"/>
        <texture builtin="checker" height="100" name="texplane" rgb1="#2c5987" rgb2="#1f4060" type="2d" width="100"/>
        <material name="MatPlane" reflectance="0.5" shininess="1" specular="1" texrepeat="60 60" texture="texplane"/>
        <material name="geom" texture="texgeom" texuniform="true"/>
    </asset>
</mujoco>
