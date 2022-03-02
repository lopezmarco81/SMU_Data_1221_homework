--List the following details of each employee: employee number, last name, first name, sex, and salary.

Select
	s.emp_no,
	s.salary,
	e.emp_no,
	e.last_name,
	e.first_name,
	e.gender
from
	employees e
	join salaries s on e.emp_no = s.emp_no
order by
	salary desc;
