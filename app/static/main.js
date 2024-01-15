
let fin = document.getElementById('fin')
let forma = document.getElementById('forma')
let fin2 = document.getElementById('fin2')
let fin3 = document.getElementById('fin3')
let fin4 = document.getElementById('fin4')
let forma1 = document.getElementById('forma1')
let myformbut = document.getElementById('myformbut')
fin.onclick = f1
fin2.onclick = f2
fin3.onclick = f3


window.addEventListener('load', function () {
    let address = document.getElementById('id_address').value
    let name = document.getElementById('id_name').value
    let phone = document.getElementById('id_phone').value
    if ((document.getElementsByClassName('errorlist').length === 0)&&address&&name&&phone){
        f4()
    }
})


function f1(){
    forma.hidden = false
}

function json(response) {
    return response.json()
}


function f2(){
    let address = document.getElementById('address').value
    let name = document.getElementById('name').value
    let phone = document.getElementById('phone').value
    if (address&&name&&phone){
        const data = {
            address: address,
            name: name,
            phone: phone
        }
        fetch('/cart/pobeda/', {
            method: 'post',
            body: JSON.stringify(data),
            headers: {
                'Content-Type': 'application/json; charset=UTF-8',
                'X-CSRFToken': csrf_token,
            }
        })
          .then(json)
          .then(function (data) {
            console.log('Request succeeded with JSON response', data.mes);
            window.location.href = data.link
          })
          .catch(function (error) {
            console.log('Request failed', error);
          });

    }
    else{
        alert('ne ok')
    }
}

function f3(){
    let address = document.getElementById('address').value
    let name = document.getElementById('name').value
    let phone = document.getElementById('phone').value
    if (address&&name&&phone){

        let url = '/cart/complete'
        $.ajax(url, {
            method: 'POST',
            data: {'address': address, 'name': name, 'phone': phone},
            success: function (responce){
                console.log(responce.mes)
                window.location.href = responce.link},
            error: function (responce){
                console.log(responce.mes)}
        })
    }
    else{
        alert('ne ok')
    }
}

function f4(){
    console.log('f4')
    let address = document.getElementById('id_address').value
    let name = document.getElementById('id_name').value
    let phone = document.getElementById('id_phone').value
    if (address&&name&&phone){
        console.log(address, name, phone)
        let url = '/cart/complete'
        $.ajax(url, {
            method: 'POST',
            data: {'address': address, 'name': name, 'phone': phone},
            success: function (responce){
                console.log(responce.mes)
                window.location.href = responce.link},
            error: function (responce){
                console.log(responce.mes)}
        })
    }
    else{
        alert('ne ok')
    }
}