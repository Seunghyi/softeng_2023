function reverse() {

  let str = document.getElementById('inputS').value;
  document.getElementById("valueS").innerHTML = str;
  document.getElementById("valueA").innerHTML = str.split('').reverse().join('');
}
