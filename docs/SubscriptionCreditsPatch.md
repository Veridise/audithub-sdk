# SubscriptionCreditsPatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**monthly_credits** | [**MonthlyCredits2**](MonthlyCredits2.md) |  | 

## Example

```python
from audithub_sdk.models.subscription_credits_patch import SubscriptionCreditsPatch

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionCreditsPatch from a JSON string
subscription_credits_patch_instance = SubscriptionCreditsPatch.from_json(json)
# print the JSON string representation of the object
print(SubscriptionCreditsPatch.to_json())

# convert the object into a dict
subscription_credits_patch_dict = subscription_credits_patch_instance.to_dict()
# create an instance of SubscriptionCreditsPatch from a dict
subscription_credits_patch_from_dict = SubscriptionCreditsPatch.from_dict(subscription_credits_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


