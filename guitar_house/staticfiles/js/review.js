

    window.onload= function() {
        const cardText = document.getElementsByClassName('card-info')
        const reviewBtn=document.getElementById('review-btn')
        const divReview = document.getElementById('write-review')
        reviewBtn.addEventListener('click', () => {
            const form = document.createElement('form');
            divReview.appendChild(form)

            const text = document.createElement('input');
            text.type = 'text'
            const input = document.createElement('input');
            input.type = 'submit'

            form.appendChild(text)
            form.appendChild(input);
            reviewBtn.style.display = 'none'
        input.addEventListener('click',postReview)
        function postReview(e){
            e.preventDefault()
            const name = text.value
            const url = 'http://localhost:8000/guitars/review/'
            fetch(url + '1/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({name, text}),
            })

        }
        })


        fetch('http://localhost:8000/guitars/review/1')
            .then(response => response.json())
            .then((reviews) =>{
                let info = Object.values(reviews);
                let review = Object.values(info)

                for (let i = 0; i < review.length; i++) {
                    let {text, name} = review[i];
                    let hName = document.createElement('h1');
                    hName.innerHTML = name
                    let pText = document.createElement('p');
                    pText.innerHTML = text
                    cardText[i].appendChild(hName);
                    cardText[i].appendChild(pText);
                }




    })
    }



