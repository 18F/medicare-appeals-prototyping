drop table if exists tmp_lvl3_appeals;
drop table if exists tmp_lvl2_appeals;
drop table if exists tmp_lvl1_appeals;
truncate appeal cascade;

create table if not exists
    tmp_lvl3_appeals
as
    select
        distinct on (data.lvl3_appeal_number)
        data.*
    from
    ((
        select
            null as lvl4_appeal_number,
            reconsider_number as lvl3_appeal_number,
            'lvl3_appeals' as table_name
        from
            lvl3_appeals
    ) union (
        select
            l4.lvl4_docket_number as lvl4_appeal_number,
            l3.lvl3_appeal_number,
            'lvl4_appeals_lvl3_related' as table_name
        from
            lvl4_appeals_lvl3_related l3 inner join lvl4_appeals l4 using (lvl3_appeal_number)
    )) as data
    where
        data.lvl3_appeal_number is not null;

create table if not exists
    tmp_lvl2_appeals
as
    select
        data.*
    from
    ((
        select
            appeal_number as lvl2_appeal_number,
            null as lvl3_appeal_number,
            'lvl2_appeals' as table_name
        from
            lvl2_appeals
    ) union (
        select
            lvl2_appeal_number,
            null as lvl3_appeal_number,
            'lvl3_appeals_lvl2_related' as table_name
        from
            lvl3_appeals_lvl2_related
    ) union (
        select
            lvl2_appeal_number,
            lvl3_appeal_number,
            'lvl4_appeals_lvl2_related' as table_name
        from
            lvl4_appeals_lvl2_related
    )) as data
    where
        lvl2_appeal_number is not null;

create table if not exists
    tmp_lvl1_appeals
as
    select
        data.*
    from
    ((
        select
            appeal_number as lvl1_appeal_number,
            null as lvl2_appeal_number,
            'lvl1_appeals' as table_name
        from
            lvl1_appeals
    ) union (
        select
            lvl1_appeal_number,
            lvl2_appeal_number,
            'lvl2_appeals_lvl1_related' as table_name
        from
            lvl2_appeals_lvl1_related
    ) union (
        select
            lvl1_appeal_number,
            lvl2_appeal_number,
            'lvl3_appeals_lvl1_related' as table_name
        from
            lvl3_appeals_lvl1_related
    ) union (
        select
            lvl1_appeal_number,
            lvl2_appeal_number,
            'lvl4_appeals_lvl1_related' as table_name
        from
            lvl4_appeals_lvl1_related
    )) as data
    where
        lvl1_appeal_number is not null;
