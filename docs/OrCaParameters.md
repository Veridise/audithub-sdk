# OrCaParameters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disable_user_proxies** | **bool** |  | [optional] 
**fuzz_pure** | **bool** |  | [optional] 
**fuzz_targets** | **List[str]** |  | [optional] 
**fuzzing_blacklist** | [**List[FuzzingBlacklistEntry]**](FuzzingBlacklistEntry.md) |  | [optional] 
**language** | **str** | The language the source files are written in. | [optional] [default to 'solidity']
**timeout** | **int** | How long to fuzz ( in seconds) . | [optional] [default to 600]
**fork_network** | **str** |  | [optional] 
**fork_block_number** | **int** |  | [optional] 

## Example

```python
from audithub_sdk.models.or_ca_parameters import OrCaParameters

# TODO update the JSON string below
json = "{}"
# create an instance of OrCaParameters from a JSON string
or_ca_parameters_instance = OrCaParameters.from_json(json)
# print the JSON string representation of the object
print(OrCaParameters.to_json())

# convert the object into a dict
or_ca_parameters_dict = or_ca_parameters_instance.to_dict()
# create an instance of OrCaParameters from a dict
or_ca_parameters_from_dict = OrCaParameters.from_dict(or_ca_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


