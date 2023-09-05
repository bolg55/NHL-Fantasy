## Simple version - copy array to notepad and create CSV

var players = [];
jQuery('.players-list tbody tr').each((i,v) => {
	var playerValue = jQuery(v).children('td.pv').html();
	var playerName = jQuery(v).children('td.player_name').children('.player-name').children('.last-name').html() + " " + jQuery(v).children('td.player_name').children('.player-name').children('.last-name').html();

players.push({'pv':playerValue,'name':playerName});

})

console.log(players);



## More advanced version - writes directly to CSV

var players = [];
jQuery('.players-list tbody tr').each((i, v) => {
    var playerValue = jQuery(v).children('td.pv').html();
    var playerName = jQuery(v).children('td.player_name').children('.player-name').children('.last-name').html() + " " + jQuery(v).children('td.player_name').children('.player-name').children('.last-name').html();
    players.push({ 'pv': playerValue, 'name': playerName });
});

// Convert players array to CSV format
function arrayToCSV(objArray) {
    const array = typeof objArray !== 'object' ? JSON.parse(objArray) : objArray;
    let str = `${Object.keys(array[0]).map(value => `"${value}"`).join(",")}\r\n`;

    return array.reduce((str, next) => {
        str += `${Object.values(next).map(value => `"${value}"`).join(",")}\r\n`;
        return str;
    }, str);
}

var csv = arrayToCSV(players);

// Create a blob from the CSV string
var blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' });
var link = document.createElement("a");
if (link.download !== undefined) { // feature detection
    var url = URL.createObjectURL(blob);
    link.setAttribute("href", url);
    link.setAttribute("download", "players_data.csv");
    link.style.visibility = 'hidden';
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
}
