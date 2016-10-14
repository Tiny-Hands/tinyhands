# Dream Suite

Tiny Hands International

![Codeship Status](https://app.codeship.com/projects/79c5fb20-1e83-0132-0c4f-7a12a542bc63/status?branch=master)
# Setup

## Docker

1. Make sure you install Docker [here](https://www.docker.com/) and docker-compose by executing: `sudo pip install docker-compose`
2. Clone the repository and cd into it
3. execute the `setup.sh` script in the root of the repo (this might take a few minutes)
4. run `docker-compose up -d` to start running the project
5. The created local.env file may need some secrets before the project will run. Ask for the secrets from whoever is helping you get started
6. If all of the steps were successful, you can find the application running on [port 80 on localhost](http://localhost).
7. If you can't figure this out, contact Ben Duggan.

## Vagrant + Docker setup (For Windows or Mac)

1. make sure you have the latest version of [Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org/wiki/Downloads) installed
2. if you are on windows, you should install [gitbash](https://git-scm.com/downloads) for easiness and niceness
3. clone the repository
4. cd into the project directory
5. execute `vagrant up --provision`
6. Execute `vagrant ssh` and `cd /vagrant`to get access to docker/docker-compose commands inside the vagrant box
7. Execute the `setup.sh` script in the root of the repo (this might take a few minutes)
8. Run `docker-compose up -d` to start running the project
9. the server should be running on `192.168.36.36/`

## Installing Sanitized Test Data
execute `docker-compose run --rm web sh /data/bin/install_test_db.sh`

The sanitized database has two accounts preconfigured for testing both of which have the password 'pass'
  - test_sup@example.com - is a super user account
  - test1 - is a user account

## Docker/Docker-Compose Cheat Sheet

- `docker-compose up -d` Turn on all of the containers listed in the docker-compose.yml file
- `docker-compose run --rm <container-name> bash` open a bash session inside a copy of the container
- `docker-compose kill <container name>*` Turn off the running containers
- `docker-compose rm <container name>*` Delete the containers
- `docker-compose run <container-name> <command>` Run a command inside of a copy of a container
- `docker-compose build` - rebuild the containers specified in the docker-compose.yml file
- `docker stop $(docker ps -a -q)` - stop all running containers on machine
- `docker rm $(docker ps -a -q)` - remove all containers on machine
- `docker exec -it <container-id> bash` - run an interactive shell inside the actual running container

# local.env and common.env files

In the root project directory there are three files used that contain environment variables. These files are used inside of the containers. If you look at the docker-compose.yml file you can see that these are imported into all of the containers.

- common.env file: This is for key-value pairs that are okay to be public knowledge. That way we can share their values.
- local.env file: This is for key-value pairs that should not be known to the public. Think passwords, secret keys, other stuff you don't want the world knowing about (Since one day it would be nice to make this an open-source project). Since we do not want these being released, this is not tracked in the repository.
- local.env.dist: This is where you put the keys that should go into the local.env file. In this file the format should be `<key>=`. This way we know what environment variables need to exist/be set to run the project, but we are not putting the actual values in version control


# Testing

## Django Unit Tests:

Execute the `./manage.py test` command in a new container. eg. `docker-compose run web ./manage.py test`


## Deployment Process

### Building containers

I have created a build script to automate the build process of docker-containers. Just run the script and manually check to see if there were any problems in the build process. Note that at the end, it provides a build number with which the images have been tagged. This version number is automatically put into a file called dreamsuite_tag in the root of the repository as well so that you do not have to remember it.

execute: `./build-containers.sh`

### Pushing containers

There is a push containers script in the root of the repository. This script takes in a version number as the 1st argument and pushes the containers to DockerHub with the specified tag. The following command pushes the docker containers with the tag number that was generated by the build-containers script.

``./push-containers.sh `cat dreamsuite_tag` ``

### Deploy new build on server [Warning: Currently not running]
The easiest way to do this is by using [SPUDS](https://github.com/tu-software-studio/SPUDS). All you have to do is send an HTTP request to the right url with the following json structure:
"""
{
     "environment": "<staging|production>",
     "tag":"<empty|build-number>",
     "secret": "<shared secret>"
}
"""
