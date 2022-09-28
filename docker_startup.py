#!/usr/bin/env python3


__author__ = "Sehran"
__version__ = "1.0"

import os
import subprocess

root_dir = os.getcwd()
portfolio_frontend_react = "portfolio-frontend-react"
portfolio_backend_java = "portfolio-backend-java"

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
    user_input = None
    while user_input is None:
        stack = input("Please choose the preferred tech stack: \n"
                      "1. React + Java \n"
                      "2. React + Python (Not Available yet) \n"
                      "Your choice: ")
        try:
            user_input = int(stack)
            if user_input == 1:
                return user_input
            else:
                print("Invalid number")
                user_input = None

        except ValueError:
            print("{input_value} is not a number, please enter a number only.".format(input_value=stack))

    return user_input


def code_exists(folder):
    return os.path.exists(root_dir + '/' + folder)


def get_source_code(tech_stack_number):
    if tech_stack_number == 1:
        # React + Java
        if not code_exists(portfolio_backend_java):
            os.system(git_clone_cmd + java_backend)
        else:
            print("Java directory already exist!")
            os.chdir(root_dir + '/' + portfolio_backend_java)
            print("Pulling the latest code")
            os.system("git pull")
            os.chdir(root_dir)

        if not code_exists(portfolio_frontend_react):
            print("Code does not exists")
            os.system(git_clone_cmd + react_frontend)
        else:
            print("React directory already exists")
            os.chdir(root_dir + '/' + portfolio_frontend_react)
            print("Pulling the latest code")
            os.system("git pull")
            os.chdir(root_dir)


def run_docker_compose(preference):
    if preference == 1:
        os.system("docker-compose -f java-react-docker-compose.yml up -d")


def main():
    user_preference = get_preferred_techstack()
    get_source_code(user_preference)
    if is_docker_daemon_running():
        run_docker_compose(user_preference)
        print("Docker containers up and running")
    else:
        print('Docker daemon is not running. Please start docker daemon')


if __name__ == "__main__":
    main()
