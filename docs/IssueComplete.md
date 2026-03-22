# IssueComplete


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Issue unique id. | 
**gh_issue_url** | **str** |  | 
**gh_security_advisory_url** | **str** |  | 
**created_at** | **datetime** | The time at which the issue was created. | 
**last_updated_at** | **datetime** | The time at which the issue was last updated. | 
**created_by** | **str** | The user that created the issue. | 
**last_updated_by** | **str** | The user that last updated the issue. | 
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
from audithub_sdk.models.issue_complete import IssueComplete

# TODO update the JSON string below
json = "{}"
# create an instance of IssueComplete from a JSON string
issue_complete_instance = IssueComplete.from_json(json)
# print the JSON string representation of the object
print(IssueComplete.to_json())

# convert the object into a dict
issue_complete_dict = issue_complete_instance.to_dict()
# create an instance of IssueComplete from a dict
issue_complete_from_dict = IssueComplete.from_dict(issue_complete_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


