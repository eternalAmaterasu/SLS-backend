CREATE TABLE user_detail (
    email              VARCHAR(100) NOT NULL,
    name               VARCHAR(100) NOT NULL,
    password           VARCHAR(100) NOT NULL
);

ALTER TABLE user_detail ADD CONSTRAINT user_detail_pk primary key(email);


CREATE TABLE qna(
    id                VARCHAR(51) NOT NULL,
    question          VARCHAR(512) NOT NULL,
    options           VARCHAR(100)
);

ALTER TABLE qna
    ADD CONSTRAINT qna_pk primary key (id);


CREATE TABLE answers
(
    email    VARCHAR(100) NOT NULL REFERENCES user_detail (email),
    id       VARCHAR(51)  NOT NULL REFERENCES qna (id),
    response VARCHAR(100)
);

insert into qna(id, question, options)
values ('1', 'Are you a working professional?', '["Yes", "No"]');
insert into qna(id, question, options)
values ('2', 'Are you a student?', '["Yes", "No"]');
insert into qna(id, question, options)
values ('3', 'Do you wear formals for meetings?', '["Yes", "No"]');
insert into qna(id, question, options)
values ('4', 'Are you a party animal?', '["Yes", "No"]');
insert into qna(id, question, options)
values ('5', 'Are you a colorful person? You like mixing things up?', '["Yes", "No"]');
insert into qna(id, question, options)
values ('6', 'Do you consider yourself to be a cross-dresser?', '["Yes", "No"]');
insert into qna(id, question, options)
values ('7', 'Do you like to go heavy on the accessories?', '["Yes", "No"]');
insert into qna(id, question, options)
values ('8', 'Do you like to go heavy on the accessories?', '["Yes", "No", "occasionally"]');
insert into qna(id, question, options)
values ('9', 'Do you consider yourself to be picky with your clothes?', '["Yes", "No"]');
insert into qna(id, question, options)
values ('10', 'Do you consider yourself to be picky with your clothes?', '["Yes", "No"]');
insert into qna(id, question, options)
values ('11', 'Do you care about fashion over comfort?', '["Yes", "No"]');
insert into qna(id, question, options)
values ('12', 'Do you care about comfort over fashion?', '["Yes", "No"]');
insert into qna(id, question, options)
values ('13', 'Do you consider yourself to be a trend-setter or you are a follower?', '["Trend-setter", "Follower"]');
insert into qna(id, question, options)
values ('14', 'Who is your fashion icon?', '');
insert into qna(id, question, options)
values ('15', 'Do you wake up early in the morning?', '["Yes", "No"]');
insert into qna(id, question, options)
values ('16', 'At what time do you wake up in the morning?', '');
insert into qna(id, question, options)
values ('17', 'Would you like suggestions for religious events (must allow permission for calendar)?', '["Yes", "No"]');
insert into qna(id, question, options)
values ('18', 'Which religion do you follow?', '');
insert into qna(id, question, options)
values ('19', 'Is your calendar organized?', '["Yes", "No"]');