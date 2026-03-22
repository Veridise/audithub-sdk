# StepDefinition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**caption** | **str** |  | 
**short_name** | **str** |  | 
**is_tool** | **bool** | Denotes if the step is running a tool. If false it&#39;s just a preparation step. | [optional] [default to False]

## Example

```python
from audithub_sdk.models.step_definition import StepDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of StepDefinition from a JSON string
step_definition_instance = StepDefinition.from_json(json)
# print the JSON string representation of the object
print(StepDefinition.to_json())

# convert the object into a dict
step_definition_dict = step_definition_instance.to_dict()
# create an instance of StepDefinition from a dict
step_definition_from_dict = StepDefinition.from_dict(step_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


