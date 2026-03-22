# TaskPatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 

## Example

```python
from audithub_sdk.models.task_patch import TaskPatch

# TODO update the JSON string below
json = "{}"
# create an instance of TaskPatch from a JSON string
task_patch_instance = TaskPatch.from_json(json)
# print the JSON string representation of the object
print(TaskPatch.to_json())

# convert the object into a dict
task_patch_dict = task_patch_instance.to_dict()
# create an instance of TaskPatch from a dict
task_patch_from_dict = TaskPatch.from_dict(task_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


