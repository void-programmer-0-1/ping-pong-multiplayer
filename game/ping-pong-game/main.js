import './style.css'

let counter = 0;

document.getElementById("counter").addEventListener("click", function(){
  counter++;
  document.getElementById("count").innerText = `${counter}`;
});