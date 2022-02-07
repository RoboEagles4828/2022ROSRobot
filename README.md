# 2022ROSRobot
ROS Robot code for the 2022 season. 

## Windows 11 Install
Execute the following commands from command line. You will restart several times throught this process.
1. Install VS Code \
`winget install -e --id Microsoft.VisualStudioCode`
2. Install Docker \
`winget install -e --id Docker.DockerDesktop` \
**NOTE**: Docker will ask to update WSL2 kernal, here is the [installer](https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi)
3. Set default WSL version to WSL2 \
`wsl --set-default-version 2`
4. Install Ubuntu WSL \
`winget install -e --id Canonical.Ubuntu.2004`
5. Install GPU driver for WSLg \
[Intel GPU](https://downloadcenter.intel.com/download/30579/Intel-Graphics-Windows-DCH-Drivers) \
[NVIDIA GPU](https://developer.nvidia.com/cuda/wsl) \
[AMD GPU](https://community.amd.com/t5/radeon-pro-graphics/announcing-amd-support-for-gpu-accelerated-machine-learning/ba-p/414185)
6. Update WSL \
`wsl --update`

Test your install of wsl and wslg by opening ubuntu and running a linux GUI app


## Opening the Dev Container
1. Open VS Code and install the Remote Development extension
2. Press F1 to bring up the command palette and use the command: \
Remote-Containers: Clone Repository in Container Volume..
3. Put the clone link for this repo in and hit enter
`https://github.com/RoboEagles4828/2022ROSRobot.git`
4. Container should open, save the workspace to your local so you can access the container easily.