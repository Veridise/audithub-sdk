# User


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

## Example

```python
from audithub_sdk.models.user import User

# TODO update the JSON string below
json = "{}"
# create an instance of User from a JSON string
user_instance = User.from_json(json)
# print the JSON string representation of the object
print(User.to_json())

# convert the object into a dict
user_dict = user_instance.to_dict()
# create an instance of User from a dict
user_from_dict = User.from_dict(user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


