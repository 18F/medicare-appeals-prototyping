drop table if exists provider_mapping;
drop table if exists appellant_mapping;

create table if not exists
    provider_mapping
as
    select
        distinct on (data.national_provider_id)
        data.national_provider_id as national_provider_id,
        uuid_generate_v4()::text as alt_national_provider_id,
        data.provider_name
    from
        tmp_claims as data;

create table if not exists
    appellant_mapping
as
    select
        distinct on (data.appellant_id)
        data.appellant_id as appellant_id,
        uuid_generate_v4()::text as alt_appellant_id
    from
        tmp_claims as data;
