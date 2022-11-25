
const btn_sidebar = document.querySelectorAll('.btn-sidebar');

if (document.body.addEventListener){
    document.body.addEventListener('click',yourHandler,false);
}
else{
    document.body.attachEvent('onclick',yourHandler);//for IE
}

function yourHandler(e){
    e = e || window.event;
    var target = e.target || e.srcElement;
    if (target.className.match(/keyword/))
    {
        '.btn-sidebar'
    }
}



// const db_table_header = document.querySelector('#db-table-header');
// const db_table_header_li = document.createElement('li');

// db_table_header.append(db_table_header_li)