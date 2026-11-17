# ExtraCreditsConfigAdmin


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | 
**credits** | **str** |  | 
**expiry_timeframe** | **str** | Positive option expiry duration, defaulting to 365 days (one year). | [optional] [default to 'P1Y']
**price** | **str** |  | [optional] 
**stripe_price_id** | **str** |  | [optional] 
**id** | **int** |  | 

## Example

```python
from audithub_sdk.models.extra_credits_config_admin import ExtraCreditsConfigAdmin

# TODO update the JSON string below
json = "{}"
# create an instance of ExtraCreditsConfigAdmin from a JSON string
extra_credits_config_admin_instance = ExtraCreditsConfigAdmin.from_json(json)
# print the JSON string representation of the object
print(ExtraCreditsConfigAdmin.to_json())

# convert the object into a dict
extra_credits_config_admin_dict = extra_credits_config_admin_instance.to_dict()
# create an instance of ExtraCreditsConfigAdmin from a dict
extra_credits_config_admin_from_dict = ExtraCreditsConfigAdmin.from_dict(extra_credits_config_admin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


