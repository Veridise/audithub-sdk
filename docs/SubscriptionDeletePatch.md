# SubscriptionDeletePatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 

## Example

```python
from audithub_sdk.models.subscription_delete_patch import SubscriptionDeletePatch

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionDeletePatch from a JSON string
subscription_delete_patch_instance = SubscriptionDeletePatch.from_json(json)
# print the JSON string representation of the object
print(SubscriptionDeletePatch.to_json())

# convert the object into a dict
subscription_delete_patch_dict = subscription_delete_patch_instance.to_dict()
# create an instance of SubscriptionDeletePatch from a dict
subscription_delete_patch_from_dict = SubscriptionDeletePatch.from_dict(subscription_delete_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


