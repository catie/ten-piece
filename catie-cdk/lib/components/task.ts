import { ManagedPolicy, Role, ServicePrincipal } from "aws-cdk-lib/aws-iam";
import { ServiceComponent, ServiceComponentProps } from "./component";
import { TaskDefinition } from "./definition";
import { ContainerDefinition, ContainerImage, CpuArchitecture, FargateService, FargateTaskDefinition, LogDrivers, OperatingSystemFamily } from "aws-cdk-lib/aws-ecs";
import { SubnetType } from "aws-cdk-lib/aws-ec2";

export class ServiceTask extends ServiceComponent {
    readonly container: ContainerDefinition;

    public constructor(props: ServiceComponentProps, definition: TaskDefinition) {
        super(props);

        const executionRole = new Role(this, `${this.componentName}ExecutionRole`, {
            assumedBy: new ServicePrincipal("ecs-tasks.amazonaws.com"),
            managedPolicies: [
                ManagedPolicy.fromAwsManagedPolicyName(
                    "service-role/AmazonECSTaskExecutionRolePolicy"
                ),
            ],
        });

        const taskDefinition = new FargateTaskDefinition(
            this,
            `${this.componentName}Definition`,
            {
                executionRole,
                runtimePlatform: {
                    operatingSystemFamily: OperatingSystemFamily.LINUX,
                    cpuArchitecture: CpuArchitecture.X86_64,
                },
            }
        );

        this.container = taskDefinition.addContainer(`${this.componentName}Container`, {
            image: ContainerImage.fromRegistry("https://gallery.ecr.aws/sam/build-python3.9"),
            memoryLimitMiB: 512,
            cpu: 256,
            logging: LogDrivers.awsLogs({ streamPrefix: this.context.serviceName }),
            environment: {
                STAGE: this.context.stage,
            }
        });

        this.container.addPortMappings({
            containerPort: definition.port ?? 3000,
        });

        new FargateService(this, `${this.componentName}Service`, {
            cluster: this.context.serviceCore,
            taskDefinition: taskDefinition,
            assignPublicIp: true,
            vpcSubnets: { subnetType: SubnetType.PUBLIC },
            securityGroups: [this.context.securityGroup],
        });
    }

    public addEnvironment(varName: string, value: string): void {
        this.container.addEnvironment(varName, value);
    }
}