<img width="100" alt="Screenshot 2021-06-29 at 8 12 27 AM" src="https://user-images.githubusercontent.com/39675511/123728969-d2a87b00-d8b1-11eb-9ece-558d4021f816.png">

# Swagger-petstore API automation with python, request library and pytest

## Table of Contents

- [Tools And Technology](#tools-and-technology)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Makefile](#makefile)
- [Running test in local](#running-tests-in-local)
- [Running tests in docker container](#running-tests-in-docker-container)
- [Reports](#reports)
- [Tech approch explanation](#tech-approch-explanation)


## Tools And Technology
- python 
- request library
- pytest
- html-Report
- visual studio code editor

## Prerequisites

- Ensure ([swagger-petstoreOpenAPI 3.01.0.26 ](https://github.com/swagger-api/swagger-petstore.git)) server is up and runnning - follow the instruction in given repository README.md for local test execution

## Makefile 

- use below command to check all available command in make file and uses 
```sh
make help
```
## Installation

Clone the repository:

```sh
git clone https://github.com/sumant326541/swagger-petstore-api-automation.git
```
install dependencies and setup python environment

```sh
make all
```

## Running Tests in local

```js
make test
```

## Running Tests in docker container

- Build Docker images

```js
make docker-build
```
- Run test in docker container with emulator on host machine

```js
make docker-up
```
- OR

```js
make docker-test
```


## Reports

- to open html report

 ```js
make report
``` 

## Tech approch explanation

 ### request library with python
 Full HTTP Support with exlent error handling and assertion
 Easy to maintain data driven test

 ### Pytest framework
 Very eassy to start test execution 
 different marker to controll and skip test
 Customize test discovery, execution, logging, or reporting via hook functions 
 Generate reports, run tests in parallel, and integration with CI/CD
 
 - Conftest 
   - Global and shared fixture through out the test
   - Centralize envirnment setting, test data and common const
   - Cleaner test code
   - reusabilty

### Makefile
- Simplifies environment setup
- Streamlines dependency installation
- Automates repetitive tasks for faster development

        