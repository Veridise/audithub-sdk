# IssueConfigurationOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**likelihood** | [**List[IssueLikelihood]**](IssueLikelihood.md) |  | 
**impact** | [**List[IssueImpact]**](IssueImpact.md) |  | 
**severity** | [**List[IssueSeverity]**](IssueSeverity.md) |  | 
**status** | [**List[IssueStatus]**](IssueStatus.md) |  | 

## Example

```python
from audithub_sdk.models.issue_configuration_options import IssueConfigurationOptions

# TODO update the JSON string below
json = "{}"
# create an instance of IssueConfigurationOptions from a JSON string
issue_configuration_options_instance = IssueConfigurationOptions.from_json(json)
# print the JSON string representation of the object
print(IssueConfigurationOptions.to_json())

# convert the object into a dict
issue_configuration_options_dict = issue_configuration_options_instance.to_dict()
# create an instance of IssueConfigurationOptions from a dict
issue_configuration_options_from_dict = IssueConfigurationOptions.from_dict(issue_configuration_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


