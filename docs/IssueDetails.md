# IssueDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Clarifies the type of model returned in data. &#39;complete&#39; is the complete data model, while &#39;public&#39; is only its public part | 
**data** | [**Data**](Data.md) |  | 
**functions** | [**List[IssueStateTransitionFunction]**](IssueStateTransitionFunction.md) | A list of transition functions that are available based on the current status for the issue | [optional] 

## Example

```python
from audithub_sdk.models.issue_details import IssueDetails

# TODO update the JSON string below
json = "{}"
# create an instance of IssueDetails from a JSON string
issue_details_instance = IssueDetails.from_json(json)
# print the JSON string representation of the object
print(IssueDetails.to_json())

# convert the object into a dict
issue_details_dict = issue_details_instance.to_dict()
# create an instance of IssueDetails from a dict
issue_details_from_dict = IssueDetails.from_dict(issue_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


