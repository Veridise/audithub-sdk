# ProjectDependency


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**npm** | [**NPMProjectDependency**](NPMProjectDependency.md) |  | [optional] 
**foundry** | **bool** |  | [optional] 

## Example

```python
from audithub_sdk.models.project_dependency import ProjectDependency

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectDependency from a JSON string
project_dependency_instance = ProjectDependency.from_json(json)
# print the JSON string representation of the object
print(ProjectDependency.to_json())

# convert the object into a dict
project_dependency_dict = project_dependency_instance.to_dict()
# create an instance of ProjectDependency from a dict
project_dependency_from_dict = ProjectDependency.from_dict(project_dependency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


