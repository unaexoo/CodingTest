-- 코드를 입력하세요
SELECT a.category, SUM(b.sales) TOTAL_SALES
FROM book a, book_sales b
WHERE TO_CHAR(b.sales_date,'MM') = '01'
AND a.book_id = b.book_id
GROUP BY a.category
ORDER BY 1;