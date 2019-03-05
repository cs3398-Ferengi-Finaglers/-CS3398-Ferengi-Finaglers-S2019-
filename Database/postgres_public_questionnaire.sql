CREATE TABLE public.questionnaire
(
    user_id integer DEFAULT nextval('questionnaire_used_id_seq'::regclass) PRIMARY KEY NOT NULL,
    question1 char NOT NULL,
    question2 char NOT NULL,
    question3 char NOT NULL,
    question4 char NOT NULL,
    question5 char NOT NULL,
    question6 char NOT NULL,
    question7 char NOT NULL,
    question8 char NOT NULL,
    question9 char NOT NULL,
    question10 char NOT NULL
);
INSERT INTO public.questionnaire (user_id, question1, question2, question3, question4, question5, question6, question7, question8, question9, question10) VALUES (1, 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A');