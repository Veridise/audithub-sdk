# audithub_sdk.UiApi

All URIs are relative to *https://audithub.dev.veridise.tools/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_organization_projects_ui_organizations_organization_id_projects_get**](UiApi.md#get_organization_projects_ui_organizations_organization_id_projects_get) | **GET** /ui/organizations/{organization_id}/projects | Get Organization Projects
[**post_my_organization_ui_my_organizations_post**](UiApi.md#post_my_organization_ui_my_organizations_post) | **POST** /ui/my-organizations | Post My Organization


# **get_organization_projects_ui_organizations_organization_id_projects_get**
> List[ProjectForUI] get_organization_projects_ui_organizations_organization_id_projects_get(organization_id)

Get Organization Projects

Returns all projects of an organization, including latest version id.

### Example


```python
import audithub_sdk
from audithub_sdk.models.project_for_ui import ProjectForUI
from audithub_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://audithub.dev.veridise.tools/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = audithub_sdk.Configuration(
    host = "https://audithub.dev.veridise.tools/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
async with audithub_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = audithub_sdk.UiApi(api_client)
    organization_id = 56 # int | 

    try:
        # Get Organization Projects
        api_response = await api_instance.get_organization_projects_ui_organizations_organization_id_projects_get(organization_id)
        print("The response of UiApi->get_organization_projects_ui_organizations_organization_id_projects_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UiApi->get_organization_projects_ui_organizations_organization_id_projects_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 

### Return type

[**List[ProjectForUI]**](ProjectForUI.md)

### Authorization

[OpenIdConnect](../README.md#OpenIdConnect)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_my_organization_ui_my_organizations_post**
> IdAndMessageResponse post_my_organization_ui_my_organizations_post(new_organization)

Post My Organization

Post Organization and assign the user as an organization user

### Example


```python
import audithub_sdk
from audithub_sdk.models.id_and_message_response import IdAndMessageResponse
from audithub_sdk.models.new_organization import NewOrganization
from audithub_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://audithub.dev.veridise.tools/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = audithub_sdk.Configuration(
    host = "https://audithub.dev.veridise.tools/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
async with audithub_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = audithub_sdk.UiApi(api_client)
    new_organization = audithub_sdk.NewOrganization() # NewOrganization | 

    try:
        # Post My Organization
        api_response = await api_instance.post_my_organization_ui_my_organizations_post(new_organization)
        print("The response of UiApi->post_my_organization_ui_my_organizations_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UiApi->post_my_organization_ui_my_organizations_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_organization** | [**NewOrganization**](NewOrganization.md)|  | 

### Return type

[**IdAndMessageResponse**](IdAndMessageResponse.md)

### Authorization

[OpenIdConnect](../README.md#OpenIdConnect)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

