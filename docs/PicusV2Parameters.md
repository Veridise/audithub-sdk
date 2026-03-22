# PicusV2Parameters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** |  | 
**solver** | **str** |  | [optional] 
**smt_file** | **str** |  | [optional] 
**no_solver** | **bool** |  | [optional] 
**no_optimization** | **bool** |  | [optional] 
**no_range_analysis** | **bool** |  | [optional] 
**no_linear** | **bool** |  | [optional] 
**no_table** | **bool** |  | [optional] 
**no_basis** | **bool** |  | [optional] 
**no_poly** | **bool** |  | [optional] 
**solver_timeout** | **int** |  | [optional] 
**time_limit** | **int** |  | [optional] 
**assume_deterministic** | **List[str]** |  | [optional] 
**enable_debug** | **bool** |  | [optional] 
**apply_rewrites** | **bool** |  | [optional] 

## Example

```python
from audithub_sdk.models.picus_v2_parameters import PicusV2Parameters

# TODO update the JSON string below
json = "{}"
# create an instance of PicusV2Parameters from a JSON string
picus_v2_parameters_instance = PicusV2Parameters.from_json(json)
# print the JSON string representation of the object
print(PicusV2Parameters.to_json())

# convert the object into a dict
picus_v2_parameters_dict = picus_v2_parameters_instance.to_dict()
# create an instance of PicusV2Parameters from a dict
picus_v2_parameters_from_dict = PicusV2Parameters.from_dict(picus_v2_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


