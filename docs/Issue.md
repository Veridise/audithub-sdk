# Issue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Issue unique id. | 
**gh_issue_url** | **str** |  | 
**gh_security_advisory_url** | **str** |  | 
**status** | **str** | State describing the next action item for resolving this issue. | 
**revision_id** | **int** | Unique id for issue revisions. This is used to track concurrent modifications | 
**resolutions** | [**List[IssueResolution]**](IssueResolution.md) | The list resolution PRs or resolution commits to resolve this issue | [optional] 
**description** | **str** | The long, markdown formatted text that describes the issue in detail. | 
**affected_files** | [**List[SourceReference]**](SourceReference.md) | A list of locations in files. | 
**type** | **List[int]** | Categorization of the issue’s root cause. | 
**title** | **str** | Title for this issue. | 
**likelihood** | **int** | Probability that the issue will be exploited.. | 
**impact** | **int** | Magnitude of the effect on the protocol if the issue is exploited. | 
**severity** | **int** | The protocol risk associated to an issue, based on its likelihood and impact. | 

## Example

```python
from audithub_sdk.models.issue import Issue

# TODO update the JSON string below
json = "{}"
# create an instance of Issue from a JSON string
issue_instance = Issue.from_json(json)
# print the JSON string representation of the object
print(Issue.to_json())

# convert the object into a dict
issue_dict = issue_instance.to_dict()
# create an instance of Issue from a dict
issue_from_dict = Issue.from_dict(issue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


