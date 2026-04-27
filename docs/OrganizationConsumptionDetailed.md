# OrganizationConsumptionDetailed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_date** | **datetime** |  | [optional] 
**to_date** | **datetime** |  | [optional] 
**versions** | [**List[VersionResources]**](VersionResources.md) |  | 

## Example

```python
from audithub_sdk.models.organization_consumption_detailed import OrganizationConsumptionDetailed

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationConsumptionDetailed from a JSON string
organization_consumption_detailed_instance = OrganizationConsumptionDetailed.from_json(json)
# print the JSON string representation of the object
print(OrganizationConsumptionDetailed.to_json())

# convert the object into a dict
organization_consumption_detailed_dict = organization_consumption_detailed_instance.to_dict()
# create an instance of OrganizationConsumptionDetailed from a dict
organization_consumption_detailed_from_dict = OrganizationConsumptionDetailed.from_dict(organization_consumption_detailed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


