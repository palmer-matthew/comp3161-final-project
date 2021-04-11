window.onload = function(event){
    event.preventDefault();
    var ingredients = [];
    var inglist = [];
    var inslist = [];

    var pass_regex = /^[\w\s\(@!*)]+$/;
    var number_regex = /^[1-9]\d{1,5}$/;
    var alphaspace_regex = /^[\w\s]+$/;

    const addbtn = document.querySelector('.add');
    const adding = document.querySelector('.ai');
    const instruct = document.querySelector('.instruct');
    const select1 = document.querySelector('#ingredient');
    const select2 = document.querySelector('#measurement');
    const input = document.querySelector('#instruction');
    const display1 = document.querySelector('.sel-ing');
    const display2 = document.querySelector('.sel-ins');
    const error = document.querySelector(".error");


    function r(element){
        let v = element.id;
        let start1 = `
        <thead>
            <tr>
                <th class="text-center" colspan="2">Ingredients</th>
            </tr>
        </thead>
        <tbody>`;
        let end1 = '</tbody>';
        
        element.addEventListener('click', (event) => {
            event.preventDefault();

            inslist.splice(v, 1);

            for(i=0; i < inslist.length; i++){
                start1 += `
                <tr>
                    <td>${i+1}. ${inslist[i]}</td>
                    <td class="center fs-3 btn click" id=${i}> &times; </td>
                </tr>`;
                
            }
            display2.innerHTML = start1 + end1;

            if(inslist.length < 1){
                display2.classList.remove('activet');
            }else{
                let x = display2.querySelectorAll('.click');
                x.forEach(ele => r(ele));
            }
        });
    }


    function remo(element){
        let v = element.id;
        let start1 = `
        <thead>
            <tr>
                <th class="text-center" colspan="2">Ingredients</th>
            </tr>
        </thead>
        <tbody>`;
        let end1 = '</tbody>';
        
        element.addEventListener('click', (event) => {
            event.preventDefault();

            ingredients.splice(v, 1);
            inglist.splice(v, 1);

            for(i=0; i < inglist.length; i++){
                start1 += `
                <tr>
                    <td>${inglist[i][1]} ${inglist[i][2]}</td>
                    <td class="center fs-3 btn click" id=${inglist[i][0]}> &times; </td>
                </tr>`;
                
            }
            display1.innerHTML = start1 + end1;

            if(inglist.length < 1){
                display1.classList.remove('activet');
            }else{
                let x = display1.querySelectorAll('.click');
                x.forEach(ele => remo(ele));
            }
        });
    }

    function getIngredients(){
        fetch('/api/ingredients', {
            method: 'GET'
        }).then(response => response.json())
        .then(data => {
            let response = data.data;
            if(response == 'NOK'){
                select1.innerHTML = '<option value="null">No Options Available</option>';
            }else{
                iHTML = "";
                for(i=0; i < response.length; i++){
                    iHTML += `<option value=${response[i].key}>${response[i].name}</option>`;
                }
                select1.innerHTML = iHTML;
            }
        }).catch(error => console.log(error));
    }

    function getMeasurements(){
        fetch('/api/measurements', {
            method: 'GET'
        }).then(response => response.json())
        .then(data => {
            let response = data.data;
            if(response == 'NOK'){
                select2.innerHTML = '<option value="null">No Options Available</option>';
            }else{
                iHTML = "";
                for(i=0; i < response.length; i++){
                    iHTML += `<option value=${response[i].key}>${response[i].qty} ${response[i].unit}</option>`;
                }
                select2.innerHTML = iHTML;
            }
        }).catch(error => console.log(error));
    }

    addbtn.addEventListener('click', (event) => {


        event.preventDefault();

        let form = document.forms[0];
        let element = form.elements;
        not_sanitized = false;
        for(i = 0; i < element.length; i++){
            switch(element[i].name){
                case 'recipe_name':
                    if(element[i].value.match(alphaspace_regex) == null){
                        not_sanitized = true
                    }
                    break;

                case 'calorie_count':
                    if(element[i].value.match(number_regex) == null){
                        not_sanitized = true
                    }
                    break;

                case 'serving':
                    if(element[i].value.match(number_regex) == null){
                        not_sanitized = true
                    }
                    break;

                case 'prep_time':
                    if(element[i].value.match(number_regex) == null){
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
        if (!not_sanitized){
            var formfield = document.createElement("input");
            formfield.type = "hidden";
            formfield.name = "ingredients";

            var formfield1 = document.createElement("input");
            formfield1.type = "hidden";
            formfield1.name = "instruct";

            console.log(inglist);
            console.log(inslist);

            var formval = "";
            var formval1 = "";

            for(i=0; i < inglist.length; i++){
                if(i == 0){
                    formval += inglist[i][0];
                }else{
                    formval += ',' + inglist[i][0];
                }
            }

            for(i=0; i < inslist.length; i++){
                if(i == 0){
                    formval1 += inslist[i];
                }else{
                    formval1 += '|' + inslist[i];
                }
            }

            formfield.value = formval;
            formfield1.value = formval1
            form.appendChild(formfield);
            form.appendChild(formfield1);

            form.submit();
        }

    });

    adding.addEventListener('click', (event) => {
        event.preventDefault();
        
        let iID = select1.selectedOptions[0].value;
        let mID = select2.selectedOptions[0].value;
        let ival = select1.selectedOptions[0].textContent;
        let mval = select2.selectedOptions[0].textContent;
        let data = `${mID}|${iID}`;
        let start = `
        <thead>
            <tr>
                <th class="text-center" colspan="2">Ingredients</th>
            </tr>
        </thead>
        <tbody>`;
        let end = '</tbody>';
        if(!ingredients.includes(iID)){
            inglist.push([data, mval, ival, iID]);
            ingredients.push(iID);
        }

        if(display1.classList.contains('activet')){
            for(i=0; i < inglist.length; i++){
                start += `
                <tr>
                    <td>${inglist[i][1]} ${inglist[i][2]}</td>
                    <td class="center fs-3 btn click" id=${inglist[i][0]}> &times; </td>
                </tr>`;
                
            }
            display1.innerHTML = start + end;
        }else{
            display1.classList.add('activet');
            for(i=0; i < inglist.length; i++){
                start += `
                    <tr>
                        <td>${inglist[i][1]} ${inglist[i][2]}</td>
                        <td class="center fs-3 btn click" id=${i}> &times; </td>
                    </tr>`;
            }
            display1.innerHTML = start + end;
        }
        
        if(inglist.length > 0){
            let x = display1.querySelectorAll('.click');
            x.forEach(ele => remo(ele));
        }
    });


    instruct.addEventListener('click', (event) => {

        event.preventDefault();

        let data = input.value;
        let start = `
        <thead>
            <tr>
                <th class="text-center" colspan="2">Instructions</th>
            </tr>
        </thead>
        <tbody>`;
        let end = '</tbody>';

        if (data != "" || data == null){
            inslist.push(data);
        }

        if(display2.classList.contains('activet')){
            for(i=0; i < inslist.length; i++){
                start += `
                <tr>
                    <td>${i+1}. ${inslist[i]}</td>
                    <td class="center fs-3 btn click" id=${i}> &times; </td>
                </tr>`;
                
            }
            input.value = "";
            display2.innerHTML = start + end;
        }else{
            if(inslist.length > 0){
                display2.classList.add('activet');
                for(i=0; i < inslist.length; i++){
                    start += `
                    <tr>
                        <td>${i+1}. ${inslist[i]}</td>
                        <td class="center fs-3 btn click" id=${i}> &times; </td>
                    </tr>`;
                    
                }
                input.value = "";
                display2.innerHTML = start + end;
            }
        }
        
        if(inslist.length > 0){
            let x = display2.querySelectorAll('.click');
            x.forEach(ele => r(ele));
        }

    });

    getIngredients();
    getMeasurements();
}