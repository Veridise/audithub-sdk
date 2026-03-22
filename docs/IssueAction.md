# IssueAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**function_id** | **int** |  | 
**extra** | [**ExtraFunctionArguments**](ExtraFunctionArguments.md) |  | 

## Example

```python
from audithub_sdk.models.issue_action import IssueAction

# TODO update the JSON string below
json = "{}"
# create an instance of IssueAction from a JSON string
issue_action_instance = IssueAction.from_json(json)
# print the JSON string representation of the object
print(IssueAction.to_json())

# convert the object into a dict
issue_action_dict = issue_action_instance.to_dict()
# create an instance of IssueAction from a dict
issue_action_from_dict = IssueAction.from_dict(issue_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


