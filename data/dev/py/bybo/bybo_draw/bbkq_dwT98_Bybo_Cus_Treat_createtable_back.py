


# DROP TABLES
sql_truncate = """ CREATE TABLE `T98_Bybo_Cus_Treat` (
Chrg_Dt date NOT NULL    DEFAULT '1900-01-01'COMMENT'收费日期',
Chrg_Sngl_Stat varchar(200) NOT NULL    DEFAULT ''COMMENT'收费单状态',
Chrg_Hour Varchar(10) NOT NULL    DEFAULT ''COMMENT'收费小时',
Comb_Pay_Ind Varchar(10) NOT NULL    DEFAULT ''COMMENT'组合付款标志',
Chrg_Typ_Cd Varchar(10) NOT NULL    DEFAULT ''COMMENT'收费类型代码',
Rtn_Fee_Typ_Cd Varchar(10) NOT NULL    DEFAULT ''COMMENT'退费类型代码',
Sell_Chnl_Cd Varchar(10) NOT NULL    DEFAULT ''COMMENT'销售渠道代码',
Chrg_Scne_Cd Varchar(10) NOT NULL    DEFAULT ''COMMENT'收费场景代码',
Fst_Choic_Pay_Md Varchar(200) NOT NULL    DEFAULT ''COMMENT'首选付款方式',
Sec_Choic_Pay_Md Varchar(200) NOT NULL    DEFAULT ''COMMENT'次选付款方式',
Oth_Pay_Md Varchar(200) NOT NULL    DEFAULT ''COMMENT'其他付款方式',
Dr_Id varchar(50) NOT NULL    DEFAULT ''COMMENT'医生编号',
Treat_Advsr_Id varchar(50) NOT NULL    DEFAULT ''COMMENT'治疗咨询师编号',
Office_Id varchar(50) NOT NULL    DEFAULT ''COMMENT'诊所编号',
Patient_Id varchar(50) NOT NULL    DEFAULT ''COMMENT'客户编号',
Patient_Fst_Lvl_Src varchar(50) NOT NULL    DEFAULT ''COMMENT'客户一级来源',
Patient_Sec_Lvl_Src varchar(50) NOT NULL    DEFAULT ''COMMENT'客户二级来源',
Patient_Thd_Lvl_Src varchar(50) NOT NULL    DEFAULT ''COMMENT'客户三级来源',
Patient_Age int NOT NULL    DEFAULT '0'COMMENT'客户就诊时年龄',
Patient_Gender varchar(10) NOT NULL    DEFAULT ''COMMENT'客户性别',
Treat_Main_Cls varchar(200) NOT NULL    DEFAULT ''COMMENT'治疗项目大类',
Treat_Sub_Cls varchar(200) NOT NULL    DEFAULT ''COMMENT'治疗项目子类',
Treat_Nm varchar(200) NOT NULL    DEFAULT ''COMMENT'治疗项目名称',
Resv_Dr_Id varchar(50) NOT NULL    DEFAULT ''COMMENT'预约医生编号',
Resv_Advsr_Id varchar(50) NOT NULL    DEFAULT ''COMMENT'预约咨询师编号',
Regi_Typ varchar(200) NOT NULL    DEFAULT ''COMMENT'挂号类型',
Sngl_Item_Discnt_Amt decimal(18,2) NOT NULL    DEFAULT '0'COMMENT'单项折扣金额',
Recvbl_Amt decimal(18,2) NOT NULL    DEFAULT '0'COMMENT'应收金额',
Recv_Amt decimal(18,2) NOT NULL    DEFAULT '0'COMMENT'实收金额',
Arrears_Amt decimal(18,2) NOT NULL    DEFAULT '0'COMMENT'欠费金额'

) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='拜博客户就诊汇总';"""
sql_P1_Rollback22099 = """

                                                            """
sql_P1_Del = """
               
                                                                        """
sql2Tmp = """

                                   """

