CREATE SCHEMA bookdb;
USE bookdb;

CREATE TABLE `book` (
    `id` INT PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(255),
    `author` VARCHAR(255),
    `publish_date` DATE,
    `publish_name` VARCHAR(255),
    `borrowed` BOOL,
    `price` float,
    `intro` VARCHAR(255)
);

CREATE TABLE `role` (
    `id` INT,
    `role_name` VARCHAR(255),
    `max_number` INT,
    `max_day` INT
);

INSERT INTO `role` VALUES (1, '教师', 15, 180);
INSERT INTO `role` VALUES (2, '研究生', 10, 180);
INSERT INTO `role` VALUES (3, '本科生', 5, 60);
INSERT INTO `role` VALUES (4, '其他', 5, 30);

CREATE TABLE `user`  (
  `id` int primary key auto_increment,
  `user_name` varchar(255),
  `password` varchar(255),
  `sex` varchar(255),
  `balance` float,
  `phone_number` varchar(255),
  `role_id` int,
  `unit` varchar(255)
);

create table administor(
	`id` int primary key auto_increment,
    `name` varchar(255),
    `password` varchar(255)
);

SET FOREIGN_KEY_CHECKS = 1;

insert into book values(1,'三体','刘慈欣','2008-01-15','重庆出版社',0,59.62,'科幻名著三体');
insert into book values(2,'活着','余华','2012-08-01','作家出版社',0,22.78,'经典名著活着');
insert into book values(3,'C++ Primer Plus','史蒂芬·普拉达','2015-07-01','人民邮电出版社',0,120,'C++学习必买书籍');
insert into book values(4,'人民日报','人民日报社','2021-12-01','人民日报社',0,12.5,'官方报纸人民日报');
insert into book values(5,'资治通鉴','司马光','2010-08-01','中华书局',0,150,'史学古籍资治通鉴');
insert into book values(6,'红楼梦','曹雪芹','1998-01-01','中华书局',0,180,'经典巨著红楼梦');

insert into administor values(1,'admin','admin');

insert into `user` values(1,'陈恒硕','sbchenhengshuo','男',0,'13604660566',3,'吉林大学');