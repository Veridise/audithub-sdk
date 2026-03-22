# Task


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | [optional] 
**tool_name** | **str** |  | 
**tool_version** | **str** |  | 
**tool_parameters** | **str** |  | [optional] 
**tool_extra** | **str** |  | [optional] 
**version_id** | **int** |  | 
**steps** | [**List[TaskStep]**](TaskStep.md) |  | [optional] 
**status** | **str** |  | 
**info_text** | **str** |  | [optional] 
**created_at** | **datetime** |  | 
**started_at** | **datetime** |  | [optional] 
**finished_at** | **datetime** |  | [optional] 
**artifacts** | [**List[Artifact]**](Artifact.md) |  | [optional] 
**findings_counters** | **Dict[str, int]** |  | [optional] 

## Example

```python
from audithub_sdk.models.task import Task

# TODO update the JSON string below
json = "{}"
# create an instance of Task from a JSON string
task_instance = Task.from_json(json)
# print the JSON string representation of the object
print(Task.to_json())

# convert the object into a dict
task_dict = task_instance.to_dict()
# create an instance of Task from a dict
task_from_dict = Task.from_dict(task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


