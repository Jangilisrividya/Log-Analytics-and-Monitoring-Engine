#schema files define the structure of data and type of data,role book of data
#it ensures all rows follows the same structure of data
#helps to validate data
#faster processing,easier analytics(filtering,mapping,grouping and anomoloy detection becomes simple and faster)
LOG_SCHEMA = {
    "timestamp": "datetime64[ns]",
    "level": "string",
    "service": "string",
    "message": "string",
}
#dataframe df.astype(log_schema)
