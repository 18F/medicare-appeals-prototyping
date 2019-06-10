update
    tmp_claims
set
    appellant_id = appellant_mapping.alt_appellant_id,
    appellant_uuid = appellant_mapping.id,
    appellant_name = appellant_mapping.appellant_name
from
    appellant_mapping
where
    tmp_claims.appellant_id = appellant_mapping.appellant_id;

update
    tmp_claims
set
    original_claim_id = claim_id_mapping.alt_original_claim_id
from
    claim_id_mapping
where
    tmp_claims.original_claim_id = claim_id_mapping.original_claim_id;

update
    tmp_claims
set
    national_provider_id = provider_id_mapping.alt_national_provider_id,
    provider_uuid = provider_id_mapping.id
from
    provider_id_mapping
where
    tmp_claims.national_provider_id = provider_id_mapping.national_provider_id;

update
    tmp_claims
set
    provider_name = provider_name_mapping.alt_provider_name
from
    provider_name_mapping
where
    tmp_claims.provider_name = provider_name_mapping.provider_name;

update
    tmp_claims
set
    reviewer_name = reviewer_mapping.alt_reviewer_name
from
    reviewer_mapping
where
    tmp_claims.reviewer_name = reviewer_mapping.reviewer_name;

update
    tmp_appeals
set
    reviewer_name = reviewer_mapping.alt_reviewer_name
from
    reviewer_mapping
where
    tmp_appeals.reviewer_name = reviewer_mapping.reviewer_name;

update
    tmp_procedure_codes
set
    original_claim_id = claim_id_mapping.alt_original_claim_id
from
    claim_id_mapping
where
    tmp_procedure_codes.original_claim_id = claim_id_mapping.original_claim_id;
