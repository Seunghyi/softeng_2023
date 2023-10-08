function reverse() {

    let str = document.getElementById('inputA').value;
    document.getElementById("valueA").innerHTML = str;
    document.getElementById("valueB").innerHTML = str.split('').reverse().join('');
}


