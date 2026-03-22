# UserForAdmin


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**email** | **str** |  | 
**rights** | **List[str]** |  | 
**disable_online_notifications** | **bool** |  | 
**disable_digest_notifications** | **bool** |  | 
**onboarded_via** | **str** |  | [optional] 
**tour_done** | **List[str]** |  | 
**captcha** | **bool** |  | 

## Example

```python
from audithub_sdk.models.user_for_admin import UserForAdmin

# TODO update the JSON string below
json = "{}"
# create an instance of UserForAdmin from a JSON string
user_for_admin_instance = UserForAdmin.from_json(json)
# print the JSON string representation of the object
print(UserForAdmin.to_json())

# convert the object into a dict
user_for_admin_dict = user_for_admin_instance.to_dict()
# create an instance of UserForAdmin from a dict
user_for_admin_from_dict = UserForAdmin.from_dict(user_for_admin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


