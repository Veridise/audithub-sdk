# TaskCreditConsumption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**computing_credits** | **str** | Computing credits for finished execution; zero for unfinished tasks. | 
**ai_credits** | **str** | Recorded credit reservations for unfinished tasks; calculated AI credits for finished tasks. | 
**total_credits** | **str** |  | 

## Example

```python
from audithub_sdk.models.task_credit_consumption import TaskCreditConsumption

# TODO update the JSON string below
json = "{}"
# create an instance of TaskCreditConsumption from a JSON string
task_credit_consumption_instance = TaskCreditConsumption.from_json(json)
# print the JSON string representation of the object
print(TaskCreditConsumption.to_json())

# convert the object into a dict
task_credit_consumption_dict = task_credit_consumption_instance.to_dict()
# create an instance of TaskCreditConsumption from a dict
task_credit_consumption_from_dict = TaskCreditConsumption.from_dict(task_credit_consumption_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


