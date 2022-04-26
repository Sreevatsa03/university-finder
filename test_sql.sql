use universities;

select c.name as club_name, c.type, u.name as university_name from club as c
	join university as u
		on c.university = u.federal_school_code
	order by university_name;
        
select n.first_name, n.last_name, n.occupation, n.est_net_worth, n.graduating_class, u.name as university_name from notable_alum as n
	join university as u
		on n.university = u.federal_school_code
	order by university_name;
    
select d.name, d.num_students, u.name as university_name from department as d
	join university as u
		on d.university = u.federal_school_code
	order by university_name;