# ArchiveInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input_type** | **str** |  | [optional] [default to 'archive']
**url** | **str** |  | [optional] 

## Example

```python
from audithub_sdk.models.archive_input import ArchiveInput

# TODO update the JSON string below
json = "{}"
# create an instance of ArchiveInput from a JSON string
archive_input_instance = ArchiveInput.from_json(json)
# print the JSON string representation of the object
print(ArchiveInput.to_json())

# convert the object into a dict
archive_input_dict = archive_input_instance.to_dict()
# create an instance of ArchiveInput from a dict
archive_input_from_dict = ArchiveInput.from_dict(archive_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


