# SourceReference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version_id** | **int** | A reference to the version this file belongs in. | 
**relative_path** | **str** | The path from the archive root of the referenced file or folder. | 
**line_from** | **int** |  | [optional] 
**line_to** | **int** |  | [optional] 

## Example

```python
from audithub_sdk.models.source_reference import SourceReference

# TODO update the JSON string below
json = "{}"
# create an instance of SourceReference from a JSON string
source_reference_instance = SourceReference.from_json(json)
# print the JSON string representation of the object
print(SourceReference.to_json())

# convert the object into a dict
source_reference_dict = source_reference_instance.to_dict()
# create an instance of SourceReference from a dict
source_reference_from_dict = SourceReference.from_dict(source_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


