# audithub_sdk.SubscriptionsApi

All URIs are relative to *https://audithub.dev.veridise.tools/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_current_organization_subscriptions_organizations_organization_id_subscriptions_get**](SubscriptionsApi.md#get_current_organization_subscriptions_organizations_organization_id_subscriptions_get) | **GET** /organizations/{organization_id}/subscriptions | Get Current Organization Subscriptions
[**get_organization_subscription_organizations_organization_id_subscriptions_subscription_id_get**](SubscriptionsApi.md#get_organization_subscription_organizations_organization_id_subscriptions_subscription_id_get) | **GET** /organizations/{organization_id}/subscriptions/{subscription_id} | Get Organization Subscription
[**patch_subscription_organizations_organization_id_subscriptions_subscription_id_patch**](SubscriptionsApi.md#patch_subscription_organizations_organization_id_subscriptions_subscription_id_patch) | **PATCH** /organizations/{organization_id}/subscriptions/{subscription_id} | Patch Subscription
[**post_organization_subscription_organizations_organization_id_subscriptions_post**](SubscriptionsApi.md#post_organization_subscription_organizations_organization_id_subscriptions_post) | **POST** /organizations/{organization_id}/subscriptions | Post Organization Subscription
[**put_organization_subscription_organizations_organization_id_subscriptions_subscription_id_put**](SubscriptionsApi.md#put_organization_subscription_organizations_organization_id_subscriptions_subscription_id_put) | **PUT** /organizations/{organization_id}/subscriptions/{subscription_id} | Put Organization Subscription


# **get_current_organization_subscriptions_organizations_organization_id_subscriptions_get**
> object get_current_organization_subscriptions_organizations_organization_id_subscriptions_get(organization_id)

Get Current Organization Subscriptions

Get currently active organization subscriptions

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
    api_instance = audithub_sdk.SubscriptionsApi(api_client)
    organization_id = 56 # int | 

    try:
        # Get Current Organization Subscriptions
        api_response = await api_instance.get_current_organization_subscriptions_organizations_organization_id_subscriptions_get(organization_id)
        print("The response of SubscriptionsApi->get_current_organization_subscriptions_organizations_organization_id_subscriptions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->get_current_organization_subscriptions_organizations_organization_id_subscriptions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 

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

# **get_organization_subscription_organizations_organization_id_subscriptions_subscription_id_get**
> OrganizationSubscription get_organization_subscription_organizations_organization_id_subscriptions_subscription_id_get(organization_id, subscription_id)

Get Organization Subscription

Get organization subscription

### Example


```python
import audithub_sdk
from audithub_sdk.models.organization_subscription import OrganizationSubscription
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
    api_instance = audithub_sdk.SubscriptionsApi(api_client)
    organization_id = 56 # int | 
    subscription_id = 56 # int | 

    try:
        # Get Organization Subscription
        api_response = await api_instance.get_organization_subscription_organizations_organization_id_subscriptions_subscription_id_get(organization_id, subscription_id)
        print("The response of SubscriptionsApi->get_organization_subscription_organizations_organization_id_subscriptions_subscription_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->get_organization_subscription_organizations_organization_id_subscriptions_subscription_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **subscription_id** | **int**|  | 

### Return type

[**OrganizationSubscription**](OrganizationSubscription.md)

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

# **patch_subscription_organizations_organization_id_subscriptions_subscription_id_patch**
> SuccessAndMessageResponse patch_subscription_organizations_organization_id_subscriptions_subscription_id_patch(organization_id, subscription_id, resource_patch)

Patch Subscription

Patch subscription

### Example


```python
import audithub_sdk
from audithub_sdk.models.resource_patch import ResourcePatch
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
    api_instance = audithub_sdk.SubscriptionsApi(api_client)
    organization_id = 56 # int | 
    subscription_id = 56 # int | 
    resource_patch = audithub_sdk.ResourcePatch() # ResourcePatch | 

    try:
        # Patch Subscription
        api_response = await api_instance.patch_subscription_organizations_organization_id_subscriptions_subscription_id_patch(organization_id, subscription_id, resource_patch)
        print("The response of SubscriptionsApi->patch_subscription_organizations_organization_id_subscriptions_subscription_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->patch_subscription_organizations_organization_id_subscriptions_subscription_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **subscription_id** | **int**|  | 
 **resource_patch** | [**ResourcePatch**](ResourcePatch.md)|  | 

### Return type

[**SuccessAndMessageResponse**](SuccessAndMessageResponse.md)

### Authorization

[OpenIdConnect](../README.md#OpenIdConnect)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_organization_subscription_organizations_organization_id_subscriptions_post**
> IdAndMessageResponse post_organization_subscription_organizations_organization_id_subscriptions_post(organization_id, new_organization_subscription)

Post Organization Subscription

Create new organization subscription

### Example


```python
import audithub_sdk
from audithub_sdk.models.id_and_message_response import IdAndMessageResponse
from audithub_sdk.models.new_organization_subscription import NewOrganizationSubscription
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
    api_instance = audithub_sdk.SubscriptionsApi(api_client)
    organization_id = 56 # int | 
    new_organization_subscription = audithub_sdk.NewOrganizationSubscription() # NewOrganizationSubscription | 

    try:
        # Post Organization Subscription
        api_response = await api_instance.post_organization_subscription_organizations_organization_id_subscriptions_post(organization_id, new_organization_subscription)
        print("The response of SubscriptionsApi->post_organization_subscription_organizations_organization_id_subscriptions_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->post_organization_subscription_organizations_organization_id_subscriptions_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **new_organization_subscription** | [**NewOrganizationSubscription**](NewOrganizationSubscription.md)|  | 

### Return type

[**IdAndMessageResponse**](IdAndMessageResponse.md)

### Authorization

[OpenIdConnect](../README.md#OpenIdConnect)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_organization_subscription_organizations_organization_id_subscriptions_subscription_id_put**
> SuccessAndMessageResponse put_organization_subscription_organizations_organization_id_subscriptions_subscription_id_put(organization_id, subscription_id, new_organization_subscription)

Put Organization Subscription

Update active organization subscription

### Example


```python
import audithub_sdk
from audithub_sdk.models.new_organization_subscription import NewOrganizationSubscription
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
    api_instance = audithub_sdk.SubscriptionsApi(api_client)
    organization_id = 56 # int | 
    subscription_id = 56 # int | 
    new_organization_subscription = audithub_sdk.NewOrganizationSubscription() # NewOrganizationSubscription | 

    try:
        # Put Organization Subscription
        api_response = await api_instance.put_organization_subscription_organizations_organization_id_subscriptions_subscription_id_put(organization_id, subscription_id, new_organization_subscription)
        print("The response of SubscriptionsApi->put_organization_subscription_organizations_organization_id_subscriptions_subscription_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->put_organization_subscription_organizations_organization_id_subscriptions_subscription_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **subscription_id** | **int**|  | 
 **new_organization_subscription** | [**NewOrganizationSubscription**](NewOrganizationSubscription.md)|  | 

### Return type

[**SuccessAndMessageResponse**](SuccessAndMessageResponse.md)

### Authorization

[OpenIdConnect](../README.md#OpenIdConnect)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

