# audithub_sdk.CustomDetectorsStdLibApi

All URIs are relative to *https://audithub.dev.veridise.tools/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_custom_detectors_library_custom_detectors_library_get**](CustomDetectorsStdLibApi.md#get_custom_detectors_library_custom_detectors_library_get) | **GET** /custom-detectors-library | Get Custom Detectors Library
[**get_custom_detectors_library_version_custom_detectors_library_version_id_get**](CustomDetectorsStdLibApi.md#get_custom_detectors_library_version_custom_detectors_library_version_id_get) | **GET** /custom-detectors-library/{version_id} | Get Custom Detectors Library Version


# **get_custom_detectors_library_custom_detectors_library_get**
> Dict[str, object] get_custom_detectors_library_custom_detectors_library_get()

Get Custom Detectors Library

Returns the latest version of the Custom Detectors Library

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
    api_instance = audithub_sdk.CustomDetectorsStdLibApi(api_client)

    try:
        # Get Custom Detectors Library
        api_response = await api_instance.get_custom_detectors_library_custom_detectors_library_get()
        print("The response of CustomDetectorsStdLibApi->get_custom_detectors_library_custom_detectors_library_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomDetectorsStdLibApi->get_custom_detectors_library_custom_detectors_library_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**Dict[str, object]**

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

# **get_custom_detectors_library_version_custom_detectors_library_version_id_get**
> object get_custom_detectors_library_version_custom_detectors_library_version_id_get(version_id)

Get Custom Detectors Library Version

Returns a specific version of the Custom Detectors Library

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
    api_instance = audithub_sdk.CustomDetectorsStdLibApi(api_client)
    version_id = 'version_id_example' # str | 

    try:
        # Get Custom Detectors Library Version
        api_response = await api_instance.get_custom_detectors_library_version_custom_detectors_library_version_id_get(version_id)
        print("The response of CustomDetectorsStdLibApi->get_custom_detectors_library_version_custom_detectors_library_version_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomDetectorsStdLibApi->get_custom_detectors_library_version_custom_detectors_library_version_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_id** | **str**|  | 

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
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

