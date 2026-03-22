# IssueSeverity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**caption** | **str** |  | 

## Example

```python
from audithub_sdk.models.issue_severity import IssueSeverity

# TODO update the JSON string below
json = "{}"
# create an instance of IssueSeverity from a JSON string
issue_severity_instance = IssueSeverity.from_json(json)
# print the JSON string representation of the object
print(IssueSeverity.to_json())

# convert the object into a dict
issue_severity_dict = issue_severity_instance.to_dict()
# create an instance of IssueSeverity from a dict
issue_severity_from_dict = IssueSeverity.from_dict(issue_severity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


