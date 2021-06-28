


# DROP TABLES
T98_Bybo_CRM_Patient_Card_sql_create= """ CREATE TABLE IF NOT EXISTS T98_Bybo_CRM_Patient_Card(
Card_Code varchar(50) NOT NULL    DEFAULT ''COMMENT'卡券编码',
Sell_Prc decimal(18,2) NOT NULL    DEFAULT '0'COMMENT'售价',
Card_Extnl_Sell_Prc_Amt decimal(18,2) NOT NULL    DEFAULT '0'COMMENT'卡券外部售价金额',
Cust_Card_Bind_Dt date NOT NULL   DEFAULT '1900-01-01'COMMENT'客户卡券绑定日期',
Cust_CRM_Nm varchar(50) NOT NULL    DEFAULT ''COMMENT'客户CRM姓名',
Cust_Ekanya_Id varchar(50) NOT NULL    DEFAULT ''COMMENT'客户E看牙编号',
Cust_Belg_OfficeId  varchar(50) NOT NULL    DEFAULT ''COMMENT'客户所属门店编号',
Cust_CRM_Id varchar(50) NOT NULL    DEFAULT ''COMMENT'客户CRM编号',
InDm_timestamp datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '进入DM的时间'
)ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='拜博CRM卡券';"""
# Treat_sql_create_detail_tmp= """ """
# Treat_sql_create_tmp= """  """

# Cus_Treat_dtail_tmp_truncate= """ 	 """
# Cus_Treat_dtail_tmp_insert= """ """
# Cus_Treat_tmp_truncate= """"""
#
# # INSERT RECORDS str_to_date('{end_date}','%Y-%m-%d %H:%i:%s')

Cus_Treat_insert_tmp = """"""
T98_Bybo_CRM_Patient_Card_del = """ delete from  bbkq_dm.T98_Bybo_CRM_Patient_Card where Cust_Card_Bind_Dt >='{self.begin_date}'  and Cust_Card_Bind_Dt<='{self.end_date}'"""
T98_Bybo_CRM_Patient_Card_insert="""
insert into T98_Bybo_CRM_Patient_Card (
Card_Code
,Sell_Prc
,Card_Extnl_Sell_Prc_Amt
,Cust_Card_Bind_Dt
,Cust_CRM_Nm
,Cust_Ekanya_Id
,Cust_Belg_OfficeId
,Cust_CRM_Id
,InDm_timestamp)

select 
a.CardNo as Card_Code
,ifnull(c.SalePrice,'0') as Sell_Prc
,a.ExternalPrice as Card_Extnl_Sell_Prc_Amt
,a.CreatedOnDate as Cust_Card_Bind_Dt
,ifnull(d.Name,'') as Cust_CRM_Nm
,ifnull(d.PatientId,'') as Cust_Ekanya_Id
,ifnull(f.OfficeId,'') as Cust_Belg_OfficeId 
,ifnull(a.AccountId,'') as Cust_CRM_Id
,now() as InDm_timestamp
from bbkq_dw.T01_Patient_Card_H a 
left join bbkq_dw.T04_Card_H b on a.CardNo=b.CardNo
left join bbkq_dw.T03_Template_H c on b.TemplateId=c.TemplateId
left join bbkq_dw.T01_PotentialCustomer_H d on a.AccountId=d.AccountId
left join bbkq_dw.T01_Promoter_H e on a.TransactorID=e.PromoterId
left join bbkq_dw.T01_Provider_H f on e.ProviderId=f.ProviderId
where
a.CreatedOnDate BETWEEN '{self.begin_date}'  and '{self.end_date}' and
a.AccountId is not null and 
(a.ExternalPrice<'200000'  or a.ExternalPrice is null) and 
a.statecode =0 and a.statuscode =1;

"""

# QUERY LISTS
# T98_Bybo_CRM_Patient_Card_sql_create=""""""


T98_Bybo_CRM_Patient_Card_Create = [T98_Bybo_CRM_Patient_Card_sql_create]
                       # sql_P1_Rollback22099: {'begin_date': 'self.begin_date', 'end_date': 'self.end_date'},
                       # sql_P1_Del: {'begin_date': 'self.begin_date', 'end_date': 'self.end_date'},
                       # sql2Tmp:['begin_date','end_date']
T98_Bybo_CRM_Patient_Card_Treat = [T98_Bybo_CRM_Patient_Card_del,T98_Bybo_CRM_Patient_Card_insert]

