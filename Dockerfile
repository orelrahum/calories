# Use Node.js 16 as the base image
FROM node:16

# Set the working directory in the container
WORKDIR /usr/src/app

# Install a specific version of Yarn (1.22)
# RUN npm install -g yarn

# Copy the package.json and yarn.lock files to the working directory
COPY package.json yarn.lock ./

# Install dependencies using Yarn
RUN yarn install --frozen-lockfile

# Copy the rest of the application code
COPY . .

# Expose the desired port (e.g., 3000 if your app runs on this port)
EXPOSE 3000

# Command to run your application (adjust as needed for your project)
CMD ["yarn", "start"]
