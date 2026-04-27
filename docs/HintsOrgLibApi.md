# audithub_sdk.HintsOrgLibApi

All URIs are relative to *https://audithub.dev.veridise.tools/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_hint_organizations_organization_id_hints_hint_id_delete**](HintsOrgLibApi.md#delete_hint_organizations_organization_id_hints_hint_id_delete) | **DELETE** /organizations/{organization_id}/hints/{hint_id} | Delete Hint
[**get_blacklisted_hints_organizations_organization_id_projects_project_id_blacklisted_hints_get**](HintsOrgLibApi.md#get_blacklisted_hints_organizations_organization_id_projects_project_id_blacklisted_hints_get) | **GET** /organizations/{organization_id}/projects/{project_id}/blacklisted-hints | Get Blacklisted Hints
[**get_hint_organizations_organization_id_hints_hint_id_get**](HintsOrgLibApi.md#get_hint_organizations_organization_id_hints_hint_id_get) | **GET** /organizations/{organization_id}/hints/{hint_id} | Get Hint
[**get_hints_organizations_organization_id_hints_get**](HintsOrgLibApi.md#get_hints_organizations_organization_id_hints_get) | **GET** /organizations/{organization_id}/hints | Get Hints
[**post_hint_organizations_organization_id_hints_post**](HintsOrgLibApi.md#post_hint_organizations_organization_id_hints_post) | **POST** /organizations/{organization_id}/hints | Post Hint
[**put_blacklisted_hints_organizations_organization_id_projects_project_id_blacklisted_hints_put**](HintsOrgLibApi.md#put_blacklisted_hints_organizations_organization_id_projects_project_id_blacklisted_hints_put) | **PUT** /organizations/{organization_id}/projects/{project_id}/blacklisted-hints | Put Blacklisted Hints
[**put_hint_organizations_organization_id_hints_hint_id_put**](HintsOrgLibApi.md#put_hint_organizations_organization_id_hints_hint_id_put) | **PUT** /organizations/{organization_id}/hints/{hint_id} | Put Hint


# **delete_hint_organizations_organization_id_hints_hint_id_delete**
> SuccessAndMessageResponse delete_hint_organizations_organization_id_hints_hint_id_delete(organization_id, hint_id)

Delete Hint

Permanently delete a hint

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
    api_instance = audithub_sdk.HintsOrgLibApi(api_client)
    organization_id = 56 # int | 
    hint_id = 56 # int | 

    try:
        # Delete Hint
        api_response = await api_instance.delete_hint_organizations_organization_id_hints_hint_id_delete(organization_id, hint_id)
        print("The response of HintsOrgLibApi->delete_hint_organizations_organization_id_hints_hint_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HintsOrgLibApi->delete_hint_organizations_organization_id_hints_hint_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **hint_id** | **int**|  | 

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

# **get_blacklisted_hints_organizations_organization_id_projects_project_id_blacklisted_hints_get**
> List[APIBlacklistedHint] get_blacklisted_hints_organizations_organization_id_projects_project_id_blacklisted_hints_get(organization_id, project_id)

Get Blacklisted Hints

Get Blacklisted hints for project

### Example


```python
import audithub_sdk
from audithub_sdk.models.api_blacklisted_hint import APIBlacklistedHint
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
    api_instance = audithub_sdk.HintsOrgLibApi(api_client)
    organization_id = 56 # int | 
    project_id = 56 # int | 

    try:
        # Get Blacklisted Hints
        api_response = await api_instance.get_blacklisted_hints_organizations_organization_id_projects_project_id_blacklisted_hints_get(organization_id, project_id)
        print("The response of HintsOrgLibApi->get_blacklisted_hints_organizations_organization_id_projects_project_id_blacklisted_hints_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HintsOrgLibApi->get_blacklisted_hints_organizations_organization_id_projects_project_id_blacklisted_hints_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **project_id** | **int**|  | 

### Return type

[**List[APIBlacklistedHint]**](APIBlacklistedHint.md)

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

# **get_hint_organizations_organization_id_hints_hint_id_get**
> Hint get_hint_organizations_organization_id_hints_hint_id_get(organization_id, hint_id)

Get Hint

Returns hint attributes

### Example


```python
import audithub_sdk
from audithub_sdk.models.hint import Hint
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
    api_instance = audithub_sdk.HintsOrgLibApi(api_client)
    organization_id = 56 # int | 
    hint_id = 56 # int | 

    try:
        # Get Hint
        api_response = await api_instance.get_hint_organizations_organization_id_hints_hint_id_get(organization_id, hint_id)
        print("The response of HintsOrgLibApi->get_hint_organizations_organization_id_hints_hint_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HintsOrgLibApi->get_hint_organizations_organization_id_hints_hint_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **hint_id** | **int**|  | 

### Return type

[**Hint**](Hint.md)

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

# **get_hints_organizations_organization_id_hints_get**
> List[HintWithId] get_hints_organizations_organization_id_hints_get(organization_id)

Get Hints

Returns all Hints of an organization

### Example


```python
import audithub_sdk
from audithub_sdk.models.hint_with_id import HintWithId
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
    api_instance = audithub_sdk.HintsOrgLibApi(api_client)
    organization_id = 56 # int | 

    try:
        # Get Hints
        api_response = await api_instance.get_hints_organizations_organization_id_hints_get(organization_id)
        print("The response of HintsOrgLibApi->get_hints_organizations_organization_id_hints_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HintsOrgLibApi->get_hints_organizations_organization_id_hints_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 

### Return type

[**List[HintWithId]**](HintWithId.md)

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

# **post_hint_organizations_organization_id_hints_post**
> IdAndMessageResponse post_hint_organizations_organization_id_hints_post(organization_id, hint)

Post Hint

Post Hint

### Example


```python
import audithub_sdk
from audithub_sdk.models.hint import Hint
from audithub_sdk.models.id_and_message_response import IdAndMessageResponse
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
    api_instance = audithub_sdk.HintsOrgLibApi(api_client)
    organization_id = 56 # int | 
    hint = audithub_sdk.Hint() # Hint | 

    try:
        # Post Hint
        api_response = await api_instance.post_hint_organizations_organization_id_hints_post(organization_id, hint)
        print("The response of HintsOrgLibApi->post_hint_organizations_organization_id_hints_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HintsOrgLibApi->post_hint_organizations_organization_id_hints_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **hint** | [**Hint**](Hint.md)|  | 

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

# **put_blacklisted_hints_organizations_organization_id_projects_project_id_blacklisted_hints_put**
> SuccessAndMessageResponse put_blacklisted_hints_organizations_organization_id_projects_project_id_blacklisted_hints_put(organization_id, project_id, api_blacklisted_hint)

Put Blacklisted Hints

Update Blacklisted hints for project

### Example


```python
import audithub_sdk
from audithub_sdk.models.api_blacklisted_hint import APIBlacklistedHint
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
    api_instance = audithub_sdk.HintsOrgLibApi(api_client)
    organization_id = 56 # int | 
    project_id = 56 # int | 
    api_blacklisted_hint = [audithub_sdk.APIBlacklistedHint()] # List[APIBlacklistedHint] | 

    try:
        # Put Blacklisted Hints
        api_response = await api_instance.put_blacklisted_hints_organizations_organization_id_projects_project_id_blacklisted_hints_put(organization_id, project_id, api_blacklisted_hint)
        print("The response of HintsOrgLibApi->put_blacklisted_hints_organizations_organization_id_projects_project_id_blacklisted_hints_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HintsOrgLibApi->put_blacklisted_hints_organizations_organization_id_projects_project_id_blacklisted_hints_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **project_id** | **int**|  | 
 **api_blacklisted_hint** | [**List[APIBlacklistedHint]**](APIBlacklistedHint.md)|  | 

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

# **put_hint_organizations_organization_id_hints_hint_id_put**
> SuccessAndMessageResponse put_hint_organizations_organization_id_hints_hint_id_put(organization_id, hint_id, hint)

Put Hint

Update hint attributes

### Example


```python
import audithub_sdk
from audithub_sdk.models.hint import Hint
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
    api_instance = audithub_sdk.HintsOrgLibApi(api_client)
    organization_id = 56 # int | 
    hint_id = 56 # int | 
    hint = audithub_sdk.Hint() # Hint | 

    try:
        # Put Hint
        api_response = await api_instance.put_hint_organizations_organization_id_hints_hint_id_put(organization_id, hint_id, hint)
        print("The response of HintsOrgLibApi->put_hint_organizations_organization_id_hints_hint_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HintsOrgLibApi->put_hint_organizations_organization_id_hints_hint_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **hint_id** | **int**|  | 
 **hint** | [**Hint**](Hint.md)|  | 

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

