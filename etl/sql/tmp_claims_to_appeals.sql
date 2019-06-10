drop table if exists tmp_holistic_appeals;
drop table if exists tmp_l1;
drop table if exists tmp_l12;
drop table if exists tmp_l123;
drop table if exists tmp_l1234;

create table if not exists
    tmp_l1
as
    select
        data.*
    from ((
        select
            appeal_number as lvl1_appeal_number,
            null as lvl2_appeal_number
        from
            lvl1_appeals
        group by
            appeal_number
    ) union (
        select
            lvl1_appeal_number,
            lvl2_appeal_number
        from
            lvl2_appeals_lvl1_related
        group by
            lvl1_appeal_number,
            lvl2_appeal_number
    ) union (
        select
            lvl1_appeal_number,
            lvl2_appeal_number
        from
            lvl3_appeals_lvl1_related
        group by
            lvl1_appeal_number,
            lvl2_appeal_number
    ) union (
        select
            lvl1_appeal_number,
            lvl2_appeal_number
        from
            lvl4_appeals_lvl1_related
        group by
            lvl1_appeal_number,
            lvl2_appeal_number
    )) as data;

create table if not exists
    tmp_l12
as
    select
        l1.lvl1_appeal_number,
        l2.*
    from ((
        select
            appeal_number as lvl2_appeal_number,
            null as lvl3_appeal_number
        from
            lvl2_appeals
        group by
            appeal_number
    ) union (
        select
            lvl2_appeal_number,
            null as lvl3_appeal_number
        from
            lvl3_appeals_lvl2_related
        group by
            lvl2_appeal_number
    ) union (
        select
            lvl2_appeal_number,
            lvl3_appeal_number
        from
            lvl4_appeals_lvl2_related
        group by
            lvl2_appeal_number,
            lvl3_appeal_number
    )) l2 full outer join tmp_l1 l1 using (lvl2_appeal_number);

create table if not exists
    tmp_l123
as
    select
        l12.lvl1_appeal_number,
        l12.lvl2_appeal_number,
        l3.*
    from ((
        select
            reconsider_number as lvl3_appeal_number,
            null as lvl4_appeal_number
        from
            lvl3_appeals
        group by
            reconsider_number
    ) union (
        select
            lvl3_appeal_number,
            null as lvl4_appeal_number
        from
            lvl4_appeals_lvl3_related
        group by
            lvl3_appeal_number,
            lvl4_appeal_number
    )) l3 full outer join tmp_l12 l12 using (lvl3_appeal_number);

create table if not exists
    tmp_l1234
as
    select
        l123.lvl1_appeal_number,
        l123.lvl2_appeal_number,
        l123.lvl3_appeal_number,
        l4.lvl4_appeal_number
    from (
        select
            l4.lvl4_docket_number as lvl4_appeal_number,
            l3.lvl3_appeal_number
        from
            lvl4_appeals_lvl3_related l3 left join lvl4_appeals l4 using (lvl3_appeal_number)
        group by
            l4.lvl4_docket_number,
            l3.lvl3_appeal_number
    ) l4 full outer join tmp_l123 l123 using (lvl3_appeal_number);


create table if not exists
    tmp_holistic_appeals
as
    select
        uuid_generate_v4() as id,
        tmp_l1234.*
    from
        tmp_l1234
    group by
        lvl1_appeal_number,
        lvl2_appeal_number,
        lvl3_appeal_number,
        lvl4_appeal_number;

update
    tmp_claims
set
    holistic_appeal_id = tmp_holistic_appeals.id
from
    tmp_holistic_appeals
where
    tmp_claims.lvl1_appeal_number = tmp_holistic_appeals.lvl1_appeal_number;

update
    tmp_claims
set
    holistic_appeal_id = tmp_holistic_appeals.id
from
    tmp_holistic_appeals
where
    tmp_claims.lvl2_appeal_number = tmp_holistic_appeals.lvl2_appeal_number;

update
    tmp_claims
set
    holistic_appeal_id = tmp_holistic_appeals.id
from
    tmp_holistic_appeals
where
    tmp_claims.lvl3_appeal_number = tmp_holistic_appeals.lvl3_appeal_number;

update
    tmp_appeals
set
    holistic_appeal_id = tmp_holistic_appeals.id
from
    tmp_holistic_appeals
where
    tmp_appeals.original_appeal_id = tmp_holistic_appeals.lvl1_appeal_number;

update
    tmp_appeals
set
    holistic_appeal_id = tmp_holistic_appeals.id
from
    tmp_holistic_appeals
where
    tmp_appeals.original_appeal_id = tmp_holistic_appeals.lvl2_appeal_number;

update
    tmp_appeals
set
    holistic_appeal_id = tmp_holistic_appeals.id
from
    tmp_holistic_appeals
where
    tmp_appeals.original_appeal_id = tmp_holistic_appeals.lvl3_appeal_number;

update
    tmp_appeals
set
    holistic_appeal_id = tmp_holistic_appeals.id
from
    tmp_holistic_appeals
where
    tmp_appeals.original_appeal_id = tmp_holistic_appeals.lvl4_appeal_number;
