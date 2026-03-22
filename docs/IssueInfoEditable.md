# IssueInfoEditable


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**externally_shared** | **bool** | If the issue has been shared in the project public thread. | 
**status** | **str** | State describing the next action item for resolving this issue. | 
**revision_id** | **int** | Unique id for issue revisions. This is used to track concurrent modifications | 
**resolutions** | [**List[IssueResolution]**](IssueResolution.md) | The list resolution PRs or resolution commits to resolve this issue | [optional] 
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
from audithub_sdk.models.issue_info_editable import IssueInfoEditable

# TODO update the JSON string below
json = "{}"
# create an instance of IssueInfoEditable from a JSON string
issue_info_editable_instance = IssueInfoEditable.from_json(json)
# print the JSON string representation of the object
print(IssueInfoEditable.to_json())

# convert the object into a dict
issue_info_editable_dict = issue_info_editable_instance.to_dict()
# create an instance of IssueInfoEditable from a dict
issue_info_editable_from_dict = IssueInfoEditable.from_dict(issue_info_editable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


