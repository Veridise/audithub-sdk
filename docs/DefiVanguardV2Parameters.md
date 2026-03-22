# DefiVanguardV2Parameters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detector** | **List[str]** |  | [optional] 
**input_limit** | **List[str]** |  | [optional] 
**cross_version_triage** | **bool** | When this is True, findings previously discovered for this project will be suppressed. | [optional] [default to False]
**lang** | **str** |  | [optional] [default to 'solidity']
**solc** | **str** |  | [optional] 
**ignore_build_system** | **bool** | When this is True, do not use build system for project compilation. | [optional] [default to False]
**custom_detectors** | [**List[RootModelListUnionCustomDetectorFromVersionCustomDetectorFromStandardLibraryCustomDetectorFromOrganizationLibraryInner]**](RootModelListUnionCustomDetectorFromVersionCustomDetectorFromStandardLibraryCustomDetectorFromOrganizationLibraryInner.md) |  | [optional] 

## Example

```python
from audithub_sdk.models.defi_vanguard_v2_parameters import DefiVanguardV2Parameters

# TODO update the JSON string below
json = "{}"
# create an instance of DefiVanguardV2Parameters from a JSON string
defi_vanguard_v2_parameters_instance = DefiVanguardV2Parameters.from_json(json)
# print the JSON string representation of the object
print(DefiVanguardV2Parameters.to_json())

# convert the object into a dict
defi_vanguard_v2_parameters_dict = defi_vanguard_v2_parameters_instance.to_dict()
# create an instance of DefiVanguardV2Parameters from a dict
defi_vanguard_v2_parameters_from_dict = DefiVanguardV2Parameters.from_dict(defi_vanguard_v2_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


