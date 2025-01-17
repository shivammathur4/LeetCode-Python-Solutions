# Write your MySQL query statement below
Select v.customer_id,COUNT(v.visit_id) as count_no_trans
from Visits as v 
LEFT JOIN Transactions as t
ON v.visit_id = t.visit_id
where transaction_id IS NULL
GROUP BY customer_id