

function master(arg1,arg2){
    arg2.innerText = arg1.value
    let outervalve = ((arg1.value - arg1.min)/(arg1.max - arg1.min))*100;
    arg1.oninput = function(){
        arg2.innerText=arg1.value;
        let innervalve = ((arg1.value - arg1.min)/(arg1.max - arg1.min))*100;
        this.style.background = `linear-gradient(to right, #82CFD0 0%, #82CFD0 ${innervalve - 40}%,#9a6ffc ${innervalve - 20}%, #4758a4 ${innervalve}%, #DEE2E6 ${innervalve}%, #DEE2E6 100%)`;
    }
    arg1.style.background = `linear-gradient(to right, #82CFD0 0%, #82CFD0 ${outervalve - 40}%,#9a6ffc ${outervalve- 20}%, #4758a4 ${outervalve}%, #DEE2E6 ${outervalve}%, #DEE2E6 100%)`;
}
master(document.getElementsByClassName('slider')[0], document.getElementById('tvSalesValue'));
master(document.getElementsByClassName('slider')[1], document.getElementById('radioSalesValue'));
master(document.getElementById('socialSales'), document.getElementById('socialSalesValue'));



