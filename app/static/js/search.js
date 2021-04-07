window.onload = function(event){
    event.preventDefault();

    var pass_regex = /^[\w\s\(@!*)]+$/;
    var number_regex = /^[1-9]\d{1,5}$/;
    var alphaspace_regex = /^[\w\s]+$/;

    const input = document.querySelector(".srch");
    const srchbtn = document.querySelector(".add");
    const error = document.querySelector(".error");

    srchbtn.addEventListener('click', function(e){
        e.preventDefault();

        let form = document.forms[0];
        let search = form.elements['search'];
        let data = search.value;

        if(data.match(alphaspace_regex) == null){
            error.innerHTML = `<div class="alert alert-danger">Invalid Search Input</div>`;
        }else if(data.match(alphaspace_regex) != null){
            form.submit();
        }

    });
}