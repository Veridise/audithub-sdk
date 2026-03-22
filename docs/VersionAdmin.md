# VersionAdmin


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**archive_catalog** | [**Directory**](Directory.md) |  | [optional] 
**archive_abi** | **List[object]** |  | [optional] 
**created_at** | **datetime** |  | 
**input_info** | [**InputInfo**](InputInfo.md) |  | 
**project_revision_hash** | **str** |  | 
**digest** | **str** |  | 
**commit_hash** | **str** |  | 
**is_deployed** | **bool** |  | 
**deleted** | **bool** | If true, then the version has been soft-deleted. | 
**created_by** | **str** |  | 
**organization_id** | **int** |  | 
**project_id** | **int** |  | 

## Example

```python
from audithub_sdk.models.version_admin import VersionAdmin

# TODO update the JSON string below
json = "{}"
# create an instance of VersionAdmin from a JSON string
version_admin_instance = VersionAdmin.from_json(json)
# print the JSON string representation of the object
print(VersionAdmin.to_json())

# convert the object into a dict
version_admin_dict = version_admin_instance.to_dict()
# create an instance of VersionAdmin from a dict
version_admin_from_dict = VersionAdmin.from_dict(version_admin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


