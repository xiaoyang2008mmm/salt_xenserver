function post_func($uuid, $xen_ip, $action ) {
    var msg = "确定在" + $xen_ip + "UUID为:"+ $uuid + "执行"+ $action +"操作";
    if (confirm(msg) == true) {

        $.post("/xen_operation/", {
            uuid: $uuid,
            xen_ip: $xen_ip,
            action: $action,
        },
        function(data) {
            alert(data);
        });

    } else {
        return false;
    }
}
