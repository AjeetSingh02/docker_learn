* To check docker version
	* docker --version
	
* To build from Dockerfile when Dockerfile is in current directory. dot(.) signifies current directory
	* docker build . -t "name_of_image"
	* docker build . -t imagename:tag     

* Run container
	* docker run -p localhost:5001:5000 image_id
	* docker run --publish 8000:8080 --detach --name containername imagename:tag
	* docker container run --publish 8000:8080 --detach --name containername imagename:tag
		* localhost is not necessary. you can use 5001:5000 only also.
		* --publish (-p) asks Docker to forward traffic incoming on the host’s port 8000, to the container’s port 8080. Containers have their own private set of ports, so if you want to reach one from the network, you have to forward traffic to it in this way. Otherwise, firewall rules will prevent all network traffic from reaching your container, as a default security posture.
		* --detach (-d) asks Docker to run this container in the background.
		* --name specifies a name with which you can refer to your container in subsequent commands.

* To check all images
	* docker image ls 
	* docker image ls -a
	* docker images

* To get inside running container
	* docker exec -it b56fa0d76d5c bash

* Remove container
	* docker rm 91f3410eca7a --force

* Stop container
	* docker kill 9701eed5868d

* Remove image
	* docker rmi image_id/image_name --force

* To push to Docker HUB
	* Step1: Images must be namespaced correctly to share on Docker Hub. Specifically, you must name images like this:
		* docker image tag imagename:tag dockerid/repositoryname:tag
	* Step2: Push your image to Docker Hub
		* docker image push dockerid/repositoryname:tag
	* For more info: https://docs.docker.com/get-started/part3/

* To save as tar file
	* docker save imagename > imagename.tar
	* docker save pythonsmall:1 | gzip > pythonsmall.tar.gz
	* For more info: https://docs.docker.com/engine/reference/commandline/save/

* Mount volume
	* docker run -v /home/awb_user/ajeet/mount_volume:/workdir/mount -p 5053:5053 flaskapp:1
	
