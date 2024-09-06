# TenPiece Service Definition

## Overview

Directory structure:

```
- ten-piece
    - README.md (You Are Here!)
    - .gitignore
    - ten-piece/
    - ten-piece-cdk/
    - catie-cdk/
```

## TenPiece (ten-piece-app)

AWS SAM app and Python service code for the TenPiece application.

### Dev Environment Setup
These steps assume the developer alread has the TenPiece project is already checked out locally.

* Install [Python 3.12](https://www.python.org/downloads/). Confirm that `pip` was installed correctly:
    `> pip3 --version`
* Navigate to the `ten-piece-app` directory:
    `> cd ten-piece-app`
* Install the required Python dependencies:
    `> pip3 install -r requirements.txt`
* Build the project to confirm that your Python environment is set up correctly:
    `> python3 -m build`

## TenPiece CDK/Infrastructure (ten-piece-cdk)

CDK and infrastructure definitions for the TenPiece application.

### Useful commands

* `npm run build`   Compile typescript to js
* `npm run watch`   Watch for changes and compile
* `npm run test`    Perform the jest unit tests
* `npx cdk deploy`  Deploy this stack to your default AWS account/region
* `npx cdk diff`    Compare deployed stack with current state
* `npx cdk synth`   Emits the synthesized CloudFormation template

## Catie's Easy AWS CDK Library (catie-cdk)

CatieCDK is a TypeScript wrapper library for building AWS CDK applications with a minimum of fuss.