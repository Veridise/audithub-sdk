# DefiVanguardV2Input


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | An optional name for this task. If not specified, the current time in UTC will be used. | [optional] 
**parameters** | [**DefiVanguardV2Parameters**](DefiVanguardV2Parameters.md) | The parameters to pass to DeFi Vanguard v2 | 

## Example

```python
from audithub_sdk.models.defi_vanguard_v2_input import DefiVanguardV2Input

# TODO update the JSON string below
json = "{}"
# create an instance of DefiVanguardV2Input from a JSON string
defi_vanguard_v2_input_instance = DefiVanguardV2Input.from_json(json)
# print the JSON string representation of the object
print(DefiVanguardV2Input.to_json())

# convert the object into a dict
defi_vanguard_v2_input_dict = defi_vanguard_v2_input_instance.to_dict()
# create an instance of DefiVanguardV2Input from a dict
defi_vanguard_v2_input_from_dict = DefiVanguardV2Input.from_dict(defi_vanguard_v2_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


