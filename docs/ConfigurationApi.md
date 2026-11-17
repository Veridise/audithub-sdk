# audithub_sdk.ConfigurationApi

All URIs are relative to *https://audithub.dev.veridise.tools/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_api_keys_api_keys_configuration_get**](ConfigurationApi.md#get_api_keys_api_keys_configuration_get) | **GET** /api-keys-configuration | Get Api Keys
[**get_configuration_configuration_get**](ConfigurationApi.md#get_configuration_configuration_get) | **GET** /configuration | Get Configuration


# **get_api_keys_api_keys_configuration_get**
> object get_api_keys_api_keys_configuration_get()

Get Api Keys

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
    api_instance = audithub_sdk.ConfigurationApi(api_client)

    try:
        # Get Api Keys
        api_response = await api_instance.get_api_keys_api_keys_configuration_get()
        print("The response of ConfigurationApi->get_api_keys_api_keys_configuration_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->get_api_keys_api_keys_configuration_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_configuration_configuration_get**
> PublicConfiguration get_configuration_configuration_get()

Get Configuration

### Example


```python
import audithub_sdk
from audithub_sdk.models.public_configuration import PublicConfiguration
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
    api_instance = audithub_sdk.ConfigurationApi(api_client)

    try:
        # Get Configuration
        api_response = await api_instance.get_configuration_configuration_get()
        print("The response of ConfigurationApi->get_configuration_configuration_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->get_configuration_configuration_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**PublicConfiguration**](PublicConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

