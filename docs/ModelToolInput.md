# ModelToolInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | An optional name for this task. If not specified, the current time in UTC will be used. | [optional] 
**phases** | [**Dict[str, ModelToolPhaseParameters]**](ModelToolPhaseParameters.md) |  | [optional] 

## Example

```python
from audithub_sdk.models.model_tool_input import ModelToolInput

# TODO update the JSON string below
json = "{}"
# create an instance of ModelToolInput from a JSON string
model_tool_input_instance = ModelToolInput.from_json(json)
# print the JSON string representation of the object
print(ModelToolInput.to_json())

# convert the object into a dict
model_tool_input_dict = model_tool_input_instance.to_dict()
# create an instance of ModelToolInput from a dict
model_tool_input_from_dict = ModelToolInput.from_dict(model_tool_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


