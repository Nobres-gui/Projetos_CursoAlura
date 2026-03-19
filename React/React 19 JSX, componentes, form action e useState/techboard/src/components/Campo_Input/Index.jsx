import './campo-input.estilos.css'

export function Campo_Input(props){
  return(
    //...props pega todos os atributos passados para o componente e os repassa para o elemento input
    <input className='form_input' {...props}/>
  )
}