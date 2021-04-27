Select Name as Employee From Employee a
where a.Salary > (Select Salary From Employee b Where a.ManagerId=b.Id)

#Self join
Select b.name from employee a
inner join Employee b on b.managerid = a.Id
where b.salary > a.salary
