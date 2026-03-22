# ApiKeyWithSecret


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**client_id** | **str** |  | 
**client_secret** | **str** |  | 

## Example

```python
from audithub_sdk.models.api_key_with_secret import ApiKeyWithSecret

# TODO update the JSON string below
json = "{}"
# create an instance of ApiKeyWithSecret from a JSON string
api_key_with_secret_instance = ApiKeyWithSecret.from_json(json)
# print the JSON string representation of the object
print(ApiKeyWithSecret.to_json())

# convert the object into a dict
api_key_with_secret_dict = api_key_with_secret_instance.to_dict()
# create an instance of ApiKeyWithSecret from a dict
api_key_with_secret_from_dict = ApiKeyWithSecret.from_dict(api_key_with_secret_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


