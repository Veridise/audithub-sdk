# audithub_sdk.GenericApi

All URIs are relative to *https://audithub.dev.veridise.tools/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**about_about_get**](GenericApi.md#about_about_get) | **GET** /about | About
[**get_psa_psa_get**](GenericApi.md#get_psa_psa_get) | **GET** /psa | Get Psa
[**get_task_redirect_task_redirect_get**](GenericApi.md#get_task_redirect_task_redirect_get) | **GET** /task-redirect | Get Task Redirect
[**health_check_health_check_get**](GenericApi.md#health_check_health_check_get) | **GET** /health_check | Health Check
[**private_private_get**](GenericApi.md#private_private_get) | **GET** /private | Private


# **about_about_get**
> object about_about_get()

About

### Example


```python
import audithub_sdk
from audithub_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://audithub.dev.veridise.tools/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = audithub_sdk.Configuration(
    host = "https://audithub.dev.veridise.tools/api/v1"
)


# Enter a context with an instance of the API client
async with audithub_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = audithub_sdk.GenericApi(api_client)

    try:
        # About
        api_response = await api_instance.about_about_get()
        print("The response of GenericApi->about_about_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenericApi->about_about_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_psa_psa_get**
> PSA get_psa_psa_get()

Get Psa

### Example


```python
import audithub_sdk
from audithub_sdk.models.psa import PSA
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
    api_instance = audithub_sdk.GenericApi(api_client)

    try:
        # Get Psa
        api_response = await api_instance.get_psa_psa_get()
        print("The response of GenericApi->get_psa_psa_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenericApi->get_psa_psa_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**PSA**](PSA.md)

### Authorization

[OpenIdConnect](../README.md#OpenIdConnect)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task_redirect_task_redirect_get**
> object get_task_redirect_task_redirect_get(id)

Get Task Redirect

Get UI endpoint of task analysis page

### Example


```python
import audithub_sdk
from audithub_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://audithub.dev.veridise.tools/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = audithub_sdk.Configuration(
    host = "https://audithub.dev.veridise.tools/api/v1"
)


# Enter a context with an instance of the API client
async with audithub_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = audithub_sdk.GenericApi(api_client)
    id = 56 # int | 

    try:
        # Get Task Redirect
        api_response = await api_instance.get_task_redirect_task_redirect_get(id)
        print("The response of GenericApi->get_task_redirect_task_redirect_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenericApi->get_task_redirect_task_redirect_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **health_check_health_check_get**
> object health_check_health_check_get()

Health Check

### Example


```python
import audithub_sdk
from audithub_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://audithub.dev.veridise.tools/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = audithub_sdk.Configuration(
    host = "https://audithub.dev.veridise.tools/api/v1"
)


# Enter a context with an instance of the API client
async with audithub_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = audithub_sdk.GenericApi(api_client)

    try:
        # Health Check
        api_response = await api_instance.health_check_health_check_get()
        print("The response of GenericApi->health_check_health_check_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenericApi->health_check_health_check_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_private_get**
> object private_private_get()

Private

A private endpoint for inspecting the attrs of the current user

### Example


```python
import audithub_sdk
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
    api_instance = audithub_sdk.GenericApi(api_client)

    try:
        # Private
        api_response = await api_instance.private_private_get()
        print("The response of GenericApi->private_private_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenericApi->private_private_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[OpenIdConnect](../README.md#OpenIdConnect)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

