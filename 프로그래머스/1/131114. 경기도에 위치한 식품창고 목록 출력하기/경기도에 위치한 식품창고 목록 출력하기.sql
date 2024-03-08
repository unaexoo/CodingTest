-- 코드를 입력하세요
SELECT warehouse_id, warehouse_name, address, NVL(freezer_yn, 'N')
FROM food_warehouse
WHERE SUBSTR(address,INSTR(address,'_'),2) ='경기'
ORDER BY 1;