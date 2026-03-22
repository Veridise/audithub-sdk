# IssueStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 
**caption** | **str** |  | 
**is_final** | **bool** |  | 

## Example

```python
from audithub_sdk.models.issue_status import IssueStatus

# TODO update the JSON string below
json = "{}"
# create an instance of IssueStatus from a JSON string
issue_status_instance = IssueStatus.from_json(json)
# print the JSON string representation of the object
print(IssueStatus.to_json())

# convert the object into a dict
issue_status_dict = issue_status_instance.to_dict()
# create an instance of IssueStatus from a dict
issue_status_from_dict = IssueStatus.from_dict(issue_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


