drop table if exists appellant_mapping;
drop table if exists claim_id_mapping;
drop table if exists provider_id_mapping;
drop table if exists provider_name_mapping;

create table if not exists
    appellant_mapping
as
    select
        distinct on (data.appellant_id)
        data.appellant_id as appellant_id,
        substring(uuid_generate_v4()::text from 1 for 12) as alt_appellant_id
    from
        tmp_claims as data;

create table if not exists
    claim_id_mapping
as
    select
        distinct on (data.original_claim_id)
        data.original_claim_id as original_claim_id,
        substring(uuid_generate_v4()::text from 1 for 18) as alt_original_claim_id
    from
        tmp_claims as data;

create table if not exists
    provider_id_mapping
as
    select
        distinct on (data.national_provider_id)
        data.national_provider_id as national_provider_id,
        substring(uuid_generate_v4()::text from 1 for 12) as alt_national_provider_id,
        data.provider_name
    from
        tmp_claims as data;

create table if not exists
    provider_name_mapping
as
    select
        distinct on (data.provider_name)
        data.provider_name,
        generate_provider_name() as alt_provider_name
    from
        tmp_claims as data;
