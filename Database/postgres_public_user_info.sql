CREATE TABLE public.user_info
(
    user_id integer DEFAULT nextval('user_info_user_id_seq'::regclass) PRIMARY KEY NOT NULL,
    username varchar(255) NOT NULL,
    password varchar(255) NOT NULL,
    name varchar(255) NOT NULL,
    email varchar(255) NOT NULL
);
CREATE UNIQUE INDEX user_info_user_name_uindex ON public.user_info (username);
INSERT INTO public.user_info (user_id, username, password, name, email) VALUES (1, 'myName', 'somePass8', 'Ana Pryamechenko', 'apryvdfh@gmail.com');