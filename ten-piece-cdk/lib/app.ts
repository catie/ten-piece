#!/usr/bin/env node

import { App } from 'aws-cdk-lib';
import { EnvironmentContext, Service, ServiceDefinition } from 'catie-cdk';

export const definition: ServiceDefinition = {
  serviceName: "TenPiece",
  components: {
    User: {
      partitionKey: "user_id"
    },
    Scope: {
      partitionKey: "scope_id"
    },
    Tag: {
      partitionKey: "tag_id"
    },
    Character: {
      partitionKey: "character_id"
    },
    Ranking: {
      partitionKey: "ranking_id"
    },
    api: {
      assetPath: "../ten-piece-app",
    }
  },
}
const app = new App();
const environment = EnvironmentContext.fromEnvironment();

new Service(app, environment, definition);