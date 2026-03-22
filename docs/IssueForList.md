# IssueForList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | The time at which the issue was created. | 
**last_updated_at** | **datetime** | The time at which the issue was last updated. | 
**id** | **int** | Issue unique id. | 
**gh_issue_url** | **str** |  | 
**gh_security_advisory_url** | **str** |  | 
**externally_shared** | **bool** | If the issue has been shared in the project public thread. | 
**status** | **str** | State describing the next action item for resolving this issue. | 
**title** | **str** | Title for this issue. | 
**likelihood** | **int** | Probability that the issue will be exploited.. | 
**impact** | **int** | Magnitude of the effect on the protocol if the issue is exploited. | 
**severity** | **int** | The protocol risk associated to an issue, based on its likelihood and impact. | 

## Example

```python
from audithub_sdk.models.issue_for_list import IssueForList

# TODO update the JSON string below
json = "{}"
# create an instance of IssueForList from a JSON string
issue_for_list_instance = IssueForList.from_json(json)
# print the JSON string representation of the object
print(IssueForList.to_json())

# convert the object into a dict
issue_for_list_dict = issue_for_list_instance.to_dict()
# create an instance of IssueForList from a dict
issue_for_list_from_dict = IssueForList.from_dict(issue_for_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


