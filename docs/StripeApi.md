# audithub_sdk.StripeApi

All URIs are relative to *https://audithub.dev.veridise.tools/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_account_session_organizations_organization_id_stripe_account_post**](StripeApi.md#create_account_session_organizations_organization_id_stripe_account_post) | **POST** /organizations/{organization_id}/stripe/account | Create Account Session
[**create_extra_session_organizations_organization_id_stripe_extra_post**](StripeApi.md#create_extra_session_organizations_organization_id_stripe_extra_post) | **POST** /organizations/{organization_id}/stripe/extra | Create Extra Session
[**create_subscription_session_organizations_organization_id_stripe_subscription_post**](StripeApi.md#create_subscription_session_organizations_organization_id_stripe_subscription_post) | **POST** /organizations/{organization_id}/stripe/subscription | Create Subscription Session
[**decrease_extra_seats_organizations_organization_id_stripe_extra_seats_decrease_post**](StripeApi.md#decrease_extra_seats_organizations_organization_id_stripe_extra_seats_decrease_post) | **POST** /organizations/{organization_id}/stripe/extra-seats/decrease | Decrease Extra Seats
[**increase_extra_seats_organizations_organization_id_stripe_extra_seats_increase_post**](StripeApi.md#increase_extra_seats_organizations_organization_id_stripe_extra_seats_increase_post) | **POST** /organizations/{organization_id}/stripe/extra-seats/increase | Increase Extra Seats
[**request_subscription_upgrade_organizations_organization_id_stripe_upgrade_subscription_post**](StripeApi.md#request_subscription_upgrade_organizations_organization_id_stripe_upgrade_subscription_post) | **POST** /organizations/{organization_id}/stripe/upgrade-subscription | Upgrade subscription plan
[**stripe_webhook_stripe_webhook_post**](StripeApi.md#stripe_webhook_stripe_webhook_post) | **POST** /stripe/webhook | Stripe Webhook


# **create_account_session_organizations_organization_id_stripe_account_post**
> StripeSession create_account_session_organizations_organization_id_stripe_account_post(organization_id)

Create Account Session

### Example


```python
import audithub_sdk
from audithub_sdk.models.stripe_session import StripeSession
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
    api_instance = audithub_sdk.StripeApi(api_client)
    organization_id = 56 # int | 

    try:
        # Create Account Session
        api_response = await api_instance.create_account_session_organizations_organization_id_stripe_account_post(organization_id)
        print("The response of StripeApi->create_account_session_organizations_organization_id_stripe_account_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StripeApi->create_account_session_organizations_organization_id_stripe_account_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 

### Return type

[**StripeSession**](StripeSession.md)

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

# **create_extra_session_organizations_organization_id_stripe_extra_post**
> StripeSession create_extra_session_organizations_organization_id_stripe_extra_post(organization_id, extra_checkout_request)

Create Extra Session

### Example


```python
import audithub_sdk
from audithub_sdk.models.extra_checkout_request import ExtraCheckoutRequest
from audithub_sdk.models.stripe_session import StripeSession
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
    api_instance = audithub_sdk.StripeApi(api_client)
    organization_id = 56 # int | 
    extra_checkout_request = audithub_sdk.ExtraCheckoutRequest() # ExtraCheckoutRequest | 

    try:
        # Create Extra Session
        api_response = await api_instance.create_extra_session_organizations_organization_id_stripe_extra_post(organization_id, extra_checkout_request)
        print("The response of StripeApi->create_extra_session_organizations_organization_id_stripe_extra_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StripeApi->create_extra_session_organizations_organization_id_stripe_extra_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **extra_checkout_request** | [**ExtraCheckoutRequest**](ExtraCheckoutRequest.md)|  | 

### Return type

[**StripeSession**](StripeSession.md)

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

# **create_subscription_session_organizations_organization_id_stripe_subscription_post**
> StripeSession create_subscription_session_organizations_organization_id_stripe_subscription_post(organization_id, subscription_checkout_request)

Create Subscription Session

### Example


```python
import audithub_sdk
from audithub_sdk.models.stripe_session import StripeSession
from audithub_sdk.models.subscription_checkout_request import SubscriptionCheckoutRequest
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
    api_instance = audithub_sdk.StripeApi(api_client)
    organization_id = 56 # int | 
    subscription_checkout_request = audithub_sdk.SubscriptionCheckoutRequest() # SubscriptionCheckoutRequest | 

    try:
        # Create Subscription Session
        api_response = await api_instance.create_subscription_session_organizations_organization_id_stripe_subscription_post(organization_id, subscription_checkout_request)
        print("The response of StripeApi->create_subscription_session_organizations_organization_id_stripe_subscription_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StripeApi->create_subscription_session_organizations_organization_id_stripe_subscription_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **subscription_checkout_request** | [**SubscriptionCheckoutRequest**](SubscriptionCheckoutRequest.md)|  | 

### Return type

[**StripeSession**](StripeSession.md)

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

# **decrease_extra_seats_organizations_organization_id_stripe_extra_seats_decrease_post**
> SuccessAndMessageResponse decrease_extra_seats_organizations_organization_id_stripe_extra_seats_decrease_post(organization_id, stripe_extra_seats_decrease)

Decrease Extra Seats

### Example


```python
import audithub_sdk
from audithub_sdk.models.stripe_extra_seats_decrease import StripeExtraSeatsDecrease
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
    api_instance = audithub_sdk.StripeApi(api_client)
    organization_id = 56 # int | 
    stripe_extra_seats_decrease = audithub_sdk.StripeExtraSeatsDecrease() # StripeExtraSeatsDecrease | 

    try:
        # Decrease Extra Seats
        api_response = await api_instance.decrease_extra_seats_organizations_organization_id_stripe_extra_seats_decrease_post(organization_id, stripe_extra_seats_decrease)
        print("The response of StripeApi->decrease_extra_seats_organizations_organization_id_stripe_extra_seats_decrease_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StripeApi->decrease_extra_seats_organizations_organization_id_stripe_extra_seats_decrease_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **stripe_extra_seats_decrease** | [**StripeExtraSeatsDecrease**](StripeExtraSeatsDecrease.md)|  | 

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

# **increase_extra_seats_organizations_organization_id_stripe_extra_seats_increase_post**
> SuccessAndMessageResponse increase_extra_seats_organizations_organization_id_stripe_extra_seats_increase_post(organization_id, stripe_extra_seats_increase)

Increase Extra Seats

### Example


```python
import audithub_sdk
from audithub_sdk.models.stripe_extra_seats_increase import StripeExtraSeatsIncrease
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
    api_instance = audithub_sdk.StripeApi(api_client)
    organization_id = 56 # int | 
    stripe_extra_seats_increase = audithub_sdk.StripeExtraSeatsIncrease() # StripeExtraSeatsIncrease | 

    try:
        # Increase Extra Seats
        api_response = await api_instance.increase_extra_seats_organizations_organization_id_stripe_extra_seats_increase_post(organization_id, stripe_extra_seats_increase)
        print("The response of StripeApi->increase_extra_seats_organizations_organization_id_stripe_extra_seats_increase_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StripeApi->increase_extra_seats_organizations_organization_id_stripe_extra_seats_increase_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **stripe_extra_seats_increase** | [**StripeExtraSeatsIncrease**](StripeExtraSeatsIncrease.md)|  | 

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

# **request_subscription_upgrade_organizations_organization_id_stripe_upgrade_subscription_post**
> SuccessAndMessageResponse request_subscription_upgrade_organizations_organization_id_stripe_upgrade_subscription_post(organization_id, subscription_checkout_request)

Upgrade subscription plan

### Example


```python
import audithub_sdk
from audithub_sdk.models.subscription_checkout_request import SubscriptionCheckoutRequest
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
    api_instance = audithub_sdk.StripeApi(api_client)
    organization_id = 56 # int | 
    subscription_checkout_request = audithub_sdk.SubscriptionCheckoutRequest() # SubscriptionCheckoutRequest | 

    try:
        # Upgrade subscription plan
        api_response = await api_instance.request_subscription_upgrade_organizations_organization_id_stripe_upgrade_subscription_post(organization_id, subscription_checkout_request)
        print("The response of StripeApi->request_subscription_upgrade_organizations_organization_id_stripe_upgrade_subscription_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StripeApi->request_subscription_upgrade_organizations_organization_id_stripe_upgrade_subscription_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **subscription_checkout_request** | [**SubscriptionCheckoutRequest**](SubscriptionCheckoutRequest.md)|  | 

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

# **stripe_webhook_stripe_webhook_post**
> object stripe_webhook_stripe_webhook_post()

Stripe Webhook

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
    api_instance = audithub_sdk.StripeApi(api_client)

    try:
        # Stripe Webhook
        api_response = await api_instance.stripe_webhook_stripe_webhook_post()
        print("The response of StripeApi->stripe_webhook_stripe_webhook_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StripeApi->stripe_webhook_stripe_webhook_post: %s\n" % e)
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

