import { Stack } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { ServiceDefinition, SupportedDefinition } from './definition';
import { EnvironmentContext, ServiceContext } from './context';
import { ServiceTable } from './table';
import { Cluster } from 'aws-cdk-lib/aws-ecs';
import { ServiceComponentProps } from './component';
import { Peer, Port, SecurityGroup } from 'aws-cdk-lib/aws-ec2';

export class Service extends Stack {
  readonly context: ServiceContext;
  readonly coreCluster: Cluster;
  readonly securityGroup: SecurityGroup;

  constructor(scope: Construct, environment: EnvironmentContext, definition: ServiceDefinition) {
    super(scope, definition.serviceName, {
      env: {
        account: environment.awsAccountId,
        region: environment.awsRegion,
      }
    });

    this.coreCluster = new Cluster(this, `${definition.serviceName}-core`);
    this.securityGroup = new SecurityGroup(this, "SecurityGroup", {
      vpc: this.coreCluster.vpc,
      allowAllOutbound: true,
    });

    this.securityGroup.addIngressRule(Peer.anyIpv4(), Port.tcp(3000));

    this.context = new ServiceContext({
      environment: environment,
      serviceName: definition.serviceName,
      serviceCore: this.coreCluster,
      securityGroup: this.securityGroup,
    });
    Object.entries(definition.components)
      .forEach(([componentName, definition]) => this.buildComponent(componentName, definition));
  }

  private buildComponent(componentName: string, definition: SupportedDefinition): void {
    // TODO: Add more components
    new ServiceTable(this.getPropsFor(componentName), definition);
  }

  private getPropsFor(componentName: string): ServiceComponentProps {
    return {
      scope: this,
      context: this.context,
      name: componentName,
    }
  }
}
