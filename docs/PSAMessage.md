# PSAMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**msg** | **str** |  | 
**id** | **str** |  | [optional] 

## Example

```python
from audithub_sdk.models.psa_message import PSAMessage

# TODO update the JSON string below
json = "{}"
# create an instance of PSAMessage from a JSON string
psa_message_instance = PSAMessage.from_json(json)
# print the JSON string representation of the object
print(PSAMessage.to_json())

# convert the object into a dict
psa_message_dict = psa_message_instance.to_dict()
# create an instance of PSAMessage from a dict
psa_message_from_dict = PSAMessage.from_dict(psa_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


