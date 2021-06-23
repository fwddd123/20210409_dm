


# DROP TABLES
Treat_sql_create= """ CREATE TABLE IF NOT EXISTS `T98_Bybo_Cus_Treat` (
Resv_Id varchar(50) NOT NULL    DEFAULT ''COMMENT'预约编号',
Chrg_Ordr_Id varchar(50) NOT NULL    DEFAULT ''COMMENT'收费单编号',
Chrg_Ordr_Dtl_Id varchar(50) NOT NULL    DEFAULT ''COMMENT'收费单明细编号',
Prpd_Card_TX_Rec_Id varchar(50) NOT NULL    DEFAULT ''COMMENT'储值卡交易记录编号 ',
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
Arrears_Amt decimal(18,2) NOT NULL    DEFAULT '0'COMMENT'欠费金额',
Card_Comut decimal(18,2) NOT NULL    DEFAULT '0'COMMENT'卡券抵扣金额',
Biz_Amt_Memb decimal(18.2) NOT NULL    DEFAULT '0'COMMENT'储值卡营业额',
InDm_timestamp datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '进入DM的时间'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='拜博客户就诊汇总临时表';"""
Treat_sql_create_detail_tmp= """ create table IF NOT EXISTS T98_Bybo_Cus_Treat_ChDetail_tmp 
 (chargeorderid varchar(50) NOT NULL    DEFAULT ''COMMENT'',
Region  varchar(50) NOT NULL    DEFAULT ''COMMENT'',
GroupIndex   int NOT NULL    DEFAULT '0'COMMENT'',
ItemGroupIndex int NOT NULL    DEFAULT '0'COMMENT'',
RecordVersion  int NOT NULL    DEFAULT '0'COMMENT'')
ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='拜博客户就诊汇总detail临时表';"""
Treat_sql_create_tmp= """ -- 建立临时表
CREATE TABLE IF NOT EXISTS `T98_Bybo_Cus_Treat_tmp` (
Resv_Id varchar(50) NOT NULL    DEFAULT ''COMMENT'预约编号',
Chrg_Ordr_Id varchar(50) NOT NULL    DEFAULT ''COMMENT'收费单编号',
Chrg_Ordr_Dtl_Id varchar(50) NOT NULL    DEFAULT ''COMMENT'收费单明细编号',
Prpd_Card_TX_Rec_Id varchar(50) NOT NULL    DEFAULT ''COMMENT'储值卡交易记录编号 ',
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
Arrears_Amt decimal(18,2) NOT NULL    DEFAULT '0'COMMENT'欠费金额',
Card_Comut decimal(18,2) NOT NULL    DEFAULT '0'COMMENT'卡券抵扣金额',
Biz_Amt_Memb decimal(18.2) NOT NULL    DEFAULT '0'COMMENT'储值卡营业额'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='拜博客户就诊汇总临时表';"""

Cus_Treat_dtail_tmp_truncate= """truncate bbkq_dm.T98_Bybo_Cus_Treat_ChDetail_tmp; 	 
"""
Cus_Treat_dtail_tmp_insert= """insert into bbkq_dm.T98_Bybo_Cus_Treat_ChDetail_tmp 
SELECT ifnull(b.ChargeOrderId,'') as chargeorderid,
b.Region,
ifnull(b.GroupIndex,'0') GroupIndex, 
ifnull(b.ItemGroupIndex,'0') ItemGroupIndex,
MAX(b.RecordVersion) RecordVersion
from bbkq_dw.T02_ChargeOrder_H  as a
inner join bbkq_dw.T02_ChargeOrderDetail_H as b 
on a.ChargeOrderId = b.ChargeOrderId 
and b.SourceDetailId > 0
and b.IsInactive = 0 
where a.IsInactive = 0 
and a.STATUS not in('未收费','作废并撤回')
and a.Scenario in (0,6)
and a.PayDate between  '{self.begin_date}' and '{self.end_date}'
GROUP BY 1,2,3,4;         
"""
Cus_Treat_tmp_truncate= """truncate bbkq_dm.T98_Bybo_Cus_Treat_tmp; 	 
"""

