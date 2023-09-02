var districtObject = {
  "TRIVANDRUM": {
    "TRIVANDRUM":[],
    "KILIMANOOR": [],
    "NEYYATTINKARA": [],
    "ATTINGAL":[]
  },
  "ALAPPUZHA": {
    "CHERTHALA":[],
    "HARIPAD": [],
    "MAVELIKKARA": [],
    "CHENGANNUR":[]
  },
  "KANNUR": {
    "KANNUR":[],
    "PAYYANUR": [],
    "IRITTY": [],
    "KUTHUPARAMB":[]
  },
  "THRISSUR": {
    "GURUVAYUR":[],
    "IRINJALAKUDA": [],
    "CHALAKUDY": [],
    "KODUNGALLUR":[]
  },
  "ERNAKULAM": {
    "KOCHI":[],
    "ALUVA": [],
    "KOTTAYAM": [],
    "ERNAKULAM TOWN":[]
  },
}
window.onload = function() {
  var districtSel = document.getElementById("district");
  var branchSel = document.getElementById("branch");
  var chapterSel = document.getElementById("chapter");
  for (var x in districtObject) {
    districtSel.options[districtSel.options.length] = new Option(x, x);
  }
  districtSel.onchange = function() {
   
    branchSel.length = 1;

    for (var y in districtObject[this.value]) {
      branchSel.options[branchSel.options.length] = new Option(y, y);
    }
  }

}