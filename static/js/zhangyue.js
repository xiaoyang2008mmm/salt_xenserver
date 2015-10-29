$(document).ready(function() {
    //////////////////////////////////////////////////////
    //折叠js
    $(function() {
        $('[data-id=collapseFour]').collapse({
            toggle: false
        })
    });

    //////////////////////////////////////////////////////
    //

function post_func(  $uuid, $xen_ip, $action ) {
    var msg = "确定在:" + $xen_ip + "\n" + "UUID为:"+ $uuid + "\n" + "执行操作:"+ $action ;
    if (confirm(msg) == true) {

        $.post("/xen_operation/", {
            uuid: $uuid,
            xen_ip: $xen_ip,
            action: $action,
        },
        function(data) {
            alert(data);
        });
        return true; 

    } else {
        return false;
    }
}

    $('body').on('click', 'button[id*=stop]',
    function() {
        var $action = "shutdown";
        var $this = $(this);
        var $success = $this.closest('tbody').find('tr.success');
        var $warning = $this.closest('tbody').find('tr.warning');
        var index = $success.index($this.closest('tr.success')[0]);
        var $uuid = $warning.eq(index).find('td:nth-child(3)').text() ;
        var $xen_ip = $this.closest('.panel-info').find('a[data-toggle=collapse]').text().replace(/IP:/ig, '');
        if (post_func( $uuid, $xen_ip, $action ) == true) { $(this).attr({"disabled":"disabled"}).css("background-color", "gray");};
    })

    $('body').on('click', 'button[id*=start]',
    function() {
        var $action = "start";
        var $this = $(this);
        var $success = $this.closest('tbody').find('tr.success');
        var $warning = $this.closest('tbody').find('tr.warning');
        var index = $success.index($this.closest('tr.success')[0]);
        var $uuid = $warning.eq(index).find('td:nth-child(3)').text() ;
        var $xen_ip = $this.closest('.panel-info').find('a[data-toggle=collapse]').text().replace(/IP:/ig, '');
        if (post_func( $uuid, $xen_ip, $action ) == true) { $(this).attr({"disabled":"disabled"}).css("background-color", "gray");};
    })



    $('body').on('click', 'button[id*=reboot]',
    function() {
        var $action = "reboot";
        var $this = $(this);
        var $success = $this.closest('tbody').find('tr.success');
        var $warning = $this.closest('tbody').find('tr.warning');
        var index = $success.index($this.closest('tr.success')[0]);
        var $uuid = $warning.eq(index).find('td:nth-child(3)').text() ;
        var $xen_ip = $this.closest('.panel-info').find('a[data-toggle=collapse]').text().replace(/IP:/ig, '');
        if (post_func( $uuid, $xen_ip, $action ) == true) { $(this).attr({"disabled":"disabled"}).css("background-color", "gray");};
    })
    //////////////////////////////////////////////////////
});
