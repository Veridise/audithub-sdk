# VersionPatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delete** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**commit_hash** | **str** |  | [optional] 
**project_revision_hash** | **str** |  | [optional] 
**is_deployed** | **bool** |  | [optional] 

## Example

```python
from audithub_sdk.models.version_patch import VersionPatch

# TODO update the JSON string below
json = "{}"
# create an instance of VersionPatch from a JSON string
version_patch_instance = VersionPatch.from_json(json)
# print the JSON string representation of the object
print(VersionPatch.to_json())

# convert the object into a dict
version_patch_dict = version_patch_instance.to_dict()
# create an instance of VersionPatch from a dict
version_patch_from_dict = VersionPatch.from_dict(version_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


