const notaFinal = 7;
const falta = 3;
const advertencias = 0;

if (notaFinal < 7 || faltas >4) {
    console.log("Reprovado, boas festas")
} else {
    console.log("aprovado, boas festas")
}

if (faltas >= 2 && !advertencias) {
    console.log("Recebeu bônus")
} else {
   console.log("Não recebeu bônus")
}