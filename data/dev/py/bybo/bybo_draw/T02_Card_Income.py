


# DROP TABLES
T02_Card_Income_sql_create= """ CREATE TABLE IF NOT EXISTS T02_Card_Income(

DEPT_NAME varchar(50)  NULL    DEFAULT ''COMMENT'事业部',
Abbreviation varchar(50)  NULL    DEFAULT ''COMMENT'门店',
privateid varchar(50)  NULL    DEFAULT ''COMMENT'病案号',
Name varchar(50)  NULL    DEFAULT ''COMMENT'客户姓名',
Birth date  NULL    DEFAULT ''COMMENT'出生日期',
RecordCreatedTime  varchar(50)  NULL    DEFAULT ''COMMENT'缴费时间',
new_transaction_no varchar(50)  NULL    DEFAULT ''COMMENT'账单号',
new_rights_type  varchar(50)  NULL    DEFAULT ''COMMENT'卡类型',
new_card_template_idName  varchar(50)  NULL    DEFAULT ''COMMENT'卡名称',
new_card_channelsName varchar(50)  NULL    DEFAULT ''COMMENT'电商名称',
new_card_no varchar(50)  NULL    DEFAULT ''COMMENT'卡号',
new_external_price decimal(18.2)  NULL    DEFAULT ''COMMENT'原外部售价',
new_external_price1 decimal(18.2)  NULL    DEFAULT ''COMMENT'外部售价',
new_sale_price decimal(18.2)  NULL    DEFAULT ''COMMENT'内部售价',
new_group_code varchar(50)  NULL    DEFAULT ''COMMENT'组号',
new_bybo_items_idname varchar(50)  NULL    DEFAULT ''COMMENT'权益核销项目',
ItemSuperType varchar(50)  NULL    DEFAULT ''COMMENT'项目大类',
itemname  varchar(50)  NULL    DEFAULT ''COMMENT'项目名称',
ItemSubCategory varchar(50)  NULL    DEFAULT ''COMMENT'产品大类',
new_card_saleprice varchar(50)  NULL    DEFAULT ''COMMENT'权益单价',
FeeType  varchar(50)  NULL    DEFAULT ''COMMENT'操作',
PayDateTime datetime  NULL    DEFAULT ''COMMENT'划扣时间',
DeductionCode varchar(50)  NULL    DEFAULT ''COMMENT'划扣编码',
StepName varchar(50)  NULL    DEFAULT ''COMMENT'划扣步骤',
count varchar(50)  NULL    DEFAULT ''COMMENT'划扣比例',
DoctorName varchar(50)  NULL    DEFAULT ''COMMENT'划扣医生姓名',
NurseName varchar(50)  NULL    DEFAULT ''COMMENT'护士',
ConsultantName varchar(50)  NULL    DEFAULT ''COMMENT'咨询师',
ActualPrice decimal(18.2)  NULL    DEFAULT ''COMMENT'卡券划扣金额',
InDw_timestamp datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '进入DW的时间',
Partitions_ID int NOT NULL DEFAULT 0 COMMENT '分区键',
SourceName varchar(50) NOT NULL DEFAULT '' COMMENT '数据源'
)
ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='卡券划扣收入'；

)
ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='卡券划扣收入';"""
T02_Card_Income_sql_create_detail_tmp= """ """
T02_Card_Income_sql_create_tmp= """CREATE TABLE IF NOT EXISTS T02_Card_Income_tmp(

DEPT_NAME varchar(50)  NULL    DEFAULT ''COMMENT'事业部',
Abbreviation varchar(50)  NULL    DEFAULT ''COMMENT'门店',
privateid varchar(50)  NULL    DEFAULT ''COMMENT'病案号',
Name varchar(50)  NULL    DEFAULT ''COMMENT'客户姓名',
Birth date  NULL    DEFAULT ''COMMENT'出生日期',
RecordCreatedTime  varchar(50)  NULL    DEFAULT ''COMMENT'缴费时间',
new_transaction_no varchar(50)  NULL    DEFAULT ''COMMENT'账单号',
new_rights_type  varchar(50)  NULL    DEFAULT ''COMMENT'卡类型',
new_card_template_idName  varchar(50)  NULL    DEFAULT ''COMMENT'卡名称',
new_card_channelsName varchar(50)  NULL    DEFAULT ''COMMENT'电商名称',
new_card_no varchar(50)  NULL    DEFAULT ''COMMENT'卡号',
new_external_price decimal(18.2)  NULL    DEFAULT ''COMMENT'原外部售价',
new_external_price1 decimal(18.2)  NULL    DEFAULT ''COMMENT'外部售价',
new_sale_price decimal(18.2)  NULL    DEFAULT ''COMMENT'内部售价',
new_group_code varchar(50)  NULL    DEFAULT ''COMMENT'组号',
new_bybo_items_idname varchar(50)  NULL    DEFAULT ''COMMENT'权益核销项目',
ItemSuperType varchar(50)  NULL    DEFAULT ''COMMENT'项目大类',
itemname  varchar(50)  NULL    DEFAULT ''COMMENT'项目名称',
ItemSubCategory varchar(50)  NULL    DEFAULT ''COMMENT'产品大类',
new_card_saleprice varchar(50)  NULL    DEFAULT ''COMMENT'权益单价',
FeeType  varchar(50)  NULL    DEFAULT ''COMMENT'操作',
PayDateTime datetime  NULL    DEFAULT ''COMMENT'划扣时间',
DeductionCode varchar(50)  NULL    DEFAULT ''COMMENT'划扣编码',
StepName varchar(50)  NULL    DEFAULT ''COMMENT'划扣步骤',
count varchar(50)  NULL    DEFAULT ''COMMENT'划扣比例',
DoctorName varchar(50)  NULL    DEFAULT ''COMMENT'划扣医生姓名',
NurseName varchar(50)  NULL    DEFAULT ''COMMENT'护士',
ConsultantName varchar(50)  NULL    DEFAULT ''COMMENT'咨询师',
ActualPrice decimal(18.2)  NULL    DEFAULT ''COMMENT'卡券划扣金额',

)
ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='卡券划扣收入' """

