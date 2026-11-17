# OrganizationExtras


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extra_credits** | [**List[OrganizationExtra]**](OrganizationExtra.md) |  | 

## Example

```python
from audithub_sdk.models.organization_extras import OrganizationExtras

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationExtras from a JSON string
organization_extras_instance = OrganizationExtras.from_json(json)
# print the JSON string representation of the object
print(OrganizationExtras.to_json())

# convert the object into a dict
organization_extras_dict = organization_extras_instance.to_dict()
# create an instance of OrganizationExtras from a dict
organization_extras_from_dict = OrganizationExtras.from_dict(organization_extras_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


