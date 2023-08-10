//
// const showPassword = document.getElementById("show-pass-eye-div");
// const showpassicon = document.getElementById("show-pass-eye-div-icon");
// const passinput = document.getElementById('password')
// const passwordrepeat = document.querySelector('.password-repeat')
//
//
//
// // show pass repeat
// const showPasswordrepeat = document.getElementById("hide-pass-eye-div-repeat");
// const hidePasswordrepeaticon = document.getElementById("hide-pass-eye-div-icon-repeat");
//
//
//
//
// // const type =
// // password.getAttribute("type") === "password" ? "text" : "password";
// // password.setAttribute("type", type);
// showPassword.addEventListener('click',()=>{
//   const type =
//   passinput.getAttribute("type") === "password" ? "text" : "password";
//   passinput.setAttribute("type", type);
// })
//
// showPasswordrepeat.addEventListener('click',()=>{
//   const type =
//   passwordrepeat.getAttribute("type") === "password" ? "text" : "password";
//   passwordrepeat.setAttribute("type", type);
// })
//
//
//
//
//
//
//
//
//
// // show pass
// // showPassword.addEventListener("click", () => {
// //   if (showPassword.classList.contains("hide" )){
// //     showPassword.classList.remove("hide");
// //     showpassicon.classList.add("hide");
// //
// //
// //
// //   } else {
// //     showPassword.classList.add("hide");
// //     showpassicon.classList.remove("hide");
// //   }
// // });
// //
// // showpassicon.addEventListener("click", () => {
// //   if (showpassicon.classList.contains("hide")) {
// //     showpassicon.classList.remove("hide");
// //     showPassword.classList.add("hide");
// //   } else {
// //     showpassicon.classList.add("hide");
// //     showPassword.classList.remove("hide");
// //   }
// // });
//
//
// // show pass repeat
//
//
// //
// // showPasswordrepeat.addEventListener("click", () => {
// //
// //
// //   if (showPasswordrepeat.classList.contains("hide")) {
// //     showPasswordrepeat.classList.remove("hide");
// //     hidePasswordrepeaticon.classList.add("hide");
// //   } else {
// //     showPasswordrepeat.classList.add("hide");
// //     hidePasswordrepeaticon.classList.remove("hide");
// //   }
// // });
// //
// // hidePasswordrepeaticon.addEventListener("click", () => {
// //   if (hidePasswordrepeaticon.classList.contains("hide")) {
// //     hidePasswordrepeaticon.classList.remove("hide");
// //     showPasswordrepeat.classList.add("hide");
// //   } else {
// //     hidePasswordrepeaticon.classList.add("hide");
// //     showPasswordrepeat.classList.remove("hide");
// //   }
// // });
// //
// //
// //
// //
//
//
//
function tese(){
  $.ajax({ type: "GET",
         url: "/register",
          async: false,
}).then(res=>{
  Swal.fire({
  icon: 'success',
  title: 'Oops...',
  text: 'Something went wrong!',
  footer: '<a href="">Why do I have this issue?</a>'
})
  })





}



