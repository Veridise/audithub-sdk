# StepResources


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 
**resources** | [**Resources**](Resources.md) |  | 
**containers** | [**List[ContainerResources]**](ContainerResources.md) |  | 

## Example

```python
from audithub_sdk.models.step_resources import StepResources

# TODO update the JSON string below
json = "{}"
# create an instance of StepResources from a JSON string
step_resources_instance = StepResources.from_json(json)
# print the JSON string representation of the object
print(StepResources.to_json())

# convert the object into a dict
step_resources_dict = step_resources_instance.to_dict()
# create an instance of StepResources from a dict
step_resources_from_dict = StepResources.from_dict(step_resources_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


