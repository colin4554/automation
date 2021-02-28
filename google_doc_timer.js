// creates a timer in a google doc within a table.  See picture in readme for how to set up your table.  Type s or start in the command box to start

function timer() {

  var startTime = new Date().getTime();
  //Logger.log(startTime);

  for (var i=1; i <= 60; i++) {
    try {
      updateTimer();
      var nowTime = new Date().getTime();
      var sleepTime = (startTime + +1000 * i) - nowTime;
      //Logger.log(sleepTime);
      Utilities.sleep(sleepTime);
    }
    catch(err) {
      Logger.log(err);
    }
  }
}

function updateTimer() {

  try {

    var doc = DocumentApp.openByUrl("INSERT DOCUMENT URL");
    var body = doc.getBody();
    //Logger.log(body.getText());
    
    var table = body.getTables();
    //Logger.log(table[0].getNumRows());
    var text = table[0].getText();

    Logger.log(text);

    var timerDisplay = table[0].getRow(3).getCell(0);

    var command = table[0].getRow(1).getCell(2).getText();

    if (timerDisplay.getText().toLowerCase() == "done") {
      return timerDisplayCell.setText("00:00");
    }
    // Logger.log(command.toLowerCase());

    if (command.toLowerCase() == "start" || command.toLowerCase() == "start " || command.toLowerCase() == " start" || command.toLowerCase() == "s " || command.toLowerCase() === "s") {
      var minutes = table[0].getRow(1).getCell(0).getText();
      var seconds = table[0].getRow(1).getCell(1).getText();
      table[0].getRow(1).getChild(2).clear();
    } else {
      Logger.log(table[0].getRow(3).getText());
      var minutes = table[0].getRow(3).getText().split(":")[0];
      var seconds = table[0].getRow(3).getText().split(":")[1];
    }

    if (minutes == "") {
      minutes = 0;
    }
    if (seconds == "") {
      seconds = 0;
    }


    Logger.log("Time");
    Logger.log(minutes);
    Logger.log(seconds);


    countdown(parseInt(minutes), parseInt(seconds), timerDisplay);
    //timerDisplay.setText("bruh");
    doc.saveAndClose();
    return;
  }

  catch(err) {
    Logger.log(err);
    return;
  }





  
}


function countdown(minutes, seconds, timerDisplayCell) {

  try {

    //initialize time
    // let initialTime = +minutes * 60 + +seconds;
    var time = +minutes * 60 + +seconds;
    time--;

    // changes color for last 10 seconds
    if (time <= 10) {
      timerDisplayCell.setBackgroundColor("#FFA500");
    } else {
      timerDisplayCell.setBackgroundColor("#FFFFFF");
    }

    // when the timer equals 0 the timer ends
    if (time <= 0) {
      timerDisplayCell.setBackgroundColor("#FF3333");
      timerDisplayCell.setText("00:00");
      return
    }

    //timer countdown
    var timerMinutes = Math.floor(time / 60);
    if (timerMinutes < 10) {
      timerMinutes = "0" + timerMinutes;
    }
    var timerSeconds = time % 60;

    if (timerSeconds < 10) {
      timerSeconds = "0" + timerSeconds; 
    }
      
    return timerDisplayCell.setText(timerMinutes + ':' + timerSeconds);
  }

  catch(err) {
    Logger.log(err);
   // time--;
    return;
  }

}
