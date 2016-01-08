/**
 * Created by fengwu on 15/12/9.
 */


/*创建数据交换任务列表gird*/
var grid = $("#grid-transfer-data").bootgrid({
    ajax: false,
    ajaxSettings: {
        dataType: 'jsonp'
    },
    post: function () {
        return {
            searchKey: "hanzhengbo"
        }
    },
    url: "http://bi.yihaodian.com.cn/bi-cloud/bigDataHive/queryList.action",
    selection: true,
    labels: {
        noResults: "没有记录"
    },
    multiSelect: true,
    rowSelect: false,
    keepSelection: true,
    rowCount: [15, 30, 45, 60, -1],
    formatters: {
        "commands": function (column, row) {
            return "<div class=\"btn-group btn-group-xs\">" +
                "<button type=\"button\" class=\"btn btn-default command-edit\" data-row-id=\"" + row.id + "\">" +
                "<span class=\"fa fa-pencil-square-o\"></span></button> " +
                "<button type=\"button\" class=\"btn btn-default command-delete\" data-row-id=\"" + row.id + "\">" +
                "<span class=\"fa fa-trash-o\"></span></button>" +
                "<button type=\"button\" class=\"btn btn-default command-open\" data-row-id=\"" + row.id + "\">" +
                "<span class=\"fa fa-search-plus\"></span></button>" +
                "</div>";
        }
    }
}).on("loaded.rs.jquery.bootgrid", function (e) {
    /* Executes after data is loaded and rendered*/
    grid.find(".command-edit").on("click", function (e) {
        BootstrapDialog.closeAll();
        BootstrapDialog.show({
            type: 'type-info',
            title: '任务更新',
            message: "修改 id=" + $(this).data("row-id") + "?",
            buttons: [
                {
                    id: 'btn-ok',
                    icon: 'glyphicon glyphicon-ok',
                    label: '确定',
                    cssClass: 'btn-default',
                    autospin: false,
                    action: function (dialogRef) {
                        dialogRef.close();
                    }
                },
                {
                    id: 'btn-delete',
                    icon: 'glyphicon glyphicon-remove',
                    label: '取消',
                    cssClass: 'btn-default',
                    autospin: false,
                    action: function (dialogRef) {
                        dialogRef.close();
                    }
                }
            ]
        });
    }).end().find(".command-delete").on("click", function (e) {
        BootstrapDialog.closeAll();
        var dialog = new BootstrapDialog({
            type: 'type-warning',
            message: "确定删除: " + $(this).data("row-id") + "?",
            buttons: [
                {
                    id: 'btn-ok',
                    icon: 'glyphicon glyphicon-ok',
                    label: '确定',
                    cssClass: 'btn-default',
                    autospin: false,
                    action: function (dialogRef) {
                        dialogRef.close();
                    }
                },
                {
                    id: 'btn-delete',
                    icon: 'glyphicon glyphicon-remove',
                    label: '取消',
                    cssClass: 'btn-default',
                    autospin: false,
                    action: function (dialogRef) {
                        dialogRef.close();
                    }
                }
            ]
        });
        dialog.open();
    }).end().find(".command-open").on("click", function (e, selectedRows) {
        BootstrapDialog.closeAll();
        BootstrapDialog.show({
            type: 'type-success',
            title: '任务详情',
            message: "查看 id=" + $(this).data("row-id") + "?",
            buttons: [
                {
                    id: 'btn-ok',
                    icon: 'glyphicon glyphicon-ok',
                    label: '确定',
                    cssClass: 'btn-default',
                    autospin: false,
                    action: function (dialogRef) {
                        dialogRef.close();
                    }
                },
                {
                    id: 'btn-delete',
                    icon: 'glyphicon glyphicon-remove',
                    label: '取消',
                    cssClass: 'btn-default',
                    autospin: false,
                    action: function (dialogRef) {
                        dialogRef.close();
                    }
                }
            ]
        });
    });
}).on("removed.rs.jquery.bootgrid", function (e, removedRows) {

}).on("selected.rs.jquery.bootgrid", function (e, selectedRows) {
    var rowIds = [];
    for (var i = 0; i < selectedRows.length; i++) {
        rowIds.push(selectedRows[i].id)
    }
});






