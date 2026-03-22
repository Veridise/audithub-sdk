# TaskFIOData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_id** | **int** |  | 
**analysis_results** | [**List[FIOData]**](FIOData.md) |  | 

## Example

```python
from audithub_sdk.models.task_fio_data import TaskFIOData

# TODO update the JSON string below
json = "{}"
# create an instance of TaskFIOData from a JSON string
task_fio_data_instance = TaskFIOData.from_json(json)
# print the JSON string representation of the object
print(TaskFIOData.to_json())

# convert the object into a dict
task_fio_data_dict = task_fio_data_instance.to_dict()
# create an instance of TaskFIOData from a dict
task_fio_data_from_dict = TaskFIOData.from_dict(task_fio_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


