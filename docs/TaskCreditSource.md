# TaskCreditSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_type** | [**CreditSourceType**](CreditSourceType.md) |  | 
**source_id** | **int** |  | 
**period_start** | **datetime** |  | 
**credits** | **str** |  | 

## Example

```python
from audithub_sdk.models.task_credit_source import TaskCreditSource

# TODO update the JSON string below
json = "{}"
# create an instance of TaskCreditSource from a JSON string
task_credit_source_instance = TaskCreditSource.from_json(json)
# print the JSON string representation of the object
print(TaskCreditSource.to_json())

# convert the object into a dict
task_credit_source_dict = task_credit_source_instance.to_dict()
# create an instance of TaskCreditSource from a dict
task_credit_source_from_dict = TaskCreditSource.from_dict(task_credit_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


