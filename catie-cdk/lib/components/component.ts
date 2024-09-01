import { Construct } from "constructs";
import { Vpc } from "aws-cdk-lib/aws-ec2";
import { ServiceContext } from './context';

export interface ServiceComponentProps {
    readonly scope: Construct;
    readonly context: ServiceContext;
    readonly name: string;
}

export class ServiceComponent extends Construct {
    readonly componentName: string;
    readonly context: ServiceContext;
    readonly vpc: Vpc;

    public constructor(props: ServiceComponentProps) {
        super(props.scope, props.name);

        this.componentName = props.name;
        this.context = props.context;
    }
}