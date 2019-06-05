update
    tmp_claims
set
    national_provider_id = provider_mapping.alt_national_provider_id
from
    provider_mapping
where
    tmp_claims.national_provider_id = provider_mapping.national_provider_id;

update
    tmp_claims
set
   appellant_id = appellant_mapping.alt_appellant_id
from
    appellant_mapping
where
    tmp_claims.appellant_id = appellant_mapping.appellant_id;
