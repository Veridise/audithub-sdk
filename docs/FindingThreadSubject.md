# FindingThreadSubject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'finding']
**task_id** | **int** |  | 
**analysis_result_id** | **str** |  | 
**finding_id** | **str** |  | 

## Example

```python
from audithub_sdk.models.finding_thread_subject import FindingThreadSubject

# TODO update the JSON string below
json = "{}"
# create an instance of FindingThreadSubject from a JSON string
finding_thread_subject_instance = FindingThreadSubject.from_json(json)
# print the JSON string representation of the object
print(FindingThreadSubject.to_json())

# convert the object into a dict
finding_thread_subject_dict = finding_thread_subject_instance.to_dict()
# create an instance of FindingThreadSubject from a dict
finding_thread_subject_from_dict = FindingThreadSubject.from_dict(finding_thread_subject_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


