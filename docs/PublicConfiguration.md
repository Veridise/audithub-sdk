# PublicConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fork_networks** | [**List[ForkNetworkPublic]**](ForkNetworkPublic.md) |  | 
**vanguard_solc_versions** | **List[str]** |  | 
**vanguard_defi_detectors** | [**List[VanguardDetector]**](VanguardDetector.md) |  | 
**vanguard_v2_defi_detectors** | [**List[VanguardDetector]**](VanguardDetector.md) |  | 
**vanguard_zk_detectors** | [**List[VanguardDetector]**](VanguardDetector.md) |  | 
**vanguard_v2_zk_detectors** | [**List[VanguardDetector]**](VanguardDetector.md) |  | 
**node_versions** | **List[str]** |  | 
**workflow_steps** | [**Dict[str, StepDefinition]**](StepDefinition.md) |  | 
**orca** | [**Dict[str, OrcaValue]**](OrcaValue.md) |  | 
**issue_configuration_options** | [**IssueConfigurationOptions**](IssueConfigurationOptions.md) |  | 
**available_tools** | [**List[SecurityTool]**](SecurityTool.md) |  | 
**application_functions** | [**List[ApplicationFunction]**](ApplicationFunction.md) |  | 
**version_archive_size_limit** | **int** | Max allowed size of version archive in bytes | [optional] [default to 200000000]
**onboarding_package** | **str** |  | 

## Example

```python
from audithub_sdk.models.public_configuration import PublicConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of PublicConfiguration from a JSON string
public_configuration_instance = PublicConfiguration.from_json(json)
# print the JSON string representation of the object
print(PublicConfiguration.to_json())

# convert the object into a dict
public_configuration_dict = public_configuration_instance.to_dict()
# create an instance of PublicConfiguration from a dict
public_configuration_from_dict = PublicConfiguration.from_dict(public_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


