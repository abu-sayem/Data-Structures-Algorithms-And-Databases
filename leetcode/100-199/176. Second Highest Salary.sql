select max(Salary) as SecondHighestSalary
from Employee
where Salary <> (Select max(Salary) from Employee);
