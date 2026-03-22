# TaskAdmin


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | [optional] 
**tool_name** | **str** |  | 
**tool_version** | **str** |  | 
**status** | **str** |  | 
**info_text** | **str** |  | [optional] 
**version_id** | **int** |  | 
**created_at** | **datetime** |  | 
**started_at** | **datetime** |  | [optional] 
**finished_at** | **datetime** |  | [optional] 
**created_by** | **str** |  | 
**deleted** | **bool** | If true, then the task has been soft-deleted. | 
**findings_counters** | **Dict[str, int]** |  | [optional] 

## Example

```python
from audithub_sdk.models.task_admin import TaskAdmin

# TODO update the JSON string below
json = "{}"
# create an instance of TaskAdmin from a JSON string
task_admin_instance = TaskAdmin.from_json(json)
# print the JSON string representation of the object
print(TaskAdmin.to_json())

# convert the object into a dict
task_admin_dict = task_admin_instance.to_dict()
# create an instance of TaskAdmin from a dict
task_admin_from_dict = TaskAdmin.from_dict(task_admin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


