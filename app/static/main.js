let fin = document.getElementById('fin')
let forma = document.getElementById('forma')
let fin2 = document.getElementById('fin2')
fin.onclick = f1
fin2.onclick = f2


function f1(){
    forma.hidden = false
}


function f2(){
    let address = document.getElementById('address').value
    let name = document.getElementById('name').value
    let phone = document.getElementById('phone').value
    if (address&&name&&phone){
        // alert('ok')
        // fetch('/cart/complete/')
        // let resp = fetch('/cart/complete/' + address)
        // console.log(resp)
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