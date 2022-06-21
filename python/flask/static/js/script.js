const modeSelect = $("#mode");
const pointModeSelect = $("#point-mode");

function hideOnSelectMode()
{
    if(modeSelect.val() == 0)
    {
        $('#points').hide();
        $('#point-mode').hide();
        $('#append-point').hide();
        $('#remove-point').hide();
        $('#motors').show();
    }
    else
    {
        $('#motors').hide();
        $('#points').show();
        $('#point-mode').show();
        $('#append-point').show();
        $('#remove-point').show();
    }
}

hideOnSelectMode();

modeSelect.on("change", function(){
    hideOnSelectMode();
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