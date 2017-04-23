select s.appkey, 
    (s.nums - COALESCE(r.nums,0L)), 
    s.platform cnt from (select appkey,nums,platform from t where status=\'success\') s 
    left join (select appkey, nums from t where status=\'response\') r 
    on s.appkey = r.appkey;
    select * from dual group by a;
    ALTER TABLE mpns_report ADD IF NOT EXISTS 
    PARTITION (year=\'2015\', month=\'03\', day=\'30\')
    LOCATION \'/user/log/msgRecv/2015/03/30\';