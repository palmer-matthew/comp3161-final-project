`
<div class="btn-container mb-2">
            <h2 class="fw-bold text-capitalize mb-3"> Meal Plan: Kadhjskandkjsahd</h2>
            <h3 class="fw-bold mb-3 tot"> Total Calories: 54856</h3>
</div>
<div class="day section mb-5">
    <h4 class="text-decoration-underline">Day 4</h4>
    <h5>Breakfast</h5>
    <div class="py-2 card grid-card mb-3">
        <img class='image' src="{{ url_for('static', filename='img/dinner_dining_black_24dp.svg')}}" alt="">
        <div class="btn-container">
            <div>
                <p class="text-capitalize fw-bold fs-5 nbm">Name of Recipe</p>
                <p class="fs-6 fw-light nbm">Servings: 6</p>
            </div>
            <p class="nbm me-4">Created: 2020-03-12</p>
        </div>
    </div>
    <h5>Lunch</h5>
    <div class="py-2 card grid-card mb-3">
        <img class='image' src="{{ url_for('static', filename='img/dinner_dining_black_24dp.svg')}}" alt="">
        <div class="btn-container">
            <div>
                <p class="text-capitalize fw-bold fs-5 nbm">Name of Recipe</p>
                <p class="fs-6 fw-light nbm">Servings: 6</p>
            </div>
            <p class="nbm me-4">Created: 2020-03-12</p>
        </div>
    </div>
    <h5>Dinner</h5>
    <div class="py-2 card grid-card mb-3">
        <img class='image' src="{{ url_for('static', filename='img/dinner_dining_black_24dp.svg')}}" alt="">
        <div class="btn-container">
            <div>
                <p class="text-capitalize fw-bold fs-5 nbm">Name of Recipe</p>
                <p class="fs-6 fw-light nbm">Servings: 6</p>
            </div>
            <p class="nbm me-4">Created: 2020-03-12</p>
        </div>
    </div>
</div>
`
window.onload = function(event){
    event.preventDefault();
    pass_regex = /(?=.+[a-z])(?=.+[A-Z])(?=.+[0-9])/;
    number_regex = /^[1-9]\d*$/;

    const conatiner = document.querySelector('.min');
    const genbtn = document.querySelector('.gen');
    const savebtn = document.querySelector('.save');
    const cardsection = document.querySelector('.meal');
    const input = document.querySelector('.cal');


    genbtn.addEventListener('click', (event) => {

        event.preventDefault();

        console.log('Generate Button was clicked');

        value = input.value;

        if(value.match(number_regex) != null || value == ""){
            sanitized = true
        }else{
            sanitized = false
        }

        if(sanitized == true && value == ""){
            
            var searchParams = new URLSearchParams();
            searchParams.append('calorie', 'NONE');

            fetch('/api/plan', {
                method: 'POST',
                body: searchParams,
            }).then(response => response.json())
            .then(data => {
                let response = data.data;
                if(response == 'NOK'){
                    console.log('An Error Occurred')
                }else{
                    let start = `
                    <div class="btn-container mb-2">
                        <h2 class="fw-bold text-capitalize mb-3"> Meal Plan: Kadhjskandkjsahd</h2>
                        <h3 class="fw-bold mb-3 tot"> Total Calories: ${data.total}</h3>
                    </div>
                    <div class="day section mb-5">`;
                    let end = '</div>';
                    for(i=0; i < response.length; i++){
                        let day = `<h4 class="text-decoration-underline">Day ${i+1}</h4>`;
                        start += day;
                        for(j=0; j < response[i].length; j++){
                            let element = response[i][j];
                            switch(j){
                                case 0:
                                    start += '<h5>Breakfast</h5>';
                                    break;
                                case 1:
                                    start += '<h5>Lunch</h5>';
                                    break;
                                case 2:
                                    start += '<h5>Dinner</h5>';
                                    break;
                                default:
                                    break;
                            }
                            let recipe = `
                            <div class="py-2 card grid-card mb-3">
                                <img class='image' src="/static/img/dinner_dining_black_24dp.svg" alt="">
                                <div class="btn-container">
                                    <div>
                                        <p class="text-capitalize fw-bold fs-5 nbm">${element[1]}</p>
                                        <p class="fs-6 fw-light nbm">Servings: ${element[2]}</p>
                                    </div>
                                    <p class="nbm me-4">Calories: ${element[3]}</p>
                                </div>
                            </div>
                            `;
                            start += recipe;
                        }
                    }
                    start += end;
                    conatiner.classList.remove('min');
                    cardsection.innerHTML = start;
                }
                console.log(response);
            }).catch(error => console.log(error));

        }else{

            var searchParams = new URLSearchParams();
            searchParams.append('calorie', value);

            fetch('/api/plan', {
                method: 'POST',
                body: searchParams,
            }).then(response => response.json())
            .then(data => {
                let response = data.data;
                if(response == 'NOK'){
                    console.log('An Error Occurred')
                }else{
                    let start = `
                    <div class="btn-container mb-2">
                        <h2 class="fw-bold text-capitalize mb-3"> Meal Plan: Kadhjskandkjsahd</h2>
                        <h3 class="fw-bold mb-3 tot"> Total Calories: ${data.total}</h3>
                    </div>
                    <div class="day section mb-5">`;
                    let end = '</div>';
                    for(i=0; i < response.length; i++){
                        let day = `<h4 class="text-decoration-underline">Day ${i+1}</h4>`;
                        start += day;
                        for(j=0; j < response[i].length; j++){
                            let element = response[i][j];
                            switch(j){
                                case 0:
                                    start += '<h5>Breakfast</h5>';
                                    break;
                                case 1:
                                    start += '<h5>Lunch</h5>';
                                    break;
                                case 2:
                                    start += '<h5>Dinner</h5>';
                                    break;
                                default:
                                    break;
                            }
                            let recipe = `
                            <div class="py-2 card grid-card mb-3">
                                <img class='image' src="/static/img/dinner_dining_black_24dp.svg" alt="">
                                <div class="btn-container">
                                    <div>
                                        <p class="text-capitalize fw-bold fs-5 nbm">${element[1]}</p>
                                        <p class="fs-6 fw-light nbm">Servings: ${element[2]}</p>
                                    </div>
                                    <p class="nbm me-4">Calories: ${element[3]}</p>
                                </div>
                            </div>
                            `;
                            start += recipe;
                        }
                    }
                    start += end;
                    conatiner.classList.remove('min');
                    cardsection.innerHTML = start;
                }
                console.log(response);
            }).catch(error => console.log(error));
            
        }

        savebtn.classList.add('active');
        console.log(savebtn.classList)
    });

    
    savebtn.addEventListener('click', (event) =>{

        event.preventDefault();
        input.value = "";
        cardsection.innerHTML = "";
        conatiner.classList.add('min');
        savebtn.classList.remove('active');

    });

}