# IssueType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**caption** | **str** |  | 
**id** | **int** |  | 
**is_organization_specific** | **bool** | Denotes if the type is available only for the current organization. If false then its a generic type | [optional] [default to True]

## Example

```python
from audithub_sdk.models.issue_type import IssueType

# TODO update the JSON string below
json = "{}"
# create an instance of IssueType from a JSON string
issue_type_instance = IssueType.from_json(json)
# print the JSON string representation of the object
print(IssueType.to_json())

# convert the object into a dict
issue_type_dict = issue_type_instance.to_dict()
# create an instance of IssueType from a dict
issue_type_from_dict = IssueType.from_dict(issue_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


