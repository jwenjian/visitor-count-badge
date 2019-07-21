-- Table: public.total_count_record

-- DROP TABLE public.total_count_record;

CREATE TABLE public.total_count_record
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 0 MAXVALUE 2147483647 CACHE 1 ),
    repo_id character(255) COLLATE pg_catalog."default" NOT NULL,
    count integer NOT NULL DEFAULT 0,
    CONSTRAINT total_count_record_pkey PRIMARY KEY (id)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

-- Index: u_idx_repo_id

-- DROP INDEX public.u_idx_repo_id;

CREATE UNIQUE INDEX u_idx_repo_id
    ON public.total_count_record USING btree
    (repo_id COLLATE pg_catalog."default")
    TABLESPACE pg_default;

COMMENT ON INDEX public.u_idx_repo_id
    IS 'unique index for repo_id';
-- Table: public.current_day_count_record

-- DROP TABLE public.current_day_count_record;

CREATE TABLE public.current_day_count_record
(
    visit_date character(8) COLLATE pg_catalog."default" NOT NULL,
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    repo_id character(255) COLLATE pg_catalog."default" NOT NULL,
    count integer NOT NULL DEFAULT 0
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;


COMMENT ON TABLE public.current_day_count_record
    IS 'table for visitor count only in current day';

COMMENT ON COLUMN public.current_day_count_record.visit_date
    IS 'visit date in format: YYYYMMDD';

-- Index: u_idx_repo_id_visit_date

-- DROP INDEX public.u_idx_repo_id_visit_date;

CREATE UNIQUE INDEX u_idx_repo_id_visit_date
    ON public.current_day_count_record USING btree
    (visit_date COLLATE pg_catalog."default", repo_id COLLATE pg_catalog."default")
    TABLESPACE pg_default;

COMMENT ON INDEX public.u_idx_repo_id_visit_date
    IS 'make repo_id and visit_date unique';
