# ZKVanguardInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | An optional name for this task. If not specified, the current time in UTC will be used. | [optional] 
**parameters** | [**ZKVanguardParameters**](ZKVanguardParameters.md) | The parameters to pass to ZK Vanguard | 

## Example

```python
from audithub_sdk.models.zk_vanguard_input import ZKVanguardInput

# TODO update the JSON string below
json = "{}"
# create an instance of ZKVanguardInput from a JSON string
zk_vanguard_input_instance = ZKVanguardInput.from_json(json)
# print the JSON string representation of the object
print(ZKVanguardInput.to_json())

# convert the object into a dict
zk_vanguard_input_dict = zk_vanguard_input_instance.to_dict()
# create an instance of ZKVanguardInput from a dict
zk_vanguard_input_from_dict = ZKVanguardInput.from_dict(zk_vanguard_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


