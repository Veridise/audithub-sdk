# PSA


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**psa** | [**PSAMessage**](PSAMessage.md) |  | 

## Example

```python
from audithub_sdk.models.psa import PSA

# TODO update the JSON string below
json = "{}"
# create an instance of PSA from a JSON string
psa_instance = PSA.from_json(json)
# print the JSON string representation of the object
print(PSA.to_json())

# convert the object into a dict
psa_dict = psa_instance.to_dict()
# create an instance of PSA from a dict
psa_from_dict = PSA.from_dict(psa_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


