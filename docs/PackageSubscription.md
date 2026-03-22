# PackageSubscription


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duration_months** | **int** |  | 
**monthly_cpu_minutes** | **int** |  | [optional] 
**storage_mb** | **int** |  | [optional] 
**enforce_monthly_resource_consumption** | **bool** | It indicates how to enforce quotas: a) when True, monthly quotas can only be consumed within the specific month, and b) when False, quota are freely consumed any time within the subscription time window | [optional] [default to False]

## Example

```python
from audithub_sdk.models.package_subscription import PackageSubscription

# TODO update the JSON string below
json = "{}"
# create an instance of PackageSubscription from a JSON string
package_subscription_instance = PackageSubscription.from_json(json)
# print the JSON string representation of the object
print(PackageSubscription.to_json())

# convert the object into a dict
package_subscription_dict = package_subscription_instance.to_dict()
# create an instance of PackageSubscription from a dict
package_subscription_from_dict = PackageSubscription.from_dict(package_subscription_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


