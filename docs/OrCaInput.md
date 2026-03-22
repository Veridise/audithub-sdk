# OrCaInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**specs_override** | [**List[RootModelListUnionVSpecFromVersionVSpecFromStandardLibraryVSpecFromOrganizationLibraryVSpecAdHocInner]**](RootModelListUnionVSpecFromVersionVSpecFromStandardLibraryVSpecFromOrganizationLibraryVSpecAdHocInner.md) | This task will will run against these specs. | 
**hints_override** | [**List[RootModelListUnionHintFromVersionHintFromStandardLibraryHintFromOrganizationLibraryHintAdHocInner]**](RootModelListUnionHintFromVersionHintFromStandardLibraryHintFromOrganizationLibraryHintAdHocInner.md) |  | [optional] 
**deployment_script_path_override** | **str** |  | [optional] 
**on_chain** | **bool** | Specifies whether to enable on chain fuzzing | [optional] [default to False]
**deployment_info_file** | **str** |  | [optional] 
**name** | **str** | An optional name for this task. If not specified, the current time in UTC will be used. | [optional] 
**parameters** | [**OrCaParameters**](OrCaParameters.md) | The parameters to pass to OrCa | 

## Example

```python
from audithub_sdk.models.or_ca_input import OrCaInput

# TODO update the JSON string below
json = "{}"
# create an instance of OrCaInput from a JSON string
or_ca_input_instance = OrCaInput.from_json(json)
# print the JSON string representation of the object
print(OrCaInput.to_json())

# convert the object into a dict
or_ca_input_dict = or_ca_input_instance.to_dict()
# create an instance of OrCaInput from a dict
or_ca_input_from_dict = OrCaInput.from_dict(or_ca_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


