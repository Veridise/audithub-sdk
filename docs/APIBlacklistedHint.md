# APIBlacklistedHint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** |  | 
**reference** | **str** |  | 

## Example

```python
from audithub_sdk.models.api_blacklisted_hint import APIBlacklistedHint

# TODO update the JSON string below
json = "{}"
# create an instance of APIBlacklistedHint from a JSON string
api_blacklisted_hint_instance = APIBlacklistedHint.from_json(json)
# print the JSON string representation of the object
print(APIBlacklistedHint.to_json())

# convert the object into a dict
api_blacklisted_hint_dict = api_blacklisted_hint_instance.to_dict()
# create an instance of APIBlacklistedHint from a dict
api_blacklisted_hint_from_dict = APIBlacklistedHint.from_dict(api_blacklisted_hint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


