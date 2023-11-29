let fin = document.getElementById('fin')
let forma = document.getElementById('forma')
let fin2 = document.getElementById('fin2')
fin.onclick = f1
fin.onclick = f2


function f1(){
    forma.hidden = false
}


function f2(){
    let address = document.getElementById('address').value
    let name = document.getElementById('name').value
    let phone = document.getElementById('phone').value
    if (address&&name&&phone){
        // alert('ok')
        fetch()
    }
    else{
        alert('ne ok')
    }
}