# Subject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'file_range']
**file_path** | **str** |  | 
**from_line** | **int** |  | 
**to_line** | **int** |  | 
**task_id** | **int** |  | 
**analysis_result_id** | **str** |  | 
**finding_id** | **str** |  | 
**issue_id** | **int** |  | 

## Example

```python
from audithub_sdk.models.subject import Subject

# TODO update the JSON string below
json = "{}"
# create an instance of Subject from a JSON string
subject_instance = Subject.from_json(json)
# print the JSON string representation of the object
print(Subject.to_json())

# convert the object into a dict
subject_dict = subject_instance.to_dict()
# create an instance of Subject from a dict
subject_from_dict = Subject.from_dict(subject_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


