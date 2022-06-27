var api = {
    url : "http://localhost:5000/api",
    xhr : null,
    post : function (content) {
        xhr = new XMLHttpRequest();
        xhr.open("POST", "http://localhost:5000/api", true);
        xhr.setRequestHeader('Content-Type', 'application/json; charset=UTF-8');
        xhr.send(JSON.stringify(content));
     },
    get : function (content) { 
        xhr = new XMLHttpRequest();
        xhr.open("GET", this.url + "?" + content, true);
        xhr.setRequestHeader('Content-Type', 'application/json; charset=UTF-8');
        xhr.onreadystatechange = function () { 
            if(xhr.readyState === 4 && xhr.status === 200)
            {
                console.log(JSON.parse(xhr.responseText));
            }
         }
        xhr.send();
     }
}

$('#submit-motors').on('click', function () {
    var motors = [];
    for (let index = 1; index < 6 + 1; index++) {
        var element = $(`#motor-${index}`);
        motors.push(parseInt(element.val()));
    } 
    api.post({"motors": motors});
 });

 $('#submit-single-point').on('click', function () { 
    let singlePoint = {};
    singlePoint["x"] = parseInt($('#single-point-x').val());
    singlePoint["y"] = parseInt($('#single-point-y').val());
    singlePoint["z"] = parseInt($('#single-point-z').val());
    api.post({"singlePoint": singlePoint});
    });

$('#submit-arc-circle').on('click', function () { 
    let points = []
    for (let index = 1; index < 3 + 1; index++) {
        let point = {};
        point["x"] = parseFloat($(`#arc-circle-point-${index}-x`).val());
        point["y"] = parseFloat($(`#arc-circle-point-${index}-y`).val());
        point["z"] = parseFloat($(`#arc-circle-point-${index}-z`).val());
        points.push(point);
    }
    api.post({"arc-circle": points});
    console.log(points);
 });