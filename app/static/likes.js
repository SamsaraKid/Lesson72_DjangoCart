function flike(event, id){
    img = event.target
    let color = ''
    if (img.src.includes("/static/img/notlike.png")){
        img.setAttribute('src', "/static/img/like.png")
        color = 'red'
    } else {
        img.setAttribute('src', "/static/img/notlike.png")
        color = 'white'
    }
    let url = 'tofavorites/'
    $.ajax(url, {
        method: 'POST',
        data: {'k1': id, 'k2': color},
        success: function (responce){
            console.log(responce.mes)},
            // window.location.href = responce.link},
        error: function (responce){
            console.log(responce.mes)}
    })
}