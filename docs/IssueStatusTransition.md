# IssueStatusTransition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**issue_id** | **int** |  | 
**function** | **str** |  | 
**from_status** | **str** |  | 
**to_status** | **str** |  | 
**extra** | [**ExtraFunctionArguments**](ExtraFunctionArguments.md) |  | 
**created_by** | **str** |  | 
**created_at** | **datetime** |  | 

## Example

```python
from audithub_sdk.models.issue_status_transition import IssueStatusTransition

# TODO update the JSON string below
json = "{}"
# create an instance of IssueStatusTransition from a JSON string
issue_status_transition_instance = IssueStatusTransition.from_json(json)
# print the JSON string representation of the object
print(IssueStatusTransition.to_json())

# convert the object into a dict
issue_status_transition_dict = issue_status_transition_instance.to_dict()
# create an instance of IssueStatusTransition from a dict
issue_status_transition_from_dict = IssueStatusTransition.from_dict(issue_status_transition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


