window.onload = function(event){
    event.preventDefault();
    var ingredients = [];
    var inglist = [];
    var inslist = [];

    const addbtn = document.querySelector('.add');
    const adding = document.querySelector('.ai');
    const instruct = document.querySelector('.instruct');
    const select1 = document.querySelector('#ingredient');
    const select2 = document.querySelector('#measurement');
    const display1 = document.querySelector('.sel-ing');
    const display2 = document.querySelector('.sel-ins');

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
        console.log('You added something');

        let form = document.forms[0];
        form.submit();
        
    });

    adding.addEventListener('click', (event) => {
        event.preventDefault();

        let value = select1.selectedOptions[0].value;
        let val = select2.selectedOptions[0].value;

        console.log(value);
        console.log(val);
    });

    instruct.addEventListener('click', (event) => {

    });

    getIngredients();
    getMeasurements();
}