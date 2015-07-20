----------------------------------------------------------------
--- Model: Interceptee

-- START-QUERY
SELECT id, kind, interception_record_id, full_name, trim(district), trim(vdc)
FROM dataentry_interceptee
ORDER BY id;
-- END-QUERY old interceptee

----------------------------------------------------------------
-- Model: VictimInterview
-- District only

SELECT vif_number,
	   victim_address_district,
	   victim_guardian_address_district
FROM dataentry_victiminterview
order by vif_number;

-- VDC only
SELECT vif_number,
	   victim_address_vdc
	   victim_guardian_address_vdc
FROM dataentry_victiminterview
order by vif_number;

-- District and VDC
-- START-QUERY
SELECT vif_number,
	   victim_address_district,
	   victim_address_vdc,
	   victim_guardian_address_district,
	   victim_guardian_address_vdc
FROM dataentry_victiminterview
order by vif_number;
-- END-QUERY old district-vdc

----------------------------------------------------------------
-- Model: VictimInterviewPersonBox

-- START-QUERY
select id,
	   victim_interview_id,
	   address_district,
	   address_vdc
from dataentry_victiminterviewpersonbox
order by id;
-- END-QUERY old person-box

----------------------------------------------------------------
-- Model: VictimInterviewLocationBox

-- START-QUERY
select id,
	   victim_interview_id,
	   district,
	   vdc
from dataentry_victiminterviewlocationbox
order by id;
-- END-QUERY old location-box

