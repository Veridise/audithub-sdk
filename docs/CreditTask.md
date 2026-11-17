# CreditTask


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**tool_name** | **str** |  | 
**project_id** | **int** |  | 
**version_id** | **int** |  | 
**started_at** | **datetime** |  | 
**finished_at** | **datetime** |  | 
**computing_credits** | **str** |  | 
**ai_credits** | **str** |  | 
**credits_sources** | [**List[TaskCreditSource]**](TaskCreditSource.md) |  | 

## Example

```python
from audithub_sdk.models.credit_task import CreditTask

# TODO update the JSON string below
json = "{}"
# create an instance of CreditTask from a JSON string
credit_task_instance = CreditTask.from_json(json)
# print the JSON string representation of the object
print(CreditTask.to_json())

# convert the object into a dict
credit_task_dict = credit_task_instance.to_dict()
# create an instance of CreditTask from a dict
credit_task_from_dict = CreditTask.from_dict(credit_task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


