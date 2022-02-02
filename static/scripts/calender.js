const date = new Date();
const
const month = [
    "januray",
    "february",
    "march",
    "april",
    "may",
    "june",
    "july",
    "auguest",
    "sep",
    "oct",
    "nov",
    "dec"
];
document.querySelector('.date h1').innerHTML=months[date.getMonth()];
document.querySelector('.date p').innerHTML=date.toDateString();
let days ="";

for(let i=1;i<=31;i++){
days +='<div>${i</div>}'
}
