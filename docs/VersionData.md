# VersionData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] [default to 'initial']
**digest** | **str** |  | [optional] 
**commit_hash** | **str** |  | [optional] 
**data_path** | **str** | S3 reference relative to the package root | 

## Example

```python
from audithub_sdk.models.version_data import VersionData

# TODO update the JSON string below
json = "{}"
# create an instance of VersionData from a JSON string
version_data_instance = VersionData.from_json(json)
# print the JSON string representation of the object
print(VersionData.to_json())

# convert the object into a dict
version_data_dict = version_data_instance.to_dict()
# create an instance of VersionData from a dict
version_data_from_dict = VersionData.from_dict(version_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


