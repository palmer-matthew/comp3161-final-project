window.onload = function(event){
    event.preventDefault();

    const addbtn = document.querySelector('.add');
    const inventorybtn = document.querySelector('.ai');
    const input = document.querySelector('.hidden');
    const closebtn = document.querySelector('.x');
    const select = document.querySelector('#ingredient')

    addbtn.addEventListener('click', (event) => {

        event.preventDefault();

        console.log('Add Button was clicked');
        console.log(select);

        fetch('/api/ingredients', {
            method: 'GET'
        }).then(response => response.json())
        .then(data => {
            let response = data.data;
            if(response == 'NOK'){
                select.innerHTML = '<option value="null">No Options Available</option>';
            }else{
                iHTML = "";
                for(i=0; i < response.length; i++){
                    iHTML += `<option value=${response[i].key}>${response[i].name}</option>`;
                }
                select.innerHTML = iHTML;
            }
        }).catch(error => console.log(error));

        input.classList.add('active');
    });

    inventorybtn.addEventListener('click', (event) => {

        event.preventDefault();
        let value = select.selectedOptions[0].value;

        if(value == 'null' ){
            console.log('Nothing Happens');
        }else{

            var searchParams = new URLSearchParams();
            searchParams.append('iID', value);

            fetch('/api/inventory', {
                method: 'POST',
                body: searchParams,
            }).then(response => response.json())
            .then(data => {
                let response = data.data;
                if(response == 'NOK'){
                    console.log('Failed');
                }else{
                    window.location.reload();
                }
            }).catch(error => console.log(error));
        }

    });

    closebtn.addEventListener('click', (event) =>{

        event.preventDefault();
        
        select.innerHTML = "";
        input.classList.remove('active');

    });

}