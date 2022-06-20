const pointsDiv = $("#points");
let pointsCount = pointsDiv.children().length
$("#append-point").on("click", function () { 
    pointsCount += 1;
    /**
     * @type {HTMLDivElement}
     */
    pointDiv = $(`<div id="point-${pointsCount}"></div>`);
    xInput = $(`<input type="number" placeholder="x value...">`);
    yInput = $(`<input type="number" placeholder="y value...">`);
    pointDiv.append(xInput);
    pointDiv.append(yInput);
    pointsDiv.append(pointDiv);

    // Add point..
})
$("#remove-point").on("click", function () {
    if(pointsCount > 0)
    {
        $(`#point-${pointsCount}`).remove();
        pointsCount -= 1;
    }
  })