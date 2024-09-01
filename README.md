# TenPiece Service Definition

## Overview

Directory structure:

```
- ten-piece
    - README.md (You Are Here!)
    - .gitignore
    - catie-cdk/
    - ten-piece-cdk/
    - ten-piece-core/
```

## Catie's Easy AWS CDK Library (catie-cdk)

CatieCDK is a TypeScript wrapper library for building AWS CDK applications with a minimum of fuss.

## TenPiece CDK/Infrastructure (ten-piece-cdk)

CDK and infrastructure definitions for the TenPiece application.

### Useful commands

* `npm run build`   Compile typescript to js
* `npm run watch`   Watch for changes and compile
* `npm run test`    Perform the jest unit tests
* `npx cdk deploy`  Deploy this stack to your default AWS account/region
* `npx cdk diff`    Compare deployed stack with current state
* `npx cdk synth`   Emits the synthesized CloudFormation template

## TenPiece (ten-piece)

Python service code for the TenPiece application.