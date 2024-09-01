#!/usr/bin/env node
import 'source-map-support/register';
import { App } from 'aws-cdk-lib';
import { EnvironmentContext, Service, ServiceDefinition } from 'catie-cdk';

export const definition: ServiceDefinition = {
  serviceName: "TenPiece",
  components: {
    users: {
      "partitionKey": "user_id"
    },
    participants: {
      "partitionKey": "participant_id"
    },
    characters: {
      "partitionKey": "character_id"
    },
  },
}
const app = new App();
const environment = EnvironmentContext.fromEnvironment();

new Service(app, environment, definition);