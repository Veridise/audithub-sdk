# NewExtraCreditsConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | 
**credits** | [**Credits**](Credits.md) |  | 
**expiry_timeframe** | **str** | Positive option expiry duration, defaulting to 365 days (one year). | [optional] [default to 'P1Y']
**price** | [**Price**](Price.md) |  | [optional] 
**stripe_price_id** | **str** |  | [optional] 

## Example

```python
from audithub_sdk.models.new_extra_credits_config import NewExtraCreditsConfig

# TODO update the JSON string below
json = "{}"
# create an instance of NewExtraCreditsConfig from a JSON string
new_extra_credits_config_instance = NewExtraCreditsConfig.from_json(json)
# print the JSON string representation of the object
print(NewExtraCreditsConfig.to_json())

# convert the object into a dict
new_extra_credits_config_dict = new_extra_credits_config_instance.to_dict()
# create an instance of NewExtraCreditsConfig from a dict
new_extra_credits_config_from_dict = NewExtraCreditsConfig.from_dict(new_extra_credits_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


