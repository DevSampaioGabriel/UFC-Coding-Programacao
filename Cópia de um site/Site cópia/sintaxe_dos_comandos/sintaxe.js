/*
'let' é usado para declarar a variável no JS:
let x = 1;
'const' é uma variável constante no Js:
const y = 1;
'console.log' mostrará no console do navegador:
console.log(x + y)*/
/*
para fazer a condição se no JS utiliza-se:
if (1 <2) {
    console.log
}
fazer a condição senão se no JS utiliza-se:
else if (2 == 2) {

}
fazer a condição senão no Js utiliza-se:
else {

}
*/
/*comparador 'e' e 'ou' no Js:
'||' comparador 'ou'
'&&' comparador 'e'
*/
/* enquanto no JS:
while (condição) {
    console.log
}
*/
/* percorrer com JS:
for (let  = 0;  < 10; index++) {
    console.log 
}
*/
/* Definir uma função no JS:
function teste ()

{
*/
/* Lista em JS:
let lista = [1,2,3,4,5]
*/
/* Função anônima no JS:
let funcao = () => {

}
*/
/* Chamar a função no Js:
teste() 
*/
/* Utilizar o for para percorrer a lista no JS:
for (let index = 0; index < lista.lenght ; index++) {
    console.log(lista[index])
}
/*
/* Percorrendo com outro método:
lista.forEach((num)=>{
    console.log(num)
})
*/
/* Exercicios do Python no JS:
*Não é necessario ponto e vírgula ';' ao final do comando.
----
*)Declaração da váriavel recebendo um valor do tipo número(tanto float como int):
let numDeUniProd1 = Number(prompt("Digite o número de unidades do produto 1: "));
let NumDeUniProd2 = Number(prompt("Digite o número de unidades do produto 2? "));
let precoProd1 = Number(prompt("Digite o preço do produto 1: "));
let precoProd2 = Number(prompt("Digite o preço do produto 2: "));
*)Mostrar na tela usando o format parecido com o pyrhon:
console.log(`O preço a ser pago pelo produto 1 é: ${numDeProd1 * precoProd1}`)
console.log(´O preço a ser pago pelo produto 2 é: ${numDeProd2 * precoProd2}´)
----
*)Teste condicional no JS:
let anoNasci = Number(prompt("Digite o seu ano de nascimento: "));
let anoAtual = Number(prompt("Digite o ano atual: "));
const idade = anoAtual - anoNasci;
*) Condição 'se', 'senão se' e 'senão' no JS:
if ( idade < 16 ) {
    alert("Está pessoa não é eleitor ainda!");
}else if ( (idade >= 16 && idade < 18) || idade > 65 ) {
    alert("Esta pessoa é eleitor facultativo!");
}else {
    alert("Esta pessoa é eleitor obrigatório!");
}
---
* 'parseInt' é apenas tipo inteiro, enquanto 'parseFloat' apenas do tipo float.
let N = parseInt(prompt("Digite o valor de N: "));
*) Utilizando a estrutura 'for':
for (let i = 0; i <= N; i += 2) {
    if ( i == 0 ) {
        console.log(1)
    }else {
        console.log(i)
    }
}
*) Utilizando a estrutura 'while':
let i = 0;
while (i <= N) {
    if (i == 0) {
        console.log(1)
    }else {
        console.log(i)
    }
    i += 2;
} */

let a = 0;
let lista = [];
while (a >= 0) {
    a = Number(prompt("Digite o valor de N: "));
    if (a >= 0) {
        lista.push(a);
    }
}
let soma = 0;
for (let i = 0; i , lista.length; i++) {
    soma += lista[i];
} 
let media = soma / lista.length
console.log("O valor da media é: " + media)
lista.forEach(() => {
    if ((elemento % 2 == 0) && elemento > media) {
        console.log(elemento)
    }
})


