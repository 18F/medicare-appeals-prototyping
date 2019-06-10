truncate claim cascade;
truncate holistic_appeal cascade;
truncate appellant cascade;
truncate provider cascade;
truncate appeal cascade;
truncate level cascade;
truncate status cascade;
truncate appeal_to_claim cascade;

insert into claim
select
    distinct on (tc.id)
    tc.id,
    null as description,
    tc.original_claim_id,
    tc.appellant_appeal_category as claim_type,
    tpc.code as code,
    tc.appellant_appeal_category as service_place,
    coalesce(tc.amount_billed, 0.0) as amount_paid,
    coalesce(tc.amount_paid, 0.0) as amount_paid,
    coalesce(tc.amount_controversy, 0.0) as amount_controversy,
    now() at time zone 'utc' as created_at,
    now() at time zone 'utc' as updated_at
from
    tmp_claims tc left join tmp_procedure_codes tpc using (original_claim_id);

insert into holistic_appeal
select
    distinct on (holistic_appeal_id)
    holistic_appeal_id as id,
    now() at time zone 'utc' as created_at,
    now() at time zone 'utc' as updated_at
from
    tmp_claims;

insert into appellant
select
    distinct on (appellant_uuid)
    appellant_uuid as id,
    null as description,
    appellant_type,
    appellant_id as medicare_beneficiary_id,
    appellant_name as name,
    now() at time zone 'utc' as created_at,
    now() at time zone 'utc' as updated_at
from
    tmp_claims;

insert into provider
select
    distinct on (provider_uuid)
    provider_uuid as id,
    'A medicare provider' as description,
    appellant_appeal_category as provider_type,
    national_provider_id,
    provider_name as name,
    now() at time zone 'utc' as created_at,
    now() at time zone 'utc' as updated_at
from
    tmp_claims;

insert into appeal
select
    distinct on (lvl1_appeal_number)
    uuid_generate_v4() as id,
    level as description,
    lvl1_appeal_number as original_appeal_id,
    appellant_medicare_type as medicare_part,
    appellant_type as requestor_type,
    appellant_appeal_category as service_category,
    now() at time zone 'utc' as created_at,
    now() at time zone 'utc' as updated_at,
    appellant_uuid as appellant_id,
    holistic_appeal_id,
    provider_uuid as provider_id,
    coalesce(appellant_rac, 'false'::boolean) as rac
from
    tmp_claims
where
    lvl1_appeal_number is not null and
    appellant_uuid is not null and
    provider_uuid is not null;

insert into appeal
select
    distinct on (lvl2_appeal_number)
    uuid_generate_v4() as id,
    level as description,
    lvl2_appeal_number as original_appeal_id,
    appellant_medicare_type as medicare_part,
    appellant_type as requestor_type,
    appellant_appeal_category as service_category,
    now() at time zone 'utc' as created_at,
    now() at time zone 'utc' as updated_at,
    appellant_uuid as appellant_id,
    holistic_appeal_id,
    provider_uuid as provider_id,
    coalesce(appellant_rac, 'false'::boolean) as rac
from
    tmp_claims
where
    lvl2_appeal_number is not null and
    appellant_uuid is not null and
    provider_uuid is not null;

insert into appeal
select
    distinct on (lvl3_appeal_number)
    uuid_generate_v4() as id,
    level as description,
    lvl3_appeal_number as original_appeal_id,
    appellant_medicare_type as medicare_part,
    appellant_type as requestor_type,
    appellant_appeal_category as service_category,
    now() at time zone 'utc' as created_at,
    now() at time zone 'utc' as updated_at,
    appellant_uuid as appellant_id,
    holistic_appeal_id,
    provider_uuid as provider_id,
    coalesce(appellant_rac, 'false'::boolean) as rac
from
    tmp_claims
where
    lvl3_appeal_number is not null and
    appellant_uuid is not null and
    provider_uuid is not null;

insert into appeal
select
    uuid_generate_v4() as id,
    level as description,
    ta.original_appeal_id,
    a.medicare_part,
    a.requestor_type,
    a.service_category,
    now() at time zone 'utc' as created_at,
    now() at time zone 'utc' as updated_at,
    a.appellant_id,
    a.holistic_appeal_id,
    a.provider_id,
    'false'::boolean as rac
from
    appeal a inner join tmp_appeals ta using (holistic_appeal_id)
where
    a.original_appeal_id != ta.original_appeal_id;

insert into level
select
    distinct on (tc.lvl1_appeal_number)
    uuid_generate_v4() as id,
    tc.level as level_name,
    null as description,
    tc.reviewer_name,
    tc.reviewer_type,
    tc.location,
    now() at time zone 'utc' as created_at,
    now() at time zone 'utc' as updated_at,
    a.id as appeal_id,
    a.holistic_appeal_id
from
    appeal a inner join tmp_claims tc on a.original_appeal_id = tc.lvl1_appeal_number;

insert into level
select
    distinct on (tc.lvl2_appeal_number)
    uuid_generate_v4() as id,
    tc.level as level_name,
    null as description,
    tc.reviewer_name,
    tc.reviewer_type,
    tc.location,
    now() at time zone 'utc' as created_at,
    now() at time zone 'utc' as updated_at,
    a.id as appeal_id,
    a.holistic_appeal_id
from
    appeal a inner join tmp_claims tc on a.original_appeal_id = tc.lvl2_appeal_number;

insert into level
select
    distinct on (tc.lvl3_appeal_number)
    uuid_generate_v4() as id,
    tc.level as level_name,
    null as description,
    tc.reviewer_name,
    tc.reviewer_type,
    tc.location,
    now() at time zone 'utc' as created_at,
    now() at time zone 'utc' as updated_at,
    a.id as appeal_id,
    a.holistic_appeal_id