# INSERT RECORDS str_to_date('{end_date}','%Y-%m-%d %H:%i:%s')

songplay_table_insert = ("""
insert into t98_bybo_cus_treat
(Chrg_Dt
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
)

select 
date(a.PayDateTime) as Chrg_Dt,
a.Status as Chrg_Sngl_Stat,
hour(a.PayDateTime) as Chrg_Hour ,
CASE WHEN ActualPrice2+ActualPrice3>0 THEN 1 ELSE 0 END as Comb_Pay_Ind,
a.FeeType as Chrg_Typ_Cd,
a.FeeSubType as Rtn_Fee_Typ_Cd,
a.Channel as Sell_Chnl_Cd,
a.Scenario as Chrg_Scne_Cd,
a.PayType as Fst_Choic_Pay_Md,
a.PayType2 as Sec_Choic_Pay_Md,
a.PayType3 as Oth_Pay_Md,
ifnull(b.DoctorId,'') as Dr_Id,
ifnull(b.ConsultantId ,'') as Treat_Advsr_Id,
a.OfficeId as Office_Id,
a.PatientId as Patient_Id,
ifnull(c.SourceTypeLevel1,'') as Patient_Fst_Lvl_Src,
ifnull(c.SourceTypeLevel2,'') as Patient_Sec_Lvl_Src,
ifnull(c.SourceTypeLevel3,'') as Patient_Thd_Lvl_Src,
ifnull(TIMESTAMPDIFF(YEAR,c.Birth,DATE_FORMAT(ifnull(a.PayDateTime,'0'), '%Y-%m-%d %H:%i:%s')),'')+0 as Patient_Age,
ifnull(c.Sex,'') as Patient_Gender,
ifnull(b.ItemSuperType,'') as Treat_Main_Cls,
ifnull(b.ItemSubType ,'') as Treat_Sub_Cls,
ifnull(b.ItemName,'') as Treat_Nm,
ifnull(d.DoctorId,'') as Resv_Dr_Id,
ifnull(d.ConsultantId,'') as Resv_Advsr_Id,
ifnull(d.CheckInType,'') as Regi_Typ,
ifnull(SUM(b.DiscountPrice),'0')  as  Sngl_Item_Discnt_Amt,
ifnull(SUM(b.PlanPrice),'0') as Recvbl_Amt,
ifnull(SUM(b.ActualPrice),'0') as Recv_Amt,
ifnull(SUM(CASE WHEN b.Overdue>0 THEN b.Overdue WHEN a.Overdue>0 THEN a.Overdue ELSE 0 END),'0') as Arrears_Amt
from bbkq_dw.T02_ChargeOrder_H a
left join bbkq_dw.T02_ChargeOrderDetail_H  b on a.ChargeOrderId =b.ChargeOrderId 
left join bbkq_dw.T01_Patient_H c on a.PatientId=c.PatientId  
left join bbkq_dw.T02_Appointment_H d on a.AppointmentId=d.AppointmentId
where 
a.IsInactive = 0 and a.`Status` not in ('未收费','作废并撤回','已作废') and
 d.IsCancelled = 0 and d.IsFailed = 0
-- and a.RecordUpdatedTime>='2021-01-01 14:55:11'  and a.RecordUpdatedTime<='2021-05-26 14:55:11'
group by 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26;
""")
user_table_insert = ("""
""")
song_table_insert = ("""
""")
artist_table_insert = ("""
""")
time_table_insert = ("""
""")

# FIND SONGS
song_select = ("""
""")

# QUERY LISTS


order_table_Patient = [sql_truncate]
                       # sql_P1_Rollback22099: {'begin_date': 'self.begin_date', 'end_date': 'self.end_date'},
                       # sql_P1_Del: {'begin_date': 'self.begin_date', 'end_date': 'self.end_date'},
                       # sql2Tmp:['begin_date','end_date']
order_table_1 = [songplay_table_insert]

