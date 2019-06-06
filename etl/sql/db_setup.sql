create extension if not exists "uuid-ossp";

create or replace function generate_provider_name()
returns text as
$$
    declare
        provider_name varchar;
    begin
            select
                (array[
                    'Health',
                    'Super Care',
                    'Stellar Help',
                    'Amazing',
                    'Simple Life',
                    'True Care',
                    'Value',
                    'Trust Free',
                    'Wellness',
                    'Fresh Life',
                    'Renew',
                    'Healthy',
                    'Life Well',
                    'Smart Life',
                    'Alive',
                    'Helping Hands',
                    'City',
                    'Worlds Best',
                    'Superior Feelings',
                    'Valued Human',
                    'Real Life Help',
                    'Our Lady Of',
                    'Sunrise',
                    'Daybreak',
                    'Green Garden',
                    'Virtue',
                    'Helth Research',
                    'Innotech',
                    'Procision',
                    'Vision'
                ])[ceil(random()*30)] || ' ' || (array[
                    'Co',
                    'Hospice',
                    'LLC',
                    'Inc',
                    'Health Comapny',
                    'Hospital',
                    'Care',
                    'Clinic',
                    'Doctors',
                    'Partners',
                    'Heeling',
                    'Living Center',
                    'Rehabilitation',
                    'Group',
                    'Wellness',
                    'Urgent Care',
                    'Free Clinic',
                    'Health Center',
                    'Campus',
                    'Company',
                    'Trust',
                    'Well Clinic',
                    'Foundry',
                    'Gardens',
                    'Today Care',
                    'Corp',
                    'Corporation',
                    'Instruments',
                    'Tooling',
                    'Institute'
                ])[ceil(random()*30)]
            into provider_name;

            return provider_name;
    end;
$$ language plpgsql;
