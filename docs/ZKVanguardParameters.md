# ZKVanguardParameters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detector** | **List[str]** |  | [optional] 
**input_limit** | **List[str]** |  | [optional] 
**cross_version_triage** | **bool** | When this is True, findings previously discovered for this project will be suppressed. | [optional] [default to False]
**lang** | **str** |  | [optional] [default to 'circom']

## Example

```python
from audithub_sdk.models.zk_vanguard_parameters import ZKVanguardParameters

# TODO update the JSON string below
json = "{}"
# create an instance of ZKVanguardParameters from a JSON string
zk_vanguard_parameters_instance = ZKVanguardParameters.from_json(json)
# print the JSON string representation of the object
print(ZKVanguardParameters.to_json())

# convert the object into a dict
zk_vanguard_parameters_dict = zk_vanguard_parameters_instance.to_dict()
# create an instance of ZKVanguardParameters from a dict
zk_vanguard_parameters_from_dict = ZKVanguardParameters.from_dict(zk_vanguard_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


