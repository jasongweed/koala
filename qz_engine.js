
//debug to check loading array with image information
for(i=0; i<image_data_array.length; i++){
	console.log(image_data_array[i]);
}


//quiz based variables
var current_cat = "all";
var mode_question = true;
var hint_showing = false;
var current_q_index = 0;
var current_img;
var current_ans;
var current_hint;


//UI based variables
var scale_x = 1;
var scale_y = 1;

//image_data_array has been loaded by prior script and has format
//of this: [['epidermal nevus_gene.jpg','epidermal nevus','gene'], [...],...]

//functions: working
function initialize_qz(){
	//note: make sure file-derived question info list js file is loaded before this script so it can be accessed
	//note: first shuffle the array list
	shuffle(image_data_array);
	$('#answer').css('visibility','hidden');
	$('#hint').css('visibility','hidden');
	$('#googBtn').css('visibility','hidden');
	$('#googpathBtn').css('visibility','hidden');		
	getNextImage();
}

function displayAns(){
	//note: set image
}

function getNextImage(){
	//note: set image to next category-matched image in shuffled list
	for(i=current_q_index; i<image_data_array.length; i++){
		if(image_data_array[i].includes(current_cat) || current_cat=="all"){
			mode_question = true
			current_img = image_data_array[i][0];
			current_ans=image_data_array[i][1];
			current_hint=image_data_array[i][3];
			$('#answer').text(current_ans);
			$('#hint').text(current_hint);
			$('#nextBtn').text("See answer");
			$('#derm_img').attr("src", "images_shareable/".concat(current_img));
			console.log("current ans: "+current_ans);
			console.log("current hint: "+current_hint);
			//document.getElementById("derm_img").style.transform = "scale("+scale_x+","+scale_x+")";
			current_q_index=i+1;
			//restart if at end
			if(i==image_data_array.length){i=0; current_q_index=0;}
			break;
		}
	}
}

/**
 * Shuffles array in place.
 * @param {Array} a items An array containing the items.
 */
function shuffle(a) {
    var j, x, i;
    for (i = a.length - 1; i > 0; i--) {
        j = Math.floor(Math.random() * (i + 1));
        x = a[i];
        a[i] = a[j];
        a[j] = x;
    }
    return a;
}


///							  ///
//Quiz interface functionality///
///							  ///

//click see-answer button, also loads next image if answer seen

$(document).ready(function(){
	
	$('#nextBtn').click(function(){
		if(mode_question){
			//display answer and transition to answer mode
			$('#answer').css('visibility','visible');
			$('#googBtn').css('visibility','visible');
			$('#googpathBtn').css('visibility','visible');
			$('#nextBtn').text("Next");
			mode_question=false;
		}else{
			//transition to next question mode
			getNextImage();
			$('#answer').css('visibility','hidden');
			$('#hint').css('visibility','hidden');
			$('#googBtn').css('visibility','hidden');
			$('#googpathBtn').css('visibility','hidden');
			$('#nextBtn').text("See Answer");
			mode_question=true;
		}
	});

	$('#hintBtn').click(function(){
			$('#hint').css('visibility','visible');
	});

	//radio button functionality

	$('#radioBtnInfx').click(function(){
		//see if infx previously chosen, if so remove
		current_cat=="infx"
	});

	$('#radioBtnInflam').click(function(){
		//see if inflam previously chosen, if so remove
		current_cat="inflam";
	});

	$('#radioBtnNeo').click(function(){
		//see if neo previously chosen, if so remove
		current_cat="neo";
	});

	$('#radioBtnGene').click(function(){
		current_cat="gene";
	});

	$('#googBtn').click(function(){
		window.open("https:google.com/search?q="+current_ans+"+dermnet");
	});

	$('#googpathBtn').click(function(){
				// for image search: https://www.google.com/search?tbm=isch&q=skin+condition+name
		window.open("https://www.google.com/search?tbm=isch&q="+"+pathology+"+current_ans);
	});

	$('#smallerBtn').click(function(){
		scale_x = scale_x/1.2;
		document.getElementById("derm_img").style.transform = "scale("+scale_x+","+scale_x+")";
	});

	$('#biggerBtn').click(function(){
		scale_x = scale_x*1.2;
		document.getElementById("derm_img").style.transform = "scale("+scale_x+","+scale_x+")";

	});

});



//main()
setTimeout(function() { initialize_qz(); },750);

