# HintFromVersion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'version']
**relative_path** | **str** | Relative path from the version archive&#39;s root | 

## Example

```python
from audithub_sdk.models.hint_from_version import HintFromVersion

# TODO update the JSON string below
json = "{}"
# create an instance of HintFromVersion from a JSON string
hint_from_version_instance = HintFromVersion.from_json(json)
# print the JSON string representation of the object
print(HintFromVersion.to_json())

# convert the object into a dict
hint_from_version_dict = hint_from_version_instance.to_dict()
# create an instance of HintFromVersion from a dict
hint_from_version_from_dict = HintFromVersion.from_dict(hint_from_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


