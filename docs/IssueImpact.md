# IssueImpact


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**caption** | **str** |  | 

## Example

```python
from audithub_sdk.models.issue_impact import IssueImpact

# TODO update the JSON string below
json = "{}"
# create an instance of IssueImpact from a JSON string
issue_impact_instance = IssueImpact.from_json(json)
# print the JSON string representation of the object
print(IssueImpact.to_json())

# convert the object into a dict
issue_impact_dict = issue_impact_instance.to_dict()
# create an instance of IssueImpact from a dict
issue_impact_from_dict = IssueImpact.from_dict(issue_impact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


