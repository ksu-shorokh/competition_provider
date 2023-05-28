-- DROP SCHEMA public;

CREATE SCHEMA public AUTHORIZATION pg_database_owner;

COMMENT ON SCHEMA public IS 'standard public schema';
-- public."Клубы" definition

-- Drop table

-- DROP TABLE public."Клубы";

CREATE TABLE public."Клубы" (
	код_клуба int2 NOT NULL,
	название_клуба varchar(100) NULL,
	адрес varchar(200) NULL,
	контактная_информация varchar(50) NULL,
	директор varchar(60) NULL,
	CONSTRAINT "Клубы_pkey" PRIMARY KEY ("код_клуба")
);

-- Permissions

ALTER TABLE public."Клубы" OWNER TO postgres;
GRANT ALL ON TABLE public."Клубы" TO postgres;


-- public."Место_проведения" definition

-- Drop table

-- DROP TABLE public."Место_проведения";

CREATE TABLE public."Место_проведения" (
	код_места int2 NOT NULL,
	город varchar(30) NULL,
	адрес varchar(200) NULL,
	CONSTRAINT "Место_проведения_pkey" PRIMARY KEY ("код_места")
);

-- Permissions

ALTER TABLE public."Место_проведения" OWNER TO postgres;
GRANT ALL ON TABLE public."Место_проведения" TO postgres;


-- public."Программы" definition

-- Drop table

-- DROP TABLE public."Программы";

CREATE TABLE public."Программы" (
	код_программы int2 NOT NULL,
	название_программы varchar(40) NULL,
	количество_человек int2 NULL,
	CONSTRAINT "Программы_pkey" PRIMARY KEY ("код_программы")
);

-- Permissions

ALTER TABLE public."Программы" OWNER TO postgres;
GRANT ALL ON TABLE public."Программы" TO postgres;


-- public."Спортивные_разряды" definition

-- Drop table

-- DROP TABLE public."Спортивные_разряды";

CREATE TABLE public."Спортивные_разряды" (
	код_разряда int2 NOT NULL,
	название_разряда varchar(40) NULL,
	CONSTRAINT "Спортивные_разряды_pkey" PRIMARY KEY ("код_разряда")
);

-- Permissions

ALTER TABLE public."Спортивные_разряды" OWNER TO postgres;
GRANT ALL ON TABLE public."Спортивные_разряды" TO postgres;


-- public."Тренеры" definition

-- Drop table

-- DROP TABLE public."Тренеры";

CREATE TABLE public."Тренеры" (
	код_тренера int2 NOT NULL,
	фио varchar(100) NULL,
	дата_рождения date NULL,
	звание varchar(100) NULL,
	CONSTRAINT "Тренеры_pkey" PRIMARY KEY ("код_тренера")
);

-- Permissions

ALTER TABLE public."Тренеры" OWNER TO postgres;
GRANT ALL ON TABLE public."Тренеры" TO postgres;


-- public."Участники" definition

-- Drop table

-- DROP TABLE public."Участники";

CREATE TABLE public."Участники" (
	код_участника int2 NOT NULL,
	фи varchar(100) NULL,
	дата_рождения date NULL,
	статус bool NULL,
	CONSTRAINT "Участники_pkey" PRIMARY KEY ("код_участника")
);

-- Permissions

ALTER TABLE public."Участники" OWNER TO postgres;
GRANT ALL ON TABLE public."Участники" TO postgres;


-- public."График_соревнований" definition

-- Drop table

-- DROP TABLE public."График_соревнований";

CREATE TABLE public."График_соревнований" (
	код_соревнований int2 NOT NULL,
	название_соревнования varchar(100) NULL,
	код_места int2 NULL,
	уровень_соревнования varchar(40) NULL,
	дата_начала date NULL,
	дата_окончания date NULL,
	допуск_разрядов varchar(40) NULL,
	программы_и_количество_участников varchar(100) NULL,
	дополнительная_информация varchar(200) NULL,
	CONSTRAINT "График_соревнований_pkey" PRIMARY KEY ("код_соревнований"),
	CONSTRAINT "График_соревнований_код_места_fkey" FOREIGN KEY (код_места) REFERENCES public."Место_проведения"(код_места)
);

-- Permissions

ALTER TABLE public."График_соревнований" OWNER TO postgres;
GRANT ALL ON TABLE public."График_соревнований" TO postgres;


-- public."Результаты" definition

-- Drop table

-- DROP TABLE public."Результаты";

CREATE TABLE public."Результаты" (
	код_результата int2 NOT NULL,
	код_соревнований int2 NULL,
	код_участника int2 NULL,
	код_тренера int2 NULL,
	код_клуба int2 NULL,
	код_программы int2 NULL,
	код_разряда int2 NULL,
	сумма_баллов numeric NULL,
	место int2 NULL,
	CONSTRAINT "Результаты_pkey" PRIMARY KEY ("код_результата"),
	CONSTRAINT "Результаты_код_клуба_fkey" FOREIGN KEY (код_клуба) REFERENCES public."Клубы"(код_клуба),
	CONSTRAINT "Результаты_код_программы_fkey" FOREIGN KEY (код_программы) REFERENCES public."Программы"(код_программы),
	CONSTRAINT "Результаты_код_разряда_fkey" FOREIGN KEY (код_разряда) REFERENCES public."Спортивные_разряды"(код_разряда),
	CONSTRAINT "Результаты_код_соревнований_fkey" FOREIGN KEY (код_соревнований) REFERENCES public."График_соревнований"(код_соревнований),
	CONSTRAINT "Результаты_код_тренера_fkey" FOREIGN KEY (код_тренера) REFERENCES public."Тренеры"(код_тренера),
	CONSTRAINT "Результаты_код_участника_fkey" FOREIGN KEY (код_участника) REFERENCES public."Участники"(код_участника)
);

-- Permissions

ALTER TABLE public."Результаты" OWNER TO postgres;
GRANT ALL ON TABLE public."Результаты" TO postgres;




-- Permissions

GRANT ALL ON SCHEMA public TO pg_database_owner;
GRANT USAGE ON SCHEMA public TO public;
