# IssueInfoBaseComplete


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**promoted_findings** | [**List[FindingReference]**](FindingReference.md) | Tool findings related to this issue. | 
**candidate_for_tool** | **List[int]** | If one or more of our tools would be a good candidate for finding this issue. | 
**raised_by** | **List[str]** | The user that raised the issue. Allows for a potentially different user than the one that inputs it. | 
**poc_author** | **List[str]** | AuditHub user that created the PoC. | 
**document_authors** | **List[str]** | The list of auditors that authored the document for this issue. | 
**description** | **str** | The long, markdown formatted text that describes the issue in detail. | 
**affected_files** | [**List[SourceReference]**](SourceReference.md) | A list of locations in files. | 
**type** | **List[int]** | Categorization of the issue’s root cause. | 
**title** | **str** | Title for this issue. | 
**likelihood** | **int** | Probability that the issue will be exploited.. | 
**impact** | **int** | Magnitude of the effect on the protocol if the issue is exploited. | 
**severity** | **int** | The protocol risk associated to an issue, based on its likelihood and impact. | 

## Example

```python
from audithub_sdk.models.issue_info_base_complete import IssueInfoBaseComplete

# TODO update the JSON string below
json = "{}"
# create an instance of IssueInfoBaseComplete from a JSON string
issue_info_base_complete_instance = IssueInfoBaseComplete.from_json(json)
# print the JSON string representation of the object
print(IssueInfoBaseComplete.to_json())

# convert the object into a dict
issue_info_base_complete_dict = issue_info_base_complete_instance.to_dict()
# create an instance of IssueInfoBaseComplete from a dict
issue_info_base_complete_from_dict = IssueInfoBaseComplete.from_dict(issue_info_base_complete_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


