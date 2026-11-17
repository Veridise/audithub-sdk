"""Regression coverage for the November 2026 API schema update."""
import asyncio
from pathlib import Path

import audithub_sdk as sdk


def test_agent_input_serialization():
    model = sdk.AgentInput.from_dict({
        "budget": "standard", "parameters": {
            "input_limit": ["src/"], "extra_context": "Review access control",
            "generate_pocs": True,
        },
    })
    assert model is not None
    assert model.to_dict() == {
        "budget": "standard", "parameters": {
            "input_limit": ["src/"], "extra_context": "Review access control",
            "generate_pocs": True,
        },
    }


def test_problem_details_validation_response():
    payload = {"title": "Validation failed", "type": "validation_error",
               "status": 422, "errors": [
                   {"loc": ["body", "name"], "msg": "Field required", "type": "missing", "input": None},
               ]}
    error = sdk.HTTPValidationError.from_dict(payload)
    assert error is not None
    assert error.to_dict() == payload


def test_credit_summary_request_serialization():
    async def check():
        config = sdk.Configuration(host="https://example.invalid/api/v1")
        async with sdk.ApiClient(config) as client:
            request = sdk.CreditsApi(client)._get_credit_summary_organizations_organization_id_credits_summary_get_serialize(
                organization_id=42, current_only=True, _request_auth=None,
                _content_type=None, _headers=None, _host_index=None,
            )
            assert request[0] == "GET"
            assert request[1] == "https://example.invalid/api/v1/organizations/42/credits/summary?current_only=true"
    asyncio.run(check())


def test_current_credit_and_orca_fields():
    assert "plan_id" in sdk.NewOrganizationSubscription.model_fields
    assert "monthly_credits" in sdk.NewOrganizationSubscription.model_fields
    assert "cpu_minutes" not in sdk.NewOrganizationSubscription.model_fields
    assert "auxiliary_deployment_script" in sdk.OrCaInput.model_fields
    assert "detail" not in sdk.HTTPValidationError.model_fields


def test_new_api_groups_exported_and_old_models_removed():
    for name in ("CreditsApi", "ProjectDocumentsApi", "StripeApi", "UiApi"):
        assert hasattr(sdk, name)
    models = Path(sdk.__file__).parent / "models"
    for name in ("organization_quota", "picus_input", "zk_vanguard_input"):
        assert not (models / (name + ".py")).exists()


def test_default_host_retains_schema_origin():
    assert sdk.Configuration().host == "https://audithub.dev.veridise.tools/api/v1"
