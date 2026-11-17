# SubscriptionDurationPatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**start_time** | **datetime** | New inclusive start in UTC. Task funding uses start_time &lt;&#x3D; task.started_at &lt; end_time. The entire subscription must have no task allocations; all periods are regenerated. | 
**end_time** | **datetime** |  | [optional] 

## Example

```python
from audithub_sdk.models.subscription_duration_patch import SubscriptionDurationPatch

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionDurationPatch from a JSON string
subscription_duration_patch_instance = SubscriptionDurationPatch.from_json(json)
# print the JSON string representation of the object
print(SubscriptionDurationPatch.to_json())

# convert the object into a dict
subscription_duration_patch_dict = subscription_duration_patch_instance.to_dict()
# create an instance of SubscriptionDurationPatch from a dict
subscription_duration_patch_from_dict = SubscriptionDurationPatch.from_dict(subscription_duration_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


