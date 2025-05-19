var obj = { name: "akal", dept: "mathematics" }

for (var key in obj) {
    console.log(key)
    console.log(obj[key])

}

// for (var key of arr){
//      console.log(key)
// }

var arr = [1, 2, 3, 4, 5]

var arr2 = [...arr, 6, 7, 8]

console.log(arr2)

//Destructuring operator 
var marks = [90, 99, 97, 98, "fail"]

var [m1, m2, m3, m4, m5] = marks;
console.log(m1)
console.log(m2)
console.log(m3)
console.log(m4)
console.log(m5)

// callback function
function sayBye() {
    console.log("bye")
}
function demo(name, callback) {
    console.log("hello " + name)
    callback()
}
demo("akal", sayBye);

const btn = document.getElementById('btn');
btn.onclick = function () {
    window.open("https://www.instagram.com/")
}