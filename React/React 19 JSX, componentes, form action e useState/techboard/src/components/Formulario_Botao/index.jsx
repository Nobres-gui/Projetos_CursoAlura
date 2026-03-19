import './formulario-botao.estilos.css'

export function Formulario_Botao(props){
    return(
        <button className="form_botao" type={props.type}>{props.texto}</button>
    )
}