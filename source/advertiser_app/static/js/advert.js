function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    console.log(cookieValue)
    return cookieValue;
}

function decline(event){
    let btn = event.currentTarget
    let pk = (btn.parentElement).id
    let myData = new Object()
    myData[pk] = 'decline'
    let formData = JSON.stringify(myData)
    event.stopPropagation()
    $.ajax({
            headers: {
                'X-CSRFToken': getCookie('csrftoken')
            },
            url: "http://127.0.0.1:8000/advert/moderate/"+pk+"/",
            data: formData,
            cache: false,
            processData: false,
            contentType: false,
            type: 'POST',
            dataType: "json",
            success: function () {
                window.reload()
            }
        });
}
function approve(event){
    let btn = event.currentTarget
    let pk = (btn.parentElement).id
    let myData = new Object()
    myData[pk] = 'approve'
    let formData = JSON.stringify(myData)
    event.stopPropagation()
    $.ajax({
            headers: {
                'X-CSRFToken': getCookie('csrftoken')
            },
            url: "http://127.0.0.1:8000/advert/moderate/"+pk+"/",
            data: formData,
            cache: false,
            processData: false,
            contentType: false,
            type: 'POST',
            dataType: "json"
        });
}
