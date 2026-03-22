# UserOrganizationSetting


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disable_online_notifications** | **bool** |  | 
**disable_digest_notifications** | **bool** |  | 

## Example

```python
from audithub_sdk.models.user_organization_setting import UserOrganizationSetting

# TODO update the JSON string below
json = "{}"
# create an instance of UserOrganizationSetting from a JSON string
user_organization_setting_instance = UserOrganizationSetting.from_json(json)
# print the JSON string representation of the object
print(UserOrganizationSetting.to_json())

# convert the object into a dict
user_organization_setting_dict = user_organization_setting_instance.to_dict()
# create an instance of UserOrganizationSetting from a dict
user_organization_setting_from_dict = UserOrganizationSetting.from_dict(user_organization_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