# INSERT RECORDS str_to_date('{end_date}','%Y-%m-%d %H:%i:%s')

Cus_Treat_insert_tmp = """insert into T98_Bybo_Cus_Treat_tmp
(Resv_Id
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
,Regi_Typ`
,Sngl_Item_Discnt_Amt
,Recvbl_Amt
,Recv_Amt
,Arrears_Amt
,Card_Comut,
Biz_Amt_Memb)

select 
d.AppointmentId as Resv_Id
,a.ChargeOrderId as Chrg_Ordr_Id
,b.ChargeOrderDetailId as Chrg_Ordr_Dtl_Id,
'' as Prpd_Card_TX_Rec_Id,
a.PayDate as Chrg_Dt,
a.`Status` as Chrg_Sngl_Stat,
hour(a.PayDateTime) as Chrg_Hour,
CASE WHEN a.ActualPrice2+a.ActualPrice3>0 THEN 1 ELSE 0 END as Comb_Pay_Ind,
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
ifnull(SUM(CASE WHEN (a.PayType <> '健保通' and a.PayType2 <> '健保通' and a.PayType3 <> '健保通' )  
    THEN ifnull(b.ActualPrice,a.ActualPrice) ELSE 0 END),'0') as Recv_Amt,
ifnull(SUM(CASE WHEN b.Overdue>0 THEN b.Overdue WHEN a.Overdue>0 THEN a.Overdue ELSE 0 END),'0') as Arrears_Amt,
0 as Card_Comut,
0 as Biz_Amt_Memb
from bbkq_dw.T02_ChargeOrder_H  as a
left join (select s.* from bbkq_dw.T02_ChargeOrderDetail_H as s
inner join bbkq_dm.T98_Bybo_Cus_Treat_ChDetail_tmp as t 
on s.chargeorderid = t.chargeorderid
and s.Region = t.Region
and s.RecordVersion = t.RecordVersion
and ifnull(s.GroupIndex,0) = t.GroupIndex
and ifnull(s.ItemGroupIndex,0) = t.ItemGroupIndex
where s.IsInactive = 0
and s.SourceDetailId > 0
) b  on a.chargeorderid = b.chargeorderid 
left join bbkq_dw.T01_Patient_H c on a.PatientId=c.PatientId  
left join bbkq_dw.T02_Appointment_H d on a.AppointmentId=d.AppointmentId and d.IsCancelled = 0 and d.IsFailed = 0
where 
a.IsInactive = 0 
and a.STATUS not in('未收费','作废并撤回') 
and a.Scenario in (0,6)
and a.PayDate between '{self.begin_date}' and '{self.end_date}'
and a.End_date='2099-01-01 00:00:00' and b.End_date='2099-01-01 00:00:00' and c.End_date='2099-01-01 00:00:00' and d.End_date='2099-01-01 00:00:00'
group by 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30
-- 减去现金卡券
union all
select 
d.AppointmentId as Resv_Id,
a.ChargeOrderId as Chrg_Ordr_Id
,'' as Chrg_Ordr_Dtl_Id,
'' as Prpd_Card_TX_Rec_Id,
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
'' as Dr_Id,
''as Treat_Advsr_Id,
a.OfficeId as Office_Id,
a.PatientId as Patient_Id,
ifnull(c.SourceTypeLevel1,'') as Patient_Fst_Lvl_Src,
ifnull(c.SourceTypeLevel2,'') as Patient_Sec_Lvl_Src,
ifnull(c.SourceTypeLevel3,'') as Patient_Thd_Lvl_Src,
ifnull(TIMESTAMPDIFF(YEAR,c.Birth,DATE_FORMAT(ifnull(a.PayDateTime,'0'), '%Y-%m-%d %H:%i:%s')),'')+0 as Patient_Age,
ifnull(c.Sex,'') as Patient_Gender,
'' as Treat_Main_Cls,
'' as Treat_Sub_Cls,
'' as Treat_Nm,
ifnull(d.DoctorId,'') as Resv_Dr_Id,
ifnull(d.ConsultantId,'') as Resv_Advsr_Id,
ifnull(d.CheckInType,'') as Regi_Typ,
0 as  Sngl_Item_Discnt_Amt,
0 as Recvbl_Amt,
ifnull((SUM(CASE WHEN PayType like '%现金%' and PayType <> '现金' THEN ifnull(a.ActualPrice1,0) ELSE 0 END +
    CASE WHEN PayType2 like '%现金%' and PayType2 <> '现金' THEN ifnull(a.ActualPrice2,0) ELSE 0 END  +
 CASE WHEN PayType3 like '%现金%' and PayType3 <> '现金' THEN ifnull(a.ActualPrice3,0) ELSE 0 END
    )*-1 ),'0') as Recv_Amt,
0 as Arrears_Amt,
0 as Card_Comut,
0 as Biz_Amt_Memb
from bbkq_dw.T02_ChargeOrder_H  as a
 left join bbkq_dw.T02_Appointment_H d on a.AppointmentId=d.AppointmentId and d.IsCancelled = 0 and d.IsFailed = 0
 left join bbkq_dw.T01_Patient_H c on a.PatientId=c.PatientId  
where 
a.IsInactive = 0 
and a.STATUS not in('未收费','作废并撤回') 
and a.Scenario in (0,6)
and a.PayDate between '{self.begin_date}' and '{self.end_date}'
and a.End_date='2099-01-01 00:00:00' and d.End_date='2099-01-01 00:00:00' and c.End_date='2099-01-01 00:00:00'
GROUP BY 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30
union all
select 
d.AppointmentId as Resv_Id
,a.ChargeOrderId as Chrg_Ordr_Id
,'' as Chrg_Ordr_Dtl_Id,
'' as Prpd_Card_TX_Rec_Id,
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
'' as Dr_Id,
''as Treat_Advsr_Id,
a.OfficeId as Office_Id,
a.PatientId as Patient_Id,
ifnull(c.SourceTypeLevel1,'') as Patient_Fst_Lvl_Src,
ifnull(c.SourceTypeLevel2,'') as Patient_Sec_Lvl_Src,
ifnull(c.SourceTypeLevel3,'') as Patient_Thd_Lvl_Src,
ifnull(TIMESTAMPDIFF(YEAR,c.Birth,DATE_FORMAT(ifnull(a.PayDateTime,'0'), '%Y-%m-%d %H:%i:%s')),'')+0 as Patient_Age,
ifnull(c.Sex,'') as Patient_Gender,
'' as Treat_Main_Cls,
'' as Treat_Sub_Cls,
'' as Treat_Nm,
ifnull(d.DoctorId,'') as Resv_Dr_Id,
ifnull(d.ConsultantId,'') as Resv_Advsr_Id,
ifnull(d.CheckInType,'') as Regi_Typ,
0 as  Sngl_Item_Discnt_Amt,
0 as Recvbl_Amt,
ifnull((SUM(CASE WHEN PayType like '%卡券抵扣%'  THEN ifnull(a.ActualPrice1,0) ELSE 0 END +
    CASE WHEN PayType2 like '%卡券抵扣%' THEN ifnull(a.ActualPrice2,0) ELSE 0 END  +
 CASE WHEN PayType3 like '%卡券抵扣%'   THEN ifnull(a.ActualPrice3,0) ELSE 0 END)*-1),'0') as Recv_Amt,
0 as Arrears_Amt,
ifnull((SUM(CASE WHEN PayType like '%卡券抵扣%'  THEN ifnull(a.ActualPrice1,0) ELSE 0 END +
    CASE WHEN PayType2 like '%卡券抵扣%' THEN ifnull(a.ActualPrice2,0) ELSE 0 END  +
 CASE WHEN PayType3 like '%卡券抵扣%'   THEN ifnull(a.ActualPrice3,0) ELSE 0 END)),'0') as Card_Comut,
 0 as Biz_Amt_Memb
from bbkq_dw.T02_ChargeOrder_H  as a
 left join bbkq_dw.T02_Appointment_H d on a.AppointmentId=d.AppointmentId and d.IsCancelled = 0 and d.IsFailed = 0
 left join bbkq_dw.T01_Patient_H c on a.PatientId=c.PatientId  
where 
a.IsInactive = 0 
and a.STATUS not in('未收费','作废并撤回') 
and a.Scenario in (0,6)
and a.PayDate between '{self.begin_date}' and '{self.end_date}'
and a.End_date='2099-01-01 00:00:00' and d.End_date='2099-01-01 00:00:00' and c.End_date='2099-01-01 00:00:00'
GROUP BY 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30
union all
--   储值卡
SELECT 
'' as Resv_Id
,'' as Chrg_Ordr_Id
,'' as Chrg_Ordr_Dtl_Id
,ifnull(a.MemberShipTransactionId,'') as Prpd_Card_TX_Rec_Id,
ifnull(a.RecordCreatedDate,'1900-01-01') as Chrg_Dt,
'已收费' Chrg_Sngl_Stat,
hour(A.RecordCreatedTime) Chrg_Hour,
'0' Comb_Pay_Ind,
(CASE a.TransactionTypeCode WHEN '0' THEN 'A' WHEN '1' THEN 'B' WHEN '2' THEN 'C' ELSE 'D' END) as Chrg_Typ_Cd,
'0' Rtn_Fee_Typ_Cd,
'0' Sell_Chnl_Cd,
'2' Chrg_Scne_Cd,
a.PayType as Fst_Choic_Pay_Md,
'' Sec_Choic_Pay_Md,
'' Oth_Pay_Md,
ifnull(a.DoctorId,'') as Dr_Id,
''  as Treat_Advsr_Id,
ifnull(a.TransactionOfficeId,'') as Office_Id,
ifnull(a.PatientId,'')  as Patient_Id,
ifnull(b.SourceTypeLevel1,'') as Patient_Fst_Lvl_Src,
ifnull(b.SourceTypeLevel2,'') as Patient_Sec_Lvl_Src,
ifnull(b.SourceTypeLevel3,'') as Patient_Thd_Lvl_Src,
0 as Patient_Age,
b.sex as Gender,
'' as Treat_Main_Cls,
'' as Treat_Sub_Cls,
'' as Treat_Nm,
'' as Resv_Dr_Id,
'' as Resv_Advsr_Id,
'' as Regi_Typ,
0 as  Sngl_Item_Discnt_Amt,
0 as Recvbl_Amt,

sum(case when a.TransactionTypeCode in (1,2) and a.Amount  is not null then  a.Amount 
 when a.TransactionTypeCode in (0,3) and PrincipalAmount  is not null then  PrincipalAmount end ) as  Recv_Amt,
0 as Arrears_Amt,
0 Dr_Incom,
sum(case when a.TransactionTypeCode in (1,2) and a.Amount  is not null then  a.Amount 
when a.TransactionTypeCode in (0,3) and PrincipalAmount  is not null then  PrincipalAmount end ) as  Biz_Amt_Memb
FROM bbkq_dw.t02_membershiptransaction_h as A
left join bbkq_dw.t01_patient_h b on a.patientId=b.PatientID
WHERE A.TransactionTypecode in (0,1,2,3) 
and A.IsInactive = '0'  
and A.PayType <> '余额调整' 
and a.RecordCreatedDate between '{self.begin_date}' and '{self.end_date}' and
a.End_date='2099-01-01 00:00:00' and b.End_date='2099-01-01 00:00:00' 

GROUP BY 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30;

"""
Cus_Treat_del = """delete from t98_bybo_cus_treat
where Chrg_Dt>='{self.begin_date}'  and Chrg_Dt<='{self.end_date}'
"""
Cus_Treat_insert="""
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










Cus_Treat_Create = [Treat_sql_create,Treat_sql_create_detail_tmp,Treat_sql_create_tmp]
                       # sql_P1_Rollback22099: {'begin_date': 'self.begin_date', 'end_date': 'self.end_date'},
                       # sql_P1_Del: {'begin_date': 'self.begin_date', 'end_date': 'self.end_date'},
                       # sql2Tmp:['begin_date','end_date']
Cus_Treat = [Cus_Treat_dtail_tmp_truncate,Cus_Treat_dtail_tmp_insert,Cus_Treat_tmp_truncate,Cus_Treat_insert_tmp,Cus_Treat_del,Cus_Treat_insert




]

