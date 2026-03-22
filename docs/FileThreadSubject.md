# FileThreadSubject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'file_range']
**file_path** | **str** |  | 
**from_line** | **int** |  | 
**to_line** | **int** |  | 

## Example

```python
from audithub_sdk.models.file_thread_subject import FileThreadSubject

# TODO update the JSON string below
json = "{}"
# create an instance of FileThreadSubject from a JSON string
file_thread_subject_instance = FileThreadSubject.from_json(json)
# print the JSON string representation of the object
print(FileThreadSubject.to_json())

# convert the object into a dict
file_thread_subject_dict = file_thread_subject_instance.to_dict()
# create an instance of FileThreadSubject from a dict
file_thread_subject_from_dict = FileThreadSubject.from_dict(file_thread_subject_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


