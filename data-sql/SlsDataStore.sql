CREATE TABLE user_detail (
    name               VARCHAR(100) NOT NULL,
    email              VARCHAR(100) NOT NULL,
    password           VARCHAR(100) NOT NULL
);

ALTER TABLE user_detail ADD CONSTRAINT user_detail_pk primary key(email);



CREATE TABLE user_qna (
    email              VARCHAR(100) NOT NULL,
    qna                VARCHAR(5000) NOT NULL
);

ALTER TABLE user_qna ADD CONSTRAINT user_qna_pk primary key(email);



CREATE TABLE qna (
    id                VARCHAR(51) NOT NULL,
    question          VARCHAR(512) NOT NULL
);

ALTER TABLE qna ADD CONSTRAINT qna_pk primary key(id);