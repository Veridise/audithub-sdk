# OrganizationConsumption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu_minutes** | **int** |  | 
**storage_mb** | **int** |  | 
**from_date** | **datetime** |  | [optional] 
**to_date** | **datetime** |  | [optional] 

## Example

```python
from audithub_sdk.models.organization_consumption import OrganizationConsumption

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationConsumption from a JSON string
organization_consumption_instance = OrganizationConsumption.from_json(json)
# print the JSON string representation of the object
print(OrganizationConsumption.to_json())

# convert the object into a dict
organization_consumption_dict = organization_consumption_instance.to_dict()
# create an instance of OrganizationConsumption from a dict
organization_consumption_from_dict = OrganizationConsumption.from_dict(organization_consumption_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


