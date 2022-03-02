--In descending order, list the frequency count of employee last names, i.e., how many employees share each last name.
Select
	e.last_name,
	count(emp_no) as num_employees
From
	employees e
group by
	e.last_name
order by
	num_employees desc;
	
