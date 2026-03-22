# AccountingData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**step_code** | **str** |  | [optional] 
**container_name** | **str** |  | [optional] 
**system** | **bool** |  | 
**created_at** | **datetime** |  | 
**entry_timestamp** | **datetime** |  | 
**entry_text** | **str** |  | 
**entry_type** | **str** |  | 
**entry_unit** | **str** |  | 
**entry_value** | **str** |  | 
**machine_info** | [**MachineInfo**](MachineInfo.md) |  | [optional] 

## Example

```python
from audithub_sdk.models.accounting_data import AccountingData

# TODO update the JSON string below
json = "{}"
# create an instance of AccountingData from a JSON string
accounting_data_instance = AccountingData.from_json(json)
# print the JSON string representation of the object
print(AccountingData.to_json())

# convert the object into a dict
accounting_data_dict = accounting_data_instance.to_dict()
# create an instance of AccountingData from a dict
accounting_data_from_dict = AccountingData.from_dict(accounting_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


