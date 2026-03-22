# UserProjectSetting


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disable_online_notifications** | **bool** |  | 
**disable_digest_notifications** | **bool** |  | 

## Example

```python
from audithub_sdk.models.user_project_setting import UserProjectSetting

# TODO update the JSON string below
json = "{}"
# create an instance of UserProjectSetting from a JSON string
user_project_setting_instance = UserProjectSetting.from_json(json)
# print the JSON string representation of the object
print(UserProjectSetting.to_json())

# convert the object into a dict
user_project_setting_dict = user_project_setting_instance.to_dict()
# create an instance of UserProjectSetting from a dict
user_project_setting_from_dict = UserProjectSetting.from_dict(user_project_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


