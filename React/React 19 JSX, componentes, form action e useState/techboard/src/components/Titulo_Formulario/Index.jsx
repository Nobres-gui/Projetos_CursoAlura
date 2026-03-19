import './titulo-formulario.estilos.css'
//props é um OBJETO
//props.nome_da_prop
export function Titulo_Formulario(props){
  return(
    <h2 className='titulo_formulario' >{props.titulo}</h2>
  )
}