# IssueResolution


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resolution_pr** | **str** |  | [optional] 
**resolution_commit** | **str** |  | [optional] 

## Example

```python
from audithub_sdk.models.issue_resolution import IssueResolution

# TODO update the JSON string below
json = "{}"
# create an instance of IssueResolution from a JSON string
issue_resolution_instance = IssueResolution.from_json(json)
# print the JSON string representation of the object
print(IssueResolution.to_json())

# convert the object into a dict
issue_resolution_dict = issue_resolution_instance.to_dict()
# create an instance of IssueResolution from a dict
issue_resolution_from_dict = IssueResolution.from_dict(issue_resolution_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


