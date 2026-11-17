# audithub_sdk.CustomDetectorsOrgLibApi

All URIs are relative to *https://audithub.dev.veridise.tools/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_custom_detector_organizations_organization_id_custom_detectors_custom_detector_id_delete**](CustomDetectorsOrgLibApi.md#delete_custom_detector_organizations_organization_id_custom_detectors_custom_detector_id_delete) | **DELETE** /organizations/{organization_id}/custom_detectors/{custom_detector_id} | Delete Custom Detector
[**get_custom_detector_organizations_organization_id_custom_detectors_custom_detector_id_get**](CustomDetectorsOrgLibApi.md#get_custom_detector_organizations_organization_id_custom_detectors_custom_detector_id_get) | **GET** /organizations/{organization_id}/custom_detectors/{custom_detector_id} | Get Custom Detector
[**get_custom_detectors_organizations_organization_id_custom_detectors_get**](CustomDetectorsOrgLibApi.md#get_custom_detectors_organizations_organization_id_custom_detectors_get) | **GET** /organizations/{organization_id}/custom_detectors | Get Custom Detectors
[**post_custom_detector_organizations_organization_id_custom_detectors_post**](CustomDetectorsOrgLibApi.md#post_custom_detector_organizations_organization_id_custom_detectors_post) | **POST** /organizations/{organization_id}/custom_detectors | Post Custom Detector
[**put_custom_detector_organizations_organization_id_custom_detectors_custom_detector_id_put**](CustomDetectorsOrgLibApi.md#put_custom_detector_organizations_organization_id_custom_detectors_custom_detector_id_put) | **PUT** /organizations/{organization_id}/custom_detectors/{custom_detector_id} | Put Custom Detector


# **delete_custom_detector_organizations_organization_id_custom_detectors_custom_detector_id_delete**
> SuccessAndMessageResponse delete_custom_detector_organizations_organization_id_custom_detectors_custom_detector_id_delete(organization_id, custom_detector_id)

Delete Custom Detector

Permanently delete a custom detector

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
    api_instance = audithub_sdk.CustomDetectorsOrgLibApi(api_client)
    organization_id = 56 # int | 
    custom_detector_id = 56 # int | 

    try:
        # Delete Custom Detector
        api_response = await api_instance.delete_custom_detector_organizations_organization_id_custom_detectors_custom_detector_id_delete(organization_id, custom_detector_id)
        print("The response of CustomDetectorsOrgLibApi->delete_custom_detector_organizations_organization_id_custom_detectors_custom_detector_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomDetectorsOrgLibApi->delete_custom_detector_organizations_organization_id_custom_detectors_custom_detector_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **custom_detector_id** | **int**|  | 

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

# **get_custom_detector_organizations_organization_id_custom_detectors_custom_detector_id_get**
> CustomDetector get_custom_detector_organizations_organization_id_custom_detectors_custom_detector_id_get(organization_id, custom_detector_id)

Get Custom Detector

Returns custom detector attributes

### Example


```python
import audithub_sdk
from audithub_sdk.models.custom_detector import CustomDetector
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
    api_instance = audithub_sdk.CustomDetectorsOrgLibApi(api_client)
    organization_id = 56 # int | 
    custom_detector_id = 56 # int | 

    try:
        # Get Custom Detector
        api_response = await api_instance.get_custom_detector_organizations_organization_id_custom_detectors_custom_detector_id_get(organization_id, custom_detector_id)
        print("The response of CustomDetectorsOrgLibApi->get_custom_detector_organizations_organization_id_custom_detectors_custom_detector_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomDetectorsOrgLibApi->get_custom_detector_organizations_organization_id_custom_detectors_custom_detector_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **custom_detector_id** | **int**|  | 

### Return type

[**CustomDetector**](CustomDetector.md)

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

# **get_custom_detectors_organizations_organization_id_custom_detectors_get**
> List[CustomDetectorWithId] get_custom_detectors_organizations_organization_id_custom_detectors_get(organization_id)

Get Custom Detectors

Returns all Custom Detectors of a  organization

### Example


```python
import audithub_sdk
from audithub_sdk.models.custom_detector_with_id import CustomDetectorWithId
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
    api_instance = audithub_sdk.CustomDetectorsOrgLibApi(api_client)
    organization_id = 56 # int | 

    try:
        # Get Custom Detectors
        api_response = await api_instance.get_custom_detectors_organizations_organization_id_custom_detectors_get(organization_id)
        print("The response of CustomDetectorsOrgLibApi->get_custom_detectors_organizations_organization_id_custom_detectors_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomDetectorsOrgLibApi->get_custom_detectors_organizations_organization_id_custom_detectors_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 

### Return type

[**List[CustomDetectorWithId]**](CustomDetectorWithId.md)

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

# **post_custom_detector_organizations_organization_id_custom_detectors_post**
> IdAndMessageResponse post_custom_detector_organizations_organization_id_custom_detectors_post(organization_id, custom_detector)

Post Custom Detector

Post custom detector

### Example


```python
import audithub_sdk
from audithub_sdk.models.custom_detector import CustomDetector
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
    api_instance = audithub_sdk.CustomDetectorsOrgLibApi(api_client)
    organization_id = 56 # int | 
    custom_detector = audithub_sdk.CustomDetector() # CustomDetector | 

    try:
        # Post Custom Detector
        api_response = await api_instance.post_custom_detector_organizations_organization_id_custom_detectors_post(organization_id, custom_detector)
        print("The response of CustomDetectorsOrgLibApi->post_custom_detector_organizations_organization_id_custom_detectors_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomDetectorsOrgLibApi->post_custom_detector_organizations_organization_id_custom_detectors_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **custom_detector** | [**CustomDetector**](CustomDetector.md)|  | 

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

# **put_custom_detector_organizations_organization_id_custom_detectors_custom_detector_id_put**
> SuccessAndMessageResponse put_custom_detector_organizations_organization_id_custom_detectors_custom_detector_id_put(organization_id, custom_detector_id, custom_detector)

Put Custom Detector

Update custom detector attributes

### Example


```python
import audithub_sdk
from audithub_sdk.models.custom_detector import CustomDetector
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
    api_instance = audithub_sdk.CustomDetectorsOrgLibApi(api_client)
    organization_id = 56 # int | 
    custom_detector_id = 56 # int | 
    custom_detector = audithub_sdk.CustomDetector() # CustomDetector | 

    try:
        # Put Custom Detector
        api_response = await api_instance.put_custom_detector_organizations_organization_id_custom_detectors_custom_detector_id_put(organization_id, custom_detector_id, custom_detector)
        print("The response of CustomDetectorsOrgLibApi->put_custom_detector_organizations_organization_id_custom_detectors_custom_detector_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomDetectorsOrgLibApi->put_custom_detector_organizations_organization_id_custom_detectors_custom_detector_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **custom_detector_id** | **int**|  | 
 **custom_detector** | [**CustomDetector**](CustomDetector.md)|  | 

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

