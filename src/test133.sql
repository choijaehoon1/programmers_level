SELECT t2.ANIMAL_ID, t2.NAME
FROM ANIMAL_INS t1 right outer join ANIMAL_OUTS t2
ON t1.ANIMAL_ID = t2.ANIMAL_ID
WHERE t1.ANIMAL_ID IS NULL
ORDER BY t2.ANIMAL_ID;

