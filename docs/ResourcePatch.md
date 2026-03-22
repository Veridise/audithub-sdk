# ResourcePatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 

## Example

```python
from audithub_sdk.models.resource_patch import ResourcePatch

# TODO update the JSON string below
json = "{}"
# create an instance of ResourcePatch from a JSON string
resource_patch_instance = ResourcePatch.from_json(json)
# print the JSON string representation of the object
print(ResourcePatch.to_json())

# convert the object into a dict
resource_patch_dict = resource_patch_instance.to_dict()
# create an instance of ResourcePatch from a dict
resource_patch_from_dict = ResourcePatch.from_dict(resource_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


