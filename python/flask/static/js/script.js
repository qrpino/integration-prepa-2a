class Point{
    /**
    * @param {Number} index
    * @param {HTMLDivElement} divPoints
    */
    constructor(index, divPoints){
        /**
         * @type {Number}
         */
        this.index = index;
        /**
         * @type {JQuery|HTMLDivElement}
         */
        this.parentDiv = divPoints;
        /**
         * @type {JQuery|HTMLDivElement}
         */
        this.div = $(`<div id=point-${this.index}></div>`);
        /**
         * @type {JQuery|HTMLInputElement}
         */
        this.xInput = $(`<input type="number" name="point-${this.index}-x>`);
        this.xInput.appendTo(this.div);
        /**
         * @type {JQuery|HTMLInputElement}
         */
        this.yInput = $(`<input type="number" name="point-${this-index}-y`);
        this.yInput.appendTo(this.div);

        this.appendButton = $(`<input type="button" value="Rajouter un ${index}ème point">`);
        this.appendButton.on("click", function(){Point(index+1, divPoints)})
        this.appendButton.appendTo(this.div);

        this.removeButton = $(`<input type="button" value="Supprimer ce point"`);
        this.removeButton.on("click", function(){$(`#point-${index}`).remove()});
        this.removeButton.appendTo(this.div);
    }
}