# AIBudget


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | 

## Example

```python
from audithub_sdk.models.ai_budget import AIBudget

# TODO update the JSON string below
json = "{}"
# create an instance of AIBudget from a JSON string
ai_budget_instance = AIBudget.from_json(json)
# print the JSON string representation of the object
print(AIBudget.to_json())

# convert the object into a dict
ai_budget_dict = ai_budget_instance.to_dict()
# create an instance of AIBudget from a dict
ai_budget_from_dict = AIBudget.from_dict(ai_budget_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


