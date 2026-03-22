# PicusParameters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** | A path to a Circom file or R1CS file. | 
**solver** | **str** | The solver to use. | [optional] [default to 'cvc5']
**timeout** | **int** | Number of seconds to spend for each query. | [optional] [default to 5]
**opt_level** | **int** |  | [optional] 
**strong** | **bool** | Check that all signals are properly constrained | [optional] [default to False]

## Example

```python
from audithub_sdk.models.picus_parameters import PicusParameters

# TODO update the JSON string below
json = "{}"
# create an instance of PicusParameters from a JSON string
picus_parameters_instance = PicusParameters.from_json(json)
# print the JSON string representation of the object
print(PicusParameters.to_json())

# convert the object into a dict
picus_parameters_dict = picus_parameters_instance.to_dict()
# create an instance of PicusParameters from a dict
picus_parameters_from_dict = PicusParameters.from_dict(picus_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


