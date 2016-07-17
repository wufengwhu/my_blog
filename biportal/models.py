import uuid
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.
from django.forms import Textarea, TextInput, RadioSelect, ModelForm

TRANSACTION_CHOICES = (
    ('2', '关闭'),
)

DB_CHOICES = (
    ('-1', '请选择'),
    ('NoSQL', (
        ('hiveDB', 'HiveDB'),
        ('mongoDB', 'MongoDB'),
    )),

    ('MySQL', (
        ('38', 'mysql-3rd_platform-master    [etlqry @ mysql-3rd.int.yihaodian.com:3306/3rd_platform]'),
    )),

    ('Oracle', (
        ('6', 'oracle-ETL    [ETL @ ex4-dw1.int.yihaodian.com:1521/edwstd01]'),
    )),
)
EXTRACT_METHODS = (
    ('1', 'SQOOP_MR'),
    ('2', 'SQOOP_JDBC'),
    ('3', 'YHD'),
)


class DataTransJob(models.Model):
    """ 数据交换任务的model """
    HELP_TEXT_FOR_TABLE_NAME = '<i class=\"fa fa-info\"> ' \
                               '例如<code>dw.tablename,MySql</code>库表名前不需要<code>schema</code></i>'
    job_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    job_description = models.TextField(verbose_name='作业简述', blank=False)

    db_s_infos = models.CharField(choices=DB_CHOICES, verbose_name='源库', max_length=50, default='hiveDB')

    db_d_infos = models.CharField(choices=DB_CHOICES, verbose_name='目标库', max_length=50, default="-1")

    extract_options = models.CharField(choices=EXTRACT_METHODS, verbose_name='抽取方式', max_length=50,
                                       default='SQOOP_MR')

    extract_duration = models.PositiveSmallIntegerField(default=10, blank=True, verbose_name='预计使用时长',
                                                        help_text='<i class=\"fa fa-info\"> 单位分钟</i>')

    s_table_name = models.CharField(verbose_name='表名 *', max_length=100, blank=False,
                                    help_text=HELP_TEXT_FOR_TABLE_NAME)

    select_sql = models.TextField(verbose_name='select 语句 *', blank=False,
                                  help_text='<i class=\"fa fa-info\"> '
                                            '例如:<code>select col1,col2..coln from dw.tablename where ds '
                                            '= \'${param1}\'</code></i>')

    hive_pretreatment_sql = models.TextField(verbose_name='预处理sql', blank=True,
                                             help_text='<i class=\"fa fa-info\"> '
                                                       '例如:<code>select count(1) as num from dw.tablename</code></i>')
    hive_posttreatment_sql = models.TextField(verbose_name='后处理sql', blank=True,
                                              help_text='<i class=\"fa fa-info\"> '
                                                        '例如:<code>select count(1) as num from dw.tablename</code></i>')
    # hive作为源库字段域
    mr_job_parallelism = models.PositiveSmallIntegerField(validators=[MaxValueValidator(20, "最大并行度不能超过20"),
                                                                      MinValueValidator(1, "最小并行度不能小与1")],
                                                          verbose_name='导出并行任务数', default=1,
                                                          help_text='<i class=\"fa fa-info\"> '
                                                                    '用来指定从hive导出数据的并发度</i>')
    dynamic_parameter_list = models.CharField(verbose_name='动态参数列表', max_length=200, blank=True,
                                              help_text='<i class=\"fa fa-info\"> '
                                                        '用<code>,</code>分隔, 命令行调用时按照列表顺序传参,例如:'
                                                        '<code>param1,param2,...paramX</code></i>')

    # hive作为目标库字段域

    # oracle mysql 目标库字段域
    d_table_name = models.CharField(verbose_name='表名', max_length=100, blank=False,
                                    help_text=HELP_TEXT_FOR_TABLE_NAME)
    d_table_field_list = models.CharField(verbose_name='字段列表', blank=True,
                                          max_length=200, help_text='<i class=\"fa fa-info\"> 缺省为全部字段 </i>')
    d_pretreatment_sql = models.TextField(verbose_name='预处理sql', blank=True,
                                          help_text='<i class=\"fa fa-info\"> '
                                                    '例如:<code>delete from dw.tablename where date_id=date '
                                                    '\'${param1}\'</code></i>')
    d_posttreatment_sql = models.TextField(verbose_name='后处理sql', blank=True,
                                           help_text='<i class=\"fa fa-info\"> 默认为空</i>')
    is_transaction = models.CharField(verbose_name='事务', max_length=10, default='2',
                                      choices=TRANSACTION_CHOICES,
                                      help_text='<i class=\"fa fa-info\">无特别需要,默认关闭</i>')

    create_time = models.DateTimeField(default=now())

    def _str_(self):
        return self.job_description


class DataTransJobForm(ModelForm):
    class Meta:
        model = DataTransJob
        exclude = ['job_id']
        labels = {
        }

        help_texts = {
            ''
        }
        widgets = {
            'job_description': Textarea(attrs={'rows': 5, 'cols': 85, 'placeholder': '请简要描述作业目的, 默认为空'}),
            'select_sql': Textarea(attrs={'rows': 1, 'cols': 85}),
            'hive_pretreatment_sql': Textarea(attrs={'rows': 1, 'cols': 85, 'placeholder': '默认为空'}),
            'hive_posttreatment_sql': Textarea(attrs={'rows': 1, 'cols': 85, 'placeholder': '默认为空'}),
            'd_pretreatment_sql': Textarea(attrs={'rows': 1, 'cols': 85, 'placeholder': ' 默认为空'}),
            'd_posttreatment_sql': Textarea(attrs={'rows': 1, 'cols': 85, 'placeholder': ' 默认为空'}),
            's_table_name': TextInput(attrs={'required': 'required', 'placeholder': '必填'}),
            'is_transaction': RadioSelect(),
        }
        error_messages = {
            'job_description': {
                'max_length': _("作业描述太长"),
            },
        }

    def clean(self):
        cleaned_data = super(DataTransJobForm, self).clean()
