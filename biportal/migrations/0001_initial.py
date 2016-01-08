# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import uuid
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataTransJob',
            fields=[
                ('job_id', models.UUIDField(default=uuid.uuid4, editable=False, serialize=False, primary_key=True)),
                ('job_description', models.TextField(verbose_name='作业简述')),
                ('db_s_infos', models.CharField(default='hiveDB', max_length=50, verbose_name='源库', choices=[('-1', '请选择'), ('NoSQL', (('hiveDB', 'HiveDB'), ('mongoDB', 'MongoDB'))), ('MySQL', (('38', 'mysql-3rd_platform-master\xa0\xa0\xa0\xa0[etlqry @ mysql-3rd.int.yihaodian.com:3306/3rd_platform]'),)), ('Oracle', (('6', 'oracle-ETL\xa0\xa0\xa0\xa0[ETL @ ex4-dw1.int.yihaodian.com:1521/edwstd01]'),))])),
                ('db_d_infos', models.CharField(default='-1', max_length=50, verbose_name='目标库', choices=[('-1', '请选择'), ('NoSQL', (('hiveDB', 'HiveDB'), ('mongoDB', 'MongoDB'))), ('MySQL', (('38', 'mysql-3rd_platform-master\xa0\xa0\xa0\xa0[etlqry @ mysql-3rd.int.yihaodian.com:3306/3rd_platform]'),)), ('Oracle', (('6', 'oracle-ETL\xa0\xa0\xa0\xa0[ETL @ ex4-dw1.int.yihaodian.com:1521/edwstd01]'),))])),
                ('extract_options', models.CharField(default='SQOOP_MR', max_length=50, verbose_name='抽取方式', choices=[('1', 'SQOOP_MR'), ('2', 'SQOOP_JDBC'), ('3', 'YHD')])),
                ('extract_duration', models.PositiveSmallIntegerField(default=10, verbose_name='预计使用时长', help_text='<i class="fa fa-info"> 单位分钟</i>', blank=True)),
                ('s_table_name', models.CharField(max_length=100, help_text='<i class="fa fa-info"> 例如<code>dw.tablename,MySql</code>库表名前不需要<code>schema</code></i>', verbose_name='表名 *')),
                ('select_sql', models.TextField(help_text='<i class="fa fa-info"> 例如:<code>select col1,col2..coln from dw.tablename where ds = \'${param1}\'</code></i>', verbose_name='select 语句 *')),
                ('hive_pretreatment_sql', models.TextField(verbose_name='预处理sql', help_text='<i class="fa fa-info"> 例如:<code>select count(1) as num from dw.tablename</code></i>', blank=True)),
                ('hive_posttreatment_sql', models.TextField(verbose_name='后处理sql', help_text='<i class="fa fa-info"> 例如:<code>select count(1) as num from dw.tablename</code></i>', blank=True)),
                ('mr_job_parallelism', models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(20, '最大并行度不能超过20'), django.core.validators.MinValueValidator(1, '最小并行度不能小与1')], help_text='<i class="fa fa-info"> 用来指定从hive导出数据的并发度</i>', verbose_name='导出并行任务数')),
                ('dynamic_parameter_list', models.CharField(verbose_name='动态参数列表', max_length=200, help_text='<i class="fa fa-info"> 用<code>,</code>分隔, 命令行调用时按照列表顺序传参,例如:<code>param1,param2,...paramX</code></i>', blank=True)),
                ('d_table_name', models.CharField(max_length=100, help_text='<i class="fa fa-info"> 例如<code>dw.tablename,MySql</code>库表名前不需要<code>schema</code></i>', verbose_name='表名')),
                ('d_table_field_list', models.CharField(verbose_name='字段列表', max_length=200, help_text='<i class="fa fa-info"> 缺省为全部字段 </i>', blank=True)),
                ('d_pretreatment_sql', models.TextField(verbose_name='预处理sql', help_text='<i class="fa fa-info"> 例如:<code>delete from dw.tablename where date_id=date \'${param1}\'</code></i>', blank=True)),
                ('d_posttreatment_sql', models.TextField(verbose_name='后处理sql', help_text='<i class="fa fa-info"> 默认为空</i>', blank=True)),
                ('is_transaction', models.CharField(default='2', max_length=10, help_text='<i class="fa fa-info">无特别需要,默认关闭</i>', verbose_name='事务', choices=[('2', '关闭')])),
            ],
        ),
    ]
