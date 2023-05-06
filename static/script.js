function hide(){
    document.querySelector('.add_form').style.display='none';
}

function show(){
    document.querySelector('.add_form').style.display='flex';
    window.scrollTo(0, document.body.scrollHeight);
}

close_b = document.querySelector('.bx-x-circle');

close_b.addEventListener("click",hide);

add_item = document.querySelector('.add_item');
add_item.addEventListener("click",show);
