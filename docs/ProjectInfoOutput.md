# ProjectInfoOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**project_root** | **str** | Relative path inside archive, for current directory to use when starting external commands, such as npm | [optional] [default to '.']
**env_vars** | [**List[EnvVar]**](EnvVar.md) |  | [optional] 
**dependencies** | [**ProjectDependency**](ProjectDependency.md) |  | [optional] 
**build_system** | **str** |  | [optional] 
**contents** | **List[str]** |  | [optional] 
**src_path** | **str** | The path where we can find the sources to process.         This is relative path inside archive, and it must be bellow project_root. | 
**include_path** | **str** |  | [optional] 
**specs_path** | **str** |  | [optional] 
**hints_path** | **str** |  | [optional] 
**deployment_script_path** | **str** |  | [optional] 
**input_info** | [**InputInfo**](InputInfo.md) |  | 

## Example

```python
from audithub_sdk.models.project_info_output import ProjectInfoOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectInfoOutput from a JSON string
project_info_output_instance = ProjectInfoOutput.from_json(json)
# print the JSON string representation of the object
print(ProjectInfoOutput.to_json())

# convert the object into a dict
project_info_output_dict = project_info_output_instance.to_dict()
# create an instance of ProjectInfoOutput from a dict
project_info_output_from_dict = ProjectInfoOutput.from_dict(project_info_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


