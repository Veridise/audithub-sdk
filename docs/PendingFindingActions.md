# PendingFindingActions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state_digest** | **int** |  | 
**analysis_result_id** | **str** |  | 
**actions** | [**List[FindingActionBase]**](FindingActionBase.md) |  | 

## Example

```python
from audithub_sdk.models.pending_finding_actions import PendingFindingActions

# TODO update the JSON string below
json = "{}"
# create an instance of PendingFindingActions from a JSON string
pending_finding_actions_instance = PendingFindingActions.from_json(json)
# print the JSON string representation of the object
print(PendingFindingActions.to_json())

# convert the object into a dict
pending_finding_actions_dict = pending_finding_actions_instance.to_dict()
# create an instance of PendingFindingActions from a dict
pending_finding_actions_from_dict = PendingFindingActions.from_dict(pending_finding_actions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


