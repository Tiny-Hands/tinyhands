----------------------------------------------------------------
--- Model: Interceptee

-- START-QUERY
select interceptee.id, interceptee.kind,
	   interceptee.interception_record_id,
	   interceptee.full_name,
	   district.id,
	   district.name as district_name,
	   vdc.id,
	   vdc.name as vdc_name
from dataentry_interceptee as interceptee
left outer join dataentry_district as district
	 on interceptee.district_id = district.id
left outer join dataentry_vdc as vdc
	 on interceptee.vdc_id = vdc.id
order by interceptee.id;
-- END-QUERY interceptee

----------------------------------------------------------------
-- Model: District
-- START-QUERY
select * from dataentry_district order by id;
-- END-QUERY district

----------------------------------------------------------------
-- Model: VDC
-- START-QUERY
select * from dataentry_vdc order by id;
-- END-QUERY vdc

----------------------------------------------------------------
-- Model: VictimInterview

-- District only
select vif_number,
	   -- va_dist.id,
	   va_dist.name,
	   -- vg_dist.id,
	   vg_dist.name
from dataentry_victiminterview as VIF
left outer join dataentry_district as va_dist
	 on va_dist.id = VIF.victim_address_district_id
left outer join dataentry_district as vg_dist
	 on vg_dist.id = VIF.victim_guardian_address_district_id
order by vif_number;

-- VDC only
select vif_number,
	   -- va_vdc.id,
	   va_vdc.name,
	   -- vg_vdc.id,
	   vg_vdc.name
from dataentry_victiminterview as VIF
left outer join dataentry_vdc as va_vdc
	 on va_vdc.id = VIF.victim_address_vdc_id
left outer join dataentry_vdc as vg_vdc
	 on vg_vdc.id = VIF.victim_guardian_address_vdc_id
order by vif_number;

-- District and VDC
-- START-QUERY
select vif_number,
	   "VA",
	   va_dist.id,
	   va_dist.name,
	   va_vdc.id,
	   va_vdc.name,
	   "VG",
	   vg_dist.id,
	   vg_dist.name,
	   vg_vdc.id,
	   vg_vdc.name
from dataentry_victiminterview as VIF
left outer join dataentry_district as va_dist
	 on va_dist.id = VIF.victim_address_district_id
left outer join dataentry_vdc as va_vdc
	 on va_vdc.id = VIF.victim_address_vdc_id
left outer join dataentry_district as vg_dist
	 on vg_dist.id = VIF.victim_guardian_address_district_id
left outer join dataentry_vdc as vg_vdc
	 on vg_vdc.id = VIF.victim_guardian_address_vdc_id
order by vif_number;
-- END-QUERY district-vdc

----------------------------------------------------------------
-- Model: VictimInterviewPersonBox

-- START-QUERY
select pbox.id,
	   pbox.victim_interview_id,
	   -- dist.id,
	   dist.name,
	   -- vdc.id,
	   vdc.name
from dataentry_victiminterviewpersonbox as pbox
left outer join dataentry_district as dist
	 on dist.id = pbox.address_district_id
left outer join dataentry_vdc as vdc
	 on vdc.id = pbox.address_vdc_id
order by pbox.id;
-- END-QUERY person-box

----------------------------------------------------------------
-- Model: VictimInterviewLocationBox

-- START-QUERY
select lbox.id,
	   lbox.victim_interview_id,
	   -- dist.id,
	   dist.name,
	   -- vdc.id,
	   vdc.name
from dataentry_victiminterviewlocationbox as lbox
left outer join dataentry_district as dist
	 on dist.id = lbox.district_id
left outer join dataentry_vdc as vdc
	 on vdc.id = lbox.vdc_id
order by lbox.id;
-- END-QUERY location-box
