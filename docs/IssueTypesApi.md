# audithub_sdk.IssueTypesApi

All URIs are relative to *https://audithub.dev.veridise.tools/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_issue_type_organizations_organization_id_issue_types_type_id_delete**](IssueTypesApi.md#delete_issue_type_organizations_organization_id_issue_types_type_id_delete) | **DELETE** /organizations/{organization_id}/issue_types/{type_id} | Delete Issue Type
[**get_issue_type_organizations_organization_id_issue_types_type_id_get**](IssueTypesApi.md#get_issue_type_organizations_organization_id_issue_types_type_id_get) | **GET** /organizations/{organization_id}/issue_types/{type_id} | Get Issue Type
[**get_organization_issue_types_organizations_organization_id_issue_types_get**](IssueTypesApi.md#get_organization_issue_types_organizations_organization_id_issue_types_get) | **GET** /organizations/{organization_id}/issue_types | Get Organization Issue Types
[**post_issue_type_organizations_organization_id_issue_types_post**](IssueTypesApi.md#post_issue_type_organizations_organization_id_issue_types_post) | **POST** /organizations/{organization_id}/issue_types | Post Issue Type
[**put_issue_type_organizations_organization_id_issue_types_type_id_put**](IssueTypesApi.md#put_issue_type_organizations_organization_id_issue_types_type_id_put) | **PUT** /organizations/{organization_id}/issue_types/{type_id} | Put Issue Type


# **delete_issue_type_organizations_organization_id_issue_types_type_id_delete**
> SuccessAndMessageResponse delete_issue_type_organizations_organization_id_issue_types_type_id_delete(organization_id, type_id)

Delete Issue Type

Delete an issue type by id

### Example


```python
import audithub_sdk
from audithub_sdk.models.success_and_message_response import SuccessAndMessageResponse
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
    api_instance = audithub_sdk.IssueTypesApi(api_client)
    organization_id = 56 # int | 
    type_id = 56 # int | 

    try:
        # Delete Issue Type
        api_response = await api_instance.delete_issue_type_organizations_organization_id_issue_types_type_id_delete(organization_id, type_id)
        print("The response of IssueTypesApi->delete_issue_type_organizations_organization_id_issue_types_type_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IssueTypesApi->delete_issue_type_organizations_organization_id_issue_types_type_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **type_id** | **int**|  | 

### Return type

[**SuccessAndMessageResponse**](SuccessAndMessageResponse.md)

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

# **get_issue_type_organizations_organization_id_issue_types_type_id_get**
> IssueType get_issue_type_organizations_organization_id_issue_types_type_id_get(organization_id, type_id)

Get Issue Type

Get an issue type by id

### Example


```python
import audithub_sdk
from audithub_sdk.models.issue_type import IssueType
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
    api_instance = audithub_sdk.IssueTypesApi(api_client)
    organization_id = 56 # int | 
    type_id = 56 # int | 

    try:
        # Get Issue Type
        api_response = await api_instance.get_issue_type_organizations_organization_id_issue_types_type_id_get(organization_id, type_id)
        print("The response of IssueTypesApi->get_issue_type_organizations_organization_id_issue_types_type_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IssueTypesApi->get_issue_type_organizations_organization_id_issue_types_type_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **type_id** | **int**|  | 

### Return type

[**IssueType**](IssueType.md)

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

# **get_organization_issue_types_organizations_organization_id_issue_types_get**
> List[IssueType] get_organization_issue_types_organizations_organization_id_issue_types_get(organization_id)

Get Organization Issue Types

Get the available issue types for an organization.

### Example


```python
import audithub_sdk
from audithub_sdk.models.issue_type import IssueType
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
    api_instance = audithub_sdk.IssueTypesApi(api_client)
    organization_id = 56 # int | 

    try:
        # Get Organization Issue Types
        api_response = await api_instance.get_organization_issue_types_organizations_organization_id_issue_types_get(organization_id)
        print("The response of IssueTypesApi->get_organization_issue_types_organizations_organization_id_issue_types_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IssueTypesApi->get_organization_issue_types_organizations_organization_id_issue_types_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 

### Return type

[**List[IssueType]**](IssueType.md)

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

# **post_issue_type_organizations_organization_id_issue_types_post**
> IdAndMessageResponse post_issue_type_organizations_organization_id_issue_types_post(organization_id, issue_type_info)

Post Issue Type

Create new organization issue type

### Example


```python
import audithub_sdk
from audithub_sdk.models.id_and_message_response import IdAndMessageResponse
from audithub_sdk.models.issue_type_info import IssueTypeInfo
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
    api_instance = audithub_sdk.IssueTypesApi(api_client)
    organization_id = 56 # int | 
    issue_type_info = audithub_sdk.IssueTypeInfo() # IssueTypeInfo | 

    try:
        # Post Issue Type
        api_response = await api_instance.post_issue_type_organizations_organization_id_issue_types_post(organization_id, issue_type_info)
        print("The response of IssueTypesApi->post_issue_type_organizations_organization_id_issue_types_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IssueTypesApi->post_issue_type_organizations_organization_id_issue_types_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **issue_type_info** | [**IssueTypeInfo**](IssueTypeInfo.md)|  | 

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

# **put_issue_type_organizations_organization_id_issue_types_type_id_put**
> SuccessAndMessageResponse put_issue_type_organizations_organization_id_issue_types_type_id_put(organization_id, type_id, issue_type_info)

Put Issue Type

Put an issue type by id

### Example


```python
import audithub_sdk
from audithub_sdk.models.issue_type_info import IssueTypeInfo
from audithub_sdk.models.success_and_message_response import SuccessAndMessageResponse
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
    api_instance = audithub_sdk.IssueTypesApi(api_client)
    organization_id = 56 # int | 
    type_id = 56 # int | 
    issue_type_info = audithub_sdk.IssueTypeInfo() # IssueTypeInfo | 

    try:
        # Put Issue Type
        api_response = await api_instance.put_issue_type_organizations_organization_id_issue_types_type_id_put(organization_id, type_id, issue_type_info)
        print("The response of IssueTypesApi->put_issue_type_organizations_organization_id_issue_types_type_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IssueTypesApi->put_issue_type_organizations_organization_id_issue_types_type_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **type_id** | **int**|  | 
 **issue_type_info** | [**IssueTypeInfo**](IssueTypeInfo.md)|  | 

### Return type

[**SuccessAndMessageResponse**](SuccessAndMessageResponse.md)

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

