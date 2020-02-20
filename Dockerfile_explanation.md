**Step 1: Use the official image as a parent image**
> FROM node:current-slim

**Step 2: Set the working directory**

*Use WORKDIR to specify that all subsequent actions should be taken from the  directory /usr/src/app in your image filesystem (never the host’s filesystem)*
> WORKDIR /usr/src/app


**Step 3: Copy the file from your host to your current location**

*COPY the file package.json from your host to the present location (.) in your image (so in this case, to /usr/src/app/package.json)*
> COPY package.json .

**Step 4: Run the command inside your image filesystem**

*RUN the command npm install inside your image filesystem (which will read package.json to determine your app’s node dependencies, and install them)*
> RUN npm install

**Step 5: Inform Docker that the container is listening on the specified port at runtime.**
> EXPOSE 8080

**Step 6: Run the specified command within the container.**
> CMD [ "npm", "start" ]

**Step 7: Copy the rest of your app's source code from your host to your image filesystem.**
 > COPY . .
      
    
    
    
    
    
- You can see that these are much the same steps you might have taken to set up and install your app on your host. 
However, capturing these as a Dockerfile allows you to do the same thing inside a portable, isolated Docker image.

- The steps above built up the filesystem of our image, but there are other lines in your Dockerfile.

- The CMD directive is the first example of specifying some metadata in your image that describes how to run a container 
   based on this image. In this case, it’s saying that the containerized process that this image is meant to support is npm start.

- The EXPOSE 8080 informs Docker that the container is listening on port 8080 at runtime.

- What you see above is a good way to organize a simple Dockerfile; always start with a FROM command, follow it with the steps to build up your private filesystem, and conclude with any metadata specifications. 

