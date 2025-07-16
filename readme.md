# Packages
- All MVP packages are in jazzy-devel branch
- WOrld of stonefish is in jazzy-devel-mini-alpha
- Once all the repo are cloned, you can do
```
ros2 launch mini_alpha_bringup bringup_simulation.launch.py
```
- After the terminal say the teleop is active you can start control the AUV.
- Joy stick control
    - `start` button will enable the controller
    - `back` button will disable the controller
    - `LT` button will enable the teleoperation activities
    - `left stick` will control the surge port thruster
    - `right stick` will control the surge starboard thruster
    - Hold `LB` and press `RT` will increase the desired depth (going down) by 0.1 m
    - Hold `LB` and press `RB` will decrease the desired depth (going up) by 0.1 m
  