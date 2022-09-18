#!/usr/bin/env python3


__author__ = "Sehran"
__version__ = "1.0"

import os
import subprocess

root_dir = os.getcwd()

git_clone_cmd = "git clone "
java_backend = "https://github.com/SehDev96/portfolio-backend-java.git"
react_frontend = "https://github.com/SehDev96/portfolio-frontend-react.git"


def tech_stack(user_input):
    input_options = {
        1: "portfolio-backend-java",
        2: "portfolio-backend-python",
    }
    return input_options.get(user_input)


def is_docker_daemon_running():
    command = "docker ps -q"
    output = subprocess.getoutput(command)
    if not output:
        return True
    else:
        return False


def get_first_word(sentence):
    all_words = sentence.split()
    return all_words[0]


def get_preferred_techstack():
    stack = input("Please choose the preferred tech stack: \n"
                  "1. React + Java \n"
                  "2. React + Python\n"
                  "Your choice: ")
    return int(stack)


def build_spring_application(result):
    dir = root_dir + "/" + tech_stack(result)
    os.system("mvn -f " + dir + "/pom.xml clean package -DskipTests")
    java_docker_dir = root_dir + "/docker/java-docker/java-backend.jar"
    jar_file_dir = dir + "/target/java-backend-0.0.1-SNAPSHOT.jar"
    print("Copying jar file...")
    os.system("cp " + jar_file_dir + " " + java_docker_dir)
    print("Done copying")

def get_latest_code():
    print("Getting latest code changes")
    os.system("git checkout main")
    print("Checkedout to main")
    os.system("git pull")
    print("Fetched latest code change")

def get_source_code(tech_stack_number):
    if(tech_stack_number == 1):
        # React + Java
        os.system(git_clone_cmd + java_backend)
        os.system(git_clone_cmd + react_frontend)


def main():
    user_preference = get_preferred_techstack()
    get_source_code(user_preference)
    build_spring_application(user_preference)
    os.chdir(root_dir+"/docker/java-docker")
    if is_docker_daemon_running():
        cmd = "docker-compose up -d"
        os.system(cmd)
    else:
        print('Docker daemon is not running. Please start your docker daemon')


if __name__ == "__main__":
    main()
