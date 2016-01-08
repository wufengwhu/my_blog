/**
 * Created by fengwu on 15/12/9.
 */


function hideDiv(div) {
    $("#" + div).hide();
}

function showAdvDiv(div, hdiv) {
    $("#" + div).show();
    $("#" + hdiv).hide();
}

function isEmpty(str) {
    if (str !== null && str.length > 0) {
        return true;
    }
    return false;
}


/*创建数据交换任务的表单*/
var bi_data_form = $("#data-transfer-form").show();
bi_data_form.steps({
    headerTag: "h3",
    bodyTag: "fieldset",
    transitionEffect: "slideLeft",
    cssClass: "wizard modal-body",
    enableCancelButton: true,
    enableFinishButton: true,
    onStepChanging: function (event, currentIndex, newIndex) {
        // Allways allow previous action even if the current form is not valid!
        if (currentIndex > newIndex) {
            return true;
        }

        // 将同种库的选项禁止掉
        var source_db_select = $("select#id_db_s_infos.form-control option:selected");
        var source_optgroup_label = source_db_select.parent().attr('label');

        var target_db_select = $('select#id_db_d_infos.form-control option:selected');

        var target_optgrop_label = target_db_select.parent().attr('label');

        if (source_optgroup_label === target_optgrop_label) {
            $('#error_message_db').show();
            return false;
        } else {
            $('#error_message_db').hide();
        }

        if (newIndex === 1) {
            var pre = $("#id_hive_pretreatment_sql").parents('.form-group');
            var post = $("#id_hive_posttreatment_sql").parents('div.form-group.bootstrap3-required');
            var parallelism = $("#id_mr_job_parallelism").parents('div.form-group.bootstrap3-required');
            if (source_optgroup_label === "NoSQL") {
                // 选择了 非关系型库作源库
                pre.show();
                post.show();
                parallelism.show();
            } else {
                pre.hide();
                post.hide();
                parallelism.hide();
            }
        }
        // Needed in some cases if the user went back (clean up)
        if (currentIndex < newIndex) {
            // To remove error styles
            //form.find("#id_hive_pretreatment_sql").parents('.form-group').show();
            //form.find("#id_hive_posttreatment_sql").parents('div.form-group.bootstrap3-required').show();
            //form.find("#id_mr_job_parallelism").parents('div.form-group.bootstrap3-required').show();
        }
        //       form.validate().settings.ignore = ":disabled,:hidden";

        //              return form.valid();
        return true;
    },
    onStepChanged: function (event, currentIndex, priorIndex) {
        // Used to skip the "Warning" step if the user is old enough.
    },
    onFinishing: function (event, currentIndex) {
        return true;
    },
    onCanceled: function (event) {
        BootstrapDialog.closeAll();
        //$('#id_bi_add_data_trans').hide();
        //$('div.modal-backdrop.fade.in').hide();
    },
    onFinished: function (event, currentIndex) {
        alert("submit")
        return true;
    },

    labels: {
        cancel: "取消",
        finish: "完成",
        next: "下一步",
        previous: "上一步",
        loading: "加载中..."
    }
});

