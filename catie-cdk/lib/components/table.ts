import { Attribute, AttributeType, Table } from "aws-cdk-lib/aws-dynamodb";
import { TableDefinition } from "./definition";
import { ServiceComponent, ServiceComponentProps } from "./component";
import { Function } from "aws-cdk-lib/aws-lambda";
import { IPrincipal } from "aws-cdk-lib/aws-iam";

export class ServiceTable extends ServiceComponent {
    readonly table: Table;
    readonly handler: Function;

    public constructor(props: ServiceComponentProps, definition: TableDefinition) {
        super(props);

        const partitionKey = this.buildKey(definition.partitionKey);
        const sortKey = this.buildKey(definition.sortKey);
        if (!partitionKey) {
            throw new Error(`No partition key defined for ${this.componentName} table`);
        }

        this.table = new Table(this, `${this.componentName}-table`, {
            tableName: `${this.componentName}-${this.context.stage}`,
            partitionKey: partitionKey,
            sortKey: sortKey,
        });
    }

    private buildKey(keyName?: string): Attribute | undefined {
        if (!keyName) {
            return undefined;
        }

        return {
            type: AttributeType.STRING,
            name: keyName,
        };
    }

    public grantAccess(principal: IPrincipal): void {
        this.table.grantReadWriteData(principal);
    }
}