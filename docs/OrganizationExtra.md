# OrganizationExtra


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**extra_credit_option_id** | **int** |  | 
**purchase_time** | **datetime** |  | 
**expiry_time** | **datetime** |  | 
**credits** | **str** |  | 

## Example

```python
from audithub_sdk.models.organization_extra import OrganizationExtra

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationExtra from a JSON string
organization_extra_instance = OrganizationExtra.from_json(json)
# print the JSON string representation of the object
print(OrganizationExtra.to_json())

# convert the object into a dict
organization_extra_dict = organization_extra_instance.to_dict()
# create an instance of OrganizationExtra from a dict
organization_extra_from_dict = OrganizationExtra.from_dict(organization_extra_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


