# PutUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disable_online_notifications** | **bool** |  | 
**disable_digest_notifications** | **bool** |  | 
**tour_done** | **List[str]** |  | 

## Example

```python
from audithub_sdk.models.put_user import PutUser

# TODO update the JSON string below
json = "{}"
# create an instance of PutUser from a JSON string
put_user_instance = PutUser.from_json(json)
# print the JSON string representation of the object
print(PutUser.to_json())

# convert the object into a dict
put_user_dict = put_user_instance.to_dict()
# create an instance of PutUser from a dict
put_user_from_dict = PutUser.from_dict(put_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


