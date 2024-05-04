

    window.onload= function() {
        const cardText = document.getElementsByClassName('card-info')


        fetch('http://localhost:8000/guitars/review/1')
            .then(response => response.json())
            .then((reviews) =>{
                let info = Object.values(reviews);
                let review = Object.values(info)
                console.log(review)
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



