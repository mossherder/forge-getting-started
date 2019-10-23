//Gets all Sub-Panel J-Box families with description == J-BOX
var dbIds_needed = []
viewer.search('"Sub-Panel J-Box ["',
function(dbIds){
	viewer.model.getBulkProperties(dbIds, ['FT_Assembly_Number', 'Description', 'name'],
		function(elements){
			var panel_boxes = []
			for (i=0; i<elements.length; i++){
            	for (j=0; j<elements[i].properties.length; j++){
					//panel_boxes.push(elements[i].properties[j].displayName)
					if (elements[i].properties[j].displayName == "Description" && elements[i].properties[j].displayValue == "J-BOX"){
						panel_boxes.push(elements[i])
						dbIds_needed.push(elements[i].dbId)
                    }
				}
			}
			console.log(panel_boxes)
    	}
	)
}, ['Model'])