alter session set "_ORACLE_SCRIPT"=true;
create user c##mascota identified by mascota;
grant connect, resource to c##mascota;
alter user c##mascota default tablespace users quota unlimited on users