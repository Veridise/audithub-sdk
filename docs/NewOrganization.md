# NewOrganization


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**support_channel** | **str** |  | [optional] 
**user_limit** | **int** |  | [optional] 

## Example

```python
from audithub_sdk.models.new_organization import NewOrganization

# TODO update the JSON string below
json = "{}"
# create an instance of NewOrganization from a JSON string
new_organization_instance = NewOrganization.from_json(json)
# print the JSON string representation of the object
print(NewOrganization.to_json())

# convert the object into a dict
new_organization_dict = new_organization_instance.to_dict()
# create an instance of NewOrganization from a dict
new_organization_from_dict = NewOrganization.from_dict(new_organization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


