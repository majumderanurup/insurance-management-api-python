from fastapi import APIRouter, Depends

from app.dependencies import get_policy_service
from app.schemas.policy import PolicyRequest, PolicyResponse
from app.services.policy_service import PolicyService


router = APIRouter(
    tags=["Policy"]
)


@router.get(
    "/policies",
    response_model=list[PolicyResponse],
)
def get_policies(
    policy_service: PolicyService = Depends(get_policy_service),
):
    return policy_service.get_policies()


@router.get(
    "/policies/{policy_id}",
    response_model=PolicyResponse,
)
def get_policy(
    policy_id: int,
    policy_service: PolicyService = Depends(get_policy_service),
):
    return policy_service.get_policy(policy_id)


@router.post(
    "/policies",
    response_model=PolicyResponse,
)
def create_policy(
    policy: PolicyRequest,
    policy_service: PolicyService = Depends(get_policy_service),
):
    return policy_service.create_policy(
        customer_id=policy.customer_id,
        product_id=policy.product_id,
        start_date=policy.start_date,
        end_date=policy.end_date,
        sum_assured=policy.sum_assured,
        premium=policy.premium,
        status=policy.status,
        dependent_ids=policy.dependent_ids,
    )


@router.put(
    "/policies/{policy_id}",
    response_model=PolicyResponse,
)
def update_policy(
    policy_id: int,
    policy: PolicyRequest,
    policy_service: PolicyService = Depends(get_policy_service),
):
    return policy_service.update_policy(
        policy_id=policy_id,
        customer_id=policy.customer_id,
        product_id=policy.product_id,
        start_date=policy.start_date,
        end_date=policy.end_date,
        sum_assured=policy.sum_assured,
        premium=policy.premium,
        status=policy.status,
        dependent_ids=policy.dependent_ids,
    )


@router.delete("/policies/{policy_id}")
def delete_policy(
    policy_id: int,
    policy_service: PolicyService = Depends(get_policy_service),
):
    return policy_service.delete_policy(policy_id)