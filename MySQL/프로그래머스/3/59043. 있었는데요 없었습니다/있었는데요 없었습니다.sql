SELECT ins.ANIMAL_ID, ins.name
FROM ANIMAL_INS as ins
JOIN ANIMAL_OUTS as outs
ON ins.ANIMAL_ID = outs.ANIMAL_ID
WHERE outs.DATETIME < ins.DATETIME
ORDER BY ins.DATETIME ASC