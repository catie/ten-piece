import { IVpc, SecurityGroup } from "aws-cdk-lib/aws-ec2";
import { Cluster } from "aws-cdk-lib/aws-ecs";
import { config } from "dotenv";

export class EnvironmentContext {
    readonly stage: string;
    readonly awsAccountId: string;
    readonly awsRegion: string;

    protected constructor(stage?: string, awsAccountId?: string, awsRegion?: string) {
        if (!stage || !stage.length) {
            throw new Error("No environment stage defined; check STAGE environment variable");
        } else if (!awsAccountId || !awsAccountId.length) {
            throw new Error("No environment stage defined; check AWS_DEFAULT_ACCOUNT environment variable");
        } else if (!awsRegion || !awsRegion.length) {
            throw new Error("No environment stage defined; check AWS_DEFAULT_REGION environment variable");
        }

        this.stage = stage;
        this.awsAccountId = awsAccountId;
        this.awsRegion = awsRegion;
    }

    public static fromEnvironment(): EnvironmentContext {
        config();  // Load .env file into environment
        const awsAccountId = process.env.AWS_DEFAULT_ACCOUNT;
        const awsRegion = process.env.AWS_DEFAULT_REGION;
        const stage = process.env.STAGE ?? "test";
        return new EnvironmentContext(stage, awsAccountId, awsRegion);
    }
}

export interface ServiceContextProps {
    readonly environment: EnvironmentContext;
    readonly serviceName: string;
    readonly serviceCore: Cluster;
    readonly securityGroup: SecurityGroup;
}

export class ServiceContext extends EnvironmentContext {
    readonly serviceName: string;
    readonly serviceCore: Cluster;
    readonly securityGroup: SecurityGroup;

    public constructor(props: ServiceContextProps) {
        super(props.environment.stage, props.environment.awsAccountId, props.environment.awsRegion);
        this.serviceName = props.serviceName;
        this.serviceCore = props.serviceCore;
        this.securityGroup = props.securityGroup;
    }

    public privateCloud(): IVpc {
        return this.serviceCore.vpc;
    }
}