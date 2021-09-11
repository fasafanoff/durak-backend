CREATE TABLE IF NOT EXISTS users (
                                   login text UNIQUE,
                                   password blob,
                                   avatar blob,
                                   reg_date integer,
                                   id INTEGER PRIMARY KEY
                                      );

CREATE TABLE IF NOT EXISTS tokens (token text,
                                    login text)