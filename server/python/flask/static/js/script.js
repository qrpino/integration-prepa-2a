// Setting up the tool used to do POST or GET requests without reloading the page.
var api = {
    url : "https://stern3.imerir.org/api",
    xhr : null,
    post : function (content) {
        xhr = new XMLHttpRequest();
        xhr.open("POST", "https://stern3.imerir.org/api", true);
        xhr.setRequestHeader('Content-Type', 'application/json; charset=UTF-8');
        xhr.send(JSON.stringify(content));
     },
    // Asks for the current angles values from the robot.
    get : function () { 
        xhr = new XMLHttpRequest();
        xhr.open("GET", "https://stern3.imerir.org/api", true);
        xhr.setRequestHeader('Content-Type', 'application/json; charset=UTF-8');
        xhr.onreadystatechange = function () { 
            if(xhr.readyState === 4 && xhr.status === 200)
            {
                try {
                    let currentMotorValues = JSON.parse(xhr.responseText);
                    for (let index = 1; index < 6 + 1; index++) {
                        let currentMotorValueInput = $(`#motor-${index}-current-value`);
                        currentMotorValueInput.val(currentMotorValues["motors"][index - 1]);}
                } catch (error) {
                    console.log("Server couldn't prepare response properly.");
                }
                }
            }
            xhr.send();
         }
     }

// To keep an eye on how many points are registered.
let registeredPointsCount = 0;

/**
 * Retrieves motors angles data from the inputs.
 * @returns {Array<Number>} motors
 */
function getMotorValues()
{
    var motors = [];
        for (let index = 1; index < 6 + 1; index++) {
            var element = $(`#motor-${index}`);
            motors.push(parseInt(element.val()));
        }
    return motors;
}

/**
 * Retrieves motors angles data from the inputs or from a specific registered position.
 * @param {Array<Number>|null} p_motors
 */
function postMotorsData(p_motors = null)
{
    p_motors ? api.post({"motors": p_motors}) : api.post({"motors": getMotorValues()});
}

// Following block sets up functions which will send motors angles data to the server, whether the client clicks on an arrow or press enter.
let arrowButtons = $('.btn-arrow');
for (let index = 1; index < arrowButtons.length/2 + 1 ; index++) {
    $(`#motor-${index}-left`).on('click', function(){
        let motorInput = $(`#motor-${index}`);
        parseInt(motorInput.val()) - 5 > 0 ? motorInput.val(parseInt(motorInput.val()) - 5) : motorInput.val(0);
        postMotorsData();
    })
    $(`#motor-${index}-right`).on('click', function(){
        let motorInput = $(`#motor-${index}`);
        parseInt(motorInput.val()) + 5 < 180 ? motorInput.val(parseInt(motorInput.val()) + 5) : motorInput.val(180);
        postMotorsData();
    })
    $(`#motor-${index}`).on('keypress', function(e) {
        if (e.key === 'Enter'){
            postMotorsData();
        }
    })
};

// Following block is used to register/delete positions of the robot.
$('#register-point').on('click', function() {
    if(registeredPointsCount < 10)
    {
        if(registeredPointsCount === 0)
        {
            $('#launch-sequence').toggleClass('hidden');
        }
        registeredPointsCount += 1;
        var container = $(`<div id="container-point-${registeredPointsCount}"></div>`);
        var registeredPoint = $(`<input type="button" value="Point ${registeredPointsCount}" 
        id="point-${registeredPointsCount}"
        title="Go to following points ${JSON.stringify(getMotorValues())}" 
        data="${JSON.stringify(getMotorValues())}">`);
        registeredPoint.on('click', function() {
            console.log(registeredPoint.attr('data'))
            postMotorsData(JSON.parse(registeredPoint.attr('data')));
        });
        registeredPoint.appendTo(container);
        var removeButton = $(`<input type="button" value="Remove point" id="remove-point-${registeredPointsCount} 
        value="Remove point>`);
        removeButton.on('click', function() {
            $(`#container-point-${registeredPointsCount}`).remove();
            registeredPointsCount -= 1;
            if(registeredPointsCount === 0)
            {
                $('#launch-sequence').toggleClass('hidden');
            }
        });
        removeButton.appendTo(container);
        $('#registered-points').append(container);
    }
});

// Parse all the values from the registered points and send them to the server.
$('#launch-sequence').on('click', function(){
    points = [];
    for (let index = 1; index < registeredPointsCount+1; index++) {
        let point = JSON.parse($(`#point-${index}`).attr('data'));
        points.push(point);
    }
    api.post({"points-sequence": points})
});

// Submit button on the motors section will send a POST XMLHttpRequest,that will retrieve the values from all the motors input fields.
 $('#submit-single-point').on('click', function () { 
    let singlePoint = {};
    singlePoint["x"] = parseInt($('#single-point-x').val());
    singlePoint["y"] = parseInt($('#single-point-y').val());
    singlePoint["z"] = parseInt($('#single-point-z').val());
    api.post({"singlePoint": singlePoint});
    });

// Every second, retrieve data from the server to actualize data without reloading the page.
setInterval(function () { 
    api.get();
  }, 1000);