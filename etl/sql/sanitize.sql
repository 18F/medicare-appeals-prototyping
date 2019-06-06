update
    tmp_claims
set
   appellant_id = appellant_mapping.alt_appellant_id
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
    national_provider_id = provider_id_mapping.alt_national_provider_id
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
