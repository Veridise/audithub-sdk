# SubscriptionCheckoutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan_id** | **int** |  | 

## Example

```python
from audithub_sdk.models.subscription_checkout_request import SubscriptionCheckoutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionCheckoutRequest from a JSON string
subscription_checkout_request_instance = SubscriptionCheckoutRequest.from_json(json)
# print the JSON string representation of the object
print(SubscriptionCheckoutRequest.to_json())

# convert the object into a dict
subscription_checkout_request_dict = subscription_checkout_request_instance.to_dict()
# create an instance of SubscriptionCheckoutRequest from a dict
subscription_checkout_request_from_dict = SubscriptionCheckoutRequest.from_dict(subscription_checkout_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


