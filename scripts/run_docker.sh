# If not working, first do: sudo rm -rf /tmp/.docker.xauth
# It still not working, try running the script as root.
## Build the image first
### docker build -t r2_boxbots .
## then run this script
xhost local:root

XAUTH=/tmp/.docker.xauth

  # --user ros \
  docker run -it \
    --name=r2_boxbots_multi_container \
    --env="DISPLAY=$DISPLAY" \
    --env="QT_X11_NO_MITSHM=1" \
    --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
    --volume="${PWD}/:/root/project" \
    --mount type=bind,source=/dev/bus/usb,target=/dev/bus/usb \
    --env="XAUTHORITY=$XAUTH" \
    --volume="$XAUTH:$XAUTH" \
    --net=host \
    --privileged \
    r2_boxbots_multi \
    bash

echo "Done."