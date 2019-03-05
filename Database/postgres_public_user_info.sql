create table public.user_info
(
  user_id  serial       not null
    constraint user_info_pkey
      primary key,
  username varchar(255) not null,
  password varchar(255) not null,
  name     varchar(255) not null,
  email    varchar(255) not null
);
create unique index user_info_user_name_uindex
  on user_info (username);
INSERT INTO public.user_info (user_id, username, password, name, email) VALUES (1, 'myName', 'somePass8', 'Ana Pryamechenko', 'apryvdfh@gmail.com');
INSERT INTO public.user_info (user_id, username, password, name, email) VALUES (2, 'abcd', 'password1', 'Emily Garcia', 'dkfjhfdklh@yahoo.com');
INSERT INTO public.user_info (user_id, username, password, name, email) VALUES (3, 'efgh', 'password2', 'Carly Garcia', 'xfkjhdlfkjshdf@gmail.com');
INSERT INTO public.user_info (user_id, username, password, name, email) VALUES (4, 'jgarcia', 'password3', 'Jack Garcia', 'dlfhfkjhfd@gmail.com');
INSERT INTO public.user_info (user_id, username, password, name, email) VALUES (5, 'jogarcia', 'password4', 'John Garcia', 'kjfhsk@yahoo.com');
INSERT INTO public.user_info (user_id, username, password, name, email) VALUES (6, 'jegarcia', 'password5', 'Jesus Garcia', 'dlkfjhklh@gmail.com');
INSERT INTO public.user_info (user_id, username, password, name, email) VALUES (7, 'agarcia', 'password6', 'Ana Garcia', 'dkjfhgkdlfjh@outlook.com');
INSERT INTO public.user_info (user_id, username, password, name, email) VALUES (8, 'angarcia', 'password7', 'Anne Garcia', 'dkljfhslkh@gmail.com');
INSERT INTO public.user_info (user_id, username, password, name, email) VALUES (9, 'ngarcia', 'password8', 'Nancy Garcia', 'skdjfhkh@yahoo.com');
INSERT INTO public.user_info (user_id, username, password, name, email) VALUES (10, 'lgarcia', 'password9', 'Lemon Garcia', 'skljdhfkhj@outlook.com');
INSERT INTO public.user_info (user_id, username, password, name, email) VALUES (11, 'mgarcia', 'password10', 'Magnolia Garcia', 'kdlfhgkh@gmail.com');
INSERT INTO public.user_info (user_id, username, password, name, email) VALUES (12, 'nagarcia', 'password11', 'Natasha Garcia', 'dkjfhgkh@gmail.com');
INSERT INTO public.user_info (user_id, username, password, name, email) VALUES (13, 'ngarcia1', 'password12', 'Natasha Garcia1', 'dkjfhgkh@gmail.com');
INSERT INTO public.user_info (user_id, username, password, name, email) VALUES (14, 'ngarcia2', 'password13', 'Natasha Garcia2', 'dkjfhgkh@gmail.com');
INSERT INTO public.user_info (user_id, username, password, name, email) VALUES (15, 'ngarcia3', 'password14', 'Natasha Garcia3', 'dkjfhgkh@gmail.com');
INSERT INTO public.user_info (user_id, username, password, name, email) VALUES (16, 'ngarcia4', 'password15', 'Natasha Garcia4', 'dkjfhgkh@gmail.com');
INSERT INTO public.user_info (user_id, username, password, name, email) VALUES (17, 'ngarcia5', 'password16', 'Natasha Garcia5', 'dkjfhgkh@gmail.com');
INSERT INTO public.user_info (user_id, username, password, name, email) VALUES (18, 'ngarcia6', 'password17', 'Natasha Garcia6', 'dkjfhgkh@gmail.com');
INSERT INTO public.user_info (user_id, username, password, name, email) VALUES (19, 'ngarcia7', 'password18', 'Natasha Garcia7', 'dkjfhgkh@gmail.com');
INSERT INTO public.user_info (user_id, username, password, name, email) VALUES (20, 'ngarcia8', 'password19', 'Natasha Garcia8', 'dkjfhgkh@gmail.com');
INSERT INTO public.user_info (user_id, username, password, name, email) VALUES (21, 'ngarcia9', 'password20', 'Natasha Garcia9', 'dkjfhgkh@gmail.com');
INSERT INTO public.user_info (user_id, username, password, name, email) VALUES (22, 'ngarcia10', 'password21', 'Natasha Garcia10', 'dkjfhgkh@gmail.com');
INSERT INTO public.user_info (user_id, username, password, name, email) VALUES (23, 'ngarcia11', 'password22', 'Natasha Garcia11', 'dkjfhgkh@gmail.com');
INSERT INTO public.user_info (user_id, username, password, name, email) VALUES (24, 'ngarcia12', 'password23', 'Natasha Garcia12', 'dkjfhgkh@gmail.com');
INSERT INTO public.user_info (user_id, username, password, name, email) VALUES (25, 'ngarcia13', 'password24', 'Natasha Garcia13', 'dkjfhgkh@gmail.com');
INSERT INTO public.user_info (user_id, username, password, name, email) VALUES (26, 'ngarcia14', 'password25', 'Natasha Garcia14', 'dkjfhgkh@gmail.com');
INSERT INTO public.user_info (user_id, username, password, name, email) VALUES (27, 'ngarcia15', 'password26', 'Natasha Garcia15', 'dkjfhgkh@gmail.com');
INSERT INTO public.user_info (user_id, username, password, name, email) VALUES (28, 'ngarcia16', 'password27', 'Natasha Garcia16', 'dkjfhgkh@gmail.com');
INSERT INTO public.user_info (user_id, username, password, name, email) VALUES (29, 'ngarcia17', 'password28', 'Natasha Garcia17', 'dkjfhgkh@gmail.com');
INSERT INTO public.user_info (user_id, username, password, name, email) VALUES (30, 'ngarcia18', 'password29', 'Natasha Garcia18', 'dkjfhgkh@gmail.com');
INSERT INTO public.user_info (user_id, username, password, name, email) VALUES (31, 'ngarcia19', 'password30', 'Natasha Garcia19', 'dkjfhgkh@gmail.com');
INSERT INTO public.user_info (user_id, username, password, name, email) VALUES (32, 'ngarcia20', 'password31', 'Natasha Garcia20', 'dkjfhgkh@gmail.com');
INSERT INTO public.user_info (user_id, username, password, name, email) VALUES (33, 'ngarcia21', 'password32', 'Natasha Garcia21', 'dkjfhgkh@gmail.com');
INSERT INTO public.user_info (user_id, username, password, name, email) VALUES (34, 'ngarcia22', 'password33', 'Natasha Garcia22', 'dkjfhgkh@gmail.com');
INSERT INTO public.user_info (user_id, username, password, name, email) VALUES (35, 'ngarcia23', 'password34', 'Natasha Garcia23', 'dkjfhgkh@gmail.com');
INSERT INTO public.user_info (user_id, username, password, name, email) VALUES (36, 'ngarcia24', 'password35', 'Natasha Garcia24', 'dkjfhgkh@gmail.com');
INSERT INTO public.user_info (user_id, username, password, name, email) VALUES (37, 'ngarcia25', 'password36', 'Natasha Garcia25', 'dkjfhgkh@gmail.com');
INSERT INTO public.user_info (user_id, username, password, name, email) VALUES (38, 'ngarcia26', 'password37', 'Natasha Garcia26', 'dkjfhgkh@gmail.com');
INSERT INTO public.user_info (user_id, username, password, name, email) VALUES (39, 'ngarcia27', 'password38', 'Natasha Garcia27', 'dkjfhgkh@gmail.com');
INSERT INTO public.user_info (user_id, username, password, name, email) VALUES (40, 'ngarcia28', 'password39', 'Natasha Garcia28', 'dkjfhgkh@gmail.com');
INSERT INTO public.user_info (user_id, username, password, name, email) VALUES (41, 'ngarcia29', 'password40', 'Natasha Garcia29', 'dkjfhgkh@gmail.com');
INSERT INTO public.user_info (user_id, username, password, name, email) VALUES (42, 'ngarcia30', 'password41', 'Natasha Garcia30', 'dkjfhgkh@gmail.com');
INSERT INTO public.user_info (user_id, username, password, name, email) VALUES (43, 'ngarcia31', 'password42', 'Natasha Garcia31', 'dkjfhgkh@gmail.com');
INSERT INTO public.user_info (user_id, username, password, name, email) VALUES (44, 'ngarcia32', 'password43', 'Natasha Garcia32', 'dkjfhgkh@gmail.com');
INSERT INTO public.user_info (user_id, username, password, name, email) VALUES (45, 'ngarcia33', 'password44', 'Natasha Garcia33', 'dkjfhgkh@gmail.com');
INSERT INTO public.user_info (user_id, username, password, name, email) VALUES (46, 'ngarcia34', 'password45', 'Natasha Garcia34', 'dkjfhgkh@gmail.com');
INSERT INTO public.user_info (user_id, username, password, name, email) VALUES (47, 'ngarcia35', 'password46', 'Natasha Garcia35', 'dkjfhgkh@gmail.com');
INSERT INTO public.user_info (user_id, username, password, name, email) VALUES (48, 'ngarcia36', 'password47', 'Natasha Garcia36', 'dkjfhgkh@gmail.com');
INSERT INTO public.user_info (user_id, username, password, name, email) VALUES (49, 'ngarcia37', 'password48', 'Natasha Garcia37', 'dkjfhgkh@gmail.com');
INSERT INTO public.user_info (user_id, username, password, name, email) VALUES (50, 'ngarcia38', 'password49', 'Natasha Garcia38', 'dkjfhgkh@gmail.com');
