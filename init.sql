
-- users definition

CREATE TABLE users (
	email TEXT,
	password TEXT,
	display_name TEXT,
    user_id TEXT
);

INSERT INTO users (display_name, email, password) VALUES ('test', 'test@example.com' , 'test')
