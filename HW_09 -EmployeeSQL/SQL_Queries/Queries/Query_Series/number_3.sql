select 
	d.dept_no, 
	d.dept_name, 
	e.emp_no, 
	e.last_name, 
	e.first_name
from 
	departments as d
	join employees as e on d.dept_no = d.dept_no;
