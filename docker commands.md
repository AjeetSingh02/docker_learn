some docker and flask commands

- To check docker version

docker --version

- To check all images
docker image ls 
docker image ls -a
docker images

- To get inside running container
docker exec -it b56fa0d76d5c bash
	
- Hitting flask API in POST
curl -H "Content-Type:application/json" -X POST -d '{"input_file_path":"inputs/Store_POS.csv"}' http://localhost:5000/autoEDA

- To create requirements.txt using pipreqs package
pipreqs /user/flaskAPP          # /user/flaskAPP is the folder containing the scripts for whome you want to generate requirements.txt
pipreqs /user/flaskAPP --pypi-server http://infynp.ad.infosys.com/repository/pypi-all/simple      # Using custom proxy server

- To build from Dockerfile when Dockerfile is in current directory. dot(.) signifies current directory
docker build . -t "name_of_image"
docker build . -t flaskapp:latest     #name:version

- Run container having flask APP
docker run -p localhost:5001:5000 image_id
	
	localhost is not necessary. you can use 5001:5000 only also
	-d which detatches from the run. This means you won’t see any output. 
	   You can remove the -d if you would like to see the run process.
	-p which specifies the port it is going to run on

- Remove container
docker rm 91f3410eca7a --force

- Stop container
docker kill 9701eed5868d

- Remove image
docker rmi image_id/image_name --force

- To push to Docker HUB
https://ropenscilabs.github.io/r-docker-tutorial/04-Dockerhub.html

- To save as tar file
docker save imagename > imagename.tar
docker save pythonsmall:1 | gzip > pythonsmall.tar.gz
https://docs.docker.com/engine/reference/commandline/save/

- Downloading from GCP cloudshell
cloudshell download filename
https://cloud.google.com/shell/docs/uploading-and-downloading-files

- Mount volume
docker run -v /home/awb_user/ajeet/mount_volume:/workdir/mount -p 5053:5053 flaskapp:1
