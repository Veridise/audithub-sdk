# IssueStateTransitionFunction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**code** | **str** |  | 
**caption** | **str** |  | 
**has_comment** | **bool** |  | 
**has_pr** | **bool** |  | 
**optional_comment** | **bool** |  | 
**pre_populated_extra** | [**ExtraFunctionArguments**](ExtraFunctionArguments.md) |  | 
**available_to_developers** | **bool** |  | 

## Example

```python
from audithub_sdk.models.issue_state_transition_function import IssueStateTransitionFunction

# TODO update the JSON string below
json = "{}"
# create an instance of IssueStateTransitionFunction from a JSON string
issue_state_transition_function_instance = IssueStateTransitionFunction.from_json(json)
# print the JSON string representation of the object
print(IssueStateTransitionFunction.to_json())

# convert the object into a dict
issue_state_transition_function_dict = issue_state_transition_function_instance.to_dict()
# create an instance of IssueStateTransitionFunction from a dict
issue_state_transition_function_from_dict = IssueStateTransitionFunction.from_dict(issue_state_transition_function_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


