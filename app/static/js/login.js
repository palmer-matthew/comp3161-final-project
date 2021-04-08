window.onload = function(event){
    event.preventDefault();

    var pass_regex = /^[\w\s\(@!*)]+$/;
    var number_regex = /^[1-9]\d{1,5}$/;
    var alphaspace_regex = /^[\w\s]+$/;

    const form = document.forms[0];
    const sub = document.querySelector(".sub");
    const error = document.querySelector(".error");

    sub.addEventListener('click', function(e){
        e.preventDefault();
        let element = form.elements;
        not_sanitized = false;
        for(i = 0; i < element.length; i++){
            switch(element[i].name){
                case 'username':
                    if(element[i].value.match(alphaspace_regex) == null){
                        not_sanitized = true
                    }
                    break;

                case 'password':
                    if(element[i].value.match(pass_regex) == null){
                        not_sanitized = true
                    }
                    break;

                case 'fname':
                    if(element[i].value.match(alphaspace_regex) == null){
                        not_sanitized = true
                    }
                    break;

                case 'lname':
                    if(element[i].value.match(alphaspace_regex) == null){
                        not_sanitized = true
                    }
                    break;

                default:
                    break;
                
            }
            if(not_sanitized){
                error.innerHTML = `<div class="alert alert-danger">Invalid User Input</div>`;
                break;
            }
            
        }

        if(!not_sanitized){
            form.submit();
        }

    });

};