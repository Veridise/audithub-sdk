# FindingAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_id** | **str** |  | 
**caption** | **str** |  | 
**comment** | **str** |  | [optional] 
**created_by** | **str** |  | 
**created_at** | **datetime** |  | 

## Example

```python
from audithub_sdk.models.finding_action import FindingAction

# TODO update the JSON string below
json = "{}"
# create an instance of FindingAction from a JSON string
finding_action_instance = FindingAction.from_json(json)
# print the JSON string representation of the object
print(FindingAction.to_json())

# convert the object into a dict
finding_action_dict = finding_action_instance.to_dict()
# create an instance of FindingAction from a dict
finding_action_from_dict = FindingAction.from_dict(finding_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


