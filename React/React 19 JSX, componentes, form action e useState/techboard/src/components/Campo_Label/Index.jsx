import './campo-label.estilos.css'
export function Campo_Label(props){
  return(
    <label className='campo_label' htmlFor={props.htmlFor}>
      {props.children}
      </label>
  )
}