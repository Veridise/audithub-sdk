# TempVersion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**archive_catalog** | [**Directory**](Directory.md) |  | 

## Example

```python
from audithub_sdk.models.temp_version import TempVersion

# TODO update the JSON string below
json = "{}"
# create an instance of TempVersion from a JSON string
temp_version_instance = TempVersion.from_json(json)
# print the JSON string representation of the object
print(TempVersion.to_json())

# convert the object into a dict
temp_version_dict = temp_version_instance.to_dict()
# create an instance of TempVersion from a dict
temp_version_from_dict = TempVersion.from_dict(temp_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


