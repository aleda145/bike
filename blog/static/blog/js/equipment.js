/**
 * Created by Alexander on 2016-03-22.
 */
var x = document.getElementsByClassName("totalprice");
console.log(x);
total_price=0;
for (i=0; i< x.length; i++){
    console.log($(x[i]).text());
    total_price+=parseInt($(x[i]).text())
}
console.log(total_price);
$("#totaltotalprice").text(total_price);
$("#totaltotalprice_nocomputer").text(total_price-850);
