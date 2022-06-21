const modeSelect = $("#mode");
const pointModeSelect = $("#point-mode");
modeSelect.on("change", function(){

})

const pointsDiv = $("#points");
let pointsCount = pointsDiv.children().length
$("#append-point").on("click", function () { 
    pointsCount += 1;
    /**
     * @type {HTMLDivElement}
     */
    pointDiv = $(`<div id="point-${pointsCount}"></div>`);
    xInput = $(`<input id="point-${pointsCount}-x" type="number" placeholder="x value...">`);
    yInput = $(`<input id="point-${pointsCount}-y" type="number" placeholder="y value...">`);
    pointDiv.append(xInput);
    pointDiv.append(yInput);
    pointsDiv.append(pointDiv);
})
$("#remove-point").on("click", function () {
    if(pointsCount > 0)
    {
        $(`#point-${pointsCount}`).remove();
        pointsCount -= 1;
    }
  })