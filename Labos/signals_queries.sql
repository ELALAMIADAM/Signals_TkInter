.headers on
.mode column

SELECT * FROM signals;
-- SELECT * FROM samples;

-- .print "1) echantillons du signal 'X'"
-- SELECT * 
-- FROM signals,samples
-- WHERE signals.signal_id=samples.signal_id
--   AND signals.signal_id='X';
-- .print "1) echantillons du signal 'X'"
-- SELECT * 
-- FROM signals  NATURAL  JOIN samples
-- WHERE signal_id='X';
