use universities;

DELIMITER $$
create procedure search_by_name
(
	name_p varchar(30)
)
begin
    if not exists (select * from university where name = name_p) then
		select "There are no schools with that name in the database." as message;
	else
		select * from university where name = name_p;
	end if;
end $$
DELIMITER ;

DELIMITER $$
create procedure search_by_federal_school_code
(
	federal_school_code_p varchar(6)
)
begin
	if not exists (select * from university where federal_school_code = federal_school_code_p) then
		select "There are no schools with that federal school code in the database." as message;
	else 
		select * from university where federal_school_code = federal_school_code_p;
	end if;
end $$
DELIMITER ;

-- drop procedure search_by_name;
-- drop procedure search_by_federal_school_code;

-- SAMPLE DATA
-- insert into location values("NJ", "Princeton", 31000, "democratic", "summer: 59-85 F; winter: 21-50 F");
-- insert into university values("002627", "Princeton University", 70, TRUE, 56010, 61928, 1505, "computer science", 1, 5321, 600, FALSE, 5.6, "NJ", "Princeton");

-- delete from university where name = "Princeton University";

-- call search_by_name("Princeton University");

-- call search_by_federal_school_code("002627");