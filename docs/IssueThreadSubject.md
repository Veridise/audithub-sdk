# IssueThreadSubject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'issue']
**issue_id** | **int** |  | 

## Example

```python
from audithub_sdk.models.issue_thread_subject import IssueThreadSubject

# TODO update the JSON string below
json = "{}"
# create an instance of IssueThreadSubject from a JSON string
issue_thread_subject_instance = IssueThreadSubject.from_json(json)
# print the JSON string representation of the object
print(IssueThreadSubject.to_json())

# convert the object into a dict
issue_thread_subject_dict = issue_thread_subject_instance.to_dict()
# create an instance of IssueThreadSubject from a dict
issue_thread_subject_from_dict = IssueThreadSubject.from_dict(issue_thread_subject_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


