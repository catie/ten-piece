export interface TaskDefinition {
    readonly assetPath: string;
    readonly port?: number;
}

export interface TableDefinition {
    readonly partitionKey: string;
    readonly sortKey?: string;
}

export type SupportedDefinition = TableDefinition | TaskDefinition;

export interface ServiceDefinition {
    readonly serviceName: string;
    readonly components: { [key: string]: SupportedDefinition };
}