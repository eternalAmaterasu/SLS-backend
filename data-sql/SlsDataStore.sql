CREATE TABLE user_detail (
    email              VARCHAR(100) NOT NULL,
    name               VARCHAR(100) NOT NULL,
    password           VARCHAR(100) NOT NULL
);

ALTER TABLE user_detail ADD CONSTRAINT user_detail_pk primary key(email);


CREATE TABLE qna (
    id                VARCHAR(51) NOT NULL,
    question          VARCHAR(512) NOT NULL,
    options           VARCHAR(100)
);

ALTER TABLE qna ADD CONSTRAINT qna_pk primary key(id);


CREATE TABLE answers (
    email             VARCHAR(100) NOT NULL REFERENCES user_detail (email),
    id                VARCHAR(51) NOT NULL REFERENCES qna (id),
    response          VARCHAR(100)
);