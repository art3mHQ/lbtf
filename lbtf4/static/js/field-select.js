//
// console.log('FFfffffff!');

const fieldSelect = document.getElementById('fld-sel');
const subFieldSelect = document.getElementById('sub-fld-sel');



fieldSelect.addEventListener('change', e=>{
	// console.log(e.target.value);
	const selectedField = e.target.value;

	//reset
	subFieldSelect.innerHTML = '<option value="" disabled selected>Choose Subfield</option>';

    fetch(`subfld-json/${selectedField}/`)
    .then(resp => {
        if (resp.ok) {
        	// some fanky js style data processing to extract proper fomat (json)
            return resp.json().then((data) => {

	            const subFieldData = data.data
	            subFieldData.map(item=>{
	            	const optn = document.createElement('option')
	            	optn.textContent = item.name
	            	optn.setAttribute('value', item.id)
	            	subFieldSelect.appendChild(optn)
	            });
	            subFieldSelect.removeAttribute('disabled');
            })

        } else {
            console.log("Status: " + resp.status);
        }
    })

});
