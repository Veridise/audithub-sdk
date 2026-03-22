# ZKVanguardV2Parameters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detector** | **List[str]** |  | [optional] 
**input_limit** | **List[str]** |  | [optional] 
**cross_version_triage** | **bool** | When this is True, findings previously discovered for this project will be suppressed. | [optional] [default to False]
**lang** | **str** |  | [optional] [default to 'llzk']

## Example

```python
from audithub_sdk.models.zk_vanguard_v2_parameters import ZKVanguardV2Parameters

# TODO update the JSON string below
json = "{}"
# create an instance of ZKVanguardV2Parameters from a JSON string
zk_vanguard_v2_parameters_instance = ZKVanguardV2Parameters.from_json(json)
# print the JSON string representation of the object
print(ZKVanguardV2Parameters.to_json())

# convert the object into a dict
zk_vanguard_v2_parameters_dict = zk_vanguard_v2_parameters_instance.to_dict()
# create an instance of ZKVanguardV2Parameters from a dict
zk_vanguard_v2_parameters_from_dict = ZKVanguardV2Parameters.from_dict(zk_vanguard_v2_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


