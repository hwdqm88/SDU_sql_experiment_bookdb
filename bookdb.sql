CREATE DATABASE bookdb;
USE bookdb;

# 这张表存放书籍信息
CREATE TABLE book
(
    `b_id`         INT PRIMARY KEY AUTO_INCREMENT,
    `b_name`       VARCHAR(255) UNIQUE NOT NULL,
    `author`       VARCHAR(255)        NOT NULL,
    `publish_date` DATE,
    `publish_name` VARCHAR(255),
    `borrowed`     BOOL DEFAULT FALSE,
    `price`        FLOAT,
    `intro`        VARCHAR(255)
);

# 这张表存放四种读者的信息
CREATE TABLE role
(
    `r_id`       INT PRIMARY KEY,
    `r_name`     VARCHAR(255),
    `max_number` INT,
    `max_day`    INT
);

INSERT INTO `role`
VALUES (1, '教师', 15, 180);
INSERT INTO `role`
VALUES (2, '研究生', 10, 180);
INSERT INTO `role`
VALUES (3, '本科生', 5, 60);
INSERT INTO `role`
VALUES (4, '其他', 5, 30);

# 这张表存放用户信息，注意外键关系
CREATE TABLE user
(
    `u_id`         INT PRIMARY KEY AUTO_INCREMENT,
    `u_name`       VARCHAR(255),
    `password`     VARCHAR(255),
    `sex`          VARCHAR(255),
    `balance`      FLOAT,
    `phone_number` VARCHAR(255),
    `r_id`         INT,
    `unit`         VARCHAR(255),
    FOREIGN KEY (`r_id`) REFERENCES `role` (`r_id`)
);

# 这张表存放管理员信息
CREATE TABLE administer
(
    `a_id`     INT PRIMARY KEY AUTO_INCREMENT,
    `a_name`   VARCHAR(255),
    `password` VARCHAR(255)
);

# 这张表存放图书借阅的信息，注意外键关系
CREATE TABLE borrow
(
    `b_id` INT NOT NULL,
    `u_id` INT NOT NULL,
    FOREIGN KEY (`b_id`) REFERENCES `book` (`b_id`),
    FOREIGN KEY (`u_id`) REFERENCES `user` (`u_id`)
);

INSERT INTO `book`
VALUES (1, '三体', '刘慈欣', '2008-01-15', '重庆出版社', 0, 59.62, '科幻名著三体');
INSERT INTO `book`
VALUES (2, '活着', '余华', '2012-08-01', '作家出版社', 0, 22.78, '经典名著活着');
INSERT INTO `book`
VALUES (3, 'C++ PRIMER PLUS', '史蒂芬·普拉达', '2015-07-01', '人民邮电出版社', 0, 120, 'C++学习必买书籍');
INSERT INTO `book`
VALUES (4, '人民日报', '人民日报社', '2021-12-01', '人民日报社', 0, 12.5, '官方报纸人民日报');
INSERT INTO `book`
VALUES (5, '资治通鉴', '司马光', '2010-08-01', '中华书局', 0, 150, '史学古籍资治通鉴');
INSERT INTO `book`
VALUES (6, '红楼梦', '曹雪芹', '1998-01-01', '中华书局', 0, 180, '经典巨著红楼梦');

INSERT INTO `administer`
VALUES (1, 'admin', 'admin');

INSERT INTO `user`
VALUES (1, '陈恒硕', 'sbchenhengshuo', '男', 0, '13604660566', 3, '吉林大学');

