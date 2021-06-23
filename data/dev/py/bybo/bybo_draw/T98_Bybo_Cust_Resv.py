


# Create TABLES
CustResv_table_Create = """  CREATE TABLE IF NOT EXISTS bbkq_dm.T98_Bybo_Cust_Resv(
Resv_Treat_Dt date NOT NULL  DEFAULT '1900-01-01' COMMENT'预约治疗日期',
Resv_Treat_Cd varchar(50) NOT NULL  DEFAULT ' ' COMMENT'预约治疗项目代码',
Resv_Tm_long integer NOT NULL  DEFAULT '0' COMMENT'预约时长',
Resv_Dr_Id varchar(50) NOT NULL  DEFAULT ' ' COMMENT'预约医生编号',
Resv_Advsr_Id varchar(50) NOT NULL  DEFAULT ' ' COMMENT'预约咨询师编号',
Office_Id varchar(50) NOT NULL  DEFAULT ' ' COMMENT'诊所编号',
Patient_Id varchar(50) NOT NULL  DEFAULT ' ' COMMENT'患者编号',
Regi_Typ varchar(50) NOT NULL  DEFAULT ' ' COMMENT'挂号类型 ',
Cons_Treat varchar(200) NOT NULL  DEFAULT ' ' COMMENT'咨询治疗项目',
Resv_Treat varchar(200) NOT NULL  DEFAULT ' ' COMMENT'预约治疗项目',
Resv_Treat_Cls varchar(200) NOT NULL  DEFAULT ' ' COMMENT'预约治疗项目分类',
Vist_Ind varchar(10) NOT NULL  DEFAULT ' ' COMMENT'就诊标识',
Resv_Treat_Intrv_Days varchar(10) NOT NULL  DEFAULT ' ' COMMENT'预约治疗间隔天数',
Resv_Mtime integer NOT NULL  DEFAULT '0' COMMENT'预约人次',
InDM_timestamp datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '进入DM的时间'
)"""

CustResv_table_Del = """
                         delete from bbkq_dm.T98_Bybo_Cust_Resv
                          where
                          Resv_Treat_Dt >= str_to_date('{self.begin_date}','%Y-%m-%d')
                          and Resv_Treat_Dt <= str_to_date('{self.end_date}','%Y-%m-%d')"""

# INSERT RECORDS str_to_date('{end_date}','%Y-%m-%d %H:%i:%s')
CustResv_table_insert = """
            insert into bbkq_dm.T98_Bybo_Cust_Resv(Resv_Treat_Dt,Resv_Treat_Cd,Resv_Tm_long,Resv_Dr_Id,Resv_Advsr_Id,
            Office_Id,Patient_Id,Regi_Typ,Cons_Treat,Resv_Treat,Resv_Treat_Cls,Vist_Ind,Resv_Treat_Intrv_Days,Resv_Mtime,InDM_timestamp)
            select 
            date(StartDate) as Resv_Treat_Dt,
            a.TransactionId as Resv_Treat_Cd,
            TIMESTAMPDIFF(MINUTE,a.StartTime,a.EndTime) as Resv_Tm_long,
            a.DoctorId as Resv_Dr_Id,
            a.ConsultantId  as Resv_Advsr_Id,
            a.OfficeId as Office_Id,
            a.PatientId as Patient_Id,
            CheckInType  as Regi_Typ,
            ConsultItem as Cons_Treat,
            '' as Resv_Treat,
            '' as Resv_Treat_Cls,
            case when b.id is not null then 1 else 0 end as Vist_Ind,
            case when b.id is not null then date(b.PayDateTime) -  date(a.RecordCreatedTime) else '' end as Resv_Treat_Intrv_Days,
            count(distinct a.patientId) as Resv_Mtime,
            now()                       as InDM_timestamp
            from bbkq_dw.T02_Appointment_H a left join (select * from bbkq_dw.T02_ChargeOrder_H  where date(end_date)='2099-01-01') b on a.AppointmentId  = b.AppointmentId 
            -- left join transactioncod d on a.TransactionId = concat(Region,LPAD(d.Id, 10, 0))
            where date(a.end_date)='2099-01-01'
            and a.IsInactive = 0 
            and a.IsCancelled <> 1 
            and a.IsFailed <> 1
            and IsCheckedIn='1'
            and  a.patientId not in (select Id from BBKQ_ODS_EKANYA.patient where  Name in  ('停约'))
            and date(StartDate)>= str_to_date('{self.begin_date}','%Y-%m-%d') and date(StartDate) <= str_to_date('{self.end_date}','%Y-%m-%d')
            group by Resv_Treat_Dt,
            Resv_Treat_Cd,
            TransactionId,
            Resv_Tm_long,
            Resv_Dr_Id,
            Resv_Advsr_Id,
            Office_Id,
            Patient_Id,
            Regi_Typ,
            Cons_Treat,
            Vist_Ind
            """


# FIND SONGS
FIND_select = ("""
""")

# QUERY LISTS
Cust_Resv = [CustResv_table_Create,CustResv_table_Del,CustResv_table_insert]


