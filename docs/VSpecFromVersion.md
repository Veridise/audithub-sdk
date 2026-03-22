# VSpecFromVersion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'version']
**relative_path** | **str** | Relative path from the version archive&#39;s root | 

## Example

```python
from audithub_sdk.models.v_spec_from_version import VSpecFromVersion

# TODO update the JSON string below
json = "{}"
# create an instance of VSpecFromVersion from a JSON string
v_spec_from_version_instance = VSpecFromVersion.from_json(json)
# print the JSON string representation of the object
print(VSpecFromVersion.to_json())

# convert the object into a dict
v_spec_from_version_dict = v_spec_from_version_instance.to_dict()
# create an instance of VSpecFromVersion from a dict
v_spec_from_version_from_dict = VSpecFromVersion.from_dict(v_spec_from_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


