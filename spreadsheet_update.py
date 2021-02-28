function updateSpreadsheet() {   

  // spreadsheet
  var FILE = SpreadsheetApp.openByUrl("INSERT URL");
  var SHEET = FILE.getSheetByName("INSERT SHEET NAME");

  var doc = DocumentApp.openByUrl("INSERT DOCUMENT NAME");
  var body = doc.getBody();
  var text = body.getText();
  Logger.log(text);

  var list = text.split(" ");

  let numberOfSpeeches = {'Afghanistan' : 0, 'Algeria' : 0, 'Australia' : 0, 'Brazil' : 0, 'Canada' : 0, 'China' : 0, 'Colombia' : 0, 'Denmark' : 0, 'Egypt' : 0, 'Ethiopia' : 0, 'France' : 0, 'Germany' : 0, 'India' : 0, 'Italy' : 0, 'Japan' : 0, 'Mexico' : 0, 'Netherlands' : 0, 'Niger' : 0, 'Nigeria' : 0, 'Pakistan' : 0, 'Peru' : 0, 'Philipines' : 0, 'Poland' : 0, 'Portugal' : 0, 'Romania' : 0, 'Russian Federation' : 0, 'South Africa' : 0, 'South Korea' : 0, 'Spain' : 0, 'Uganda' : 0, 'United Kingdom' : 0, 'United States' : 0, 'Vietnam' : 0, 'Yemen' : 0 };

  let numberOfMotions = {'Afghanistan' : 0, 'Algeria' : 0, 'Australia' : 0, 'Brazil' : 0, 'Canada' : 0, 'China' : 0, 'Colombia' : 0, 'Denmark' : 0, 'Egypt' : 0, 'Ethiopia' : 0, 'France' : 0, 'Germany' : 0, 'India' : 0, 'Italy' : 0, 'Japan' : 0, 'Mexico' : 0, 'Netherlands' : 0, 'Niger' : 0, 'Nigeria' : 0, 'Pakistan' : 0, 'Peru' : 0, 'Philipines' : 0, 'Poland' : 0, 'Portugal' : 0, 'Romania' : 0, 'Russian Federation' : 0, 'South Africa' : 0, 'South Korea' : 0, 'Spain' : 0, 'Uganda' : 0, 'United Kingdom' : 0, 'United States' : 0, 'Vietnam' : 0, 'Yemen' : 0 };

  let countryList = ['Afghanistan', 'Algeria', 'Australia', 'Brazil', 'Canada', 'China', 'Colombia', 'Denmark', 'Egypt', 'Ethiopia', 'France', 'Germany', 'India', 'Italy', 'Japan', 'Mexico', 'Netherlands', 'Niger', 'Nigeria', 'Pakistan', 'Peru', 'Philipines', 'Poland', 'Portugal', 'Romania', 'Russian Federation', 'South Africa', 'South Korea', 'Spain', 'Uganda', 'United Kingdom', 'United States', 'Vietnam', 'Yemen'];
  
  // counts number of times above countries are listed in document for speeches or motions (if the country has : after).  Stores data in spreadsheet by country.
  
  
  for (i in list) {
    word = list[i];
    word = toTitleCase(word);
    //Logger.log(word.substring(word.length - 1));

    // counts country that motions (denoted with : after)
    if (word.substring(word.length - 1) == ":") {
      for (i in countryList) {
        var loc = word.indexOf(countryList[i]);
        if (loc != -1) {
          var country = word.substring(loc, word.length - 1);
          numberOfMotions[country] += 1;
        }
      }
    }

    for (j in countryList) {
        var splitCountry = countryList[j].split(" ");

        // deals with compound countries
        if (splitCountry.length == 1) {
          var loc = word.indexOf(countryList[j]);
        }
        else {
          var loc = word.indexOf(splitCountry[1]);
        }

        // determines if country name exists but isn't for a motion and adds one to dict
        if (loc != -1 && word.substring(word.length - 1) != ":") {
          var country = countryList[j]
          Logger.log(country);
          numberOfSpeeches[country] += 1;
        }

    }

    

  }

  Logger.log("Number of Motions");
  Logger.log(numberOfMotions);

  Logger.log("Number of Speeches");
  Logger.log(numberOfSpeeches);


  // update google sheet

  for (i in countryList) {

    // updated # of motions
    var key = "F" + (+i + +2).toString()
    var cell = SHEET.getRange(key).setValue(numberOfMotions[countryList[i]])

    // update # of speeches
    var key = "G" + (+i + +2).toString()
    var cell = SHEET.getRange(key).setValue(numberOfSpeeches[countryList[i]])
    
    //var updatedCell = cell.toString().replace(".", "");

    // Logger.log(countryList[i] + " " + cell);
  }

    // var A1 = SHEET.getRange("I17").getValue();
    // var A1String = A1.toString().replace(".", "");


}

function toTitleCase(str) {
  return str.replace(
    /\w\S*/g,
    function(txt) {
      return txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase();
    }
  );
}
