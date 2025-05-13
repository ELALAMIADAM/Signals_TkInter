DROP TABLE IF EXISTS signals;
CREATE TABLE signals (
  signal_id CHAR(3) PRIMARY KEY,
  frequency FLOAT,
  amplitude FLOAT,
  phase FLOAT
);

DROP TABLE IF EXISTS samples;
CREATE TABLE samples (
  signal_id CHAR(3),
  x INTEGER,
  y INTEGER,
  FOREIGN KEY (signal_id) REFERENCES signals
);

