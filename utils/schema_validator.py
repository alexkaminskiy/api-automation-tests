from jsonschema import validate

def validate_schema(response_json, schema):
    validate(instance=response_json, schema=schema)