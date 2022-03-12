if (!window.dash_clientside) {
    window.dash_clientside = {};
}



// create the "ui" namespace within dash_clientside
window.dash_clientside.ui = { 
    // this function should be used in the callback whenever the table viewport has changed
    replaceWithLinks: function(trigger) {
        // find all dash-table cells that are in column 0
        let cells = document.getElementsByClassName("dash-cell column-3");

        Array.from(cells).forEach((elem, index, array) => {
            // each cell element should be modified with a new link
            // elem.children[0].innerText contains the link information, which we append to a specified route on our server
            elem.children[0].innerHTML =
                '<a target="_blank" href="' +'http://'+elem.children[0].innerHTML+
                '">' + ' Link ' +
                '</a>';
        });

        // arbitrary return.. callback needs a target
        return true;
    } 
}