T02_Card_Income_dtail_tmp_truncate= """truncate bbkq_dm.T98_Bybo_Cus_Treat_ChDetail_tmp; 	 
"""
T02_Card_Income_dtail_tmp_insert= """         
"""
T02_Card_Income_tmp_truncate= """truncate bbkq_dw.T02_Card_Income_tmp; 	 
"""

# INSERT RECORDS str_to_date('{end_date}','%Y-%m-%d %H:%i:%s')

T02_Card_Income_insert_tmp = """insert into bbkq_dw.T02_Card_Income_tmp
()

"""
T02_Card_Income_del = """delete from t98_bybo_cus_treat
where Chrg_Dt>='{self.begin_date}'  and Chrg_Dt<='{self.end_date}'
"""
T02_Card_Income_insert="""
insert into T98_Bybo_Cus_Treat
(
Resv_Id
,Chrg_Ordr_Id
,Chrg_Ordr_Dtl_Id
,Prpd_Card_TX_Rec_Id
,Chrg_Dt
,Chrg_Sngl_Stat
,Chrg_Hour
,Comb_Pay_Ind
,Chrg_Typ_Cd
,Rtn_Fee_Typ_Cd
,Sell_Chnl_Cd
,Chrg_Scne_Cd
,Fst_Choic_Pay_Md
,Sec_Choic_Pay_Md
,Oth_Pay_Md
,Dr_Id
,Treat_Advsr_Id
,Office_Id
,Patient_Id
,Patient_Fst_Lvl_Src
,Patient_Sec_Lvl_Src
,Patient_Thd_Lvl_Src
,Patient_Age
,Patient_Gender
,Treat_Main_Cls
,Treat_Sub_Cls
,Treat_Nm
,Resv_Dr_Id
,Resv_Advsr_Id
,Regi_Typ
,Sngl_Item_Discnt_Amt
,Recvbl_Amt
,Recv_Amt
,Arrears_Amt
,Card_Comut
,Biz_Amt_Memb
,InDM_timestamp)
select 
Resv_Id
,Chrg_Ordr_Id
,Chrg_Ordr_Dtl_Id
,Prpd_Card_TX_Rec_Id
,Chrg_Dt
,Chrg_Sngl_Stat
,Chrg_Hour
,Comb_Pay_Ind
,Chrg_Typ_Cd
,Rtn_Fee_Typ_Cd
,Sell_Chnl_Cd
,Chrg_Scne_Cd
,Fst_Choic_Pay_Md
,Sec_Choic_Pay_Md
,Oth_Pay_Md
,Dr_Id
,Treat_Advsr_Id
,Office_Id
,Patient_Id
,Patient_Fst_Lvl_Src
,Patient_Sec_Lvl_Src
,Patient_Thd_Lvl_Src
,Patient_Age
,Patient_Gender
,Treat_Main_Cls
,Treat_Sub_Cls
,Treat_Nm
,Resv_Dr_Id
,Resv_Advsr_Id
,Regi_Typ

,sum(Sngl_Item_Discnt_Amt)
,sum(Recvbl_Amt)
,sum(Recv_Amt)
,sum(Arrears_Amt)
,sum(Card_Comut)
,sum(Biz_Amt_Memb)
,now() as InDm_timestamp

from T98_Bybo_Cus_Treat_tmp
group by 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30;
        """

# QUERY LISTS
T98_Bybo_CRM_Patient_Card_sql_create=""""""










T02_Card_Income_Create = [T02_Card_Income_sql_create,T02_Card_Income_sql_create_tmp]
                       # sql_P1_Rollback22099: {'begin_date': 'self.begin_date', 'end_date': 'self.end_date'},
                       # sql_P1_Del: {'begin_date': 'self.begin_date', 'end_date': 'self.end_date'},
                       # sql2Tmp:['begin_date','end_
# T02_Card_Income = [Cus_Treat_dtail_tmp_truncate,Cus_Treat_dtail_tmp_insert,Cus_Treat_tmp_truncate,Cus_Treat_insert_tmp,Cus_Treat_del,Cus_Treat_insert




# ]

