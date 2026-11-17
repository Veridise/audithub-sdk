# ProjectDocumentData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Display name of document | 
**data** | **str** |  | 

## Example

```python
from audithub_sdk.models.project_document_data import ProjectDocumentData

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectDocumentData from a JSON string
project_document_data_instance = ProjectDocumentData.from_json(json)
# print the JSON string representation of the object
print(ProjectDocumentData.to_json())

# convert the object into a dict
project_document_data_dict = project_document_data_instance.to_dict()
# create an instance of ProjectDocumentData from a dict
project_document_data_from_dict = ProjectDocumentData.from_dict(project_document_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


