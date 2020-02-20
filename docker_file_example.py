Note: This file is named as .py file just to make it more readable.

# Use the official image as a parent image
  - FROM node:current-slim

# Set the working directory
''' Use WORKDIR to specify that all subsequent actions should be taken from the 
    directory /usr/src/app in your image filesystem (never the host’s filesystem)'''
  - WORKDIR /usr/src/app


# Copy the file from your host to your current location
'''COPY the file package.json from your host to the present location (.) in your image (so in this case, to /usr/src/app/package.json)'''
  - COPY package.json .

# Run the command inside your image filesystem
'''RUN the command npm install inside your image filesystem 
   (which will read package.json to determine your app’s node dependencies, and install them)'''
  - RUN npm install

# Inform Docker that the container is listening on the specified port at runtime.
  - EXPOSE 8080

# Run the specified command within the container.
  - CMD [ "npm", "start" ]

# Copy the rest of your app's source code from your host to your image filesystem.
  - COPY . .
