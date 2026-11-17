# ExtraCreditsConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | 
**credits** | **str** |  | 
**expiry_timeframe** | **str** | Positive option expiry duration, defaulting to 365 days (one year). | [optional] [default to 'P1Y']
**price** | **str** |  | [optional] 
**id** | **int** |  | 

## Example

```python
from audithub_sdk.models.extra_credits_config import ExtraCreditsConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ExtraCreditsConfig from a JSON string
extra_credits_config_instance = ExtraCreditsConfig.from_json(json)
# print the JSON string representation of the object
print(ExtraCreditsConfig.to_json())

# convert the object into a dict
extra_credits_config_dict = extra_credits_config_instance.to_dict()
# create an instance of ExtraCreditsConfig from a dict
extra_credits_config_from_dict = ExtraCreditsConfig.from_dict(extra_credits_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


