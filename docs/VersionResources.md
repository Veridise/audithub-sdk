# VersionResources


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**resources** | [**Resources**](Resources.md) |  | 
**tasks** | [**List[TaskResources]**](TaskResources.md) |  | 

## Example

```python
from audithub_sdk.models.version_resources import VersionResources

# TODO update the JSON string below
json = "{}"
# create an instance of VersionResources from a JSON string
version_resources_instance = VersionResources.from_json(json)
# print the JSON string representation of the object
print(VersionResources.to_json())

# convert the object into a dict
version_resources_dict = version_resources_instance.to_dict()
# create an instance of VersionResources from a dict
version_resources_from_dict = VersionResources.from_dict(version_resources_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


