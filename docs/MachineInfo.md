# MachineInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**architecture** | **str** |  | 
**container_runtime_version** | **str** |  | 
**kernel_version** | **str** |  | 
**kubelet_version** | **str** |  | 
**os_image** | **str** |  | 
**capacity_cpu** | **int** |  | 
**capacity_memory** | **str** |  | 
**instance_type** | **str** |  | 
**zone** | **str** |  | 
**region** | **str** |  | [optional] [default to '-']
**cpu_model_name** | **str** |  | 
**cpu_bogomips** | **float** |  | 

## Example

```python
from audithub_sdk.models.machine_info import MachineInfo

# TODO update the JSON string below
json = "{}"
# create an instance of MachineInfo from a JSON string
machine_info_instance = MachineInfo.from_json(json)
# print the JSON string representation of the object
print(MachineInfo.to_json())

# convert the object into a dict
machine_info_dict = machine_info_instance.to_dict()
# create an instance of MachineInfo from a dict
machine_info_from_dict = MachineInfo.from_dict(machine_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


