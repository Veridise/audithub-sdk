# FindingActionBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_id** | **str** |  | 
**caption** | **str** |  | 
**comment** | **str** |  | [optional] 

## Example

```python
from audithub_sdk.models.finding_action_base import FindingActionBase

# TODO update the JSON string below
json = "{}"
# create an instance of FindingActionBase from a JSON string
finding_action_base_instance = FindingActionBase.from_json(json)
# print the JSON string representation of the object
print(FindingActionBase.to_json())

# convert the object into a dict
finding_action_base_dict = finding_action_base_instance.to_dict()
# create an instance of FindingActionBase from a dict
finding_action_base_from_dict = FindingActionBase.from_dict(finding_action_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


