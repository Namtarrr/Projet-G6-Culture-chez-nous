--------------------------------------------------------
--  Fichier créé - vendredi-janvier-17-2025   
--------------------------------------------------------
--------------------------------------------------------
--  DDL for Table REGION
--------------------------------------------------------

  CREATE TABLE "BDN3992A"."REGION" 
   (	"codeReg" VARCHAR2(5 BYTE), 
	"nomReg" VARCHAR2(50 BYTE), 
	"numdep" VARCHAR2(5 BYTE)
   ) SEGMENT CREATION IMMEDIATE 
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255 
 NOCOMPRESS LOGGING
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS" ;
REM INSERTING into BDN3992A.REGION
SET DEFINE OFF;
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('28','Normandie','50');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('44','Grand Est','51');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('44','Grand Est','52');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('52','Pays de la Loire','53');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('44','Grand Est','54');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('44','Grand Est','55');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('53','Bretagne','56');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('44','Grand Est','57');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('27','Bourgogne-Franche-Comté','58');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('32','Hauts-de-France','59');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('32','Hauts-de-France','60');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('28','Normandie','61');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('32','Hauts-de-France','62');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('84','Auvergne-Rhône-Alpes','63');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('75','Nouvelle-Aquitaine','64');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('76','Occitanie','65');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('76','Occitanie','66');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('44','Grand Est','67');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('44','Grand Est','68');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('84','Auvergne-Rhône-Alpes','69');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('27','Bourgogne-Franche-Comté','70');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('84','Auvergne-Rhône-Alpes','01');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('32','Hauts-de-France','02');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('84','Auvergne-Rhône-Alpes','03');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('93','Provence-Alpes-Côte d Azur','04');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('93','Provence-Alpes-Côte d Azur','05');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('93','Provence-Alpes-Côte d Azur','06');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('84','Auvergne-Rhône-Alpes','07');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('44','Grand Est','08');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('76','Occitanie','09');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('44','Grand Est','10');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('76','Occitanie','11');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('76','Occitanie','12');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('93','Provence-Alpes-Côte d Azur','13');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('28','Normandie','14');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('84','Auvergne-Rhône-Alpes','15');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('75','Nouvelle-Aquitaine','16');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('75','Nouvelle-Aquitaine','17');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('24','Centre-Val de Loire','18');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('75','Nouvelle-Aquitaine','19');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('27','Bourgogne-Franche-Comté','21');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('53','Bretagne','22');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('75','Nouvelle-Aquitaine','23');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('75','Nouvelle-Aquitaine','24');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('27','Bourgogne-Franche-Comté','25');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('84','Auvergne-Rhône-Alpes','26');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('27','Bourgogne-Franche-Comté','71');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('52','Pays de la Loire','72');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('84','Auvergne-Rhône-Alpes','73');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('84','Auvergne-Rhône-Alpes','74');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('11','Île-de-France','75');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('28','Normandie','76');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('11','Île-de-France','77');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('11','Île-de-France','78');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('75','Nouvelle-Aquitaine','79');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('32','Hauts-de-France','80');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('76','Occitanie','81');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('76','Occitanie','82');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('93','Provence-Alpes-Côte d Azur','83');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('93','Provence-Alpes-Côte d Azur','84');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('52','Pays de la Loire','85');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('75','Nouvelle-Aquitaine','86');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('75','Nouvelle-Aquitaine','87');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('44','Grand Est','88');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('27','Bourgogne-Franche-Comté','89');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('27','Bourgogne-Franche-Comté','90');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('11','Île-de-France','91');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('11','Île-de-France','92');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('11','Île-de-France','93');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('11','Île-de-France','94');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('11','Île-de-France','95');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('1','Guadeloupe','971');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('2','Martinique','972');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('3','Guyane','973');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('4','La Réunion','974');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('6','Mayotte','976');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('0','Collectivités d outre-mer','987');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('0','Collectivités d outre-mer','988');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('28','Normandie','27');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('24','Centre-Val de Loire','28');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('53','Bretagne','29');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('94','Corse','2A');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('94','Corse','2B');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('76','Occitanie','30');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('76','Occitanie','31');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('76','Occitanie','32');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('75','Nouvelle-Aquitaine','33');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('76','Occitanie','34');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('53','Bretagne','35');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('24','Centre-Val de Loire','36');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('24','Centre-Val de Loire','37');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('84','Auvergne-Rhône-Alpes','38');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('27','Bourgogne-Franche-Comté','39');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('75','Nouvelle-Aquitaine','40');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('24','Centre-Val de Loire','41');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('84','Auvergne-Rhône-Alpes','42');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('84','Auvergne-Rhône-Alpes','43');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('52','Pays de la Loire','44');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('24','Centre-Val de Loire','45');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('76','Occitanie','46');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('75','Nouvelle-Aquitaine','47');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('76','Occitanie','48');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('52','Pays de la Loire','49');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('0','Collectivités d outre-mer','984');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('0','Collectivités d outre-mer','986');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('0','Collectivités d outre-mer','989');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('0','Collectivités d outre-mer','978');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('0','Collectivités d outre-mer','975');
Insert into BDN3992A.REGION ("codeReg","nomReg","numdep") values ('0','Collectivités d outre-mer','977');
--------------------------------------------------------
--  DDL for Index SYS_C002000706
--------------------------------------------------------

  CREATE UNIQUE INDEX "BDN3992A"."SYS_C002000706" ON "BDN3992A"."REGION" ("numdep") 
  PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS" ;
--------------------------------------------------------
--  Constraints for Table REGION
--------------------------------------------------------

  ALTER TABLE "BDN3992A"."REGION" MODIFY ("codeReg" NOT NULL ENABLE);
  ALTER TABLE "BDN3992A"."REGION" ADD PRIMARY KEY ("numdep")
  USING INDEX PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS"  ENABLE;
