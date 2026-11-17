# NewOrganizationExtra


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extra_option_id** | **int** |  | 
**start_date** | **datetime** | Purchase time and inclusive credit-period start in UTC. | 
**credits** | [**Credits1**](Credits1.md) |  | [optional] 
**purchase_price** | [**PurchasePrice**](PurchasePrice.md) |  | 

## Example

```python
from audithub_sdk.models.new_organization_extra import NewOrganizationExtra

# TODO update the JSON string below
json = "{}"
# create an instance of NewOrganizationExtra from a JSON string
new_organization_extra_instance = NewOrganizationExtra.from_json(json)
# print the JSON string representation of the object
print(NewOrganizationExtra.to_json())

# convert the object into a dict
new_organization_extra_dict = new_organization_extra_instance.to_dict()
# create an instance of NewOrganizationExtra from a dict
new_organization_extra_from_dict = NewOrganizationExtra.from_dict(new_organization_extra_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


