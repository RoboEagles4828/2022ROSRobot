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
`winget install -e --id Canonical.Ubuntu`

5. Search for and open Ubuntu to finish install. (Press enter if it appears the terminal isn't doing anything)

6. Install GPU driver for WSLg \
[Intel GPU](https://downloadcenter.intel.com/download/30579/Intel-Graphics-Windows-DCH-Drivers) \
[NVIDIA GPU](https://developer.nvidia.com/cuda/wsl) \
[AMD GPU](https://community.amd.com/t5/radeon-pro-graphics/announcing-amd-support-for-gpu-accelerated-machine-learning/ba-p/414185)

7. Update WSL by opening terminal as administrator and execute: \
`wsl --update` \
`wsl --shutdown`

8. (*Optional*) Test to make sure WSLg is installed. \
    Open Ubuntu and Excute the following: \
    `sudo apt update && sudo apt install -y xterm` \
    `xterm` \
    A window that looks like a terminal should appear.

9. Open VS Code and install the Remote Development extension

10. In VS Code go to settings -> Extensions -> Remote - Containers and turn on Execute in WSL

11. Press F1 to bring up the command palette and use the command: \
`Remote-Containers: Clone Repository in Container Volume..`

12. Paste the git link for this repo: \
`https://github.com/RoboEagles4828/2022ROSRobot.git`

13. The developement container will start to open, click on the notification in the bottom right to see progress.

14. When you are fully in the container, File -> Save Workspace As.. -> Show local -> Name the file and Save

15. Test that gazebo works by executing `gazebo` in the terminal
