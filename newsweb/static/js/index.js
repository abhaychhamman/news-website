// alert("dakjkgjkafjgk")

let next=document.getElementById("next")
let question=document.getElementById("question")
let totalques=document.getElementById("totalques")
let container_ques=document.getElementById("container_ques")
let form=document.getElementById("form")
let submit=document.getElementById("submit")

let a=""
next.addEventListener("click", function() {
    // console.log("ajdkjgk")
    // console.log(question.value)
    a=question.value+"."
    totalques.value=totalques.value+a
    console.log(a)
    container_ques.innerHTML+="<li>"+a+"</li>"
 
  });
  