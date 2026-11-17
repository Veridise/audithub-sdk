# AgentParameters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input_limit** | **List[str]** |  | [optional] 
**extra_context** | **str** |  | [optional] 
**generate_pocs** | **bool** |  | [optional] [default to False]

## Example

```python
from audithub_sdk.models.agent_parameters import AgentParameters

# TODO update the JSON string below
json = "{}"
# create an instance of AgentParameters from a JSON string
agent_parameters_instance = AgentParameters.from_json(json)
# print the JSON string representation of the object
print(AgentParameters.to_json())

# convert the object into a dict
agent_parameters_dict = agent_parameters_instance.to_dict()
# create an instance of AgentParameters from a dict
agent_parameters_from_dict = AgentParameters.from_dict(agent_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


