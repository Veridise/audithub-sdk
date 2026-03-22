# EffectiveUserAccessRestriction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**function** | **str** |  | 
**value** | **int** |  | [optional] 

## Example

```python
from audithub_sdk.models.effective_user_access_restriction import EffectiveUserAccessRestriction

# TODO update the JSON string below
json = "{}"
# create an instance of EffectiveUserAccessRestriction from a JSON string
effective_user_access_restriction_instance = EffectiveUserAccessRestriction.from_json(json)
# print the JSON string representation of the object
print(EffectiveUserAccessRestriction.to_json())

# convert the object into a dict
effective_user_access_restriction_dict = effective_user_access_restriction_instance.to_dict()
# create an instance of EffectiveUserAccessRestriction from a dict
effective_user_access_restriction_from_dict = EffectiveUserAccessRestriction.from_dict(effective_user_access_restriction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


