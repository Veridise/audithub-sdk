# PackageExtraCredits


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extra_option_id** | **int** |  | [optional] 
**extra_option_name** | **str** |  | [optional] 

## Example

```python
from audithub_sdk.models.package_extra_credits import PackageExtraCredits

# TODO update the JSON string below
json = "{}"
# create an instance of PackageExtraCredits from a JSON string
package_extra_credits_instance = PackageExtraCredits.from_json(json)
# print the JSON string representation of the object
print(PackageExtraCredits.to_json())

# convert the object into a dict
package_extra_credits_dict = package_extra_credits_instance.to_dict()
# create an instance of PackageExtraCredits from a dict
package_extra_credits_from_dict = PackageExtraCredits.from_dict(package_extra_credits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


