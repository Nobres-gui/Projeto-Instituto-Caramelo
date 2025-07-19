console.log(usuarioLogado);
var botoes_Login = document.querySelector(".container__navBar-login");
var icon_User = document.querySelector(".icon__user");

if (usuarioLogado == "sim") {
  botoes_Login.style.display = "none";
  icon_User.style.display = "flex";
} else {
  botoes_Login.style.display = "flex";
  icon_User.style.display = "none";
}
