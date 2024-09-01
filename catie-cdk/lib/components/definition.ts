export interface TableDefinition {
    readonly partitionKey: string;
    readonly sortKey?: string;
}

export type SupportedDefinition = TableDefinition;

export interface ServiceDefinition {
    readonly serviceName: string;
    readonly components: { [key: string]: SupportedDefinition };
}