# ModelToolPhaseParameters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input_files** | **List[str]** |  | [optional] 
**exit_code** | **int** |  | [optional] 
**sleep** | **int** |  | [optional] 
**generate_findings** | **bool** |  | [optional] 
**generate_accounting** | **bool** |  | [optional] 
**findings_completed** | **bool** |  | [optional] 
**findings_error_message** | **str** |  | [optional] 
**findings_warning** | **int** |  | [optional] 
**findings_low** | **int** |  | [optional] 
**findings_medium** | **int** |  | [optional] 
**findings_high** | **int** |  | [optional] 
**findings_critical** | **int** |  | [optional] 

## Example

```python
from audithub_sdk.models.model_tool_phase_parameters import ModelToolPhaseParameters

# TODO update the JSON string below
json = "{}"
# create an instance of ModelToolPhaseParameters from a JSON string
model_tool_phase_parameters_instance = ModelToolPhaseParameters.from_json(json)
# print the JSON string representation of the object
print(ModelToolPhaseParameters.to_json())

# convert the object into a dict
model_tool_phase_parameters_dict = model_tool_phase_parameters_instance.to_dict()
# create an instance of ModelToolPhaseParameters from a dict
model_tool_phase_parameters_from_dict = ModelToolPhaseParameters.from_dict(model_tool_phase_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


