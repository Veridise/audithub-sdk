# audithub_sdk.SubscriptionsApi

All URIs are relative to *https://audithub.dev.veridise.tools/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_extras_organizations_organization_id_extras_get**](SubscriptionsApi.md#get_extras_organizations_organization_id_extras_get) | **GET** /organizations/{organization_id}/extras | List organization extra credits
[**get_subscription_organizations_organization_id_subscriptions_subscription_id_get**](SubscriptionsApi.md#get_subscription_organizations_organization_id_subscriptions_subscription_id_get) | **GET** /organizations/{organization_id}/subscriptions/{subscription_id} | Get an organization subscription
[**get_subscriptions_organizations_organization_id_subscriptions_get**](SubscriptionsApi.md#get_subscriptions_organizations_organization_id_subscriptions_get) | **GET** /organizations/{organization_id}/subscriptions | List organization subscriptions
[**patch_subscription_organizations_organization_id_subscriptions_subscription_id_patch**](SubscriptionsApi.md#patch_subscription_organizations_organization_id_subscriptions_subscription_id_patch) | **PATCH** /organizations/{organization_id}/subscriptions/{subscription_id} | Update or soft delete an organization subscription
[**post_extra_organizations_organization_id_extras_post**](SubscriptionsApi.md#post_extra_organizations_organization_id_extras_post) | **POST** /organizations/{organization_id}/extras | Create organization extra credits
[**post_subscription_organizations_organization_id_subscriptions_post**](SubscriptionsApi.md#post_subscription_organizations_organization_id_subscriptions_post) | **POST** /organizations/{organization_id}/subscriptions | Create an organization subscription


# **get_extras_organizations_organization_id_extras_get**
> OrganizationExtras get_extras_organizations_organization_id_extras_get(organization_id)

List organization extra credits

Returns all extras, including expired grants and grants from previous subscriptions, ordered by purchase time descending. Expiry is exclusive.

### Example


```python
import audithub_sdk
from audithub_sdk.models.organization_extras import OrganizationExtras
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
        # List organization extra credits
        api_response = await api_instance.get_extras_organizations_organization_id_extras_get(organization_id)
        print("The response of SubscriptionsApi->get_extras_organizations_organization_id_extras_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->get_extras_organizations_organization_id_extras_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 

### Return type

[**OrganizationExtras**](OrganizationExtras.md)

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

# **get_subscription_organizations_organization_id_subscriptions_subscription_id_get**
> OrganizationSubscription get_subscription_organizations_organization_id_subscriptions_subscription_id_get(organization_id, subscription_id)

Get an organization subscription

Return a subscription belonging to the specified organization.

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
        # Get an organization subscription
        api_response = await api_instance.get_subscription_organizations_organization_id_subscriptions_subscription_id_get(organization_id, subscription_id)
        print("The response of SubscriptionsApi->get_subscription_organizations_organization_id_subscriptions_subscription_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->get_subscription_organizations_organization_id_subscriptions_subscription_id_get: %s\n" % e)
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
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscriptions_organizations_organization_id_subscriptions_get**
> List[OrganizationSubscription] get_subscriptions_organizations_organization_id_subscriptions_get(organization_id)

List organization subscriptions

Return all the organization's subscriptions, ordered by start time descending.

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

    try:
        # List organization subscriptions
        api_response = await api_instance.get_subscriptions_organizations_organization_id_subscriptions_get(organization_id)
        print("The response of SubscriptionsApi->get_subscriptions_organizations_organization_id_subscriptions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->get_subscriptions_organizations_organization_id_subscriptions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 

### Return type

[**List[OrganizationSubscription]**](OrganizationSubscription.md)

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

# **patch_subscription_organizations_organization_id_subscriptions_subscription_id_patch**
> ResponsePatchSubscriptionOrganizationsOrganizationIdSubscriptionsSubscriptionIdPatch patch_subscription_organizations_organization_id_subscriptions_subscription_id_patch(organization_id, subscription_id, data)

Update or soft delete an organization subscription

Update a subscription belonging to the organization. Returns the updated subscription for duration or credit changes, or a success message for deletion. Select the change using `action`:

- `duration`: provide the new `start_time` and `end_time`. Both may change, even after the subscription starts. Free subscriptions must remain open-ended when changing dates through PATCH. Funding periods include the start and exclude the end.
- `credits`: provide `monthly_credits` to override the plan's monthly grant. For either action, any task allocation associated with this subscription causes HTTP 409.
- `delete`: soft delete the subscription, preserving its database row and credit records.

### Example


```python
import audithub_sdk
from audithub_sdk.models.data import Data
from audithub_sdk.models.response_patch_subscription_organizations_organization_id_subscriptions_subscription_id_patch import ResponsePatchSubscriptionOrganizationsOrganizationIdSubscriptionsSubscriptionIdPatch
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
    data = audithub_sdk.Data() # Data | 

    try:
        # Update or soft delete an organization subscription
        api_response = await api_instance.patch_subscription_organizations_organization_id_subscriptions_subscription_id_patch(organization_id, subscription_id, data)
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
 **data** | [**Data**](Data.md)|  | 

### Return type

[**ResponsePatchSubscriptionOrganizationsOrganizationIdSubscriptionsSubscriptionIdPatch**](ResponsePatchSubscriptionOrganizationsOrganizationIdSubscriptionsSubscriptionIdPatch.md)

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

# **post_extra_organizations_organization_id_extras_post**
> IdAndMessageResponse post_extra_organizations_organization_id_extras_post(organization_id, new_organization_extra)

Create organization extra credits

Requires an active subscription. Creates extra credits and a funding period atomically, expiring based on extra credit config. The supplied credits override the option's credit amount.

### Example


```python
import audithub_sdk
from audithub_sdk.models.id_and_message_response import IdAndMessageResponse
from audithub_sdk.models.new_organization_extra import NewOrganizationExtra
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
    new_organization_extra = audithub_sdk.NewOrganizationExtra() # NewOrganizationExtra | 

    try:
        # Create organization extra credits
        api_response = await api_instance.post_extra_organizations_organization_id_extras_post(organization_id, new_organization_extra)
        print("The response of SubscriptionsApi->post_extra_organizations_organization_id_extras_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->post_extra_organizations_organization_id_extras_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **new_organization_extra** | [**NewOrganizationExtra**](NewOrganizationExtra.md)|  | 

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
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_subscription_organizations_organization_id_subscriptions_post**
> IdAndMessageResponse post_subscription_organizations_organization_id_subscriptions_post(organization_id, new_organization_subscription)

Create an organization subscription

Create a subscription for an existing organization and generate its credit periods. Apply the plan's organization access restrictions. When a free subscription is active at the new start time, its end and its credit period's end are set to that start time. Other overlapping subscriptions are rejected with HTTP 409..

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
        # Create an organization subscription
        api_response = await api_instance.post_subscription_organizations_organization_id_subscriptions_post(organization_id, new_organization_subscription)
        print("The response of SubscriptionsApi->post_subscription_organizations_organization_id_subscriptions_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->post_subscription_organizations_organization_id_subscriptions_post: %s\n" % e)
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
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

