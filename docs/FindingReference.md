# FindingReference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_id** | **int** | The task that produced the finding. | 
**analysis_result_id** | **int** | The id of the analysis result that contains this finding. | 
**finding_id** | **str** | The reference to the finding. | 

## Example

```python
from audithub_sdk.models.finding_reference import FindingReference

# TODO update the JSON string below
json = "{}"
# create an instance of FindingReference from a JSON string
finding_reference_instance = FindingReference.from_json(json)
# print the JSON string representation of the object
print(FindingReference.to_json())

# convert the object into a dict
finding_reference_dict = finding_reference_instance.to_dict()
# create an instance of FindingReference from a dict
finding_reference_from_dict = FindingReference.from_dict(finding_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


