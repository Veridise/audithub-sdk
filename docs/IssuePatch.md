# IssuePatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**IssueAction**](IssueAction.md) |  | [optional] 
**delete** | **bool** |  | [optional] 

## Example

```python
from audithub_sdk.models.issue_patch import IssuePatch

# TODO update the JSON string below
json = "{}"
# create an instance of IssuePatch from a JSON string
issue_patch_instance = IssuePatch.from_json(json)
# print the JSON string representation of the object
print(IssuePatch.to_json())

# convert the object into a dict
issue_patch_dict = issue_patch_instance.to_dict()
# create an instance of IssuePatch from a dict
issue_patch_from_dict = IssuePatch.from_dict(issue_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


