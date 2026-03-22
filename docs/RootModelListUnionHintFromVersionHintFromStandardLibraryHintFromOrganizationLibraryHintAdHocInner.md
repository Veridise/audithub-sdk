# RootModelListUnionHintFromVersionHintFromStandardLibraryHintFromOrganizationLibraryHintAdHocInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'version']
**relative_path** | **str** | Relative path from the version archive&#39;s root | 
**library_version** | **str** |  | [optional] 
**category** | **str** |  | 
**name** | **str** |  | 
**id** | **int** | The id of the Hint from the organization&#39;s library. | 
**filename** | **str** | The filename for this Hint. | 
**contents** | **str** | The contents of this file | 
**encoding** | **str** | The encoding of the contents. Currently, only &#39;plain&#39; is supported, which simply places the value of the contents JSON key to the file | [optional] [default to 'plain']

## Example

```python
from audithub_sdk.models.root_model_list_union_hint_from_version_hint_from_standard_library_hint_from_organization_library_hint_ad_hoc_inner import RootModelListUnionHintFromVersionHintFromStandardLibraryHintFromOrganizationLibraryHintAdHocInner

# TODO update the JSON string below
json = "{}"
# create an instance of RootModelListUnionHintFromVersionHintFromStandardLibraryHintFromOrganizationLibraryHintAdHocInner from a JSON string
root_model_list_union_hint_from_version_hint_from_standard_library_hint_from_organization_library_hint_ad_hoc_inner_instance = RootModelListUnionHintFromVersionHintFromStandardLibraryHintFromOrganizationLibraryHintAdHocInner.from_json(json)
# print the JSON string representation of the object
print(RootModelListUnionHintFromVersionHintFromStandardLibraryHintFromOrganizationLibraryHintAdHocInner.to_json())

# convert the object into a dict
root_model_list_union_hint_from_version_hint_from_standard_library_hint_from_organization_library_hint_ad_hoc_inner_dict = root_model_list_union_hint_from_version_hint_from_standard_library_hint_from_organization_library_hint_ad_hoc_inner_instance.to_dict()
# create an instance of RootModelListUnionHintFromVersionHintFromStandardLibraryHintFromOrganizationLibraryHintAdHocInner from a dict
root_model_list_union_hint_from_version_hint_from_standard_library_hint_from_organization_library_hint_ad_hoc_inner_from_dict = RootModelListUnionHintFromVersionHintFromStandardLibraryHintFromOrganizationLibraryHintAdHocInner.from_dict(root_model_list_union_hint_from_version_hint_from_standard_library_hint_from_organization_library_hint_ad_hoc_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


