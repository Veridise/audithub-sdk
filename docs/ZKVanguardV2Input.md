# ZKVanguardV2Input


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | An optional name for this task. If not specified, the current time in UTC will be used. | [optional] 
**parameters** | [**ZKVanguardV2Parameters**](ZKVanguardV2Parameters.md) | The parameters to pass to ZK Vanguard v2 | 

## Example

```python
from audithub_sdk.models.zk_vanguard_v2_input import ZKVanguardV2Input

# TODO update the JSON string below
json = "{}"
# create an instance of ZKVanguardV2Input from a JSON string
zk_vanguard_v2_input_instance = ZKVanguardV2Input.from_json(json)
# print the JSON string representation of the object
print(ZKVanguardV2Input.to_json())

# convert the object into a dict
zk_vanguard_v2_input_dict = zk_vanguard_v2_input_instance.to_dict()
# create an instance of ZKVanguardV2Input from a dict
zk_vanguard_v2_input_from_dict = ZKVanguardV2Input.from_dict(zk_vanguard_v2_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


