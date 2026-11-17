# audithub_sdk.VSpecsOrgLibApi

All URIs are relative to *https://audithub.dev.veridise.tools/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_vspec_organizations_organization_id_vspecs_vspec_id_delete**](VSpecsOrgLibApi.md#delete_vspec_organizations_organization_id_vspecs_vspec_id_delete) | **DELETE** /organizations/{organization_id}/vspecs/{vspec_id} | Delete Vspec
[**get_vspec_organizations_organization_id_vspecs_vspec_id_get**](VSpecsOrgLibApi.md#get_vspec_organizations_organization_id_vspecs_vspec_id_get) | **GET** /organizations/{organization_id}/vspecs/{vspec_id} | Get Vspec
[**get_vspecs_organizations_organization_id_vspecs_get**](VSpecsOrgLibApi.md#get_vspecs_organizations_organization_id_vspecs_get) | **GET** /organizations/{organization_id}/vspecs | Get Vspecs
[**post_vspec_organizations_organization_id_vspecs_post**](VSpecsOrgLibApi.md#post_vspec_organizations_organization_id_vspecs_post) | **POST** /organizations/{organization_id}/vspecs | Post Vspec
[**put_vspec_organizations_organization_id_vspecs_vspec_id_put**](VSpecsOrgLibApi.md#put_vspec_organizations_organization_id_vspecs_vspec_id_put) | **PUT** /organizations/{organization_id}/vspecs/{vspec_id} | Put Vspec


# **delete_vspec_organizations_organization_id_vspecs_vspec_id_delete**
> SuccessAndMessageResponse delete_vspec_organizations_organization_id_vspecs_vspec_id_delete(organization_id, vspec_id)

Delete Vspec

Permanently delete a vspec

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
    api_instance = audithub_sdk.VSpecsOrgLibApi(api_client)
    organization_id = 56 # int | 
    vspec_id = 56 # int | 

    try:
        # Delete Vspec
        api_response = await api_instance.delete_vspec_organizations_organization_id_vspecs_vspec_id_delete(organization_id, vspec_id)
        print("The response of VSpecsOrgLibApi->delete_vspec_organizations_organization_id_vspecs_vspec_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VSpecsOrgLibApi->delete_vspec_organizations_organization_id_vspecs_vspec_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **vspec_id** | **int**|  | 

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

# **get_vspec_organizations_organization_id_vspecs_vspec_id_get**
> VSpec get_vspec_organizations_organization_id_vspecs_vspec_id_get(organization_id, vspec_id)

Get Vspec

Returns vspec attributes

### Example


```python
import audithub_sdk
from audithub_sdk.models.v_spec import VSpec
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
    api_instance = audithub_sdk.VSpecsOrgLibApi(api_client)
    organization_id = 56 # int | 
    vspec_id = 56 # int | 

    try:
        # Get Vspec
        api_response = await api_instance.get_vspec_organizations_organization_id_vspecs_vspec_id_get(organization_id, vspec_id)
        print("The response of VSpecsOrgLibApi->get_vspec_organizations_organization_id_vspecs_vspec_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VSpecsOrgLibApi->get_vspec_organizations_organization_id_vspecs_vspec_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **vspec_id** | **int**|  | 

### Return type

[**VSpec**](VSpec.md)

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

# **get_vspecs_organizations_organization_id_vspecs_get**
> List[VSpecWithId] get_vspecs_organizations_organization_id_vspecs_get(organization_id)

Get Vspecs

Returns all VSpecs of a  organization

### Example


```python
import audithub_sdk
from audithub_sdk.models.v_spec_with_id import VSpecWithId
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
    api_instance = audithub_sdk.VSpecsOrgLibApi(api_client)
    organization_id = 56 # int | 

    try:
        # Get Vspecs
        api_response = await api_instance.get_vspecs_organizations_organization_id_vspecs_get(organization_id)
        print("The response of VSpecsOrgLibApi->get_vspecs_organizations_organization_id_vspecs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VSpecsOrgLibApi->get_vspecs_organizations_organization_id_vspecs_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 

### Return type

[**List[VSpecWithId]**](VSpecWithId.md)

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

# **post_vspec_organizations_organization_id_vspecs_post**
> IdAndMessageResponse post_vspec_organizations_organization_id_vspecs_post(organization_id, v_spec)

Post Vspec

Post vspec

### Example


```python
import audithub_sdk
from audithub_sdk.models.id_and_message_response import IdAndMessageResponse
from audithub_sdk.models.v_spec import VSpec
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
    api_instance = audithub_sdk.VSpecsOrgLibApi(api_client)
    organization_id = 56 # int | 
    v_spec = audithub_sdk.VSpec() # VSpec | 

    try:
        # Post Vspec
        api_response = await api_instance.post_vspec_organizations_organization_id_vspecs_post(organization_id, v_spec)
        print("The response of VSpecsOrgLibApi->post_vspec_organizations_organization_id_vspecs_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VSpecsOrgLibApi->post_vspec_organizations_organization_id_vspecs_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **v_spec** | [**VSpec**](VSpec.md)|  | 

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

# **put_vspec_organizations_organization_id_vspecs_vspec_id_put**
> SuccessAndMessageResponse put_vspec_organizations_organization_id_vspecs_vspec_id_put(organization_id, vspec_id, v_spec)

Put Vspec

Update vspec attributes

### Example


```python
import audithub_sdk
from audithub_sdk.models.success_and_message_response import SuccessAndMessageResponse
from audithub_sdk.models.v_spec import VSpec
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
    api_instance = audithub_sdk.VSpecsOrgLibApi(api_client)
    organization_id = 56 # int | 
    vspec_id = 56 # int | 
    v_spec = audithub_sdk.VSpec() # VSpec | 

    try:
        # Put Vspec
        api_response = await api_instance.put_vspec_organizations_organization_id_vspecs_vspec_id_put(organization_id, vspec_id, v_spec)
        print("The response of VSpecsOrgLibApi->put_vspec_organizations_organization_id_vspecs_vspec_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VSpecsOrgLibApi->put_vspec_organizations_organization_id_vspecs_vspec_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **vspec_id** | **int**|  | 
 **v_spec** | [**VSpec**](VSpec.md)|  | 

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

