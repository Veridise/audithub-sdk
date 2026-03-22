# TaskResources


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**resources** | [**Resources**](Resources.md) |  | 
**steps** | [**List[StepResources]**](StepResources.md) |  | 

## Example

```python
from audithub_sdk.models.task_resources import TaskResources

# TODO update the JSON string below
json = "{}"
# create an instance of TaskResources from a JSON string
task_resources_instance = TaskResources.from_json(json)
# print the JSON string representation of the object
print(TaskResources.to_json())

# convert the object into a dict
task_resources_dict = task_resources_instance.to_dict()
# create an instance of TaskResources from a dict
task_resources_from_dict = TaskResources.from_dict(task_resources_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