from
    appeal a inner join tmp_claims tc on a.original_appeal_id = tc.lvl3_appeal_number;

insert into level
select
    distinct on (ta.original_appeal_id)
    uuid_generate_v4() as id,
    ta.level as level_name,
    null as description,
    ta.reviewer_name,
    ta.reviewer_type,
    ta.location,
    now() at time zone 'utc' as created_at,
    now() at time zone 'utc' as updated_at,
    a.id as appeal_id,
    a.holistic_appeal_id
from
    (
        select
            aa.id,
            aa.original_appeal_id,
            aa.holistic_appeal_id
        from
           appeal aa left join level l on aa.id = l.appeal_id
        where
            l.appeal_id is null
    ) a inner join tmp_appeals ta using (original_appeal_id);

insert into status
select
    uuid_generate_v4() as id,
    null as description,
    tc.category,
    tc.action,
    tc.created_at,
    now() at time zone 'utc' as updated_at,
    a.id as appeal_id
from ((
    select
        unnest(array[
            lvl1_appeal_number,
            lvl2_appeal_number,
            lvl3_appeal_number
        ]) as original_appeal_id,
        'Open' as category,
        'Initiated' as action,
        status_open_date as created_at
    from
        tmp_claims
) union (
     select
        unnest(array[
            lvl1_appeal_number,
            lvl2_appeal_number,
            lvl3_appeal_number
        ]) as original_appeal_id,
        'Closed' as category,
        status_closed_action as action,
        status_closed_date as created_at
    from
        tmp_claims
    where
        status_closed_action is not null
)) tc inner join appeal a using (original_appeal_id)
where
    tc.created_at is not null;

insert into status
select
    uuid_generate_v4() as id,
    null as description,
    ta.category,
    ta.action,
    ta.created_at,
    now() at time zone 'utc' as updated_at,
    a.id as appeal_id
from (
    select
        aa.id,
        aa.original_appeal_id,
        aa.holistic_appeal_id
    from
        appeal aa left join status s on aa.id = s.appeal_id
    where
        s.appeal_id is null
) a inner join ((
    select
        original_appeal_id,
        'Open' as category,
        status_closed_action as action,
        status_open_date as created_at
    from
        tmp_appeals
    where
        status_open_date is not null and
        status_closed_date is null and
        status_closed_action not ilike '%close%'
) union (
    select
        original_appeal_id,
        'Open' as category,
        'Initiated' as action,
        status_open_date - '6 month'::interval as created_at
    from
        tmp_appeals
    where
        status_open_date is not null and
        status_closed_date is null and
        status_closed_action ilike '%close%'
) union (
    select
        original_appeal_id,
        'Closed' as category,
        status_closed_action as action,
        status_open_date as created_at
    from
        tmp_appeals
    where
        status_open_date is not null and
        status_closed_date is null and
        status_closed_action ilike '%close%'
) union (
    select
        original_appeal_id,
        'Open' as category,
        'Initiated' as action,
        status_open_date as created_at
    from
        tmp_appeals
    where
        status_open_date is not null and
        status_closed_date is not null
) union (
    select
        original_appeal_id,
        'Closed' as category,
        status_closed_action as action,
        status_closed_date as created_at
    from
        tmp_appeals
    where
        status_open_date is not null and
        status_closed_date is not null
) union (
    select
        original_appeal_id,
        'Open' as category,
        'Initiated' as action,
        status_closed_date  - '6 month'::interval as created_at
    from
        tmp_appeals
    where
        status_open_date is null and
        status_closed_date is not null
) union (
    select
        original_appeal_id,
        'Closed' as category,
        coalesce(status_closed_action, 'Favorable') as action,
        status_closed_date as created_at
    from
        tmp_appeals
    where
        status_open_date is null and
        status_closed_date is not null
) union (
    select
        original_appeal_id,
        'Open' as category,
        'Initiated' as action,
        now() at time zone 'utc' - '12 month'::interval as created_at
    from
        tmp_appeals
    where
        status_open_date is null and
        status_closed_date is null
) union (
    select
        original_appeal_id,
        'Open' as category,
        coalesce(status_closed_action, 'Favorable') as action,
        now() at time zone 'utc' - '6 month'::interval as created_at
    from
        tmp_appeals
    where
        status_open_date is null and
        status_closed_date is null
)) as ta using (original_appeal_id);


insert into appeal_to_claim
select
    uuid_generate_v4() as id,
    now() at time zone 'utc' as created_at,
    now() at time zone 'utc' as updated_at,
    tc.appeal_id,
    c.id as claim_id
from (
    select
        c.original_claim_id,
        c.original_appeal_id,
        a.id as appeal_id
    from
        (
            select
                unnest(array[
                    lvl1_appeal_number,
                    lvl2_appeal_number,
                    lvl3_appeal_number
                ]) as original_appeal_id,
                original_claim_id
            from
                tmp_claims
        ) c inner join appeal a using (original_appeal_id)
) as tc inner join claim c using (original_claim_id);

insert into appeal_to_claim
select
    uuid_generate_v4() as id,
    now() at time zone 'utc' as created_at,
    now() at time zone 'utc' as updated_at,
    nc.appeal_id,
    ac.claim_id
from (
    select
        a.id as appeal_id,
        a.holistic_appeal_id
    from
        appeal a left join appeal_to_claim atc on a.id = atc.appeal_id
    where
        atc is null
) nc inner join (
    select
        a.id as appeal_id,
        a.holistic_appeal_id,
        atc.claim_id
    from
        appeal a inner join appeal_to_claim atc on a.id = atc.appeal_id
) ac using (holistic_appeal_id)
where
    ac.appeal_id != nc.appeal_id;
