# ProjectInfoInput


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
from audithub_sdk.models.project_info_input import ProjectInfoInput

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectInfoInput from a JSON string
project_info_input_instance = ProjectInfoInput.from_json(json)
# print the JSON string representation of the object
print(ProjectInfoInput.to_json())

# convert the object into a dict
project_info_input_dict = project_info_input_instance.to_dict()
# create an instance of ProjectInfoInput from a dict
project_info_input_from_dict = ProjectInfoInput.from_dict(project_info_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


