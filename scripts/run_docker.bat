

docker run -it \
  --name=r2_boxbots_container \
  -e DISPLAY=host.docker.internal:0.0 \
  -e LIBGL_ALWAYS_INDIRECT=0 \
  --volume="${PWD}/../:/root/project" \
  r2_boxbots \
  bash